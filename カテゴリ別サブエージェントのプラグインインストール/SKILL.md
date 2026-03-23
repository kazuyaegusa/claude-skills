# カテゴリ別サブエージェントのプラグインインストール

> 10カテゴリ（Core Development、Language Specialists、Infrastructure、Quality & Security、Data & AI、Developer Experience、Specialized Domains、Business & Product、Meta & Orchestration、Research & Analysis）に分類された127以上のサブエージェントを、Claude Code プラグインマーケットプレイス経由で一括または個別にインストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

プロジェクトや個人の専門領域に応じて必要なエージェントだけを選択的に導入でき、不要なエージェントによるノイズを避けられる。またプラグイン形式のため、更新やアンインストールも容易

## いつ使うのか

新規プロジェクト開始時、チーム標準ツールセットを構築する時、特定技術スタック（React、Kubernetes、Terraform等）に特化した開発環境を整える時

## やり方

1. `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents` でマーケットプレイスに追加
2. `claude plugin install voltagent-lang` のように、カテゴリ名に対応するプラグイン名を指定してインストール（例: voltagent-core-dev, voltagent-infra, voltagent-qa-sec等）
3. インストール後、Claude Codeセッション内で該当サブエージェントが自動的に利用可能になる
4. 明示的に呼び出す場合は「Have the code-reviewer subagent analyze my latest commits」のように指示

### 入力

- 利用中のClaude Code環境
- 必要とする技術領域の把握（フロントエンド、インフラ、セキュリティ等）

### 出力

- プロジェクトまたはグローバルにインストールされたサブエージェント群
- 各エージェントのメタデータ（name, description, tools, model）

## 使うツール・ライブラリ

- Claude Code CLI
- VoltAgent/awesome-claude-code-subagents プラグインマーケットプレイス

## コード例

```
# カテゴリ別インストール例
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang    # 言語特化エージェント
claude plugin install voltagent-infra   # インフラ・DevOps
claude plugin install voltagent-qa-sec  # テスト・セキュリティ
```

## 前提知識

- Claude Code CLI がインストールされていること
- Claude Codeの基本操作（エージェント起動、ツール実行）の理解
- YAMLフロントマターの基本構文知識（エージェントカスタマイズ時）
- gitの基本操作（リポジトリクローン、ファイルコピー）
- 対象プロジェクトの技術スタックと開発フローの把握

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Independent Context Windows: Every subagent operates within its own isolated context space, preventing cross-contamination between different tasks」

> 「Domain-Specific Intelligence: Subagents come equipped with carefully crafted instructions tailored to their area of expertise」

> 「Shared Across Projects: After creating a subagent, you can utilize it throughout various projects and distribute it among team members」

> 「Granular Tool Permissions: You can configure each subagent with specific tool access rights」
