# uvでFastMCPをインストール

> Astral社のuvパッケージマネージャでfastmcpをインストールする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

公式推奨の方法であり、依存関係解決と環境管理が高速で確実

## いつ使うのか

FastMCPを新規導入する時、または最新版にアップグレードする時

## やり方

1. `uv pip install fastmcp`を実行
2. インストール確認とアップグレードはドキュメント参照（gofastmcp.com/getting-started/installation）

### 入力

- uv環境（または通常のpip環境）

### 出力

- fastmcpパッケージ

## 使うツール・ライブラリ

- uv

## コード例

```
uv pip install fastmcp
```

## 前提知識

- Python 3.x基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol (MCP)の概要理解
- 非同期プログラミング（async/await）の基礎（応用時）
