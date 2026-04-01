# トークン最適化3点セット

> model=sonnet、MAX_THINKING_TOKENS=10000、CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50 の設定でトークン消費を60-70%削減しつつ品質を維持する

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

デフォルト設定（opus、31999思考トークン、95%コンパクト閾値）は高品質だがコストが高い。タスクの80%はSonnetで十分であり、思考トークン削減と早期コンパクトで長時間セッションの品質低下を防げる

## いつ使うのか

Claude Codeの月額コストが高騰している、長時間セッションで応答品質が低下している、コンテキストウィンドウが枯渇しているとき

## やり方

1. ~/.claude/settings.json に "model": "sonnet", "env": {"MAX_THINKING_TOKENS": "10000", "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"} を追加 2. 複雑なアーキテクチャ議論時のみ /model opus で切り替え 3. 無関係タスク間で /clear（無料リセット） 4. 論理的区切り（調査完了→実装開始、マイルストーン完了→次タスク）で /compact 5. /cost でトークン消費監視

### 入力

- ~/.claude/settings.json

### 出力

- トークン消費60-70%削減
- コンテキスト50%時点での自動コンパクト
- 思考トークン削減によるリクエスト単価低減

## 使うツール・ライブラリ

- Claude Code CLI

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

// 使用中のコマンド
/model opus       // 複雑なタスクのみ
/clear            // 無関係タスク間
/compact          // 論理的区切り
/cost             // コスト監視
```

## 前提知識

- Claude Code CLI v2.1.0以上のインストール
- Node.js環境（フックスクリプト実行用）
- Git（リポジトリクローン用）
- 対象言語の開発環境（TypeScript/Python/Go等）
- Claude Codeのサブスクリプション（トークン消費制限緩和のため推奨）
- AIエージェント・プロンプトエンジニアリングの基礎知識
