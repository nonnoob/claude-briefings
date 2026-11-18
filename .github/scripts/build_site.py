#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建阅读站：把各任务的归档渲染成一个静态站点。

阅读站是归档的只读派生视图（见 CONTEXT.md）：本脚本只读 */archive/*.md，
产物全部写进输出目录，不入库、不回写仓库里的任何文件。归档是唯一的内容来源，
所以这里对格式一律宽容——早期归档不满足格式契约（表格、粗体行、缺 `# `）也要能读，
格式是否合规是看门狗的事，不是阅读站的事。

任务目录自动发现：仓库根下任何含 archive/<目录名>_<YYYY-MM-DD>[_HHmm].md 的目录
都会出现在站点上，新建任务无需登记。展示顺序见 site/order.txt。

用法：build_site.py <输出目录>
"""
import html
import json
import os
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE_SRC = ROOT / "site"

ARCHIVE_RE = re.compile(r"^(?P<slug>.+)_(?P<date>\d{4}-\d{2}-\d{2})(?:_(?P<time>\d{4}))?\.md$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
HR_RE = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^:?-+:?$")
HEADLINE_RE = re.compile(r"^\**(?:今日|本周|本期)要闻\**[：:]\s*(.*)$")
EMPTY_PREFIX = "本期没有值得报告"
TAGS_RE = re.compile(r"^((?:【[^】]{1,6}】)+)")
# 站点的显示范围最长 7 天，多留两天余量（时区差、构建间隔）
HEADLINE_DAYS = 9
TAG_CLASS = {"续报": "follow", "传闻": "rumor", "单源": "single", "矛盾": "conflict"}

# 裸链接在中文标点、全角字符、汉字处截断：归档里 URL 后面常常直接跟"、""；"
URL = r"https?://[^\s<>\"　-〿＀-￯一-鿿]+"
INLINE_RE = re.compile(
    r"\[(?P<text>[^\]\n]+)\]\((?P<href>https?://[^\s)]+)\)"
    r"|(?P<url>" + URL + r")"
    r"|\*\*(?P<bold>.+?)\*\*"
    r"|`(?P<code>[^`\n]+)`"
)


def link(href, text):
    return (
        f'<a href="{html.escape(href, quote=True)}" target="_blank" '
        f'rel="noopener noreferrer">{html.escape(text)}</a>'
    )


def trim_url(url):
    """把句末标点和未配对的右括号从 URL 尾部剥下来，返回 (url, 剥下的尾巴)。"""
    tail = ""
    while url:
        c = url[-1]
        if c in ".,;:!?*'" or (c == ")" and url.count(")") > url.count("(")):
            tail = c + tail
            url = url[:-1]
        else:
            break
    return url, tail


def inline(text):
    out = []
    pos = 0
    for m in INLINE_RE.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        if m.group("href"):
            out.append(link(m.group("href"), m.group("text")))
        elif m.group("url"):
            url, tail = trim_url(m.group("url"))
            out.append(link(url, url) + html.escape(tail))
        elif m.group("bold") is not None:
            out.append(f"<strong>{inline(m.group('bold'))}</strong>")
        else:
            out.append(f"<code>{html.escape(m.group('code'))}</code>")
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)


def item_html(text):
    """条目最前缀的【续报】【传闻】等标记渲染成色块，其余按行内规则处理。"""
    m = TAGS_RE.match(text)
    if not m:
        return inline(text)
    tags = re.findall(r"【([^】]+)】", m.group(1))
    badges = "".join(
        f'<span class="tag tag-{TAG_CLASS.get(t, "other")}">{html.escape(t)}</span>' for t in tags
    )
    return badges + inline(text[m.end():].lstrip())


def is_block_start(line):
    s = line.strip()
    return (
        not s
        or HEADING_RE.match(line)
        or HR_RE.match(line)
        or line.startswith(">")
        or line.startswith("|")
        or LIST_RE.match(line)
    )


def render_table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    head = None
    if len(cells) > 1 and all(TABLE_SEP_RE.match(c) for c in cells[1]):
        head, cells = cells[0], cells[2:]
    out = ['<div class="table-wrap"><table>']
    if head:
        out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
    out.append("<tbody>")
    for row in cells:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render(lines):
    """把归档正文（已去掉标题行）渲染成 HTML 片段。"""
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue

        if HR_RE.match(line):
            out.append("<hr>")
            i += 1
            continue

        m = HEADING_RE.match(line)
        if m:
            # 页面上 h1 是站名、h2 是日期，归档里的板块标题从 h3 起
            level = min(max(3, len(m.group(1)) + 1), 6)
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if line.startswith(">"):
            quote = []
            while i < n and lines[i].startswith(">"):
                quote.append(re.sub(r"^>\s?", "", lines[i].rstrip()))
                i += 1
            cls = ' class="window"' if quote[0].startswith("覆盖窗口") else ""
            out.append(f"<blockquote{cls}>" + "<br>".join(inline(q) for q in quote) + "</blockquote>")
            continue

        if line.startswith("|"):
            rows = []
            while i < n and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            out.append(render_table(rows))
            continue

        m = LIST_RE.match(line)
        if m:
            ordered = m.group(2)[0].isdigit()
            items = []
            while i < n:
                cur = lines[i].rstrip()
                m = LIST_RE.match(cur)
                if m and not HR_RE.match(cur):
                    items.append([len(m.group(1)), m.group(3)])
                    i += 1
                elif cur.strip() and cur[0].isspace():
                    # 缩进的续行并入上一条
                    items[-1][1] += " " + cur.strip()
                    i += 1
                elif not cur.strip():
                    # 空行隔开的条目仍算同一个列表
                    j = i
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and LIST_RE.match(lines[j]) and not HR_RE.match(lines[j]):
                        i = j
                    else:
                        break
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>")
            for indent, text in items:
                cls = ' class="sub"' if indent >= 2 else ""
                out.append(f"<li{cls}>{item_html(text)}</li>")
            out.append(f"</{tag}>")
            continue

        para = []
        while i < n and not is_block_start(lines[i]):
            para.append(lines[i].strip())
            i += 1
        cls = ""
        if HEADLINE_RE.match(para[0]):
            cls = ' class="headline"'
        elif para[0].startswith(EMPTY_PREFIX):
            cls = ' class="empty"'
        out.append(f"<p{cls}>" + "<br>".join(inline(p) for p in para) + "</p>")
    return "".join(out)


def plain(text):
    """去掉行内 markdown 记号，供首页卡片当纯文本显示。"""
    text = re.sub(r"\[([^\]\n]+)\]\(https?://[^\s)]+\)", r"\1", text)
    return text.replace("**", "").replace("`", "").strip()


def parse_archive(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    first = next((i for i, l in enumerate(lines) if l.strip()), None)
    if first is None:
        return None

    # 首行是标题：`# <emoji> <任务名> · <日期>`；早期归档可能缺 `# `
    title = None
    head = lines[first].strip()
    if head.startswith("# ") or " · " in head:
        title = re.sub(r"^#+\s*", "", head)
        if " · " in title:
            title = title.rsplit(" · ", 1)[0]
        body = lines[first + 1:]
    else:
        body = lines[first:]

    headline = ""
    empty = False
    for l in body:
        s = l.strip()
        m = HEADLINE_RE.match(s)
        if m and not headline:
            headline = plain(m.group(1))
        if s.startswith(EMPTY_PREFIX):
            empty = True
            if not headline:
                headline = plain(s)
    if not headline:
        # 没有要闻行的早期归档：退而取第一段正文或第一条条目
        for l in body:
            s = l.strip()
            if not s or s.startswith(("#", ">", "|")) or HR_RE.match(s):
                continue
            m = LIST_RE.match(s)
            headline = plain(m.group(3) if m else s)
            break
    headline = re.sub(r"\s*来源[：:].*$", "", headline)
    if len(headline) > 220:
        headline = headline[:220] + "…"

    return {
        "title": title,
        "headline": headline,
        "empty": empty,
        "html": render(body),
    }


def read_order():
    path = SITE_SRC / "order.txt"
    if not path.exists():
        return []
    order = []
    for l in path.read_text(encoding="utf-8").splitlines():
        l = l.split("#", 1)[0].strip()
        if l:
            order.append(l)
    return order


def build(out_dir):
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "data").mkdir(parents=True)

    topics = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[0] not in "._"):
        archive = d / "archive"
        if not archive.is_dir():
            continue
        runs = []
        for f in sorted(archive.glob("*.md")):
            m = ARCHIVE_RE.match(f.name)
            if not m or m.group("slug") != d.name:
                continue
            parsed = parse_archive(f)
            if parsed is None:
                continue
            runs.append((m.group("date"), m.group("time") or "", f.stem, parsed))
        if not runs:
            continue
        runs.sort(key=lambda r: (r[0], r[1]))

        (out_dir / "data" / d.name).mkdir()
        for _, _, stem, parsed in runs:
            (out_dir / "data" / d.name / f"{stem}.json").write_text(
                json.dumps({"html": parsed["html"]}, ensure_ascii=False), encoding="utf-8"
            )

        latest = runs[-1][3]
        # 只给最近几天的运行带上要闻（首页在最近一期是空期时要用），更早的不带，索引不随归档无限变大
        recent = (datetime.now(timezone.utc) - timedelta(days=HEADLINE_DAYS)).strftime("%Y-%m-%d")
        topics.append({
            "slug": d.name,
            # 任务名取最近一份归档的标题，改名后站点自动跟随
            "title": next((r[3]["title"] for r in reversed(runs) if r[3]["title"]), d.name),
            "headline": latest["headline"],
            "runs": [
                {"date": date, "time": time or None, "empty": p["empty"],
                 **({"headline": p["headline"]} if date >= recent and not p["empty"] else {})}
                for date, time, _, p in runs
            ],
        })

    if not topics:
        sys.exit("没有发现任何归档，拒绝构建空站点")

    order = read_order()
    rank = {slug: i for i, slug in enumerate(order)}
    topics.sort(key=lambda t: (rank.get(t["slug"], len(order)), t["slug"]))

    index = {
        "built": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo": os.environ.get("GITHUB_REPOSITORY", ""),
        "topics": topics,
    }
    (out_dir / "data" / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
    )
    shutil.copy(SITE_SRC / "index.html", out_dir / "index.html")
    print(f"阅读站已构建：{len(topics)} 个任务，{sum(len(t['runs']) for t in topics)} 份归档 -> {out_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(Path(sys.argv[1]).resolve())
