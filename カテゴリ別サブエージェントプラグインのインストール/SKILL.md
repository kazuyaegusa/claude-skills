# カテゴリ別サブエージェントプラグインのインストール

> 127以上のサブエージェントを9つのカテゴリ（Core Development、Language Specialists、Infrastructure等）に分類し、必要なものだけをプラグインとして導入する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全てのエージェントを一括導入すると管理が煩雑になるため、用途別にパッケージ化することで必要最小限のエージェントセットを維持できる

## いつ使うのか

特定のドメイン（例：言語専門家、インフラ、QA/セキュリティ）に集中的に取り組むプロジェクトで、関連エージェントをまとめて導入したい時

## やり方

1. `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents` でマーケットプレイスに追加
2. `claude plugin install voltagent-lang` のように、カテゴリ別パッケージ名（voltagent-core-dev、voltagent-infra等）を指定してインストール
3. インストール後、自動的に `~/.claude/agents/` に配置され、Claude Codeが必要時に自動起動する

### 入力

- 対象カテゴリのプラグイン名（例：voltagent-lang、voltagent-qa-sec）

### 出力

- 指定カテゴリのサブエージェント群が `~/.claude/agents/` に配置され、即座に利用可能になる

## 使うツール・ライブラリ

- Claude Code CLI
- VoltAgent/awesome-claude-code-subagents リポジトリ

## コード例

```
# 言語専門家カテゴリをインストール
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang

# インフラ・DevOps専門家をインストール
claude plugin install voltagent-infra
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）

## 根拠

> 「voltagent-meta orchestration agents work best when other categories installed」
