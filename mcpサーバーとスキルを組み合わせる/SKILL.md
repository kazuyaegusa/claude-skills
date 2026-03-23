# MCPサーバーとスキルを組み合わせる

> Model Context Protocol (MCP)サーバーが提供するツールをSKILL.mdから呼び出し、複雑な外部サービス連携を実現する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

生のMCPツールは低レベルAPIであり、使い方をAIが毎回推論する必要がある。スキルでラップすることで、ドメイン知識（認証フロー、エラーハンドリング、ベストプラクティス）を事前注入でき、AIの成功率が上がる

## いつ使うのか

Linear/Jira/Slack等の外部サービスをClaude Codeから操作したいが、APIの細部をAIに毎回説明したくない時、チーム全体で安全な操作パターンを強制したい時

## やり方

1. MCPサーバーをインストール・起動（例: Linear, NotebookLM, Postgres MCP）
2. SKILL.mdにMCPツールの呼び出しパターンを記述
3. 認証方法、エラー時のリトライロジック、read-only制約などをスキル内で明示
4. Claude Codeがスキルをロードすると、MCPツール＋ドメイン知識を統合した高レベルな操作が可能になる

### 入力

- MCPサーバーのインストール情報
- APIの認証トークンや接続設定
- 安全な操作の制約（read-only、レート制限等）

### 出力

- MCPツールを活用する高レベルなスキル
- AIが外部サービスを正しく操作できるガードレール

## 使うツール・ライブラリ

- Model Context Protocol (MCP)
- linear-claude-skill
- postgres MCP
- notebooklm MCP

## コード例

```
# postgres skill example
1. Connect using MCP postgres server
2. Execute ONLY read-only queries (SELECT)
3. Defense-in-depth: timeout 30s, max 1000 rows
4. Return results as JSON
```

## 前提知識

- Claude Codeの基本的な使い方（プロンプト実行、ツール呼び出し）
- GitHubリポジトリのクローン・PRの基本操作
- SKILL.mdの配置場所（`~/.claude/skills/`）の理解
- （MCPスキル使用時）Model Context Protocolの概念とサーバーインストール方法

## 根拠

> 「A curated list of Claude Skills」

> 「100以上のスキルリンク（docx, pdf, test-driven-development, VibeSec-Skill, aws-skills, postgres, linear-claude-skill等）」

> 「[Tip] If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」

> 「MCP integration examples: Linear, NotebookLM, Postgres with read-only safety」
