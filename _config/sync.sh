#!/bin/bash
# Claude Code スキル・設定 自動同期スクリプト
#
# launchd から定期実行される。手動実行も可。
# 動作: ローカル変更を push + リモート変更を pull
#
# 同期対象:
#   - ~/.claude/CLAUDE.md        （グローバル開発ルール）
#   - ~/.claude/settings.json    （Claude Code 設定）
#   - ~/.claude/keybindings.json （キーバインド設定）
#   - ~/.claude/commands/*.md    （スラッシュコマンド）
#   - ~/.claude/skills/          （スキル本体 — Git リポジトリ全体）

SKILLS_DIR="$HOME/.claude/skills"
CLAUDE_DIR="$HOME/.claude"
CONFIG_DIR="$SKILLS_DIR/_config"
LOG="$HOME/.claude/sync.log"

# ログファイルが大きくなりすぎたら切り詰める（1MB上限）
if [ -f "$LOG" ] && [ "$(wc -c < "$LOG" 2>/dev/null)" -gt 1048576 ]; then
    tail -200 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
fi

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOG"; }

# Git リポジトリでなければ終了
if [ ! -d "$SKILLS_DIR/.git" ]; then
    log "ERROR: $SKILLS_DIR is not a git repo"
    exit 1
fi

cd "$SKILLS_DIR" || exit 1

# 単一ファイルの差分コピー（ローカル → リポジトリ）
sync_file_to_repo() {
    local src="$1" dst="$2"
    [ -f "$src" ] || return 1
    if ! diff -q "$src" "$dst" > /dev/null 2>&1; then
        cp "$src" "$dst"
        return 0
    fi
    return 1
}

# ローカルの設定変更を _config/ に反映
sync_config_to_repo() {
    local changed=false

    # CLAUDE.md
    sync_file_to_repo "$CLAUDE_DIR/CLAUDE.md" "$CONFIG_DIR/CLAUDE.md" && changed=true

    # settings.json
    sync_file_to_repo "$CLAUDE_DIR/settings.json" "$CONFIG_DIR/settings.json" && changed=true

    # keybindings.json
    if [ -f "$CLAUDE_DIR/keybindings.json" ]; then
        sync_file_to_repo "$CLAUDE_DIR/keybindings.json" "$CONFIG_DIR/keybindings.json" && changed=true
    fi

    # commands/*.md
    mkdir -p "$CONFIG_DIR/commands"
    for cmd in "$CLAUDE_DIR/commands/"*.md; do
        [ -f "$cmd" ] || continue
        local filename
        filename=$(basename "$cmd")
        sync_file_to_repo "$cmd" "$CONFIG_DIR/commands/$filename" && changed=true
    done

    # リポジトリ側にだけ残っているコマンドを削除（ローカルで消されたもの）
    for repo_cmd in "$CONFIG_DIR/commands/"*.md; do
        [ -f "$repo_cmd" ] || continue
        local filename
        filename=$(basename "$repo_cmd")
        if [ ! -f "$CLAUDE_DIR/commands/$filename" ]; then
            rm "$repo_cmd"
            changed=true
        fi
    done

    echo "$changed"
}

# ローカル変更を commit + push
push_local() {
    sync_config_to_repo > /dev/null

    if [ -n "$(git status --porcelain)" ]; then
        git add -A
        git commit -m "auto-sync: $(hostname) $(date '+%Y-%m-%d %H:%M')" --no-gpg-sign 2>/dev/null
        log "COMMIT: local changes committed"
    fi

    if ! git push origin main 2>/dev/null; then
        git pull --rebase origin main 2>/dev/null
        git push origin main 2>/dev/null
    fi
    log "PUSH: done"
}

# リモート変更を pull + 設定に反映
pull_remote() {
    git pull --rebase origin main 2>/dev/null
    log "PULL: done"

    # _config/ → ローカル設定
    [ -f "$CONFIG_DIR/CLAUDE.md" ] && cp "$CONFIG_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
    [ -f "$CONFIG_DIR/settings.json" ] && cp "$CONFIG_DIR/settings.json" "$CLAUDE_DIR/settings.json"
    [ -f "$CONFIG_DIR/keybindings.json" ] && cp "$CONFIG_DIR/keybindings.json" "$CLAUDE_DIR/keybindings.json"

    mkdir -p "$CLAUDE_DIR/commands"
    for cmd in "$CONFIG_DIR/commands/"*.md; do
        [ -f "$cmd" ] || continue
        cp "$cmd" "$CLAUDE_DIR/commands/"
    done
}

# メイン
log "SYNC START"
push_local
pull_remote
log "SYNC DONE"
