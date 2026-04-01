# Anaconda環境でNode.jsをインストールしてgemini-cliを導入

> conda-forgeからNode.jsをインストールし、隔離されたconda環境内でnpm install -gを実行する

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: agent-orchestration

## なぜ使うのか

企業ネットワークや制限された環境で、システムグローバルにNode.jsをインストールできない場合でも、conda環境内で完結できる

## いつ使うのか

企業プロキシ下でnpmが使えない、システムにNode.jsを入れられない、複数バージョンのNode.jsを切り替えたい場合

## やり方

1. `conda create -y -n gemini_env -c conda-forge nodejs` で環境作成
2. `conda activate gemini_env` で環境有効化
3. `npm install -g @google/gemini-cli` でインストール
4. `gemini` コマンドが環境内で利用可能になる
5. 不要時は `conda deactivate` で無効化

### 入力

- Anaconda/Minicondaがインストール済み
- conda-forgeチャンネルへのアクセス

### 出力

- conda環境内にNode.js + Gemini CLIがインストール
- 環境アクティブ時にgeminiコマンドが利用可能

## 使うツール・ライブラリ

- Anaconda/Miniconda
- conda-forge
- npm

## コード例

```
conda create -y -n gemini_env -c conda-forge nodejs
conda activate gemini_env
npm install -g @google/gemini-cli
gemini
```

## 前提知識

- Node.js 18以上の基本的な理解
- ターミナル操作の基礎知識
- npmパッケージマネージャーの基本的な使い方
- LLM APIの基本概念（プロンプト、トークン、コンテキストウィンドウ）
- OAuth認証フローの概要理解（ブラウザベース認証）
- JSON形式の基本的なパース方法
- （GitHub Actions利用の場合）GitHub Actionsの基本構文
- （MCP利用の場合）Model Context Protocolの概要

## 根拠

> 「Install with Anaconda: conda create -y -n gemini_env -c conda-forge nodejs」（Anaconda環境でのインストール手順）
