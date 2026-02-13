#!/bin/bash
# Claude Code 環境セットアップスクリプト
#
# 使い方:
#   git clone https://github.com/kazuyaegusa/claude-skills.git
#   cd claude-skills
#   bash setup-env.sh
#
# このスクリプトは以下を行う:
#   1. ~/.claude/skills/ にスキルをシンボリックリンク
#   2. ~/.claude/CLAUDE.md をコピー
#   3. ~/.claude/settings.json をコピー
#   4. ~/.claude/commands/ をコピー
#   5. MCP 設定のテンプレートを配置
#   6. 自動同期 launchd エージェントを登録（5分おき）

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"

echo "=== Claude Code 環境セットアップ ==="
echo "  リポジトリ: $SCRIPT_DIR"
echo "  Claude 設定: $CLAUDE_DIR"
echo

# Claude Code がインストールされているか確認
if ! command -v claude &> /dev/null; then
    echo "エラー: Claude Code がインストールされていません。"
    echo "  https://docs.anthropic.com/en/docs/claude-code からインストールしてください。"
    exit 1
fi

# ~/.claude ディレクトリ作成
mkdir -p "$CLAUDE_DIR"
mkdir -p "$CLAUDE_DIR/commands"

# 1. スキルのセットアップ
# このリポジトリ自体が skills/ に配置される想定
if [ "$SCRIPT_DIR" != "$CLAUDE_DIR/skills" ]; then
    echo "[1/5] スキルディレクトリをセットアップ..."
    if [ -d "$CLAUDE_DIR/skills" ] && [ ! -L "$CLAUDE_DIR/skills" ]; then
        echo "  既存の skills/ をバックアップ → skills.bak/"
        mv "$CLAUDE_DIR/skills" "$CLAUDE_DIR/skills.bak"
    fi
    ln -sfn "$SCRIPT_DIR" "$CLAUDE_DIR/skills"
    echo "  完了: $CLAUDE_DIR/skills → $SCRIPT_DIR"
else
    echo "[1/5] スキル: 既に正しい位置にあります"
fi

# 2. CLAUDE.md をコピー
echo "[2/5] CLAUDE.md をセットアップ..."
if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
    echo "  既存の CLAUDE.md をバックアップ → CLAUDE.md.bak"
    cp "$CLAUDE_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md.bak"
fi
cp "$SCRIPT_DIR/_config/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"
echo "  完了"

# 3. settings.json をコピー
echo "[3/5] settings.json をセットアップ..."
if [ -f "$CLAUDE_DIR/settings.json" ]; then
    echo "  既存の settings.json をバックアップ → settings.json.bak"
    cp "$CLAUDE_DIR/settings.json" "$CLAUDE_DIR/settings.json.bak"
fi
cp "$SCRIPT_DIR/_config/settings.json" "$CLAUDE_DIR/settings.json"
echo "  完了"

# 4. commands/ をコピー
echo "[4/5] commands/ をセットアップ..."
for cmd in "$SCRIPT_DIR/_config/commands/"*.md; do
    if [ -f "$cmd" ]; then
        filename=$(basename "$cmd")
        cp "$cmd" "$CLAUDE_DIR/commands/$filename"
        echo "  コピー: $filename"
    fi
done
echo "  完了"

# 5. MCP 設定テンプレート
echo "[5/5] MCP 設定..."
if [ -f "$CLAUDE_DIR/.mcp.json" ]; then
    echo "  既存の .mcp.json が見つかりました（スキップ）"
    echo "  手動で更新する場合: $SCRIPT_DIR/_config/mcp.json.template を参照"
else
    echo "  テンプレートを配置しました"
    echo "  手動で設定する場合: $SCRIPT_DIR/_config/mcp.json.template を編集して"
    echo "  ~/.claude/.mcp.json にコピーしてください"
fi

# 6. 自動同期 launchd エージェント登録
echo "[6/6] 自動同期デーモンをセットアップ..."
PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_FILE="$PLIST_DIR/com.claude-skills-sync.plist"
mkdir -p "$PLIST_DIR"

# HOME パスをこのデバイスに合わせて plist を生成
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
        <string>-c</string>
        <string>\$HOME/.claude/skills/_config/sync.sh</string>
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
        <string>$HOME</string>
    </dict>
</dict>
</plist>
PLIST_EOF

launchctl unload "$PLIST_FILE" 2>/dev/null
launchctl load "$PLIST_FILE"
echo "  完了: 5分おきに自動同期（ログイン時にも実行）"

echo
echo "=== セットアップ完了 ==="
echo
echo "確認:"
echo "  スキル:    $(ls -1 "$CLAUDE_DIR/skills/" | grep -c SKILL.md 2>/dev/null || echo 0) 個"
echo "  コマンド:  $(ls -1 "$CLAUDE_DIR/commands/"*.md 2>/dev/null | wc -l | tr -d ' ') 個"
echo "  CLAUDE.md: $([ -f "$CLAUDE_DIR/CLAUDE.md" ] && echo '配置済み' || echo '未配置')"
echo "  settings:  $([ -f "$CLAUDE_DIR/settings.json" ] && echo '配置済み' || echo '未配置')"
echo
echo "Claude Code を再起動すると設定が反映されます。"
