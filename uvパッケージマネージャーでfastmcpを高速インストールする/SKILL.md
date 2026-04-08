# uvパッケージマネージャーでFastMCPを高速インストールする

> Rust製の高速Pythonパッケージマネージャーuvを使ってFastMCPをインストールする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: dev-tool

## なぜ使うのか

公式推奨の方法。pipより高速で依存関係の解決が確実

## いつ使うのか

FastMCPを初めてインストールする時、または最新版にアップグレードする時

## やり方

1. ターミナルでuv pip install fastmcpを実行
2. インストール確認（公式ドキュメント参照）

### 入力

- uv CLI（未インストールならcurl -LsSf https://astral.sh/uv/install.sh | sh）

### 出力

- fastmcpパッケージと依存ライブラリ一式

## 使うツール・ライブラリ

- uv（Astral製）

## コード例

```
uv pip install fastmcp
```

## 前提知識

- Python 3.x の基本文法（関数定義、デコレータ）
- 型ヒント（type hints）の理解
- MCP（Model Context Protocol）の概念（LLMとツールを接続するプロトコル）
- FastAPIやFlaskのようなPythonフレームワークの使用経験があると理解が早い

## 根拠

> 「We recommend installing FastMCP with uv」（公式推奨インストール方法）
