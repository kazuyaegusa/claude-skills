# Hooksによるライフサイクル介入

> Claude Codeの特定のライフサイクルイベント（ファイル書き込み前後、コマンド実行前後など）で任意のスクリプトを実行し、AIの動作を制御または拡張する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

AIが生成したコードを人間が毎回レビューするのは非効率。自動化可能なチェック（lint、test、セキュリティスキャン）はHooksで実施し、違反があれば操作をブロックすることで品質を保ちつつ高速に開発できる

## いつ使うのか

コード品質チェック、セキュリティスキャン、通知送信、マルチエージェント通信、TDD規律の強制など、「特定タイミングで必ず実行したい処理」がある場合

## やり方

1. `.claude/hooks.json`に hook定義を追加（例：`on_before_write`イベント）
2. 実行するスクリプト（Bash、Python、Node.js等）のパスと引数を指定
3. スクリプトは標準出力にJSON形式で結果を返す（`{"approved": false, "message": "..."}`でブロック可能）
4. Claude Codeが該当イベント発生時に自動でスクリプトを呼び出す

例：TDD Guardは`on_before_write`でファイル変更を監視し、テストより先に実装コードが書かれた場合に書き込みをブロック

### 入力

- Hook定義ファイル（`.claude/hooks.json`）
- 実行するスクリプト
- イベント種別（on_before_write, on_after_bash等）

### 出力

- スクリプトからの承認/拒否レスポンス
- エラーメッセージやログ
- 通知（デスクトップ、Slack等）

## 使うツール・ライブラリ

- TDD Guard
- parry（prompt injection scanner）
- Dippy（安全なbashコマンドの自動承認）
- CC Notify（デスクトップ通知）
- Claude Code Hook Comms（マルチエージェント通信）

## コード例

```
{
  "hooks": [
    {
      "event": "on_before_write",
      "script": "./scripts/tdd_check.sh",
      "args": ["${file_path}", "${content}"]
    }
  ]
}
```

## 前提知識

- Claude Codeの基本的な使い方（CLI操作、プロンプト入力、ファイル編集）
- Gitの基礎知識（branch、commit、PR）
- シェルスクリプト/Python/Node.jsの基礎（Hooks実装時）
- Docker/tmuxの基礎知識（Orchestrators使用時）
- JSON/YAML形式の理解（設定ファイル編集時）

## 根拠

> "Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle."

> "Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task"

> "CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards"

> "Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities."

> "ccflare - Claude Code usage dashboard with a web-UI that would put Tableau to shame. Thoroughly comprehensive metrics, frictionless setup, detailed logging, really really nice UI."
