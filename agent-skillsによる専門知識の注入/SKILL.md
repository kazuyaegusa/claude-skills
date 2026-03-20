# Agent Skillsによる専門知識の注入

> Claude Codeに特定ドメイン（科学研究・セキュリティ監査・DevOps IaC・フルスタック開発等）の専門知識・ワークフローを事前学習させ、高品質な実装を初回から得る

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

汎用LLMは広範な知識を持つが、特定ドメインの深い知識・ベストプラクティスは不足しがち。Skillsで専門知識を注入することで、人間の指示が曖昧でも適切な実装が得られる

## いつ使うのか

専門性が高く、人間の指示だけでは不十分な場合。特にセキュリティ・科学計算・インフラコード等、ミスが致命的な領域

## やり方

1. ドメインに応じたSkillsを選定（例：セキュリティ監査→「Trail of Bits Security Skills」、科学研究→「Claude Scientific Skills」、DevOps→「cc-devops-skills」）
2. Skillsをダウンロード（通常は`.claude/skills/`に配置）
3. CLAUDE.mdまたはプロンプトでSkillsを参照（「Use the security audit skill to review this code」等）
4. Claude CodeがSkillsのコンテキストを読み込み、専門的な分析・実装を実行
5. 出力を確認し、Skillsが不足していれば追加・カスタマイズ

### 入力

- 対象ドメイン（セキュリティ・科学・DevOps・フルスタック等）
- 既存のClaude Code設定（CLAUDE.md等）

### 出力

- ドメイン特化型の高品質実装
- ベストプラクティス準拠のコード
- 専門的なレビュー・監査結果

## 使うツール・ライブラリ

- Trail of Bits Security Skills（セキュリティ監査）
- Claude Scientific Skills（科学研究・工学・分析）
- cc-devops-skills（DevOps IaC）
- Fullstack Dev Skills（フルスタック開発）
- Superpowers（SDLC全般のベストプラクティス）

## コード例

```
// CLAUDE.md example
## Security
Use the Trail of Bits Security Skills for all code audits.
Run static analysis with CodeQL/Semgrep before any PR merge.
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ファイル操作承認等）
- gitの基礎知識（branch, commit, PR等）
- 開発ワークフローの基礎（TDD, CI/CD, コードレビュー等の概念）
- JSON/Markdown形式の読み書き（Hooks設定、CLAUDE.md記述に必要）

## 根拠

> 「A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.」

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.」

> 「ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI.」

> 「Trail of Bits Security Skills - A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection.」
