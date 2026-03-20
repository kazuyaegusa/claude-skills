# 対話式インストーラーによる選択的導入

> 提供されているシェルスクリプト `install-agents.sh` を使い、カテゴリとエージェントを選択的にインストール/アンインストールする

- 出典: https://github.com/VoltAgent/awesome-claude-code-subagents
- 投稿者: VoltAgent
- カテゴリ: claude-code-workflow

## なぜ使うのか

127以上のエージェント全てをインストールすると管理が煩雑になるため、必要なものだけを選んで導入したい場合がある

## いつ使うのか

プラグイン一括導入ではなく、特定のエージェントだけを試したい場合や、カスタマイズしたエージェント定義を管理したい場合

## やり方

1. `git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git` でリポジトリをクローン
2. `cd awesome-claude-code-subagents && ./install-agents.sh` を実行
3. 対話式メニューでカテゴリを選択
4. エージェントを選択してインストール（グローバル or プロジェクト）
5. 不要なエージェントは同じスクリプトでアンインストール可能

### 入力

- リポジトリクローン（または単体インストーラースクリプト）
- シェル実行環境

### 出力

- 選択したエージェントのみが配置される
- インストール/アンインストール履歴

## 使うツール・ライブラリ

- Bash
- Git
- curl（スタンドアロン版利用時）

## コード例

```
# リポジトリクローン版
git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git
cd awesome-claude-code-subagents
./install-agents.sh

# スタンドアロン版（cloneなし）
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh
./install-agents.sh
```

## 前提知識

- Claude Codeの基本操作（CLI起動、エージェント呼び出し）
- サブエージェントの概念理解（独立コンテキスト、ツール権限、モデル選択）
- YAML frontmatter形式の基本構造
- Git操作（クローン、ファイルコピー）またはcurlコマンドの使用
- 対象領域（言語・インフラ・QA等）の基礎知識（各エージェントを活用する場合）

## 根拠

> 「claude plugin marketplace add VoltAgent/awesome-claude-code-subagents」
