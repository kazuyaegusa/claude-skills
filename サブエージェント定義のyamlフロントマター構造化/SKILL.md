# サブエージェント定義のYAMLフロントマター構造化

> 各サブエージェントをYAMLフロントマター（name, description, tools, model）+ 詳細プロンプトの形式で定義し、役割・権限・モデル選択を明示する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

サブエージェントの責務範囲、利用可能ツール、コスト効率を明確にすることで、適切なタスク配分と安全性を保証する

## いつ使うのか

新しい専門分野のサブエージェントを作成したい時、既存エージェントをカスタマイズしたい時

## やり方

1. `---` で囲まれたYAMLフロントマターに `name`（エージェント名）、`description`（起動条件）、`tools`（許可ツール）、`model`（opus/sonnet/haiku）を記述
2. フロントマター後に、役割説明、チェックリスト、通信プロトコル、ワークフローを含む詳細プロンプトを記述
3. ファイルを `.claude/agents/` または `~/.claude/agents/` に配置
4. Claude Codeが `description` に合致するタスクを検出すると自動起動、または明示的に「Have the code-reviewer subagent analyze...」のように呼び出す

### 入力

- 役割定義（何の専門家か、いつ起動するか）
- 許可ツールリスト（Read, Write, Edit, Bash, Grep等）
- 使用モデル（opus: 高度推論、sonnet: 日常コーディング、haiku: 軽量タスク）
- 詳細プロンプト（チェックリスト、パターン、ガイドライン）

### 出力

- 独立したコンテキストで動作する専門エージェント
- チーム全体で共有可能な `.md` ファイル

## 使うツール・ライブラリ

- YAML frontmatter
- Markdown

## コード例

```
---
name: security-auditor
description: Security vulnerability analysis and OWASP compliance
tools: Read, Grep, Glob
model: opus
---

You are a security auditor specializing in OWASP Top 10...

## Checklist
- [ ] SQL injection vectors
- [ ] XSS vulnerabilities
...

## Communication Protocol
Report findings in CVE format...
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Independent Context Windows: Every subagent operates within its own isolated context space, preventing cross-contamination between different tasks」

> 「Domain-Specific Intelligence: Subagents come equipped with carefully crafted instructions tailored to their area of expertise」

> 「Shared Across Projects: After creating a subagent, you can utilize it throughout various projects and distribute it among team members」

> 「Granular Tool Permissions: You can configure each subagent with specific tool access rights」
