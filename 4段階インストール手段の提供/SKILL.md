# 4段階インストール手段の提供

> プラグイン方式、手動コピー、対話型スクリプト、スタンドアロンインストーラの4種類を用意し、ユーザーの環境と好みに応じて選択可能にする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

チーム全体への一括配布、個人カスタマイズ、CI/CD統合など利用シーンが多様なため。初心者は対話型、上級者は手動/スクリプト、エンタープライズはプラグイン、という使い分けを可能にする

## いつ使うのか

プラグイン: チーム標準化時、手動: カスタマイズが必要な時、対話型/スタンドアロン: 初回セットアップ時、エージェントインストーラ: Claude Code内で完結させたい時

## やり方

1. **プラグイン方式**: `claude plugin marketplace add VoltAgent/awesome-claude-code-subagents` → `claude plugin install voltagent-lang` でカテゴリ単位インストール
2. **手動インストール**: リポジトリをcloneし、目的のエージェントファイルを `~/.claude/agents/` (グローバル)または `.claude/agents/` (プロジェクト固有)にコピー
3. **対話型スクリプト**: `./install-agents.sh` を実行し、カテゴリ選択→エージェント選択→インストール/アンインストールをメニュー形式で行う
4. **スタンドアロン**: `curl -sO https://.../install-agents.sh && chmod +x install-agents.sh && ./install-agents.sh` でクローン不要で実行
5. **エージェントインストーラ**: `agent-installer.md` を `~/.claude/agents/` に配置し、Claude Code内で "Find PHP agents and install php-pro globally" のように自然言語で検索・インストール

### 入力

- インストール先パス(~/.claude/agents/ または .claude/agents/)
- 対象エージェント/カテゴリ名

### 出力

- 指定パスにコピーされたエージェント定義ファイル
- Claude Codeから即座に呼び出し可能な状態

## 使うツール・ライブラリ

- curl
- bash
- Claude Code plugin CLI

## コード例

```
# プラグイン方式
claude plugin install voltagent-lang

# スタンドアロン
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh

# エージェントインストーラ
curl -s https://.../agent-installer.md -o ~/.claude/agents/agent-installer.md
# Claude Code内で: "Find PHP agents and install php-pro globally"
```

## 前提知識

- Claude Code CLIの基本操作(/agents コマンド、サブエージェント概念)
- Markdownの読み書き(frontmatterとYAML構文)
- Bashコマンド(curl, chmod)の基礎知識
- プロジェクトとグローバルの設定ファイル配置の違い(~/.config vs .config的な概念)
- 開発ライフサイクル(開発→テスト→デプロイ→運用)の理解

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Smart Model Routing: Each subagent includes a model field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Project Subagents: .claude/agents/ Current project only Higher precedence, Global Subagents: ~/.claude/agents/ All projects Lower precedence」

> 「127+ subagents covering a wide range of development use cases」

> 「4 installation options: As Claude Code Plugin, Manual Installation, Interactive Installer, Standalone Installer, Agent Installer」
