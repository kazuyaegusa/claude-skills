# Hooksによるガードレール実装

> Claude Codeの操作（ファイル書き込み・コマンド実行等）をフックして自動検証・承認制御を追加する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

TDD違反・インジェクション攻撃・破壊的コマンドの実行を防ぎ、安全性と品質を保証するため

## いつ使うのか

リアルタイムで品質チェック・セキュリティ検証を強制したいとき

## やり方

1. `~/.claude/hooks/`に実行可能スクリプトを配置
2. `on_file_write`, `on_bash_command`等のイベントに対応
3. スクリプトでvalidation（AST解析・パターンマッチ等）
4. 成功時は許可、失敗時はブロック＋フィードバック
5. TDD Guard（テストなしの実装をブロック）、Dippy（安全なコマンドのみ自動承認）等を参考に実装

### 入力

- フックイベント（ファイルパス・コマンド等）
- 検証ロジック（AST・正規表現・外部ツール）

### 出力

- 許可/ブロック判定
- フィードバックメッセージ

## 使うツール・ライブラリ

- Bashスクリプト
- TypeScript/Python（パース用）
- AST解析ライブラリ

## コード例

```
#!/bin/bash
# on_file_write hook例
FILE_PATH=$1
if [[ ! -f "${FILE_PATH%.ts}.test.ts" ]]; then
  echo '{"allow": false, "feedback": "Test file missing"}'
  exit 1
fi
echo '{"allow": true}'
```

## 前提知識

- Claude Codeの基本操作（CLI使用・セッション管理）
- マークダウンフォーマットの理解
- Bash/Python/TypeScriptのいずれかでスクリプト作成経験
- Git・GitHub CLIの基礎知識
- LLMエージェントの基本概念（プロンプトエンジニアリング・コンテキスト管理）

## 根拠

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "Agent Teams - Launch Claude Code session that is connected to a swarm of Claude Code Agents"
