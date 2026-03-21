# 4種類のインストール手法の使い分け

> プラグイン、手動コピー、対話式インストーラ、AI経由インストールの4つの方法を用途に応じて選択する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

チーム構成、技術レベル、ワークフローの違いに対応し、誰でも簡単にサブエージェントを導入できるようにするため

## いつ使うのか

プラグイン: 定期更新を受けたい時、手動: カスタマイズ前提の時、対話式: 初回導入時、AI経由: 非技術者や探索的な導入時

## やり方

1. **プラグイン（推奨）**: カテゴリ単位で一括導入したい場合、`claude plugin install voltagent-xxx` を実行
2. **手動コピー**: 特定エージェントのみ必要な場合、リポジトリをクローンし、`.md` ファイルを `~/.claude/agents/` または `.claude/agents/` にコピー
3. **対話式インストーラ**: `./install-agents.sh` を実行し、カテゴリを閲覧しながら選択的にインストール/アンインストール
4. **AI経由（agent-installer）**: `agent-installer.md` をインストールし、Claude Code内で「Find PHP agents and install php-pro globally」のように自然言語で指示

### 入力

- 導入したいエージェントの種類（カテゴリ or 個別）
- グローバル or プロジェクト限定の選択

### 出力

- 指定エージェントが適切なディレクトリに配置される
- 即座に利用可能な状態

## 使うツール・ライブラリ

- Claude Code CLI
- Bash
- curl
- agent-installer.md

## コード例

```
# プラグイン方式
claude plugin install voltagent-lang

# 手動コピー
cp categories/02-language-specialists/python-pro.md ~/.claude/agents/

# 対話式インストーラ（clone不要）
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh

# AI経由インストール
curl -s https://raw.githubusercontent.com/.../agent-installer.md -o ~/.claude/agents/agent-installer.md
# 次にClaude Codeで: "Find PHP agents and install php-pro globally"
```

## 前提知識

- Claude Codeの基本的な使い方（サブエージェント機能の理解）
- YAMLフロントマターとMarkdownの読み書き
- コマンドラインツール（claude CLI、curl、bash）の操作経験
- 開発ドメイン知識（各サブエージェントを効果的に使うため、対象領域の基礎理解が必要）

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Domain-Specific Intelligence: Subagents come equipped with carefully crafted instructions tailored to their area of expertise」

> 「Shared Across Projects: After creating a subagent, you can utilize it throughout various projects and distribute it among team members」

> 「model field that automatically routes it to the right Claude model — balancing quality and cost: opus (Deep reasoning), sonnet (Everyday coding), haiku (Quick tasks)」

> 「Read-only agents (reviewers, auditors): Read, Grep, Glob - analyze without modifying」
