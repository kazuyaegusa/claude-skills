# エージェント生成ファイルのチャット送り返し機能

> AIエージェントがローカルで生成したスクリーンショット、PDF、グラフ等のファイルを、チャットアプリに自動的に送信する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントが生成したアウトプットをターミナルで確認する必要がなくなり、チャット内で完結した作業フローが実現する

## いつ使うのか

エージェントが生成したチャートやレポートをチャットで即座に確認したい場合

## やり方

1. エージェントのシステムプロンプトに `cc-connect send --image <path>` コマンドの説明を注入
2. エージェントがファイル生成後、このコマンドを実行
3. cc-connectがファイルパスを受け取り、チャットプラットフォームのファイルアップロードAPIを呼び出し
4. チャットに画像・ファイルとして表示
5. config.tomlの `attachment_send` で機能のON/OFF制御

### 入力

- エージェントが生成したファイルの絶対パス
- `cc-connect send --image/--file <path>` コマンド

### 出力

- チャットアプリ上に表示された画像・ファイル

## 使うツール・ライブラリ

- チャットプラットフォームのFile Upload API
- Feishu Image Upload API
- Telegram sendPhoto API

## コード例

```
# エージェント内で実行
cc-connect send --image /tmp/chart.png
cc-connect send --file /tmp/report.pdf

# config.toml
attachment_send = "on"  # or "off" to disable
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法

## 根拠

> "Voice & Images — Send voice messages or screenshots; cc-connect handles STT/TTS and multimodal forwarding"

> "cc-connect send --image /absolute/path/to/chart.png"
