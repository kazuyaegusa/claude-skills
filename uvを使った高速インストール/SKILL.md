# uvを使った高速インストール

> uvパッケージマネージャーを使ってFastMCPをインストールする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: other

## なぜ使うのか

uvは高速なPythonパッケージマネージャーで、従来のpipよりも大幅に速くインストールが完了する

## いつ使うのか

FastMCPを新規インストールする時、高速なセットアップを望む時

## やり方

1. ターミナルで`uv pip install fastmcp`を実行

### 入力

- uvがインストールされた環境

### 出力

- インストール済みのfastmcpパッケージ

## 使うツール・ライブラリ

- uv
- fastmcp

## コード例

```
uv pip install fastmcp
```

## 前提知識

- Pythonの基本的な関数定義・型ヒント・デコレータの知識
- Model Context Protocol（MCP）の概念理解（LLMがツールを呼び出すプロトコル）
- LLMツール統合の基本的な理解
