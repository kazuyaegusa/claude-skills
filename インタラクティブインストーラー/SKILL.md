# インタラクティブインストーラー

> シェルスクリプトベースの対話的UIでカテゴリ・エージェントを選択し、インストール/アンインストールを実行する

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

コマンドラインに不慣れなユーザーでも、対話形式でエージェントを管理できる。また、リポジトリをクローンせずに直接GitHubから取得できるスタンドアロン版もあり、導入障壁が低い

## いつ使うのか

GUIツールなしでエージェントを管理したい時、または自動化スクリプトに組み込みたい時

## やり方

1. `git clone`してリポジトリをローカルに取得
2. `./install-agents.sh`を実行
3. 対話メニューでカテゴリ選択→エージェント選択→インストール先（グローバル/プロジェクト）を指定
4. スタンドアロン版は`curl -sO https://.../install-agents.sh && chmod +x install-agents.sh && ./install-agents.sh`で実行

### 入力

- 選択したいカテゴリ/エージェント名
- インストール先（~/.claude/agents/ または .claude/agents/）

### 出力

- 選択されたエージェントが指定パスに配置される

## 使うツール・ライブラリ

- Bash
- curl
- GitHub Raw Content API

## コード例

```
# Option 2: Interactive Installer
git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git
cd awesome-claude-code-subagents
./install-agents.sh

# Option 3: Standalone Installer (no clone)
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh
```

## 前提知識

- Claude Code CLIがインストールされている
- claude plugin機能の基本的な理解
- サブエージェントの概念（独立したコンテキストウィンドウ、ドメイン特化型プロンプト）
- Markdown/YAMLの基本文法
