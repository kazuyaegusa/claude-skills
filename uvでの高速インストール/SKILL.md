# uvでの高速インストール

> uvパッケージマネージャーを使ってFastMCPを高速にインストールする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: automation-pipeline

## なぜ使うのか

uvは従来のpipより高速で依存関係解決が確実なため、開発環境のセットアップを迅速化できる

## いつ使うのか

FastMCPの初回セットアップ時、CI/CD環境での高速ビルド時

## やり方

1. uv環境を準備
2. `uv pip install fastmcp` を実行

### 入力

- uv実行環境

### 出力

- fastmcpパッケージ（依存関係含む）

## 使うツール・ライブラリ

- uv
- fastmcp

## コード例

```
uv pip install fastmcp
```

## 前提知識

- Python 3.xの基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol（MCP）の概要
- LLMツール統合の基本的な動機

## 根拠

> We recommend installing FastMCP with uv: `uv pip install fastmcp`
