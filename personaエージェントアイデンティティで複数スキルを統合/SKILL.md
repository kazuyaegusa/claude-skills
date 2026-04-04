# Persona（エージェントアイデンティティ）で複数スキルを統合

> Startup CTO、Growth Marketer、Solo Founderなど、特定の役割に必要なスキルセット・優先順位・コミュニケーションスタイルを1つのPersona定義ファイルにまとめる

- 出典: https://github.com/alirezarezvani/claude-skills
- 投稿者: alirezarezvani
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキル単体は「どう実行するか」を定義するが、「どのスキルをいつ使うか」の判断ロジックは含まない。Personaで役割全体の思考パターン・優先基準を定義すれば、エージェントは状況に応じて適切なスキルを自動選択できる

## いつ使うのか

複数のスキルを組み合わせた大規模タスク（6週間の製品ローンチなど）を実行するとき。役割ベースの意思決定が必要な場面

## やり方

1. agents/personas/TEMPLATE.md をコピー
2. Role Definition（役割の責務・意思決定基準）を記述
3. Skill Loadout（この役割が使うスキル一覧）をリスト化
4. Workflows（フェーズごとの作業手順）を定義
5. Communication Style（報告形式・トーン）を指定
6. ~/.claude/agents/{persona-name}.md として配置
7. エージェント起動時に「Use startup-cto persona」と指示

### 入力

- 役割定義（CTO/PM/Marketerなど）
- その役割が使うスキル一覧
- 典型的なワークフロー（例: 週次レビュー→技術選定→チームビルディング）

### 出力

- Personaファイル（Markdown形式）
- エージェントが読み込み可能な統合プロンプト

## 使うツール・ライブラリ

- テキストエディタ
- 既存のSKILL.mdファイル群（参照用）

## コード例

```
# Startup CTO Persona

## Role Definition
- Technical strategy & architecture decisions
- Team building & hiring
- Vendor selection & technical due diligence

## Skill Loadout
- senior-architect (architecture review)
- aws-solution-architect (cloud design)
- senior-frontend (UI/UX tech stack)
- security-auditor (pre-launch security check)

## Workflows
### Week 1-2: Architecture Phase
1. Use senior-architect to review system design
2. Use aws-solution-architect for infra planning
3. Generate ADR (Architecture Decision Record)

### Week 3-4: Build Phase
1. Use senior-frontend for component structure
2. Daily code reviews with security-auditor

## Communication Style
- Technical depth: High (include trade-offs)
- Format: Bullet points + diagrams
- Tone: Direct, no fluff
```

## 前提知識

- Claude Code / Cursor / Aider 等いずれかのAIコーディングツールの基本的な使い方
- Git / GitHub の基本操作（clone, pull）
- Python 3.x の実行環境（スクリプトツール利用時）
- Bashシェルの基本知識（インストールスクリプト実行時）
- （任意）マーケティング・PM・コンプライアンス等の各ドメイン知識（該当スキル使用時）

## 根拠

> 248 production-ready Claude Code skills, plugins, and agent skills for 11 AI coding tools.

> One repo, eleven platforms. Works natively as Claude Code plugins, Codex agent skills, Gemini CLI skills, and converts to 8 more tools via scripts/convert.sh. All 332 Python tools run anywhere Python runs.

> Convert all 156 skills to 7 AI coding tools with a single script: ./scripts/convert.sh --tool all

> skill-security-auditor — Security gate — scan skills for malicious code before installation. Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation. Returns PASS / WARN / FAIL with remediation guidance. Zero dependencies.

> Personas go beyond 'use these skills' — they define how an agent thinks, prioritizes, and communicates.
