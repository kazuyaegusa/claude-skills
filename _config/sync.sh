#!/bin/bash
# Claude Code スキル・設定 自動同期スクリプト
#
# launchd から定期実行される。手動実行も可。
# 動作: ローカル変更を push + リモート変更を pull

SKILLS_DIR="$HOME/.claude/skills"
CLAUDE_DIR="$HOME/.claude"
LOG="$HOME/.claude/sync.log"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOG"; }

# Git リポジトリでなければ終了
if [ ! -d "$SKILLS_DIR/.git" ]; then
    log "ERROR: $SKILLS_DIR is not a git repo"
    exit 1
fi

cd "$SKILLS_DIR" || exit 1

# ローカルの設定変更を _config/ に反映（CLAUDE.md, settings.json, commands/）
sync_config_to_repo() {
    local changed=false

    if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
        if ! diff -q "$CLAUDE_DIR/CLAUDE.md" "$SKILLS_DIR/_config/CLAUDE.md" > /dev/null 2>&1; then
            cp "$CLAUDE_DIR/CLAUDE.md" "$SKILLS_DIR/_config/CLAUDE.md"
            changed=true
        fi
    fi

    if [ -f "$CLAUDE_DIR/settings.json" ]; then
        if ! diff -q "$CLAUDE_DIR/settings.json" "$SKILLS_DIR/_config/settings.json" > /dev/null 2>&1; then
            cp "$CLAUDE_DIR/settings.json" "$SKILLS_DIR/_config/settings.json"
            changed=true
        fi
    fi

    for cmd in "$CLAUDE_DIR/commands/"*.md; do
        [ -f "$cmd" ] || continue
        filename=$(basename "$cmd")
        if ! diff -q "$cmd" "$SKILLS_DIR/_config/commands/$filename" > /dev/null 2>&1; then
            mkdir -p "$SKILLS_DIR/_config/commands"
            cp "$cmd" "$SKILLS_DIR/_config/commands/$filename"
            changed=true
        fi
    done

    echo "$changed"
}

# ローカル変更を commit + push
push_local() {
    # 設定ファイルの変更を取り込む
    sync_config_to_repo > /dev/null

    # 未追跡・変更ファイルがあれば commit
    if [ -n "$(git status --porcelain)" ]; then
        git add -A
        git commit -m "auto-sync: $(hostname) $(date '+%Y-%m-%d %H:%M')" --no-gpg-sign 2>/dev/null
        log "COMMIT: local changes committed"
    fi

    # push（競合時は pull --rebase してからリトライ）
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

    # _config/ の内容をローカル設定に反映
    if [ -f "$SKILLS_DIR/_config/CLAUDE.md" ]; then
        cp "$SKILLS_DIR/_config/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
    fi
    if [ -f "$SKILLS_DIR/_config/settings.json" ]; then
        cp "$SKILLS_DIR/_config/settings.json" "$CLAUDE_DIR/settings.json"
    fi
    for cmd in "$SKILLS_DIR/_config/commands/"*.md; do
        [ -f "$cmd" ] || continue
        cp "$cmd" "$CLAUDE_DIR/commands/"
    done
}

# メイン
log "SYNC START"
push_local
pull_remote
log "SYNC DONE"
