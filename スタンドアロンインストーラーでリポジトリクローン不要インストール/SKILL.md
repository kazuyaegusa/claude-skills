# スタンドアロンインストーラーでリポジトリクローン不要インストール

> GitHubから直接スクリプトをダウンロードし、リポジトリクローンなしでサブエージェントをインストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

ディスク容量を節約でき、ローカルにリポジトリ全体を保持する必要がない。単発で特定エージェントを導入したい場合に最適

## いつ使うのか

CI/CD環境や一時的な環境で、リポジトリ全体をクローンせずにエージェントだけ導入したい時

## やり方

1. `curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh`
2. `chmod +x install-agents.sh`
3. `./install-agents.sh` を実行
4. スクリプトがGitHubから直接エージェント定義を取得してインストール

### 入力

- curl コマンド
- インターネット接続（GitHub APIアクセス）

### 出力

- 選択したサブエージェントが直接 ~/.claude/agents/ にダウンロード・インストールされる

## 使うツール・ライブラリ

- curl
- Bash

## コード例

```
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh
```

## 前提知識

- Claude Codeがインストール・セットアップ済み
- サブエージェントの概念理解（独立したコンテキストウィンドウ、ドメイン特化プロンプト、ツール権限管理）
- 基本的なCLI操作（curl, chmod, git clone等）
- YAMLフロントマター形式の理解（サブエージェント定義ファイルの編集時）
- Claude Codeの /agents コマンドとサブエージェント呼び出し構文の理解
