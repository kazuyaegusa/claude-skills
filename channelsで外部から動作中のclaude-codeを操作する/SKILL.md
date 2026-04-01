# Channelsで外部から動作中のClaude Codeを操作する

> Telegram/Discordから、動いているClaude Codeセッションにメッセージをプッシュしてリアルタイムに指示を出す

- 出典: https://x.com/ai_masaou/status/2035288249581617200
- 投稿者: まさお@AI駆動開発
- カテゴリ: claude-code-workflow

## なぜ使うのか

CIの結果やエラー通知を自動で流し込んだり、スマホから遠隔操作したりすることで、ターミナルに張り付かなくても汎用AIエージェントとして機能させられる

## いつ使うのか

CI/CDの結果をClaude Codeに自動通知したい時、スマホから自宅のClaude Codeを遠隔操作したい時、ターミナルのClaude Codeを外部トリガーで動かしたい時

### 具体的な適用場面

- CLAUDE.mdが長くなり、重要な指示が守られなくなった時
- PRレビュー時に最新のdiffを自動で読み込ませたい時
- CI/CD結果やエラー通知をClaude Codeセッションに直接流し込みたい時
- スマホから自宅PCのClaude Codeを操作して作業させたい時
- 他人が作ったスキルをインストールする前に安全性を確認したい時

## やり方

1. Channelsプラグインをインストール
2. Telegram/Discordで認証を完了
3. スマホやWebhookからメッセージを送信すると、動作中のClaude Codeセッションに直接届く
4. Webhook受信にも対応しているため、CI結果やエラー通知を自動で流し込める
5. ハーネスを作り込んでおけば、チャンネル経由で呼び出すだけで汎用AIエージェントとして機能（オープンクローカー的な使い方）

### 入力

- Telegram/Discordアカウント
- 動作中のClaude Codeセッション
- Webhook（任意）

### 出力

- 外部からプッシュ可能なClaude Codeセッション
- CI結果・エラー通知の自動注入

## 使うツール・ライブラリ

- Claude Code Channels
- Telegram
- Discord

## 前提知識

- Claude Codeの基本的な使い方
- CLAUDE.mdの役割と記述方法
- Skillsの基本的な作成・インストール方法
- Telegram/Discordアカウント（Channels利用時）
- Claude Coworkデスクトップ版（Dispatch利用時）

## 根拠

> HumanLayerのブログで紹介された対策がこれ <important if="テストを書いている時">

> スキルMD内に !`gh pr diff` のように書くと読み込み時にコマンドが自動実行され、出力がコンテキストに注入される

> Telegram/Discordから、動いているClaude Codeセッションにメッセージをプッシュできる

> Claude Coworkのデスクトップアプリに追加されたリモートコントロール機能 スマホアプリからデスクトップのCoworkを操作できる「トランシーバー」

> ターミナルのClaude Codeを外から操作したい → Channels / デスクトップのClaude Coworkを外から操作したい → Dispatch
