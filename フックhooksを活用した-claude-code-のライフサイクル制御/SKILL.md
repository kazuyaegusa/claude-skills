# フック（Hooks）を活用した Claude Code のライフサイクル制御

> Claude Code の動作ライフサイクルの特定ポイント（ファイル書き込み前、コマンド実行前など）でスクリプトを自動実行し、コード品質チェック・セキュリティスキャン・通知などを行う

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude が生成したコードを実際にコミットする前に、自動的に品質チェックや安全性検証を挟むことで、手動レビューの負担を減らし、リスクを低減できるため

## いつ使うのか

TDD を強制したい時、セキュリティスキャンを自動化したい時、コード整形を自動適用したい時、通知を送りたい時

## やり方

1. `.claude/hooks/` ディレクトリにフック設定ファイル（JSON）を配置
2. フックのトリガータイミング（user-prompt-submit、tool-call など）を指定
3. 実行するスクリプト（Bash、Python など）を定義
4. スクリプト内で静的解析、テスト実行、セキュリティスキャンなどを実行
5. 結果を Claude に返し、問題があれば変更をブロック

### 入力

- フック設定ファイル（JSON）
- 実行スクリプト（Bash、Python など）
- Claude Code のライフサイクルイベント

### 出力

- 自動化された品質チェック結果
- Claude へのフィードバック（エラー、警告など）
- デスクトップ通知（オプション）

## 使うツール・ライブラリ

- TDD Guard
- parry（プロンプトインジェクション検出）
- Dippy（安全なコマンド自動承認）
- TypeScript Quality Hooks

## コード例

```
{
  "name": "tdd-guard",
  "trigger": "tool-call:write",
  "script": "./hooks/tdd-guard.sh",
  "blocking": true
}
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、プロンプト入力）
- Git の基礎知識（コミット、ブランチ、PR 作成）
- Markdown の基本文法
- シェルスクリプト（Bash）の基礎知識（フック・スラッシュコマンドのカスタマイズに必要）
- JSON の基本構造（フック設定ファイルの編集に必要）

## 根拠

> "A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow."

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"
