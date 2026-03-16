# JetBrainsプラグインでより強力なコード解析を利用する

> IntelliJ/PyCharm等のJetBrains IDE解析エンジンを使ってSerenaツールを提供し、LSPより高度な言語・フレームワークサポートを得る

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

LSPは汎用的だがフレームワーク固有の解析（Spring/Django等）に弱い。JetBrains IDEの解析エンジンは商用品質で、複雑なプロジェクト構造・依存関係を正確に理解できる

## いつ使うのか

JetBrains IDEを使っており、フレームワーク固有の解析（Spring Bean依存、Djangoモデル関係等）をLLMに提供したい場合、またはLSPで不十分な精度の時

## やり方

1. JetBrains Marketplace（https://plugins.jetbrains.com/plugin/28946-serena/）からSerenaプラグインをインストール
2. IDE設定でSerenaを有効化
3. MCPクライアントがJetBrainsバックエンド経由でSerenaツールを呼び出すよう設定
4. IDE起動中にLLMがIDEの解析結果をリアルタイム利用

### 入力

- JetBrains IDE（IntelliJ IDEA/PyCharm/WebStorm/GoLand等、Rider/CLion除く）
- 対象プロジェクト（IDE対応全言語・フレームワーク）

### 出力

- LSP以上の精度でのシンボル解決
- フレームワーク固有の依存関係情報
- IDE品質のコード補完・参照検索結果

## 使うツール・ライブラリ

- Serena JetBrainsプラグイン
- IntelliJ Platform API

## 前提知識

- Model Context Protocol (MCP) の基本概念
- Language Server Protocol (LSP) の役割（IDE補完・参照解析の仕組み）
- LLMのツール呼び出し（Function Calling）の仕組み
- Python環境とuvパッケージマネージャーの使い方
- コーディングエージェント（Claude Code/Cursor等）の基本的な使用経験
