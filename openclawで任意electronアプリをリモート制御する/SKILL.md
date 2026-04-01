# openclawで任意Electronアプリをリモート制御する

> cc/openclawのリモート制御機能を使い、ネットワーク越しに任意のElectronアプリを操作する。

- 出典: https://x.com/jakevin7/status/2034189219808113096
- 投稿者: 卡比卡比
- カテゴリ: agent-orchestration

## なぜ使うのか

ローカルだけでなくリモートからもElectronアプリを制御できることで、分散エージェント構成やCI/CDからのGUIアプリ操作が可能になるから。

## いつ使うのか

複数マシンにまたがるElectronアプリ操作自動化や、リモートサーバー上のElectronアプリをエージェントから制御したい場合

### 具体的な適用場面

- 量は豊富だが拡張しにくいAntigravity UltraをAIエージェントパイプラインに組み込みたい場合
- Claude DesktopをAIエージェントから自律操作させ、コード生成→実行→フィードバックの自律ループを構築したい場合
- 任意のElectronアプリ（Slack、Notion等）をスクリプトやCIから自動操作したい場合

## やり方

1. 対象マシンにcc/openclawをインストールし、対象Electronアプリをラップする
2. openclawのリモート制御エンドポイントを有効化する
3. 別マシンまたはエージェントからリモート制御コマンドを送信する
※投稿に具体的なコマンド例は記載なし

### 入力

- リモート制御対象のElectronアプリ
- cc/openclawツール（両マシン）
- ネットワーク接続

### 出力

- リモートからのElectronアプリ操作
- 分散エージェント構成でのGUIアプリ自動制御

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
