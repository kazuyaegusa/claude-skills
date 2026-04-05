# チャット経由でのセッション・設定管理

> チャットからスラッシュコマンド（/model, /mode, /dir, /new等）でエージェントのモデル切り替え、権限モード変更、作業ディレクトリ変更、セッション管理等を実行する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: claude-code-workflow

## なぜ使うのか

ターミナルに戻らずチャットだけで全ての操作を完結させるため。外出先やスマホからでも柔軟に設定を変更できるようにするため

## いつ使うのか

エージェントの動作設定を頻繁に切り替えたい場合、外出先から設定変更したい場合、チームメンバーが設定を変えられるようにしたい場合

## やり方

1. チャットで `/model` と送ると利用可能モデル一覧表示
2. `/model switch <alias>` でモデル切り替え
3. `/mode yolo` で自動承認モードに変更（ツール実行を逐一承認不要に）
4. `/dir <path>` で作業ディレクトリ変更
5. `/new [name]` で新規セッション開始
6. `/cron add 0 6 * * * <タスク>` でcron登録

### 入力

- スラッシュコマンド（/model, /mode, /dir, /new, /cron等）

### 出力

- エージェント設定の変更
- 新規セッション作成
- 作業ディレクトリ変更
- cron登録

## 使うツール・ライブラリ

- cc-connect内蔵コマンドパーサー

## コード例

```
/model switch claude-sonnet-4
/mode yolo
/dir /path/to/project
/new feature-xyz
/cron add 0 6 * * * Summarize GitHub trending
```

## 前提知識

- ローカル環境にAIエージェント（Claude Code CLI、Cursor、Gemini CLI等）がインストール済みであること
- チャットプラットフォーム（Telegram、Discord、Slack等）のアカウントとBot作成権限
- Node.js（npm経由インストールの場合）またはGo 1.22+（ソースビルドの場合）
- 基本的なコマンドライン操作とTOML設定ファイル編集の知識
- WebSocket/Long Polling等の接続方式の基本理解（トラブルシューティング時）

## 根拠

> 「/model switch <alias>」「/mode yolo」「/dir <path>」「/new [name]」「/cron add 0 6 * * * Summarize GitHub trending」等のコマンド例
