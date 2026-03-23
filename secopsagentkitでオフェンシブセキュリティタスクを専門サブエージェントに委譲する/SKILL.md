# SecOpsAgentKitでオフェンシブセキュリティタスクを専門サブエージェントに委譲する

> .claude/agents/offsec-specialist.mdで定義された自律的なペネトレーションテスト専門エージェントに、SQLi/XSS/バイナリ解析等のタスクを委譲

- 出典: https://github.com/gadievron/raptor
- 投稿者: gadievron
- カテゴリ: claude-code-workflow

## なぜ使うのか

攻撃的セキュリティテストは多段階の試行錯誤が必要で、手動では非効率。専門スキルセット（SecOpsAgentKit）を持つサブエージェントに委譲することで、自律的な探索と検証が可能

## いつ使うのか

ペネトレーションテストを自動化したい時、多段階の攻撃シナリオを探索させたい時

## やり方

1. .claude/agents/offsec-specialist.mdでサブエージェントを定義
2. .claude/skills/SecOpsAgentKit/（gitサブモジュール）からスキルをロード
3. ユーザーが「Use the offensive security specialist agent to test this application」と指示
4. サブエージェントが安全な操作は自動実行、危険な操作はユーザー確認を要求
5. Web app testing（SQLi、XSS、CSRF）、network pentest、binary exploitation、fuzzing等を自律実行

### 入力

- テスト対象アプリケーションまたはバイナリ
- 攻撃範囲の制約（IPレンジ、許可されたアクション等）

### 出力

- 発見された脆弱性リスト
- 攻撃シナリオと検証結果
- PoC

## 使うツール・ライブラリ

- SecOpsAgentKit（gitサブモジュール）
- .claude/agents/offsec-specialist.md

## コード例

```
# .claude/agents/offsec-specialist.md (simplified)
# Agent definition for autonomous offensive security testing
# Safe operations: auto-execute
# Dangerous operations: require user confirmation
# Skills: .claude/skills/SecOpsAgentKit/

# Usage in Claude Code
"Use the offensive security specialist agent to test this web app"
```

## 前提知識

- Claude Codeの基本操作（コマンド、スキル、エージェントの概念）
- セキュリティツールの基礎知識（Semgrep、CodeQL、AFL、ペネトレーションテスト）
- LLMプロバイダのAPI認証（ANTHROPIC_API_KEY等）
- BigQuery認証（OSS Forensics使用時）
- Dockerまたはdevcontainer環境構築（オプション）

## 根拠

> RAPTOR stands for Recursive Autonomous Penetration Testing and Observation Robot.

> SecOpsAgentKit: Offensive security specialist agent with comprehensive penetration testing capabilities

> OSS Forensics: Evidence Collection via GH Archive, GitHub API, Wayback Machine, local git... Deleted Content Recovery... IOC Extraction... Evidence Verification... Hypothesis Formation
