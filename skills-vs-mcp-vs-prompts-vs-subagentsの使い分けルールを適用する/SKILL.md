# Skills vs MCP vs Prompts vs Subagentsの使い分けルールを適用する

> タスクの性質に応じて、Skills（再利用可能な手順）、MCP（外部データ統合）、Prompts（即時指示）、Subagents（独立タスク実行）、Projects（永続的背景知識）を使い分ける

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: agent-orchestration

## なぜ使うのか

各ツールは目的が異なる。同じプロンプトを繰り返すならSkill化、外部API接続ならMCP、独立エージェントならSubagent、永続的知識ならProjectを選ぶことで、効率と再利用性が最大化される

## いつ使うのか

どのツールを使うべきか迷ったとき、複数ツールの組み合わせを検討するとき

## やり方

1. 同じ指示を複数会話で繰り返している → Skillを作成
2. 外部データベース・APIにアクセスしたい → MCPサーバーを構築
3. 今回限りの指示・即座のコンテキスト → Promptを使用
4. 独立したワークフロー・制限されたツールアクセスが必要 → Subagentを作成
5. ワークスペース内で常時参照する背景知識 → Projectに追加
6. SubagentにSkillを組み込んで専門知識を付与することも可能

### 入力

- タスクの性質（再利用性、外部統合、独立性、永続性）

### 出力

- 最適なツール選択またはツール組み合わせ戦略

## 使うツール・ライブラリ

- Claude Skills
- MCP
- Prompts
- Subagents
- Projects

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Freeプランではスキル利用不可）
- YAML frontmatter、Markdown記法の基礎知識
- Git/GitHubの基本操作（バージョン管理・配布時）
- Python/JavaScriptなどスクリプト言語の基礎（カスタムスキル作成時）
- Claude Code CLI、Claude.ai、またはClaude APIの利用経験
- プロンプトエンジニアリング、MCP、Subagents、Projectsとの違いの理解

## 根拠

> Skills employ a **progressive disclosure architecture** for efficiency: 1. Metadata loading (~100 tokens) 2. Full instructions (<5k tokens) 3. Bundled resources

> Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.

> Skills vs MCP: Skills for Task-specific expertise and workflows, MCP for External data/API integration. Skills: Same format everywhere, Can include executable scripts, 30-50 tokens until loaded. MCP: Requires server configuration, Provides tools/resources.

> **Oct 16, 2025**: Claude Skills officially announced - Available across Claude.ai, Code, and API

> **Nov 13, 2025**: Anthropic publishes Skills Explained - Comprehensive guide covering progressive disclosure architecture, decision matrices
