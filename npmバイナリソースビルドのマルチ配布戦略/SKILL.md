# npm/バイナリ/ソースビルドのマルチ配布戦略

> npmパッケージ、GitHub Releases バイナリ、Goソースビルドの3方式で配布し、ユーザーの環境に応じて選択可能にする

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

npm利用者、バイナリ直接ダウンロード派、開発者（ソースビルド）それぞれに最適なインストール方法を提供することで導入障壁を下げる

## いつ使うのか

CLIツールを幅広い環境で使えるようにしたい場合

## やり方

1. npm: Go製バイナリをnode_modulesに配置し、npxから実行可能にする
2. GitHub Releases: CI/CDで各OS（Linux/macOS/Windows）×各アーキテクチャのバイナリを自動ビルド・リリース
3. ソースビルド: `make build` でGoビルド
4. 自動更新機能: `cc-connect update` でバイナリを最新版に置き換え
5. beta版は `npm install -g cc-connect@beta` または pre-release assetsから取得

### 入力

- Goソースコード
- GitHub Actions CI/CD設定
- npm package.json

### 出力

- npm公開パッケージ
- GitHub Releases バイナリ
- セルフアップデート機能

## 使うツール・ライブラリ

- Go 1.22+
- GitHub Actions
- npm
- Makefile

## コード例

```
# npmインストール
npm install -g cc-connect

# バイナリダウンロード
curl -L -o cc-connect https://github.com/chenhg5/cc-connect/releases/latest/download/cc-connect-linux-amd64
chmod +x cc-connect

# ソースビルド
git clone https://github.com/chenhg5/cc-connect.git
cd cc-connect
make build

# 自動更新
cc-connect update --pre  # beta版更新
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法

## 根拠

> "Personal WeChat (Weixin ilink) — beta / pre-release only"

> "npm install -g cc-connect@beta"
