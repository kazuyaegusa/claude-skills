# JetBrainsプラグインで最強のコード解析を提供する

> JetBrains IDE（IntelliJ、PyCharm等）のコード解析エンジンをプラグイン経由でSerenaに統合し、LSPより高度な解析を可能にする

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

JetBrains IDEは業界トップクラスのコード解析能力を持ち、フレームワーク対応・リファクタリング精度等でLSPを上回る。これをLLMエージェントに提供することで最高精度の操作が可能になる

## いつ使うのか

JetBrains IDEユーザーで、LSPでは不十分な精度・機能が必要な場合（例: Spring Boot等のフレームワーク対応が必要）

## やり方

1. JetBrainsプラグインマーケットプレイスからSerenaプラグインをインストール
2. IDE起動時にプラグインがバックグラウンドでSerena MCPサーバーと同等の機能を提供
3. LLMエージェントがIDE経由でシンボル検索・参照検索・リファクタリング等を実行
4. IDE内でリアルタイムに結果を確認しながらエージェントが動作

### 入力

- JetBrains IDE（IntelliJ IDEA、PyCharm、WebStorm等）
- Serena JetBrainsプラグイン

### 出力

- IDEコード解析結果をMCP経由でLLMに提供
- より高精度なシンボル操作・リファクタリング

## 使うツール・ライブラリ

- Serena JetBrainsプラグイン
- JetBrains IDE（IntelliJ、PyCharm等）

## 前提知識

- Model Context Protocol（MCP）の基本概念
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントの動作原理（ツール呼び出し・Function Calling）
- Python環境構築（uv等のパッケージマネージャー）
- コードベースにおけるシンボル（関数・クラス・変数等）の概念
- （JetBrainsプラグイン利用時）JetBrains IDEの基本操作

## 根拠

> 「The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs」
