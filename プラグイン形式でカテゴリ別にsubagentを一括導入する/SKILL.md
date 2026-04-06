# プラグイン形式でカテゴリ別にsubagentを一括導入する

> GitHubリポジトリをClaude Codeのプラグインマーケットプレイスに追加し、カテゴリ単位（voltagent-lang, voltagent-infra等）でsubagent群をインストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

130種以上のsubagentを個別管理せず、関連する専門家群をパッケージとして導入することで、セットアップ時間を削減し、必要な専門性を一度に揃えられる

## いつ使うのか

新規プロジェクト開始時に必要な専門家を一括セットアップしたい時、チーム全体で標準的なsubagent構成を共有したい時

## やり方

1. `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents`でリポジトリを登録
2. `claude plugin install voltagent-lang`（言語専門家）、`voltagent-infra`（インフラ）等、必要なカテゴリをインストール
3. インストールされたsubagentは自動的に利用可能になり、Claudeが適切なタイミングで起動

### 入力

- 必要な専門領域（言語、インフラ、QA、データ等）
- Claude Codeのプラグイン機能

### 出力

- カテゴリ別にインストールされた専門subagent群
- 即座に利用可能な専門知識ベース

## 使うツール・ライブラリ

- Claude Code CLI
- GitHub

## コード例

```
# プラグインマーケットプレイスに追加
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents

# 言語専門家をインストール
claude plugin install voltagent-lang

# インフラ専門家をインストール
claude plugin install voltagent-infra
```

## 前提知識

- Claude Codeの基本的な使用経験
- subagentの概念理解（独立したコンテキストを持つ専門AIアシスタント）
- YAML frontmatterの基本構文
- コマンドラインツール（curl, git）の基本操作
- 対象言語・フレームワークの基礎知識（各subagent活用時）

## 根拠

> 「claude plugin marketplace add VoltAgent/awesome-claude-code-subagents」「claude plugin install voltagent-lang」
