#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验一份归档是否满足 _template/SKILL.md 第 3 步的格式契约。

只校验正则可判定的结构，绝不涉及内容质量判断——掺进主观判断就会误报，
误报几次之后告警就会被无视，那这道防线就死了。

用法：lint_archive.py <归档文件>
输出：每行一条违规；无违规则无输出。退出码 1 表示有违规。
"""
import re
import sys


def lint(path):
    bad = []
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    if not lines:
        return ["文件为空"]

    # 1. 一级标题：首个非空行必须以 "# " 开头
    first_idx = next((i for i, l in enumerate(lines) if l.strip()), None)
    if first_idx is None:
        return ["文件只有空行"]
    if not lines[first_idx].startswith("# "):
        bad.append(f"第 {first_idx+1} 行：首行必须是 `# ` 一级标题，实际为 {lines[first_idx][:40]!r}")

    # 2. 覆盖窗口行：标题之后首个非空行必须以 "> 覆盖窗口：" 开头
    second_idx = next((i for i in range(first_idx + 1, len(lines)) if lines[i].strip()), None)
    if second_idx is None:
        bad.append("缺覆盖窗口行")
    elif not lines[second_idx].startswith("> 覆盖窗口："):
        bad.append(f"第 {second_idx+1} 行：标题之后必须紧跟 `> 覆盖窗口：` 行，实际为 {lines[second_idx][:40]!r}")

    # 3. 不得用粗体行冒充板块标题
    for i, l in enumerate(lines):
        if l.startswith("**"):
            bad.append(f"第 {i+1} 行：不得以 `**` 开头（板块标题一律用 `## `）：{l[:40]!r}")

    items = [(i, l) for i, l in enumerate(lines) if l.startswith("- ")]
    is_empty_issue = not items and any("本期没有值得报告的内容" in l for l in lines)
    if is_empty_issue:
        return bad  # 空期只校验前三条

    if not items:
        bad.append("既没有 `- ` 条目，也不是合规的空期简报（缺「本期没有值得报告的内容」）")

    # 4. 至少一个 `## ` 板块
    if items and not any(l.startswith("## ") for l in lines):
        bad.append("有条目但没有任何 `## ` 板块标题")

    for i, l in items:
        n = i + 1
        # 5. 每条必须标注来源
        if "来源：" not in l:
            bad.append(f"第 {n} 行：条目缺 `来源：`：{l[:50]!r}")
            continue
        # 6. 必须有裸链接，或显式声明无公开链接
        if "http" not in l and "（无公开链接：" not in l:
            bad.append(f"第 {n} 行：条目既无 URL 也未写「（无公开链接：<原因>）」：{l[:50]!r}")
        # 7. 不得用 markdown 链接语法
        if re.search(r"\]\(https?://", l):
            bad.append(f"第 {n} 行：来源须用裸 URL，不得用 `[名称](URL)` 语法：{l[:50]!r}")

    return bad


def main():
    if len(sys.argv) != 2:
        print("用法：lint_archive.py <归档文件>", file=sys.stderr)
        return 2
    violations = lint(sys.argv[1])
    for v in violations:
        print(v)
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
