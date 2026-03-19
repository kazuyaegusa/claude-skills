# AIエージェントへのファイル送信機能の実装

> AIエージェントがローカルで生成したスクリーンショット・グラフ・PDF等を、チャットアプリに自動送信させる。

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントが作成した成果物をユーザーが確認するには、通常ローカルファイルシステムにアクセスする必要がある。チャットに直接送信されれば、モバイルからでもすぐに確認でき、フィードバックループが高速化する。

## いつ使うのか

エージェントが生成したグラフ・レポート・スクリーンショット等を即座に確認したい時。モバイルから成果物を受け取りたい時。

## やり方

1. cc-connectをアップグレード後、チャットで `/bind setup` or `/cron setup` を実行し、プロジェクトメモリファイルにcc-connect送信コマンドを注入
2. エージェントが画像・PDFを生成した際、`cc-connect send --image /path/to/chart.png` or `cc-connect send --file /path/to/report.pdf` を実行
3. cc-connectが現在のチャットセッションに添付ファイルとして送信
4. config.tomlで `attachment_send = "on"` を設定（デフォルトon、offにすると無効化）

### 入力

- エージェントが生成したファイルの絶対パス
- cc-connect send コマンド

### 出力

- チャットアプリ内に添付ファイルが送信される

## 使うツール・ライブラリ

- cc-connect send --image/--file コマンド

## コード例

```
# セットアップ（初回のみ）
/bind setup

# エージェント側からの送信例
cc-connect send --image /absolute/path/to/chart.png
cc-connect send --file /absolute/path/to/report.pdf
cc-connect send --file /path/to/doc.pdf --image /path/to/fig.png

# config.toml で無効化する場合
[global]
attachment_send = "off"
```

## 前提知識

- ローカルマシンにNode.js or Go環境（cc-connectインストールに必要）
- Claude Code, Cursor, Gemini CLI等のAIエージェントがインストール済みであること
- メッセンジャープラットフォーム（Telegram/Slack/Discord等）のBot Token取得方法の基礎知識
- TOML形式の設定ファイル編集スキル
- WebSocket/Long Polling等の接続方式の概念理解（必須ではないが理解があると設定が楽）

## 根拠

> 「cc-connect send --image /absolute/path/to/chart.png」（添付ファイル送信コマンド）
