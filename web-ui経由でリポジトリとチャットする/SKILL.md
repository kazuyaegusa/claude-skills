# Web UI経由でリポジトリとチャットする

> GitNexusが提供するWeb UIを使い、インデックス化したリポジトリに対して自然言語で質問し、知識グラフベースの回答を得る

- 出典: https://x.com/the_agi_way/status/2035144110160716103
- 投稿者: シュンスケ
- カテゴリ: agent-orchestration

## なぜ使うのか

CLI/MCPはエージェント統合向けだが、人間が素早くコードベース全体を把握したい場合、チャット形式の方が直感的。知識グラフがあるため、単なるRAGより構造的な回答が得られる

## いつ使うのか

初めて触るコードベースを素早く理解したいとき。またはAIエージェントに任せる前に自分で構造を確認したいとき

### 具体的な適用場面

- CursorやClaude Codeで大規模コードベースを編集する際、依存関係の見落としを防ぎたいとき
- AIエージェントにコードレビューやリファクタリングを任せる際、呼び出しチェーンの破壊を避けたいとき
- 複数のAIツール（Cursor/Claude Code/Codex）を横断的に使う環境で、共通の深いコンテキストを提供したいとき
- 小さいモデル（GPT-3.5クラス）でも正確なコード編集を実現したいとき
- リポジトリ全体の構造を素早く把握してチャットで質問したいとき（Web UI経由）

## やり方

1. `gitnexus ui` コマンドでWeb UIを起動（デフォルトでlocalhost:3000）
2. ブラウザでアクセスし、インデックス化済みリポジトリを選択
3. チャット欄に「この関数はどこから呼ばれている？」「このモジュールの依存関係は？」などを入力
4. 知識グラフをクエリした結果が自然言語 + コードスニペットで返される

### 入力

- GitNexusでインデックス化済みのリポジトリ

### 出力

- Web UIでの対話型リポジトリ分析
- 依存関係・呼び出しチェーンの自然言語回答

## 使うツール・ライブラリ

- gitnexus（Web UIモード）

## 前提知識

- Tree-sitterとLSPの基本概念（構文解析・型情報取得）
- MCP（Model Context Protocol）の基礎知識
- Cursor/Claude Code/CodexなどAIコーディングツールの利用経験
- 知識グラフ・依存関係解析の基本理解

## 根拠

> 「数日前にGithubのトレンドデイリーで１位を取ったprojectにコミュニティーインテグレーションでのせてくれた」

> 「Building nervous system for agent context. Indexes any codebase into a knowledge graph — every dependency, call chain, cluster, and execution flow — then exposes it through smart tools so AI agents never miss code.」

> 「Like DeepWiki, but deeper. DeepWiki helps you understand code. GitNexus lets you analyze it — because a knowledge graph tracks every relationship, not just descriptions.」

> 「The CLI + MCP is how you make your AI agent actually reliable — it gives Cursor, Claude Code, Codex, and friends a deep architectural view of your codebase so they stop missing dependencies, breaking call chains, and shipping blind edits. Even smaller model」

> npm package: https://www.npmjs.com/package/gitnexus
