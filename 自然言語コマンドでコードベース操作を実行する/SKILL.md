# 自然言語コマンドでコードベース操作を実行する

> Claude Codeセッション内で自然言語の指示を与え、コード理解・編集・Git操作などを実行させる

- 出典: https://github.com/anthropics/claude-code
- 投稿者: anthropics
- カテゴリ: claude-code-workflow

## なぜ使うのか

複雑なタスク（複数ファイル編集、リファクタリング、Git操作）を自然言語で指示することで、手作業のコマンド列挙や手順記憶が不要になり、開発速度が向上する

## いつ使うのか

定型的なコード変更、複数ファイルに跨がるリファクタリング、Git操作の自動化が必要な時

## やり方

1. `claude` コマンドでセッションを開始
2. 自然言語で指示を入力（例：「このファイルのこの関数を説明して」「全てのconsole.logを削除して」「変更をコミットしてPRを作成して」）
3. Claude Codeがコードベースを解析し、ファイル編集・Git操作等を実行
4. 結果を確認し、必要に応じて追加指示や修正を指示

### 入力

- 自然言語での指示文
- 対象コードベース
- Git設定（コミット・PR作成時）

### 出力

- コードの説明・解析結果
- 編集されたファイル群
- Gitコミット・PR

## 使うツール・ライブラリ

- Claude Code CLI

## コード例

```
# セッション開始
$ claude

# 自然言語での指示例
> このディレクトリ内の全てのTODOコメントをリストアップして
> auth.tsのログイン処理を説明して
> 全ファイルのconsole.logをlogger.debugに置き換えて
> 変更をコミットして「refactor: replace console.log with logger」というメッセージでPRを作成
```

## 前提知識

- ターミナル操作の基本知識
- Gitの基本的な概念（コミット、PR）
- Node.js環境（npm経由インストール時）
- Anthropic APIキーまたはClaude Codeサブスクリプション
- コーディング経験（対象コードベースの言語に対する基本理解）

## 根拠

> "Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands."

> "curl -fsSL https://claude.ai/install.sh | bash"

> "This repository includes several Claude Code plugins that extend functionality with custom commands and agents."

> "Use the `/bug` command to report issues directly within Claude Code"

> "Learn more in the [official documentation](https://code.claude.com/docs/en/overview)."
