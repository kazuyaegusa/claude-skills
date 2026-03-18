# Hooks でライフサイクルに介入する

> Claude Code の動作ライフサイクル（ツール呼び出し前後、ファイル書き込み前後など）に独自スクリプトを挿入し、品質チェック・承認フロー・通知などを自動実行する仕組み

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

AI エージェントは予期しない動作をすることがあり、そのまま実行すると危険なコマンドやセキュリティ脆弱性を含むコードが生成される可能性がある。Hooks を使うことで、人間の承認が必要な操作を自動検出したり、コード品質を事前検証したり、危険な操作をブロックできる

## いつ使うのか

危険なコマンド（rm -rf など）を自動承認せずに人間確認したい場合、コード品質基準を強制したい場合、TDD ルールを守らせたい場合、デスクトップ通知で作業完了を知りたい場合

## やり方

1. `.claude/hooks/` ディレクトリに JSON 設定ファイルを配置
2. 特定のライフサイクルイベント（例: `on_tool_call`, `before_file_write`）にスクリプトをバインド
3. スクリプトは JSON レスポンスを返し、Claude の動作を承認・拒否・修正できる
4. 例: TypeScript プロジェクトで `before_file_write` に ESLint + Prettier を実行し、コード品質を自動保証

### 入力

- Hook 設定ファイル（JSON）
- 実行スクリプト（Bash, Python, Node.js など）
- 品質基準（ESLint, Prettier, テストコマンド）

### 出力

- 自動化された品質ゲート
- 承認・拒否の判定
- 通知・ログ

## 使うツール・ライブラリ

- Dippy（安全なコマンド自動承認）
- parry（プロンプトインジェクション検出）
- TDD Guard（TDD ルール強制）
- TypeScript Quality Hooks

## コード例

```
{
  "on_tool_call": {
    "bash": "./scripts/approve_bash.sh"
  },
  "before_file_write": {
    "*.ts": "eslint --fix && prettier --write"
  }
}
```

## 前提知識

- Claude Code の基本的な使い方（インストール、セッション開始、ファイル操作）
- Git の基礎知識（ブランチ、コミット、PR）
- コマンドライン操作の基本（Bash, tmux など）
- 開発プロセスの基礎知識（TDD, CI/CD, コードレビュー）

## 根拠

> A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow.

> Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.

> Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.

> Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task.

> CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards.
