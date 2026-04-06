# Hook登録によるイベント駆動型通知実装

> AIエージェントのライフサイクルイベント（SessionStart/Stop/PermissionRequest等）に音声再生・通知スクリプトをフックとして登録し、イベント発火時に自動実行する

- 出典: https://github.com/PeonPing/peon-ping
- 投稿者: PeonPing
- カテゴリ: claude-code-workflow

## なぜ使うのか

ポーリングや手動確認ではリアルタイム性が低く、開発者の認知負荷が高い。イベント駆動ならエージェント状態変化の瞬間に確実に通知でき、復帰タイミングを逃さない

## いつ使うのか

Claude Code、Cursor、Windsurf、Gemini CLI等のフック機能を持つAI開発環境で、エージェント状態変化をリアルタイムに知りたい時

## やり方

1. `~/.claude/settings.json`の`hooks`セクションに各イベント（SessionStart/Stop/PermissionRequest等）を定義
2. 各イベントに`peon.sh`スクリプトへのパスをコマンドとして登録
3. `peon.sh`内でPythonブロックがイベント名をCESPカテゴリ（session.start/task.complete/input.required等）にマッピング
4. マニフェストから該当カテゴリの音声ファイルをランダム選択（前回と重複回避）
5. `afplay`（macOS）、`pw-play/paplay/ffplay`（Linux）、PowerShell MediaPlayer（Windows）で非同期再生
6. 並行してターミナルタブタイトル更新＋デスクトップ通知送信

### 入力

- AIエージェントのイベントフック機能（SessionStart/Stop/PermissionRequest等）
- 音声ファイル（WAV/OGG/MP3等）を含むCESP準拠の音声パック
- config.json（volume/categories/pack設定）

### 出力

- イベント発火時の即座の音声再生
- 大型オーバーレイまたは標準システム通知
- ターミナルタブタイトル更新（● project: working.../✓ done/✗ error）

## 使うツール・ライブラリ

- afplay（macOS内蔵）
- pw-play/paplay/ffplay/mpv/aplay（Linux）
- PowerShell MediaPlayer（Windows）
- Python 3（イベントマッピング・設定読み込み）
- JXA Cocoa（macOS大型オーバーレイ）
- terminal-notifier/osascript（macOS標準通知）

## コード例

```
# ~/.claude/settings.json
{
  "hooks": {
    "SessionStart": [{"command": "bash ~/.claude/hooks/peon-ping/peon.sh"}],
    "Stop": [{"command": "bash ~/.claude/hooks/peon-ping/peon.sh"}],
    "PermissionRequest": [{"command": "bash ~/.claude/hooks/peon-ping/peon.sh"}]
  }
}

# peon.sh内イベントマッピング（Python）
event_map = {
  'SessionStart': 'session.start',
  'Stop': 'task.complete',
  'PermissionRequest': 'input.required',
  'PostToolUseFailure': 'task.error'
}
cesp_category = event_map.get(hook_event, None)
```

## 前提知識

- Claude Code/Cursor/Windsurf等のフック機能を持つAI開発環境の基礎知識
- シェルスクリプト（bash/PowerShell）の基本的な読み書き
- JSON設定ファイルの編集経験
- SSH/devcontainer/Codespacesの基本（リモート通知機能を使う場合）
- Model Context Protocol（MCP）の概念（MCP機能を使う場合）
