# 小さいモデルでも正確な編集を実現する

> 知識グラフを前提とすることで、GPT-3.5クラスの小さいモデルでも、依存関係を見落とさない正確なコード編集が可能になる

- 出典: https://x.com/the_agi_way/status/2035144110160716103
- 投稿者: シュンスケ
- カテゴリ: context-management

## なぜ使うのか

大きいモデル（GPT-4/Claude Opus）はコンテキストウィンドウが広いが、コストが高く遅い。小さいモデルはコンテキストが狭いため依存関係を見落としやすいが、知識グラフがあれば「必要な部分だけ」を正確に取得できる

## いつ使うのか

コスト削減や速度重視でGPT-3.5クラスのモデルを使いたいが、編集精度は妥協したくないとき

### 具体的な適用場面

- CursorやClaude Codeで大規模コードベースを編集する際、依存関係の見落としを防ぎたいとき
- AIエージェントにコードレビューやリファクタリングを任せる際、呼び出しチェーンの破壊を避けたいとき
- 複数のAIツール（Cursor/Claude Code/Codex）を横断的に使う環境で、共通の深いコンテキストを提供したいとき
- 小さいモデル（GPT-3.5クラス）でも正確なコード編集を実現したいとき
- リポジトリ全体の構造を素早く把握してチャットで質問したいとき（Web UI経由）

## やり方

1. GitNexusで知識グラフを生成
2. MCP経由で小さいモデル（例: GPT-3.5-turbo）に知識グラフツールを提供
3. モデルがコード編集時、「この変更の影響範囲は？」をMCPツールで問い合わせる
4. 知識グラフが正確な依存関係リストを返すため、モデルは狭いコンテキストでも正確に編集可能

### 入力

- GitNexus知識グラフ
- 小さいモデル（GPT-3.5/Claude Haiku等）

### 出力

- 依存関係を見落とさない正確なコード編集
- 大きいモデルと同等の信頼性

## 使うツール・ライブラリ

- gitnexus
- GPT-3.5-turbo/Claude Haiku等の小さいモデル

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
