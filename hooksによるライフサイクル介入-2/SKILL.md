# Hooksによるライフサイクル介入

> Claude Codeの特定イベント（ファイル書き込み、Bash実行前後等）に、外部スクリプトを自動実行させる

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

エージェントの自律性を保ちながら、TDD違反検知、危険コマンドブロック、通知送信など、人間が定めたガードレールを強制できる

## いつ使うのか

エージェントが特定の原則（TDD、コーディング規約、セキュリティポリシー）を自動遵守すべき時、または外部システム（通知、CI、ログ）と連携したい時

## やり方

1. `.claude/hooks/` 配下にJSON形式でフック定義を記述
2. `event`（例: `file_write`）、`run`（実行スクリプトパス）、`blocking`（true/false）を指定
3. スクリプトは標準入出力でClaude Codeとやり取り（入力: イベント詳細JSON、出力: 承認/拒否+メッセージ）
4. 例: TDD Guardは`file_write`時にテストなし実装変更を検出してブロック

### 入力

- フック定義JSON（event, run, blocking, filter等）
- 実行スクリプト（Bash, Python, TypeScript等）

### 出力

- イベント発生時の自動実行結果（承認/拒否、メッセージ）
- Claude Codeへのフィードバック

## 使うツール・ライブラリ

- .claude/hooks/ 配置
- cchooks（Python SDK）
- claude-code-hooks-sdk（PHP）
- TDD Guard（既製品）

## コード例

```
// hook定義例 (.claude/hooks/tdd-guard.json)
{
  "event": "file_write",
  "run": ".claude/hooks/tdd-guard.sh",
  "blocking": true,
  "filter": "**/*.ts"
}
```

## 前提知識

- Claude Codeの基本的な使い方（セッション開始、ファイル編集、Bash実行）
- Gitの基礎知識（ブランチ、コミット、PR）
- JSON/YAML形式の理解（設定ファイル記述用）
- （オーケストレータ使用時）Dockerまたはgit worktreeの知識
- （言語特化CLAUDE.md使用時）対象言語のビルドツール知識（pnpm, Gradle, cargo等）

## 根拠

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities.」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle.」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」

> 「TDD Guard - A hooks-driven system that monitors file operations in real-time and blocks changes that violate TDD principles.」
