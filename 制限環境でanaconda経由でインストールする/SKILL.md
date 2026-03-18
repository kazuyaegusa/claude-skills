# 制限環境でAnaconda経由でインストールする

> 企業ネットワークやエアギャップ環境でnpm直接インストールが困難な場合、Anacondaでnode.js環境を作成してからgemini-cliをインストールする

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: dev-tool

## なぜ使うのか

プロキシ・ファイアウォール・社内パッケージリポジトリなどの制約下でも、conda-forge経由でnode.jsを取得し、その環境内でnpmを使えるようにする。

## いつ使うのか

企業プロキシ配下、npmレジストリへのアクセスが制限されている、Node.jsの公式インストーラが使えない環境で導入したい場合

## やり方

1. `conda create -y -n gemini_env -c conda-forge nodejs`で専用環境を作成 2. `conda activate gemini_env`で環境を有効化 3. `npm install -g @google/gemini-cli`でCLIをインストール 4. 以降は通常通り`gemini`コマンドを使用

### 入力

- Anaconda/Miniconda環境
- conda-forgeへのアクセス（またはローカルミラー）

### 出力

- 独立したconda環境内で動作するgemini-cli
- 他のNode.jsプロジェクトと隔離された実行環境

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

- Node.js環境の基本操作（npmまたはnpxの使用経験）
- ターミナル/コマンドラインの基礎知識
- Git操作の基本（GitHub連携を使う場合）
- JSON-RPC 2.0の基礎（MCP Server自作時）
- Google Cloud Projectの概念（Code Assistライセンス利用時）
- CI/CDパイプラインの基礎（GitHub Actions統合時）

## 根拠

> 「Install with Anaconda (for restricted environments)」（制限環境対応）
