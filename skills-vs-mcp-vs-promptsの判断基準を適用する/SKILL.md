# Skills vs MCP vs Promptsの判断基準を適用する

> 「同じ指示を複数会話で繰り返す→Skill」「外部データ統合→MCP」「1回限りの指示→Prompt」「独立タスク実行→Subagent」の使い分けルールで最適なツールを選択する。

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: agent-orchestration

## なぜ使うのか

全てをPromptで対処するとコピペ地獄になり、全てをMCPで解決しようとすると手続き的知識が表現できない。適材適所で使い分けることでメンテナンス性と再利用性が向上。

## いつ使うのか

新しいワークフローを自動化する前に、どの仕組みで実装すべきか迷った時。

## やり方

1. タスクを受けたら「これは複数会話で再利用するか？」を判定
2. YES→「手続き的知識（やり方）か、外部データアクセスか？」を判定
   - 手続き的知識（例：TDDワークフロー、デバッグ手順）→Skill
   - 外部データ（例：DB照会、API統合）→MCP
3. NO→「1回限りの指示か、独立タスクか？」を判定
   - 1回限り→Prompt
   - 独立タスク（権限分離必要）→Subagent
4. SkillとMCPは併用可能（例：mcp-builder SkillでMCPサーバー構築）

### 入力

- タスクの性質（再利用性、データソース、権限要件）

### 出力

- 最適なツール選択（Skill/MCP/Prompt/Subagent）

## 使うツール・ライブラリ

- Claude Skills
- MCP
- Subagent
- System Prompt

## 前提知識

- Claude Pro/Max/Team/Enterprise契約（Free tierではSkills利用不可）
- YAML frontmatter、Markdownの基本文法
- gitによるバージョン管理の知識（Skill配布・更新管理に必要）
- Claude.ai/Code/APIのいずれかの使用経験
- （開発系Skillの場合）対象フレームワーク・ライブラリの基礎知識

## 根拠

> 「Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed」（Progressive Disclosure設計の具体的トークン数）

> 「Use Skills when: Capabilities should be accessible to any Claude instance. They're portable expertise.」（Skillsの位置づけ）

> 「⚠️ Important: Skills can execute arbitrary code in Claude's environment. Only install skills from trusted sources.」（セキュリティ警告）

> 「obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns」（コミュニティSkillの代表例）

> 「Skills vs MCP: Skills - Task-specific expertise and workflows, MCP - External data/API integration」（Skills vs MCPの明確な区別）
