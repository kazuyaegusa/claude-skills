# フック駆動の自動品質ゲート

> ツール実行の前後で自動的にチェック（console.log 検出、シークレット検出、フォーマット実行）を挟み込む

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動レビューは漏れるし時間がかかる。フックで機械的に強制すれば、品質低下を未然に防げる

## いつ使うのか

コードレビューを自動化したい、シークレット漏洩を防ぎたい、フォーマットを強制したい

## やり方

1. hooks/hooks.json に matcher（tool == "Edit" && file_path matches "\\.(ts|tsx)$"）と command（grep -n 'console\.log'）を定義
2. Claude Code が Edit/Bash/Write などのツールを実行する直前/直後にフックが自動発火
3. スクリプトが exit 2 を返すとツール実行がブロックされる
4. 既存の Node.js スクリプト（scripts/hooks/*.js）を呼び出す薄いアダプターとして設計

### 入力

- hooks/hooks.json の設定
- scripts/hooks/ 配下の Node.js スクリプト

### 出力

- console.log の自動検出
- シークレットパターン（sk-, ghp_, AKIA）の自動ブロック
- ファイル保存時の自動フォーマット

## 使うツール・ライブラリ

- Claude Code hook system
- Node.js (scripts/hooks/)
- grep, Biome/Prettier

## コード例

```
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx)$\"",
  "hooks": [{
    "type": "command",
    "command": "grep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}
```

## 前提知識

- Claude Code CLI v2.1.0 以降のインストール
- Node.js 18 以降（hooks/scripts の実行に必要）
- Git の基本操作（clone, commit, PR）
- npm/pnpm/yarn/bun のいずれか
- JSON/YAML/TOML の基本文法
- 使用する言語のツールチェーン（TypeScript なら tsc, Python なら pytest など）

## 根拠

> 「Won the Anthropic x Forum Ventures hackathon in Sep 2025 with @DRodriguezFX — built zenith.chat entirely using Claude Code.」

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 → Compacts earlier — better quality in long sessions」

> 「AgentShield integration — /security-scan skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules」

> 「Hooks fire on tool events. Example - warn about console.log: {matcher: 'tool == "Edit" && tool_input.file_path matches "\\.(ts|tsx|js|jsx)$"', hooks: [{type: 'command', command: 'grep -n 'console\.log' "$file_path" && echo '[Hook] Remove console.log' >&2'}]}」

> 「Cross-platform support — Windows, macOS, and Linux, alongside tight integration across major IDEs (Cursor, OpenCode, Antigravity) and CLI harnesses. All hooks and scripts have been rewritten in Node.js for maximum compatibility.」
