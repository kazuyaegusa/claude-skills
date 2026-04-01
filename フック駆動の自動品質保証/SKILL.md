# フック駆動の自動品質保証

> ツール実行（Edit/Bash/Submit等）の前後でフックスクリプトを発火させ、フォーマット・型チェック・console.log警告・秘密情報検出を自動実行する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動レビューは漏れが多く後追いコストが高い。ツールイベントをトリガーに自動検証することで、問題を作り込む前に防げる

## いつ使うのか

コード編集後の手動チェックを減らしたい、秘密情報の誤コミットを防ぎたい、一貫した品質基準を自動適用したいとき

## やり方

1. hooks/hooks.json に matcher（条件式）と command（実行スクリプト）を定義 2. Claude Codeは PostToolUse、Cursorは afterFileEdit、OpenCodeは file.edited でそれぞれ発火 3. scripts/hooks/*.js の共通スクリプトがフォーマット実行・型チェック・秘密情報パターンマッチを実行 4. 違反時は stderr に警告を出力または exit 2 でブロック

### 入力

- hooks/hooks.json（フック定義）
- scripts/hooks/*.js（共通スクリプト）
- ツール固有アダプタ（Cursor: .cursor/hooks/adapter.js）

### 出力

- 自動フォーマット済みファイル
- 型エラー警告
- console.log検出警告
- 秘密情報検出時のブロック

## 使うツール・ライブラリ

- Node.js
- Prettier/Biome（フォーマッタ）
- TypeScript（tsc --noEmit）
- grep（パターンマッチ）

## コード例

```
// hooks/hooks.json の例
{
  "matcher": "tool == 'Edit' && tool_input.file_path matches '\\.(ts|tsx)$'",
  "hooks": [{
    "type": "command",
    "command": "node scripts/hooks/format-and-check.js $file_path"
  }]
}

// scripts/hooks/format-and-check.js（疑似コード）
const { execSync } = require('child_process');
const file = process.argv[2];
execSync(`prettier --write ${file}`);
execSync(`tsc --noEmit ${file}`);
if (fs.readFileSync(file, 'utf8').includes('console.log')) {
  console.error('[Hook] Remove console.log');
}
```

## 前提知識

- Claude Code CLI v2.1.0以上のインストール
- Node.js環境（フックスクリプト実行用）
- Git（リポジトリクローン用）
- 対象言語の開発環境（TypeScript/Python/Go等）
- Claude Codeのサブスクリプション（トークン消費制限緩和のため推奨）
- AIエージェント・プロンプトエンジニアリングの基礎知識

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「Works across Claude Code, Codex, Cowork, and other AI agent harnesses.」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「model=sonnet, MAX_THINKING_TOKENS=10000, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50 で ~60% cost reduction」
