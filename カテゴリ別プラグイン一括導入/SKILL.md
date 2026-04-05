# カテゴリ別プラグイン一括導入

> 130+のサブエージェントを9つのカテゴリ（言語/インフラ/QA/AI/DevExp等）に分類し、`claude plugin install <カテゴリ名>`で必要なエージェント群をまとめて導入する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別インストールの手間を省き、プロジェクトに必要な専門エージェントセットを素早く揃えられる。カテゴリ単位で管理することでメンテナンス性も向上する

## いつ使うのか

新規プロジェクト立ち上げ時、または既存プロジェクトに専門エージェントを導入したい時

## やり方

1. `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents`でマーケットプレースに登録
2. `claude plugin install voltagent-lang`等でカテゴリ別プラグインをインストール
3. インストールされたエージェントは`~/.claude/agents/`に配置され、全プロジェクトで利用可能になる

### 入力

- GitHubリポジトリURL
- インストールしたいカテゴリ名（voltagent-lang, voltagent-infra等）

### 出力

- ~/.claude/agents/配下にエージェント定義ファイル（.mdファイル）が配置される
- Claude Code内で該当エージェントが自動認識され利用可能になる

## 使うツール・ライブラリ

- Claude Code CLI
- claude plugin marketplace

## コード例

```
# マーケットプレース登録
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents

# カテゴリ別インストール
claude plugin install voltagent-lang    # 言語専門家
claude plugin install voltagent-infra   # インフラ/DevOps
claude plugin install voltagent-qa-sec  # QA/セキュリティ
```

## 前提知識

- Claude Code CLIがインストールされている
- claude plugin機能の基本的な理解
- サブエージェントの概念（独立したコンテキストウィンドウ、ドメイン特化型プロンプト）
- Markdown/YAMLの基本文法

## 根拠

> claude plugin marketplace add VoltAgent/awesome-claude-code-subagents

> agent-installer: Browse and install agents from this repository via GitHub
