# uv経由でのインストールで依存解決を高速化

> FastMCPのインストールを`uv pip install fastmcp`で行い、従来のpipより高速な依存解決を利用する

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: automation-pipeline

## なぜ使うのか

FastMCPはPydanticやAnyIOなど複数の依存を持つため、pipの依存解決が遅い場合がある。uvはRust実装で依存解決が高速化されており、CI/CD環境でのビルド時間短縮にも寄与する

## いつ使うのか

FastMCPを新規プロジェクトに導入するとき。特にCI/CDパイプラインで依存インストール時間を短縮したい場合

## やり方

1. uvをインストール（`curl -LsSf https://astral.sh/uv/install.sh | sh`等）
2. `uv pip install fastmcp`を実行
3. インストール確認: `python -c "import fastmcp; print(fastmcp.__version__)"`

### 入力

- uv（Pythonパッケージインストーラー）

### 出力

- インストール済みfastmcpパッケージ

## 使うツール・ライブラリ

- uv (https://docs.astral.sh/uv/)
- fastmcp

## コード例

```
uv pip install fastmcp
```

## 前提知識

- Pythonの基本文法（関数定義、デコレータ、型ヒント）
- MCPの基本概念（ツール・リソース・プロンプトの役割）
- 非同期プログラミングの基礎（Clientsを使う場合）

## 根拠

> 「We recommend installing FastMCP with uv: uv pip install fastmcp」（推奨インストール方法）
