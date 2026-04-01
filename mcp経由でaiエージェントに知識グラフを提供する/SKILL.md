# MCP経由でAIエージェントに知識グラフを提供する

> GitNexusが生成した知識グラフをMCP（Model Context Protocol）ツールとして公開し、Cursor/Claude Code/Codexなどのエージェントから呼び出し可能にする

- 出典: https://x.com/the_agi_way/status/2035144110160716103
- 投稿者: シュンスケ
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIエージェントがコード編集時に「この変更が他のどこに影響するか」を知識グラフに問い合わせられるようにすることで、依存関係の見落としや呼び出しチェーンの破壊を防ぐ

## いつ使うのか

複数のAIツールを使っている環境で、全ツールに共通の深いコンテキストを与えたいとき。または、エージェントに「盲目的な編集」をさせたくないとき

### 具体的な適用場面

- CursorやClaude Codeで大規模コードベースを編集する際、依存関係の見落としを防ぎたいとき
- AIエージェントにコードレビューやリファクタリングを任せる際、呼び出しチェーンの破壊を避けたいとき
- 複数のAIツール（Cursor/Claude Code/Codex）を横断的に使う環境で、共通の深いコンテキストを提供したいとき
- 小さいモデル（GPT-3.5クラス）でも正確なコード編集を実現したいとき
- リポジトリ全体の構造を素早く把握してチャットで質問したいとき（Web UI経由）

## やり方

1. GitNexusインデックス化後、`gitnexus mcp start` でMCPサーバーを起動
2. Cursor/Claude Code/Codexの設定でMCPサーバーを登録（例: `mcp-servers.json` に `{"gitnexus": {"command": "gitnexus", "args": ["mcp", "start"]}}` を追加）
3. AIエージェントがコード編集時、MCPツール経由で「この関数を変更したら影響範囲は？」「この依存はどこから呼ばれている？」をクエリ可能になる
4. エージェントは知識グラフの回答を元に、より正確な編集・リファクタリングを実行

### 入力

- GitNexusでインデックス化済みのコードベース
- MCP対応のAIエージェント（Cursor/Claude Code/Codex等）

### 出力

- MCPツールとして公開された知識グラフAPI
- エージェントからのクエリに対する依存関係・影響範囲の回答

## 使うツール・ライブラリ

- gitnexus（MCP機能）
- MCP（Model Context Protocol）
- Cursor/Claude Code/Codex（クライアント側）

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
