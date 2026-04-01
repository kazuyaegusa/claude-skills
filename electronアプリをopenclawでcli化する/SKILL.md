# ElectronアプリをopenclawでCLI化する

> cc/openclawを使い、GUIのみのElectronアプリにCLIインターフェースを追加して、コマンドラインや他プログラムから操作できるようにする。

- 出典: https://x.com/jakevin7/status/2034189219808113096
- 投稿者: 卡比卡比
- カテゴリ: agent-orchestration

## なぜ使うのか

拡張性が低いGUIアプリでも、CLI化することでAIエージェントやシェルスクリプトのワークフローに組み込めるようになるから。

## いつ使うのか

Antigravity Ultra等の量は豊富だが拡張性が低いElectronアプリをAIパイプラインに組み込みたい時

### 具体的な適用場面

- 量は豊富だが拡張しにくいAntigravity UltraをAIエージェントパイプラインに組み込みたい場合
- Claude DesktopをAIエージェントから自律操作させ、コード生成→実行→フィードバックの自律ループを構築したい場合
- 任意のElectronアプリ（Slack、Notion等）をスクリプトやCIから自動操作したい場合

## やり方

1. cc/openclaw リポジトリを入手する（GitHub: openclaw/openclaw または cc/openclaw）
2. openclawコマンドで対象Electronアプリを登録・ラップする
3. CLI経由でElectronアプリのアクションを呼び出す
※投稿には具体的なコマンド例の記載なし。リポジトリのREADMEを参照すること。

### 入力

- CLI化したい対象Electronアプリ（インストール済み）
- cc/openclawツール

### 出力

- CLIから呼び出し可能なElectronアプリのラッパー
- 他ツールと組み合わせ可能なインターフェース

## 使うツール・ライブラリ

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
