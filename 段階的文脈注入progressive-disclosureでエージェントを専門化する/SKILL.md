# 段階的文脈注入（Progressive Disclosure）でエージェントを専門化する

> CLAUDE.mdをエントリポイントとし、関連性に応じてTier1（思考フレームワーク）、Tier2（エキスパートペルソナ）を段階的にロードして、汎用LLMを専門家に変える

- 出典: https://github.com/gadievron/raptor
- 投稿者: gadievron
- カテゴリ: claude-code-workflow

## なぜ使うのか

全プロンプトを常時ロードすると文脈コスト（トークン数）が膨大になる。必要な時だけロードすることで360t→925t→2500tと段階的に拡張し、コストと専門性を両立できる

## いつ使うのか

汎用LLMエージェントを特定ドメインの専門家に変えたい時、または大規模プロンプトのコスト最適化が必要な時

## やり方

1. CLAUDE.mdに常時ロードするブートストラップルール（敵対的思考、分析ガイダンス、リカバリ）を記述
2. Tier1スキルに自動ロードする思考フレームワーク（Impact×Exploitability/DetectionTime優先度計算等）を配置
3. Tier2に9種のエキスパートペルソナ（Mark Dowd、Charlie Miller等）を配置し、明示的リクエスト時のみロード
4. .claude/agents/でサブエージェント（offsec-specialist等）を定義し、自律的なタスク実行を委譲

### 入力

- CLAUDE.md（ブートストラップルール）
- Tier1スキル（思考フレームワーク）
- Tier2ペルソナ（エキスパート定義）
- サブエージェント定義（.claude/agents/）

### 出力

- 文脈に応じて専門性を発揮するエージェント
- 360t→925t→2500tの段階的トークン使用

## 使うツール・ライブラリ

- Claude Code
- CLAUDE.md
- .claude/skills/
- .claude/agents/

## コード例

```
# CLAUDE.md example structure
# Bootstrap (always loaded): adversarial thinking, analysis-guidance
# Tier1 (auto-load when relevant): Impact×Exploitability/DetectionTime prioritization
# Tier2 (explicit request): 9 expert personas (Mark Dowd, Charlie Miller, etc.)
# Agents: offsec-specialist.md for autonomous offensive security operations
```

## 前提知識

- Claude Codeの基本操作（コマンド、スキル、エージェントの概念）
- セキュリティツールの基礎知識（Semgrep、CodeQL、AFL、ペネトレーションテスト）
- LLMプロバイダのAPI認証（ANTHROPIC_API_KEY等）
- BigQuery認証（OSS Forensics使用時）
- Dockerまたはdevcontainer環境構築（オプション）
