#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""取行情：收盘价、涨跌幅、相对基准指数的超额、量比、近几个交易日收盘价。

只负责取数，不做任何判断——异动门槛、是否收盘、判断是否命中，一律由任务定义（SKILL.md）规定。
只用标准库。任一数据源失败时对应列输出 n/a，不中断。

用法：quotes.py <代码>[:<基准指数代码>] ...
代码写法：usNVDA、hk00700、sh600519、sz300750；指数如 usINX、hkHSI、sh000001。
  例：quotes.py usINX usIXIC usNVDA:usIXIC hk00700:hkHSTECH sh600519:sh000300

数据源：
  - 实时/收盘行情：腾讯行情 https://qt.gtimg.cn/q=<代码>（三地市场通用）
  - 近一个月日线（量比与近期收盘价，仅个股）：Yahoo Finance chart 接口
"""
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

UA = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 15


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read()


def tencent(codes):
    """返回 {代码: {name, close, prev, pct, time}}；取不到的代码不在结果里。"""
    out = {}
    try:
        raw = fetch("https://qt.gtimg.cn/q=" + ",".join(codes)).decode("gbk", "replace")
    except Exception as e:  # noqa: BLE001 — 任何失败都降级为"无数据"
        print(f"# 腾讯行情请求失败：{type(e).__name__} {e}")
        return out
    for line in raw.split(";"):
        if "=" not in line:
            continue
        key, val = line.strip().split("=", 1)
        f = val.strip('"').split("~")
        if len(f) < 33:
            continue
        try:
            out[key.replace("v_", "")] = {
                "name": f[1],
                "close": float(f[3]),
                "prev": float(f[4]),
                "pct": float(f[32]),
                "time": f[30],
            }
        except ValueError:
            continue
    return out


def trade_date(ts):
    """把三种时间戳写法统一成 YYYY-MM-DD HH:MM（交易所当地时间）。"""
    digits = "".join(c for c in ts if c.isdigit())
    if len(digits) < 12:
        return ts
    return f"{digits[0:4]}-{digits[4:6]}-{digits[6:8]} {digits[8:10]}:{digits[10:12]}"


def yahoo_symbol(code):
    if code.startswith("us"):
        return code[2:].replace(".", "-")
    if code.startswith("hk") and code[2:].isdigit():
        return f"{int(code[2:]):04d}.HK"
    if code.startswith("sh") and code[2:].isdigit():
        return code[2:] + ".SS"
    if code.startswith("sz") and code[2:].isdigit():
        return code[2:] + ".SZ"
    return None


def yahoo_history(code):
    """返回 [(日期, 收盘价, 成交量)]，按日期升序，只含数据完整的交易日。"""
    sym = yahoo_symbol(code)
    if not sym:
        return []
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=2mo&interval=1d"
        res = json.loads(fetch(url))["chart"]["result"][0]
        offset = res["meta"].get("gmtoffset", 0)
        q = res["indicators"]["quote"][0]
        rows = []
        for ts, c, v in zip(res["timestamp"], q["close"], q["volume"]):
            if c is None or not v:
                continue
            day = (datetime.fromtimestamp(ts, timezone.utc) + timedelta(seconds=offset)).date()
            rows.append((day.isoformat(), c, v))
        return rows
    except Exception:  # noqa: BLE001
        return []


def num(x):
    return f"{x:.3f}".rstrip("0").rstrip(".")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    pairs = [(a.split(":", 1) + [None])[:2] for a in args]
    codes = list(dict.fromkeys([c for c, _ in pairs] + [b for _, b in pairs if b]))
    q = tencent(codes)

    print("代码 | 名称 | 行情时间(交易所当地) | 收盘 | 前收 | 涨跌幅% | 基准 | 基准涨跌幅% | 超额(百分点) | 量比(当日/前20日均量) | 近5个交易日收盘 | 行情链接")
    for code, bench in pairs:
        link = f"https://qt.gtimg.cn/q={code}"
        d = q.get(code)
        if not d:
            print(f"{code} | n/a | n/a | n/a | n/a | n/a | {bench or '-'} | n/a | n/a | n/a | n/a | {link}")
            continue
        b = q.get(bench) if bench else None
        bench_pct = f"{b['pct']:+.2f}" if b else ("n/a" if bench else "-")
        excess = f"{d['pct'] - b['pct']:+.2f}" if b else ("n/a" if bench else "-")

        vol_ratio, recent = "-", "-"
        if bench:  # 只给个股取日线；指数不需要量比
            hist = yahoo_history(code)
            day = trade_date(d["time"])[:10]
            if hist:
                recent = ", ".join(f"{dt}={c:.2f}" for dt, c, _ in hist[-5:])
            if len(hist) >= 6 and hist[-1][0] == day:
                prior = [v for _, _, v in hist[-21:-1]]
                vol_ratio = f"{hist[-1][2] / (sum(prior) / len(prior)):.2f}"
            else:
                vol_ratio = "n/a"
        print(
            f"{code} | {d['name']} | {trade_date(d['time'])} | {num(d['close'])} | {num(d['prev'])} | "
            f"{d['pct']:+.2f} | {bench or '-'} | {bench_pct} | {excess} | {vol_ratio} | {recent} | {link}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
