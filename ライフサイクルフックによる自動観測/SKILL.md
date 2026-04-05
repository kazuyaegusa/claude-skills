# ライフサイクルフックによる自動観測

> Claude Codeの7つのライフサイクルイベント（SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd等）をフックし、ツール実行・ユーザー入力を自動記録する

- 出典: https://github.com/thedotmack/claude-mem
- 投稿者: thedotmack
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動ロギングは運用負荷が高く漏れが生じる。フックによる自動キャプチャで、ユーザーが意識せずとも全てのコンテキストを保存できる

## いつ使うのか

Claude Codeでプロジェクトを長期運用し、セッション間の文脈継続性が必要な時

## やり方

1. `npx claude-mem install` で7つのフックスクリプトを `~/.claude/hooks/` に配置
2. Claude Code起動時にSessionStartフックが発火、Workerサービス起動確認
3. ツール実行後にPostToolUseフックが実行結果を `/api/observation` に送信
4. SessionEndフックでセッション全体のサマリーを生成・保存

### 入力

- Claude Codeのhooksディレクトリ（`~/.claude/hooks/`）
- Workerサービス（HTTPサーバー on port 37777）

### 出力

- 観測データ（observations）のSQLite保存
- セッションサマリー（AI圧縮済み）

## 使うツール・ライブラリ

- Claude Agent SDK（フック機構）
- TypeScript/Bun（Worker実装）

## コード例

```
// PostToolUseフック疑似コード
const observation = {
  tool: toolName,
  input: toolInput,
  output: toolOutput,
  timestamp: Date.now()
};
await fetch('http://localhost:37777/api/observation', {
  method: 'POST',
  body: JSON.stringify(observation)
});
```

## 前提知識

- Claude Codeの基本操作とプラグインシステムの理解
- Node.js 18.0.0+の実行環境
- SQLiteの基本概念（テーブル、クエリ）
- ベクトル検索・埋め込みの基礎知識（Chroma理解のため）
- ライフサイクルフック・イベント駆動設計の概念
- TypeScript/JavaScript（カスタマイズ時）

## 根拠

> 「Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.」

> 「5 Lifecycle Hooks - SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd」

> 「Install with a single command: npx claude-mem install」
