# ライフサイクルフック駆動のObservation記録

> Claude CodeのSessionStart/UserPromptSubmit/PostToolUse/Stop/SessionEndの5つのフックで、全ツール使用を自動記録する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動記録は漏れが発生し、記録忘れでコンテキストが欠損する。ライフサイクルフックなら全アクションを確実に捕捉でき、ゼロコストで完全な履歴が得られる

## いつ使うのか

Claude Codeでプロジェクト開発を継続的に行う全ての場合（デフォルトで有効化すべき）

## やり方

1. `npx claude-mem install`で6つのフックスクリプト（pre-hook含む）を`~/.claude/plugins/`に配置 2. SessionStartで過去の要約を自動注入 3. UserPromptSubmitでユーザー入力を記録 4. PostToolUseで全ツール使用結果をObservationとしてSQLiteに保存 5. SessionEndでセッション全体を要約圧縮

### 入力

- Claude Codeのツール使用イベント（Read/Write/Edit/Bash等）
- ユーザープロンプト
- セッションID

### 出力

- SQLiteに保存されたObservationレコード（ツール名/引数/結果/タイムスタンプ）
- セッション要約（AI圧縮後のセマンティックサマリー）

## 使うツール・ライブラリ

- Claude Agent SDK（フック機構）
- Bun（Worker Service管理）
- SQLite 3（永続化）

## コード例

```
// フック例（SessionStart）
await fetch('http://localhost:37777/session/start', {
  method: 'POST',
  body: JSON.stringify({ sessionId, cwd })
});
// Worker APIが過去の関連要約を返却→プロンプトに自動注入
```

## 前提知識

- Claude Codeの基本的な使い方（ツール使用、セッション概念）
- Node.js 18+のインストール
- SQLiteの基本知識（オプション：データ構造理解のため）
- MCP（Model Context Protocol）の概念（オプション：検索ツール理解のため）

## 根拠

> 「Claude-Mem seamlessly preserves context across sessions by automatically capturing tool usage observations, generating semantic summaries, and making them available to future sessions.」
