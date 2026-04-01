# Claude DesktopをCLI化してAI自己制御ループを作る

> Claude Desktop（Electronアプリ）をopenclawでCLI化し、AIエージェントがClaude自身を操作してコードを書かせるメタ自己制御ループを構築する。

- 出典: https://x.com/jakevin7/status/2034189219808113096
- 投稿者: 卡比卡比
- カテゴリ: agent-orchestration

## なぜ使うのか

AIが自分自身を操作できるようになることで、タスク投入→コード生成→実行→フィードバック→再生成の自律ループが人間介在なしで回るから。

## いつ使うのか

AIエージェントがClaude Desktopを使ったコード生成を自律的に繰り返したい場合、AI自己駆動ワークフローを構築したい場合

### 具体的な適用場面

- 量は豊富だが拡張しにくいAntigravity UltraをAIエージェントパイプラインに組み込みたい場合
- Claude DesktopをAIエージェントから自律操作させ、コード生成→実行→フィードバックの自律ループを構築したい場合
- 任意のElectronアプリ（Slack、Notion等）をスクリプトやCIから自動操作したい場合

## やり方

1. cc/openclawでClaude DesktopをCLI対応にラップする
2. AIエージェントスクリプトからopenclawコマンドでClaude Desktopにタスクを送信する
3. 結果を受け取ってループする自律スクリプトを組む
※投稿に具体的なコマンド例は記載なし

### 入力

- Claude Desktop（インストール済み）
- cc/openclawツール
- AIエージェントスクリプト

### 出力

- AI自律コード生成ループ
- Claude Desktopへの自動タスク送信・結果受け取りパイプライン

## 使うツール・ライブラリ

- Claude Desktop
- cc/openclaw
- OpenCLI

## 前提知識

- Electronアプリの基本知識（Node.js/Chromium基盤のデスクトップアプリであることの理解）
- cc/openclawのインストール・設定方法（リポジトリ要確認）
- 対象ElectronアプリがPC上にインストールされていること
- AIエージェントのスクリプティング基礎（自律ループを組む場合）

## 根拠

> 「opencli 支持 CLI 化所有 electron 应用」（OpenCLIはすべてのElectronアプリのCLI化をサポート）

> 「我最近大量使用 Antigravity Ultra，虽然它量大但工具难用，并且不容易扩展。现在通过 OpenCLI 把他 CLI 化」（Antigravity UltraをOpenCLIでCLI化した実体験）

> 「Claude 桌面版也是 electron，目前也可以支持哦！现在可以 AI 自己控制自己！自己驱动自己写代码！」（Claude DesktopもElectronなのでAIが自己制御できる）

> 「通过 cc/openclaw 远程控制任何 electron 应用」（cc/openclawで任意のElectronアプリをリモート制御可能）
