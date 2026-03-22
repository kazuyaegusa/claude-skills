# Magic keywordsで即座にモード切替

> autopilot/ralph/ulw/ralplan等の予約語をプロンプトに含めるだけで、対応する実行モードを起動する

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

コマンド構文を覚えなくても、自然言語の中にキーワードを混ぜるだけで高度な機能（永続実行・最大並列化・反復計画等）を呼び出せる

## いつ使うのか

特定の実行戦略（並列化・永続実行・計画重視等）を明示的に指定したい時、またはショートカットで効率化したい時

## やり方

1. `autopilot: build a REST API for managing tasks` でフル自律実行
2. `ralph: refactor auth` で検証ループ付き永続モード
3. `ulw fix all errors` で最大並列化
4. `ralplan this feature` で反復的計画合意形成
5. キーワード不要なら通常の自然言語でも動作

### 入力

- OMCがインストール済み
- 実行したいタスクの自然言語記述

### 出力

- 指定モードでのタスク実行
- autopilot → 単一リードエージェントの自律実行
- ralph → verify/fixループでの永続実行
- ulw → 最大並列度での実行

## 使うツール・ライブラリ

- oh-my-claudecode

## コード例

```
autopilot: build a REST API for managing tasks
ralph: refactor auth module
ulw fix all TypeScript errors
ralplan implement user authentication
```

## 前提知識

- Claude Code CLIの基本操作（インストール・起動）
- Claude Max/ProサブスクリプションまたはAnthropic APIキー
- tmux（CLI workers使用時）
- Node.js/npm（プラグインインストール時）
- Git（スキルのバージョン管理時）

## 根拠

> 「Multi-agent orchestration for Claude Code. Zero learning curve.」

> 「Team runs as a staged pipeline: team-plan → team-prd → team-exec → team-verify → team-fix (loop)」

> 「32 specialized agents for architecture, research, design, testing, data science」

> 「autopilot: build a REST API for managing tasks - That's it. Everything else is automatic.」

> 「The deep interview uses Socratic questioning to clarify your thinking before any code is written」
