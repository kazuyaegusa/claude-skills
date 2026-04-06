# トークン消費最適化設定

> model選択・思考トークン制限・早期コンパクションにより、品質を保ちつつコストを60-70%削減する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

デフォルトのOpus+31,999思考トークン+95%コンパクションでは日次上限に達しやすい。大半のタスクはSonnetで十分対応可能

## いつ使うのか

Claude Code利用開始時に初期設定として導入し、日常的に運用

## やり方

1. ~/.claude/settings.json に以下を追加:
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
}
2. 通常タスクは /model sonnet で実行
3. 複雑なアーキテクチャ設計・深い推論が必要な時のみ /model opus に切り替え
4. 無関係なタスク間で /clear（即座にリセット、無料）
5. 論理的な区切り（調査完了後、マイルストーン達成後）で /compact
6. /cost でトークン消費モニタリング

### 入力

- ~/.claude/settings.json への書き込み権限

### 出力

- 通常タスクで60%コスト削減（Opus→Sonnet）
- 思考トークンで70%削減（31,999→10,000）
- 長時間セッションでの品質向上（50%で早期コンパクション）

## 使うツール・ライブラリ

- Claude Code settings.json

## コード例

```
// ~/.claude/settings.json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）

## 根拠

> 「model: sonnet — ~60% cost reduction; handles 80%+ of coding tasks」
