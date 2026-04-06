# 独立制御レイヤーによる通知モード切り替え

> 音声（enabled）・デスクトップ通知（desktop_notifications）・モバイル通知（mobile_notify.enabled）を独立したフラグで制御し、用途に応じて組み合わせる

- 出典: https://github.com/PeonPing/peon-ping
- 投稿者: PeonPing
- カテゴリ: dev-tool

## なぜ使うのか

会議中は音声のみオフ、ペアプロ時は通知のみオフ、外出時はモバイルのみオン等、状況に応じた最適な通知形態が異なる。3つを独立制御することで柔軟な使い分けが可能

## いつ使うのか

会議・ペアプロ・集中作業等で一部通知のみ抑制したい時、外出中にモバイルのみ通知を受け取りたい時

## やり方

1. `config.json`に`enabled`（音声マスタースイッチ）、`desktop_notifications`（デスクトップポップアップ）、`mobile_notify.enabled`（モバイルプッシュ）を独立設定
2. `peon pause`で音声のみオフ、`peon notifications off`でデスクトップ通知のみオフ
3. `peon mobile ntfy <topic>`でモバイル通知を有効化、`peon mobile off`で無効化
4. 各イベント時、peon.shが3つのフラグを個別チェックし、有効な通知チャネルのみ実行

### 入力

- config.jsonの3つの独立フラグ（enabled/desktop_notifications/mobile_notify.enabled）

### 出力

- 状況に応じた最適な通知形態（音声のみ/通知のみ/モバイルのみ/組み合わせ）

## 使うツール・ライブラリ

- config.json
- CLIコマンド（peon pause/notifications/mobile）

## コード例

```
# 会議中：音声オフ、通知は残す
peon pause

# ペアプロ：通知オフ、音声は残す
peon notifications off

# 外出中：モバイルのみ
peon pause
peon notifications off
peon mobile ntfy my-topic

// config.json
{
  "enabled": false,  // 音声オフ
  "desktop_notifications": true,  // デスクトップ通知オン
  "mobile_notify": {
    "enabled": true,  // モバイル通知オン
    "provider": "ntfy",
    "topic": "my-topic"
  }
}
```

## 前提知識

- Claude Code/Cursor/Windsurf等のフック機能を持つAI開発環境の基礎知識
- シェルスクリプト（bash/PowerShell）の基本的な読み書き
- JSON設定ファイルの編集経験
- SSH/devcontainer/Codespacesの基本（リモート通知機能を使う場合）
- Model Context Protocol（MCP）の概念（MCP機能を使う場合）

## 根拠

> 「Coding on a remote server or inside a container? peon-ping auto-detects SSH sessions, devcontainers, and Codespaces, then routes audio and notifications through a lightweight relay」（リモート対応の自動検出機能）

> 「enabled, desktop_notifications, mobile_notify.enabled — Three independent controls that can be mixed and matched」（独立制御の設計思想）
