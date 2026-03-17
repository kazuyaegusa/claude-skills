# JetBrainsプラグインバックエンドで最強の解析精度を実現

> Serena JetBrainsプラグインをインストールし、IntelliJ/PyCharm/WebStorm等のIDE解析エンジンをバックエンドとして活用する

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

LSPより堅牢で高機能なコード解析（フレームワーク対応、高度なリファクタリング等）が必要な場合、JetBrainsの成熟したインデックス機構を利用できるため

## いつ使うのか

既にJetBrains IDEを使用中で、最高精度のコード解析とリファクタリングが必要な商用プロジェクト

## やり方

1. JetBraains Marketplaceから「Serena」プラグインをインストール（https://plugins.jetbrains.com/plugin/28946-serena/）
2. IDE設定でSerenaプラグインを有効化
3. MCPサーバー起動時にJetBrainsバックエンドを指定（詳細は https://oraios.github.io/serena/02-usage/025_jetbrains_plugin.html）
4. LLMからのツール呼び出しがIDE解析エンジン経由で処理される

### 入力

- JetBrains IDE（IntelliJ IDEA、PyCharm、Android Studio、WebStorm、PhpStorm、RubyMine、GoLand等。Rider/CLionは非対応）
- Serena JetBrainsプラグイン

### 出力

- IDE解析エンジンによる高精度なシンボル情報、リファクタリング候補

## 使うツール・ライブラリ

- Serena JetBrainsプラグイン

## 前提知識

- MCPの概念と動作原理
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントのツール呼び出しメカニズム
- Python環境管理（uv）の基本操作
- 対象言語のLanguage Serverインストール方法（LSPバックエンド使用時）
- JetBrains IDE操作の基礎（JetBrainsバックエンド使用時）

## 根拠

> Serena is a powerful coding agent toolkit capable of turning an LLM into a fully-featured agent that works directly on your codebase.

> Serena provides essential semantic code retrieval and editing tools that are akin to an IDE's capabilities, extracting code entities at the symbol level and exploiting relational structure.

> The Serena JetBrains Plugin leverages the powerful code analysis capabilities of your JetBrains IDE. The plugin naturally supports all programming languages and frameworks that are supported by JetBrains IDEs.

> Most users report that Serena has strong positive effects on the results of their coding agents, even when used within very capable agents like Claude Code. Serena is often described to be a game changer, providing an enormous productivity boost.

> We are proud to announce that the Visual Studio Code team, together with Microsoft's Open Source Programs Office and GitHub Open Source have decided to sponsor Serena with a one-time contribution!
