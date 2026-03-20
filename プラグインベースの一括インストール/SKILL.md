# プラグインベースの一括インストール

> カテゴリ単位で複数のサブエージェントをClaude Codeプラグインとして一括インストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別ファイルコピーではなく、公式マーケットプレイス経由で導入することで、依存関係管理・更新・アンインストールが容易になるため

## いつ使うのか

複数の専門領域にまたがるエージェントを一度に導入したい場合、または公式メンテナンスされたエージェント定義を追跡したい場合

## やり方

1. `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents` でマーケットプレイスに追加
2. `claude plugin install voltagent-lang`（言語特化）や `voltagent-infra`（インフラ）等、必要なカテゴリプラグインを指定してインストール
3. インストール後、該当カテゴリのエージェントが自動的に `~/.claude/agents/` に配置される
4. `voltagent-meta` プラグインはオーケストレーション用で、他のカテゴリと併用すると効果的

### 入力

- Claude Code CLI
- インターネット接続（GitHubからの取得用）

### 出力

- カテゴリ内の全サブエージェント定義ファイル
- プラグイン管理情報

## 使うツール・ライブラリ

- Claude Code CLI
- VoltAgent公式マーケットプレイス

## コード例

```
# 言語特化エージェント群をインストール
claude plugin install voltagent-lang

# インフラ・DevOpsエージェント群をインストール
claude plugin install voltagent-infra

# メタオーケストレーションエージェント（他カテゴリと併用推奨）
claude plugin install voltagent-meta
```

## 前提知識

- Claude Codeの基本操作（CLI起動、エージェント呼び出し）
- サブエージェントの概念理解（独立コンテキスト、ツール権限、モデル選択）
- YAML frontmatter形式の基本構造
- Git操作（クローン、ファイルコピー）またはcurlコマンドの使用
- 対象領域（言語・インフラ・QA等）の基礎知識（各エージェントを活用する場合）

## 根拠

> 「Global Subagents: `~/.claude/agents/` All projects, Lower precedence」

> 「claude plugin marketplace add VoltAgent/awesome-claude-code-subagents」

> 「./install-agents.sh: This interactive script lets you browse categories, select agents, and install/uninstall them with a single command」

> 「agent-installer: Browse and install agents from this repository via GitHub」
