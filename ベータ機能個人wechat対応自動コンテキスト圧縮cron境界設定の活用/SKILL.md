# ベータ機能（個人WeChat対応、自動コンテキスト圧縮、Cron境界設定）の活用

> cc-connect@beta（プレリリース版）限定機能として、個人WeChatへの接続、長いスレッドの自動コンテキスト圧縮、Cronジョブのセッション分離・タイムアウト設定等を利用する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

個人WeChatは公式APIがなく従来は接続困難だったが、ilink長時間ポーリングで実現。自動圧縮により長いスレッドでもトークン制限を超えず動作継続。Cronジョブを独立セッションで実行することで暴走タスクがボット全体を止めるリスクを回避

## いつ使うのか

個人WeChatからAIエージェントを操作したい場合、長時間の会話スレッドでトークン制限にかかる場合、Cronジョブの暴走を防ぎたい場合

## やり方

1. `npm install -g cc-connect@beta` でベータ版をインストール（または GitHub Releasesからプレリリースバイナリ取得）
2. config.tomlで `platform = "weixin"` を指定し、docs/weixin.md に従いilink認証（QRコードスキャン）
3. 自動圧縮: config.tomlで `auto_compress = true` を有効化（閾値超過時に自動でコンテキストトリミング）
4. Cron境界: `reset_on_idle_mins` や `cron` セクションで per-job timeout設定

### 入力

- cc-connect@beta（ベータ版）
- 個人WeChat ilink認証情報（QRログイン）
- config.tomlのauto_compress、reset_on_idle_mins設定

### 出力

- 個人WeChatからの操作可能なAIエージェント
- 自動圧縮により継続動作する長いスレッド
- タイムアウト・セッション分離されたCronジョブ

## 使うツール・ライブラリ

- cc-connect@beta
- Weixin (personal) ilink API
- 自動コンテキスト圧縮ロジック

## コード例

```
# ベータ版インストール
npm install -g cc-connect@beta

# config.toml
platform = "weixin"
auto_compress = true
reset_on_idle_mins = 60

# 個人WeChat認証
weixin setup
```

## 前提知識

- ローカル環境にAIエージェント（Claude Code CLI、Cursor、Gemini CLI等）がインストール済みであること
- チャットプラットフォーム（Telegram、Discord、Slack等）のアカウントとBot作成権限
- Node.js（npm経由インストールの場合）またはGo 1.22+（ソースビルドの場合）
- 基本的なコマンドライン操作とTOML設定ファイル編集の知識
- WebSocket/Long Polling等の接続方式の基本理解（トラブルシューティング時）

## 根拠

> 「Cron with boundaries — Run jobs in a fresh session each time and cap per-job timeouts so runaway tasks don't wedge the bot.」

> 「npm install -g cc-connect」

> 「/model switch <alias>」「/mode yolo」「/dir <path>」「/new [name]」「/cron add 0 6 * * * Summarize GitHub trending」等のコマンド例
