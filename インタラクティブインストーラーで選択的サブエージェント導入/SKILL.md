# インタラクティブインストーラーで選択的サブエージェント導入

> 対話型シェルスクリプトでカテゴリをブラウズし、必要なサブエージェントだけを選択してインストール/アンインストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

全カテゴリではなく特定のエージェントだけが必要な場合、手動コピーより効率的で、視覚的にカテゴリとエージェントを確認しながら選択できるため

## いつ使うのか

特定のプロジェクトで必要なエージェントだけをピンポイントで導入したい時、エージェント一覧を視覚的に確認しながら選びたい時

## やり方

1. `git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git`
2. `cd awesome-claude-code-subagents`
3. `./install-agents.sh` を実行
4. インタラクティブメニューでカテゴリ選択→エージェント選択→インストール先（グローバル/プロジェクト）指定

### 入力

- git, curl がインストール済み
- ~/.claude/agents/ または .claude/agents/ への書き込み権限

### 出力

- 選択したサブエージェントの.mdファイルが指定パスにコピーされる

## 使うツール・ライブラリ

- Bash
- install-agents.sh

## コード例

```
git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git
cd awesome-claude-code-subagents
./install-agents.sh
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解
