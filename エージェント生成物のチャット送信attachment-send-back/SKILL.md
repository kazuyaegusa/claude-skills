# エージェント生成物のチャット送信（Attachment Send-Back）

> エージェントがローカルで生成したスクリーンショット、グラフ、PDF、バンドル等のファイルを、チャットに自動送信する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントが生成した成果物をチャット内で即座に共有・確認できるようにするため。ターミナルとチャットを行き来する手間を省くため

## いつ使うのか

エージェントが生成したグラフ・レポート・スクリーンショット等をチャットで即座に共有したい場合

## やり方

1. config.tomlで `attachment_send = "on"` を設定
2. エージェントが `/bind setup` または `/cron setup` で初期化済みであることを確認（cc-connect指示をメモリファイルに注入）
3. エージェントが `cc-connect send --image /path/to/chart.png` または `cc-connect send --file /path/to/report.pdf` を実行すると、現在のチャットに送信される
4. Feishu、Telegram等対応プラットフォームでファイルが表示される

### 入力

- エージェントが生成したファイルの絶対パス
- config.tomlの `attachment_send = "on"`

### 出力

- チャットに送信された画像またはファイル

## 使うツール・ライブラリ

- cc-connect send コマンド
- Feishu/Telegram等のファイルアップロードAPI

## コード例

```
# config.toml
attachment_send = "on"

# エージェント内から実行
cc-connect send --image /absolute/path/to/chart.png
cc-connect send --file /absolute/path/to/report.pdf
```

## 前提知識

- ローカル環境にAIエージェント（Claude Code CLI、Cursor、Gemini CLI等）がインストール済みであること
- チャットプラットフォーム（Telegram、Discord、Slack等）のアカウントとBot作成権限
- Node.js（npm経由インストールの場合）またはGo 1.22+（ソースビルドの場合）
- 基本的なコマンドライン操作とTOML設定ファイル編集の知識
- WebSocket/Long Polling等の接続方式の基本理解（トラブルシューティング時）

## 根拠

> 「cc-connect send --image /absolute/path/to/chart.png」「cc-connect send --file /absolute/path/to/report.pdf」
