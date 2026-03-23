# トークン最適化設定による 60-70% コスト削減

> model, MAX_THINKING_TOKENS, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE の 3 つを調整して、品質を維持しながらコストを大幅削減

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

デフォルト設定（Opus + 31,999 思考トークン + 95% 自動コンパクト）は過剰。Sonnet で 80% のタスクをこなせ、思考トークンは隠れコストが大きい

## いつ使うのか

日次の利用限度に達しやすい、長時間セッションで品質が下がる、コスト管理が必要な場合

## やり方

1. ~/.claude/settings.json に model: "sonnet", MAX_THINKING_TOKENS: "10000", CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: "50" を設定
2. 複雑なアーキテクチャ判断時のみ /model opus で切り替え
3. 無関係なタスク間では /clear でコンテキストリセット
4. 論理的な区切り（リサーチ完了、マイルストーン達成）で /compact を手動実行

### 入力

- settings.json への書き込み権限
- セッション中の /model, /clear, /compact コマンド実行

### 出力

- 60% のコスト削減（Opus→Sonnet）
- 70% の思考トークン削減
- 長時間セッションでの品質維持

## 使うツール・ライブラリ

- Claude Code CLI
- settings.json

## コード例

```
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
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

> 「model: sonnet → ~60% cost reduction; handles 80%+ of coding tasks」

> 「MAX_THINKING_TOKENS: 10,000 → ~70% reduction in hidden thinking cost per request」

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 → Compacts earlier — better quality in long sessions」
