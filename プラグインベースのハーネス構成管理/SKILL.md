# プラグインベースのハーネス構成管理

> エージェント・スキル・フック・ルール・MCP設定をプラグインとして一括インストールし、Claude Code等のハーネスに統合する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動コピーによる設定ミス・更新漏れを防ぎ、複数プロジェクト間で統一されたワークフローを維持するため

## いつ使うのか

新規プロジェクト立ち上げ時、または既存プロジェクトにECCを導入する初回セットアップ時

## やり方

1. `/plugin marketplace add affaan-m/everything-claude-code` でマーケットプレイス登録 2. `/plugin install everything-claude-code@everything-claude-code` でプラグインインストール 3. `./install.sh --profile full` または言語別に `./install.sh typescript python golang` でルールをインストール 4. プラグインが提供する38エージェント、156スキル、72レガシーコマンドが即座に利用可能に

### 入力

- Claude Code CLI v2.1.0以上
- 対象プロジェクトのディレクトリ
- 使用する言語スタック（TypeScript/Python/Go等）

### 出力

- ~/.claude/rules/ 配下に言語別ルール
- ~/.claude/skills/ 配下にスキル定義
- hooks/hooks.json が自動ロードされる
- プラグイン経由で /plan, /tdd, /code-review 等のコマンドが利用可能

## 使うツール・ライブラリ

- Claude Code CLI v2.1.0+
- install.sh（macOS/Linux）/ install.ps1（Windows）
- npm/pnpm/yarn/bun（依存インストール用）

## コード例

```
# Claude Code
/plugin marketplace add affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code

# ルールは手動インストール必須（プラグインシステムの制約）
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code
./install.sh --profile full
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）

## 根拠

> 「Selective install architecture — Manifest-driven install pipeline with install-plan.js and install-apply.js for targeted component installation」
