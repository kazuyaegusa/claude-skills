# Hooksによるライフサイクル介入

> Claude Codeのツール実行前後（ファイル書き込み、コミット、Bash実行等）に任意のスクリプトを自動実行し、検証・変換・通知を行う

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeが生成したコードやコマンドをそのまま実行すると、フォーマット違反やテスト失敗、セキュリティリスクが残る。Hooksで自動チェック・修正することで品質を担保

## いつ使うのか

コミット前にテスト強制、ファイル保存時にフォーマット適用、危険なBashコマンドをブロック、タスク完了時に通知、といった自動化が必要な時

## やり方

1. `~/.claude/hooks/` に `<event-name>.json` を作成
2. JSON内で `command`（実行するスクリプト）と `event`（tool_use, tool_result等）を指定
3. スクリプトは標準入力でClaude Codeのツール情報を受け取り、標準出力でJSONレスポンスを返す
4. `block: true` で実行をブロック、`message` でClaude Codeにフィードバック

### 入力

- Hookスクリプト（任意の言語、標準入出力でJSON処理）
- ~/.claude/hooks/<event>.json 設定ファイル

### 出力

- Claude Codeのツール実行前後で自動検証・修正
- 条件に応じた実行ブロック・警告

## 使うツール・ライブラリ

- TDD Guard（TDD原則違反をブロック）
- TypeScript Quality Hooks（ESLint/Prettier自動適用）
- Dippy（危険なBashコマンドを自動承認/拒否）

## コード例

```
# 例: ~/.claude/hooks/pre-commit.json
{
  "event": "tool_use",
  "tool": "Bash",
  "command": "./check-tests.sh",
  "block": true
}

# check-tests.sh: テストが通らなければClaude Codeをブロック
#!/bin/bash
npm test || echo '{"block":true,"message":"Tests failed"}'
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- Git/GitHubの基礎知識（ブランチ、コミット、PR）
- ターミナル操作とシェルスクリプトの基本
- Markdown記法の理解
- 使用する言語・フレームワークの基礎知識（TypeScript、Python、Go等）

## 根拠

> 「A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow」

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」
