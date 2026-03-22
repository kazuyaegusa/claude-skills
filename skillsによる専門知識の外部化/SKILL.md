# Skillsによる専門知識の外部化

> 特定ドメイン（セキュリティ監査、科学計算、DevOps等）の専門知識を独立したモジュール（Skill）として定義し、Claude Codeに動的にロードさせる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

全ての専門知識をプロンプトに詰め込むとトークン数が膨大になり、文脈が薄れる。Skillsとして外部化することで、必要な時だけロードし、文脈を絞って高品質な出力を得られる

## いつ使うのか

特定ドメインの深い専門知識が必要だが、常にロードする必要はない場合（セキュリティ監査、科学計算、特定フレームワークのベストプラクティスなど）

## やり方

1. `~/.claude/skills/`ディレクトリにスキル定義ファイルを配置（通常はMarkdown形式）
2. スキルには「name」「description」「when_to_use」「instructions」を記載
3. Claude Codeがタスクに応じて適切なスキルを自動選択してロード（または明示的に`/use-skill <name>`で指定）
4. スキルがロードされると、その知識を使って回答やコード生成を行う

例：Trail of Bits Security Skillsは、CodeQL/Semgrepによる静的解析、variant analysis、differential reviewなど12以上のセキュリティ監査スキルを提供

### 入力

- スキル定義ファイル（Markdown等）
- スキルを配置するディレクトリ（`~/.claude/skills/`）

### 出力

- 専門知識に基づいた高品質なコード・分析結果
- ドメイン固有のベストプラクティスに沿った提案

## 使うツール・ライブラリ

- Trail of Bits Security Skills（セキュリティ監査）
- Claude Scientific Skills（研究・科学・工学・分析）
- Superpowers（SDLC全般のベストプラクティス）
- cc-devops-skills（DevOps/IaC）

## コード例

```
---
name: security-audit
description: Perform comprehensive security audit using CodeQL and Semgrep
when_to_use: When analyzing code for vulnerabilities
---

## Instructions
1. Run CodeQL analysis on target codebase
2. Execute Semgrep with OWASP ruleset
3. Perform manual review of crypto usage
4. Generate audit report with severity ratings
```

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、プロンプト入力、ファイル編集）
- Gitの基礎知識（branch、commit、PR）
- シェルスクリプト/Python/Node.jsの基礎（Hooks実装時）
- Docker/tmuxの基礎知識（Orchestrators使用時）
- JSON/YAML形式の理解（設定ファイル編集時）

## 根拠

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI."
