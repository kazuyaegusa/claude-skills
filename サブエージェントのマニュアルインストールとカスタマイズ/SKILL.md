# サブエージェントのマニュアルインストールとカスタマイズ

> GitHubリポジトリから特定のサブエージェントファイル（Markdown形式）をダウンロードし、`~/.claude/agents/`（グローバル）または`.claude/agents/`（プロジェクト固有）に配置してカスタマイズする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

プラグイン経由ではなく、特定のエージェントだけを導入したい場合や、チーム独自の要件に合わせてエージェントの指示内容・ツール権限・モデル選択を細かく調整したい場合に有効

## いつ使うのか

特定のエージェントだけが必要な場合、社内独自のコーディング規約やツールチェーンに合わせてエージェントをカスタマイズしたい場合、プラグインインストールが制限されている環境

## やり方

1. https://github.com/VoltAgent/awesome-claude-code-subagents の該当カテゴリフォルダから必要なエージェントの`.md`ファイルを特定
2. ファイルをローカルにダウンロードまたはクローン
3. グローバル利用なら`~/.claude/agents/`、プロジェクト固有なら`.claude/agents/`にコピー
4. エージェントファイル内のYAMLフロントマター（name, description, tools, model）や本文を編集して、プロジェクト固有のルールやツールを追加
5. Claude Codeを再起動または`/agents`コマンドで認識を確認

### 入力

- GitHubリポジトリへのアクセス
- カスタマイズ要件（使用ツール、モデル選択、指示内容）

### 出力

- カスタマイズされたサブエージェント定義ファイル（.md）
- プロジェクトまたはグローバルに配置されたエージェント

## 使うツール・ライブラリ

- git clone または curl/wget
- テキストエディタ（エージェント定義編集用）

## コード例

```
# Option 3: Standalone Installer（clone不要）
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh

# Option 4: Agent Installerを使ってClaude Code内から対話的にインストール
curl -s https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/09-meta-orchestration/agent-installer.md -o ~/.claude/agents/agent-installer.md
# 次にClaude Codeで「Use the agent-installer to show me available categories」と指示
```

## 前提知識

- Claude Code CLI がインストールされていること
- Claude Codeの基本操作（エージェント起動、ツール実行）の理解
- YAMLフロントマターの基本構文知識（エージェントカスタマイズ時）
- gitの基本操作（リポジトリクローン、ファイルコピー）
- 対象プロジェクトの技術スタックと開発フローの把握

## 根拠

> 「This repository serves as the definitive collection of Claude Code subagents, specialized AI assitants designed for specific development tasks.」

> 「Smart Model Routing: Each subagent includes a model field that automatically routes it to the right Claude model — balancing quality and cost」

> 「Global Subagents: ~/.claude/agents/ - All projects - Lower precedence」「Project Subagents: .claude/agents/ - Current project only - Higher precedence」
