# フックベースの自動化（セッション永続化・フォーマット・セキュリティ）

> PreToolUse/PostToolUse/Stop/SessionStart等のフックイベントに、メモリ永続化・自動フォーマット・セキュリティ警告・戦略的圧縮提案を紐付け、手動オペレーションを削減する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じチェックや保存を手動実行すると抜け漏れが発生し、セッション間で文脈が失われる。フックで自動化すれば一貫性と再現性が向上

## いつ使うのか

セッション間で文脈が失われる、手動チェック（lint/format/型チェック）を毎回忘れる、セキュリティリスク（シークレット混入）を検出したい場合

## やり方

1. hooks/hooks.json に各イベントのトリガー条件とスクリプトを定義 2. SessionStart時に scripts/hooks/session-start.js が前回保存した .claude/session-context.md を読み込み 3. PostToolUse（Edit後）に自動フォーマット・型チェック・console.log警告 4. Stop時に scripts/hooks/session-end.js がセッション要約を保存 5. 戦略的圧縮提案フックが「研究完了→実装前」等のタイミングで /compact を推奨

### 入力

- hooks/hooks.json 設定
- scripts/hooks/*.js スクリプト
- Claude Code v2.1.0+（自動フックロード）

### 出力

- .claude/session-context.md（セッション間で永続化）
- Edit後に自動フォーマット・型チェック実行
- console.log検出時に警告
- 戦略的タイミングで /compact 提案

## 使うツール・ライブラリ

- hooks/hooks.json
- Node.js（scripts/hooks/*.js）
- Claude Code hook system

## コード例

```
// hooks/hooks.json（抜粋）
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}

// scripts/hooks/session-start.js（概要）
// 1. .claude/session-context.md を読み込み
// 2. システムプロンプトに注入してコンテキスト復元

// scripts/hooks/session-end.js（概要）
// 1. セッション全体を要約
// 2. .claude/session-context.md に保存
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）
