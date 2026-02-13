#!/bin/bash
# Claude Code 環境セットアップ（ブートストラップ対応）
#
# === 別デバイスでの使い方（1コマンドで完了） ===
#
#   curl -sL https://raw.githubusercontent.com/kazuyaegusa/claude-skills/main/setup-env.sh | bash
#
# === または手動 ===
#
#   git clone https://github.com/kazuyaegusa/claude-skills.git /tmp/claude-skills-setup
#   bash /tmp/claude-skills-setup/setup-env.sh
#

set -e

REPO_URL="https://github.com/kazuyaegusa/claude-skills.git"
CLAUDE_DIR="$HOME/.claude"
SKILLS_DIR="$CLAUDE_DIR/skills"

echo "=== Claude Code 環境セットアップ ==="
echo

# --- 前提チェック ---
if ! command -v git &> /dev/null; then
    echo "エラー: git がインストールされていません。"
    exit 1
fi

# --- macOS チェック ---
if [ "$(uname)" != "Darwin" ]; then
    echo "警告: macOS 以外の環境です。launchd 同期はスキップされます。"
fi

# --- Step 1: skills/ ディレクトリにリポジトリを配置 ---
echo "[1/6] スキルリポジトリをセットアップ..."

if [ -d "$SKILLS_DIR/.git" ]; then
    # 既に Git リポジトリがある → pull で更新
    echo "  既存リポジトリを検出。最新に更新します..."
    git -C "$SKILLS_DIR" pull --rebase origin main 2>/dev/null || true
    echo "  完了（pull）"
elif [ -d "$SKILLS_DIR" ]; then
    # ディレクトリはあるが Git リポジトリではない → バックアップして clone
    echo "  既存の skills/ をバックアップ → skills.bak/"
    mv "$SKILLS_DIR" "$SKILLS_DIR.bak.$(date +%s)"
    git clone "$REPO_URL" "$SKILLS_DIR"
    echo "  完了（clone）"
else
    # 何もない → clone
    mkdir -p "$CLAUDE_DIR"
    git clone "$REPO_URL" "$SKILLS_DIR"
    echo "  完了（clone）"
fi

# --- Step 2: CLAUDE.md ---
echo "[2/6] CLAUDE.md をセットアップ..."
if [ -f "$SKILLS_DIR/_config/CLAUDE.md" ]; then
    if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
        cp "$CLAUDE_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md.bak"
    fi
    cp "$SKILLS_DIR/_config/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
    echo "  完了"
else
    echo "  スキップ（_config/CLAUDE.md が見つかりません）"
fi

# --- Step 3: settings.json ---
echo "[3/6] settings.json をセットアップ..."
if [ -f "$SKILLS_DIR/_config/settings.json" ]; then
    if [ -f "$CLAUDE_DIR/settings.json" ]; then
        cp "$CLAUDE_DIR/settings.json" "$CLAUDE_DIR/settings.json.bak"
    fi
    cp "$SKILLS_DIR/_config/settings.json" "$CLAUDE_DIR/settings.json"
    echo "  完了"
else
    echo "  スキップ（_config/settings.json が見つかりません）"
fi

# --- Step 4: commands/ ---
echo "[4/6] commands/ をセットアップ..."
mkdir -p "$CLAUDE_DIR/commands"
count=0
for cmd in "$SKILLS_DIR/_config/commands/"*.md; do
    [ -f "$cmd" ] || continue
    cp "$cmd" "$CLAUDE_DIR/commands/"
    count=$((count + 1))
done
echo "  完了（${count} コマンド）"

# --- Step 5: MCP 設定 ---
echo "[5/6] MCP 設定..."
if [ -f "$CLAUDE_DIR/.mcp.json" ]; then
    echo "  既存の .mcp.json があります（スキップ）"
else
    echo "  テンプレート: $SKILLS_DIR/_config/mcp.json.template"
    echo "  必要に応じて手動で ~/.claude/.mcp.json を作成してください"
fi

# --- Step 6: 自動同期 (macOS のみ) ---
echo "[6/6] 自動同期デーモン..."
if [ "$(uname)" = "Darwin" ]; then
    PLIST_DIR="$HOME/Library/LaunchAgents"
    PLIST_FILE="$PLIST_DIR/com.claude-skills-sync.plist"
    mkdir -p "$PLIST_DIR"

    cat > "$PLIST_FILE" << PLIST_EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.claude-skills-sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${SKILLS_DIR}/_config/sync.sh</string>
    </array>
    <key>StartInterval</key>
    <integer>300</integer>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/tmp/claude-skills-sync.err</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin</string>
        <key>HOME</key>
        <string>${HOME}</string>
    </dict>
</dict>
</plist>
PLIST_EOF

    launchctl unload "$PLIST_FILE" 2>/dev/null || true
    launchctl load "$PLIST_FILE"
    echo "  完了（5分おき自動同期 + ログイン時実行）"
else
    echo "  スキップ（macOS 以外）"
fi

# --- 検証 ---
echo
echo "=== セットアップ完了 ==="
echo
skill_count=$(find "$SKILLS_DIR" -maxdepth 2 -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
cmd_count=$(ls "$CLAUDE_DIR/commands/"*.md 2>/dev/null | wc -l | tr -d ' ')
echo "  スキル:     ${skill_count} 個"
echo "  コマンド:   ${cmd_count} 個"
echo "  CLAUDE.md:  $([ -f "$CLAUDE_DIR/CLAUDE.md" ] && echo '配置済み' || echo '未配置')"
echo "  settings:   $([ -f "$CLAUDE_DIR/settings.json" ] && echo '配置済み' || echo '未配置')"
echo "  自動同期:   $(launchctl list 2>/dev/null | grep -q claude-skills && echo '動作中' || echo '未設定')"
echo

# スキル一覧を表示
echo "  インストール済みスキル:"
for skill in "$SKILLS_DIR"/*/SKILL.md; do
    [ -f "$skill" ] || continue
    dirname=$(basename "$(dirname "$skill")")
    echo "    - /$dirname"
done

echo
echo "Claude Code を再起動すると設定が反映されます。"
