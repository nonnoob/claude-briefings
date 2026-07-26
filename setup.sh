#!/usr/bin/env bash
# 一键配置：把 new-briefing 技能安装到 ~/.claude/skills/，并自动填入本仓库的检出路径。
# 用法：clone 本仓库后，在仓库目录里运行 ./setup.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
SKILL_SRC="$REPO_ROOT/skills/new-briefing/SKILL.md"
SKILL_DST_DIR="${HOME}/.claude/skills/new-briefing"

if [ ! -f "$SKILL_SRC" ]; then
  echo "错误：找不到 $SKILL_SRC——请在仓库检出目录里运行本脚本。" >&2
  exit 1
fi
if ! REMOTE_URL="$(git -C "$REPO_ROOT" remote get-url origin 2>/dev/null)"; then
  echo "错误：$REPO_ROOT 不是带 origin 远端的 git 检出。先 clone 你的仓库再运行。" >&2
  exit 1
fi

mkdir -p "$SKILL_DST_DIR"
if [ -f "$SKILL_DST_DIR/SKILL.md" ]; then
  cp "$SKILL_DST_DIR/SKILL.md" "$SKILL_DST_DIR/SKILL.md.bak"
  echo "已有同名技能，原文件备份为 SKILL.md.bak"
fi

# 填入检出路径；安装说明块（以"> **安装**"开头的引用行）不带入安装后的技能
REPO_ROOT="$REPO_ROOT" perl -ne 'next if /^> \*\*安装\*\*/; s/<仓库检出路径>/$ENV{REPO_ROOT}/g; print' \
  "$SKILL_SRC" > "$SKILL_DST_DIR/SKILL.md"

echo "✔ 技能已安装：${SKILL_DST_DIR}/SKILL.md"
echo "✔ 仓库检出路径：${REPO_ROOT}"
echo "✔ 状态仓库：${REMOTE_URL}（装配时自动使用）"
echo
echo "接下来："
echo "  1. 在 Claude Code 里运行 /web-setup 连接 GitHub（首次一次即可）"
echo "  2. 对 Claude 说：/new-briefing 〈主题〉 —— 自动装配任务并推送，然后照指引创建 Routine"
