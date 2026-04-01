# Dispatchでデスクトップ版Claude Coworkをリモート操作する

> スマホアプリからデスクトップのClaude Coworkを操作する「トランシーバー」機能。ローカルファイル、コネクタ、サンドボックス全てにアクセスしながらスマホから指示可能

- 出典: https://x.com/ai_masaou/status/2035288249581617200
- 投稿者: まさお@AI駆動開発
- カテゴリ: claude-code-workflow

## なぜ使うのか

ChannelsがターミナルのClaude Code向けなのに対し、DispatchはデスクトップGUI版向け。外出先からデスクトップ環境にアクセスして作業指示を出せる

## いつ使うのか

デスクトップのClaude Cowork（GUI版）を外から操作したい時、外出先からローカルファイルにアクセスして作業させたい時

### 具体的な適用場面

- CLAUDE.mdが長くなり、重要な指示が守られなくなった時
- PRレビュー時に最新のdiffを自動で読み込ませたい時
- CI/CD結果やエラー通知をClaude Codeセッションに直接流し込みたい時
- スマホから自宅PCのClaude Codeを操作して作業させたい時
- 他人が作ったスキルをインストールする前に安全性を確認したい時

## やり方

1. Claude Coworkのデスクトップアプリを起動
2. Dispatch機能を有効化
3. スマホアプリから接続
4. スマホから指示を飛ばすと、デスクトップのCoworkが実行
5. 制約: PCがスリープすると停止（クラウド実行ではなくリモコン）

### 入力

- デスクトップのClaude Cowork
- スマホアプリ
- 起動中のPC（スリープ不可）

### 出力

- スマホから操作可能なデスクトップClaude Cowork
- 外出先からのローカル作業指示

## 使うツール・ライブラリ

- Claude Cowork（デスクトップ版）
- Dispatchスマホアプリ

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
