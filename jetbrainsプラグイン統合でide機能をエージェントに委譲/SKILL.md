# JetBrainsプラグイン統合でIDE機能をエージェントに委譲

> JetBrains IDEのコード解析機能をプラグイン経由でMCPツール化し、高精度なリファクタリング・参照検索・型階層をエージェントから利用可能にする

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

JetBrains IDEの強力な解析エンジンを活用することで、プロジェクト依存関係の検索、実装検索、安全なリネーム・移動・インライン化など、LSPでは実現困難な高度な操作が可能になる

## いつ使うのか

Java/Kotlin/Python/JavaScript等のJetBrains対応言語で、高精度なリファクタリングや依存関係検索が必要な時

## やり方

1. Serena JetBrainsプラグインをインストール 2. `serena init -b JetBrains` で初期化 3. プラグインが提供するrenameFile, moveSymbol, inlineSymbol等のMCPツールをエージェントから呼び出す

### 入力

- JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm等)
- Serena JetBrainsプラグイン

### 出力

- 型階層
- 実装一覧
- 安全なリネーム・移動の実行結果

## 使うツール・ライブラリ

- JetBrains Plugin API
- MCP

## コード例

```
serena init -b JetBrains
```

## 前提知識

- Model Context Protocol (MCP)の基本的な理解
- Language Server Protocol (LSP)の概念
- uv (Pythonパッケージマネージャ)の使い方
- シンボル・参照・型階層などのIDE概念
- Claude Code/Codex/Claude Desktop等のMCP対応クライアント

## 根拠

> Serena provides essential semantic code retrieval, editing and refactoring tools that are akin to an IDE's capabilities, operating at the symbol level and exploiting relational structure.

> Serena's agent-first tool design involves robust high-level abstractions, distinguishing it from approaches that rely on low-level concepts like line numbers or primitive search patterns.

> Serena's retrieval tools allow agents to explore codebases at the symbol level, understanding structure and relationships without reading entire files.

> Serena's symbolic editing tools are less error-prone and much more token-efficient than typical alternatives.
