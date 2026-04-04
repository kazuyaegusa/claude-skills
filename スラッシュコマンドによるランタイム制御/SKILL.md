# スラッシュコマンドによるランタイム制御

> チャット内で `/model`、`/mode`、`/dir`、`/cron` 等のスラッシュコマンドを実行し、エージェントの動作パラメータをリアルタイムで変更する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: claude-code-workflow

## なぜ使うのか

ターミナルに戻らず、チャット内で完結してモデル切り替えや権限モード変更、作業ディレクトリ移動ができれば、モバイルからでも柔軟に操作できる

## いつ使うのか

エージェントの設定をチャットから動的に変更したい、定期タスクをセットアップしたい場合

## やり方

1. チャットメッセージが `/` で始まるか判定
2. コマンドをパース（例: `/model switch gpt-4`）
3. 対応する内部関数を実行（モデル設定変更、セッション切り替え等）
4. 結果をチャットに返信
5. `/cron add` の場合はcron式をパースしてスケジューラに登録

### 入力

- スラッシュコマンド文字列
- エージェントの状態管理データ

### 出力

- 設定変更の確認メッセージ
- cronジョブの登録完了通知

## 使うツール・ライブラリ

- コマンドパーサー
- cron式パーサー（robfig/cron等）

## コード例

```
if strings.HasPrefix(msg, "/") {
  cmd, args := parseCommand(msg)
  switch cmd {
    case "model":
      switchModel(args)
    case "cron":
      registerCron(args)
    case "dir":
      changeWorkDir(args)
  }
}
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法
