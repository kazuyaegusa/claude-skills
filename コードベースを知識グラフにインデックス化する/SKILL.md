# コードベースを知識グラフにインデックス化する

> 任意のコードベースをTree-sitterとLSPで解析し、依存関係・呼び出しチェーン・クラスタ・実行フローを抽出して知識グラフ（ネオグラフDB相当）に格納する

- 出典: https://x.com/the_agi_way/status/2035144110160716103
- 投稿者: シュンスケ
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントにコードを渡す際、ファイル単位やRAG的な検索では関係性が失われる。知識グラフとして構造化すれば、「この関数を変更したらどこに影響があるか」をエージェントが正確に把握できる

## いつ使うのか

AIエージェントにコードベースを正確に理解させたいとき。特に依存関係が複雑なプロジェクト、または小さいモデルで編集精度を上げたいとき

### 具体的な適用場面

- CursorやClaude Codeで大規模コードベースを編集する際、依存関係の見落としを防ぎたいとき
- AIエージェントにコードレビューやリファクタリングを任せる際、呼び出しチェーンの破壊を避けたいとき
- 複数のAIツール（Cursor/Claude Code/Codex）を横断的に使う環境で、共通の深いコンテキストを提供したいとき
- 小さいモデル（GPT-3.5クラス）でも正確なコード編集を実現したいとき
- リポジトリ全体の構造を素早く把握してチャットで質問したいとき（Web UI経由）

## やり方

1. `npm install -g gitnexus` でGitNexusをインストール
2. コードベースのルートディレクトリで `gitnexus init` を実行
3. Tree-sitter（構文解析）とLSP（型情報・定義ジャンプ）がバックグラウンドで動作し、依存関係を抽出
4. `.gitnexus/` ディレクトリに知識グラフDB（SQLite形式）が生成される
5. `gitnexus update` で差分更新（ファイル変更時に自動再インデックス可能）

### 入力

- コードベース（任意の言語、Tree-sitter対応言語推奨）
- LSP対応環境（オプションだがあると精度向上）

### 出力

- .gitnexus/ ディレクトリ内の知識グラフDB
- 依存関係・呼び出しチェーン・実行フロー情報

## 使うツール・ライブラリ

- gitnexus（npm package）
- Tree-sitter（構文解析）
- LSP（Language Server Protocol）

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
