# トークン消費の60-70%削減設定

> model, MAX_THINKING_TOKENS, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE の3設定を調整し、品質を維持しながらコストを大幅削減する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

デフォルト設定（opus + 31,999思考トークン + 95%自動圧縮）は高コスト。80%のタスクはsonnetで十分であり、思考トークンとコンテキスト圧縮タイミングを最適化すればコストと品質を両立できる

## いつ使うのか

Claude Code利用料金が予算を圧迫している、または長時間セッションでコンテキスト圧縮が頻発する場合

## やり方

1. ~/.claude/settings.json に以下を追加: {"model": "sonnet", "env": {"MAX_THINKING_TOKENS": "10000", "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"}} 2. 通常タスクは /model sonnet、複雑なアーキテクチャ判断時のみ /model opus に切り替え 3. タスク区切りで /clear（無料・即座リセット）、論理的区切りで /compact（研究完了→実装前、マイルストーン完了→次タスク前）を実行 4. /cost で定期的にトークン消費を監視

### 入力

- ~/.claude/settings.json への編集権限
- タスクの複雑度判断（sonnet vs opus選択用）

### 出力

- 通常タスクで約60%コスト削減（opus→sonnet）
- 思考トークンで約70%削減（31,999→10,000）
- 長時間セッションで品質維持（50%時点で圧縮）

## 使うツール・ライブラリ

- Claude Code CLI
- settings.json編集

## コード例

```
// ~/.claude/settings.json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
}

// セッション中のコマンド
/model sonnet    # デフォルト
/model opus      # 複雑なアーキテクチャ・深い推論時のみ
/clear           # 無関係タスク間で即座リセット
/compact         # 論理的区切りで手動圧縮
/cost            # トークン消費モニタリング
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）

## 根拠

> 「model: sonnet (default opus) → ~60% cost reduction; handles 80%+ of coding tasks」

> 「CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50 (default 95) → Compacts earlier — better quality in long sessions」
