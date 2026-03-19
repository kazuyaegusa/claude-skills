# ローカルAIエージェントのWebSocketブリッジ構築

> ローカルマシン上のCLI型AIエージェント（Claude Code, Cursor Agent等）をメッセンジャープラットフォーム（Feishu, Telegram, Discord等）と双方向接続し、チャットUIから操作可能にする。

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントはターミナルでしか動かせないため、モバイルデバイスや外出先からのアクセスが困難。また、チーム内でエージェントを共有する際、各自がCLIをセットアップする必要がある。チャットアプリ経由にすることで、既存のコミュニケーションフローに組み込め、非エンジニアでも利用可能になる。

## いつ使うのか

ローカルで動くAIエージェントを、スマホ・タブレット・リモート環境から操作したい時。複数人でエージェントを共有したい時。公開IPなしでボットを運用したい時。

## やり方

1. cc-connectをnpm or バイナリでインストール (`npm install -g cc-connect`)
2. `~/.cc-connect/config.toml` を作成し、agent type（claude/cursor/gemini等）とplatform（telegram/slack/discord等）を指定
3. 各プラットフォームのBot Token/App Credentialを取得し、config.tomlに記載
4. `cc-connect` コマンドで起動すると、指定したチャットアプリでボットが応答開始
5. チャットから `/new`, `/model`, `/mode` 等のコマンドでセッション管理・モデル切替・権限モード変更が可能
6. 画像・音声メッセージも送信でき、cc-connectがSTT/TTS・マルチモーダル変換を行ってエージェントに転送

### 入力

- ローカルにインストール済みのAIエージェント（Claude Code, Cursor Agent, Gemini CLI等）
- メッセンジャープラットフォームのBot Token/Webhook URL
- config.tomlに記載するagent/platform設定

### 出力

- チャットアプリ上で動作するAIエージェントボット
- セッション管理・モデル切替・権限制御機能
- 音声・画像のマルチモーダル入力対応
- エージェントが生成したファイル・画像のチャット送信

## 使うツール・ライブラリ

- cc-connect（Go製、npm or バイナリ配布）
- 対応エージェント: Claude Code, Codex, Cursor Agent, Qoder CLI, Gemini CLI, OpenCode, iFlow CLI
- 対応プラットフォーム: Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, LINE, QQ, QQ Bot

## コード例

```
# インストール
npm install -g cc-connect

# 設定ファイル準備
mkdir -p ~/.cc-connect
cp config.example.toml ~/.cc-connect/config.toml
vim ~/.cc-connect/config.toml

# 起動
./cc-connect

# チャットから操作例
/new my-session       # 新規セッション作成
/model sonnet        # モデル切替
/mode yolo           # 全ツール自動承認モード
/cron add 0 6 * * * Summarize GitHub trending  # 定時タスク設定
```

## 前提知識

- ローカルマシンにNode.js or Go環境（cc-connectインストールに必要）
- Claude Code, Cursor, Gemini CLI等のAIエージェントがインストール済みであること
- メッセンジャープラットフォーム（Telegram/Slack/Discord等）のBot Token取得方法の基礎知識
- TOML形式の設定ファイル編集スキル
- WebSocket/Long Polling等の接続方式の概念理解（必須ではないが理解があると設定が楽）

## 根拠

> 「7 AI Agents — Claude Code, Codex, Cursor Agent, Qoder CLI, Gemini CLI, OpenCode, iFlow CLI.」（7種類のエージェント対応）

> 「9 Chat Platforms — Feishu, DingTalk, Slack, Telegram, Discord, WeChat Work, LINE, QQ, QQ Bot (Official). Most need zero public IP.」（9プラットフォーム対応、公開IP不要）

> 「npm install -g cc-connect」（npmでのインストール方法）
