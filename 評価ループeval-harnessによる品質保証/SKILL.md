# 評価ループ（Eval Harness）による品質保証

> checkpoint評価（マイルストーン毎）とcontinuous評価（コミット毎）を組み合わせ、grader（ExactMatch/Contains/KeyExists/Schema）で自動判定

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

手動テストだけでは見逃す退行バグ・仕様違反を機械的に検出。pass@k指標で信頼性を定量化

## いつ使うのか

プロダクション品質を求めるプロジェクト、リファクタリング時の退行防止、CI/CD統合

## やり方

1. skills/eval-harness/ または skills/verification-loop/ のSKILL.mdを読み込み
2. /checkpoint コマンドで現在の検証状態（テスト結果・ビルドログ・型チェック結果）を保存
3. /verify コマンドでbuild→test→lint→typecheck→securityの順に実行
4. graderスクリプト（ExactMatch: 完全一致、Contains: 部分一致、KeyExists: JSONキー存在、Schema: 型構造）で判定
5. pass@k（k回試行中の成功回数）で信頼性スコアを算出
6. 失敗時は /learn-eval で原因パターンを抽出し、instinctに蓄積

### 入力

- テストスイート
- ビルドスクリプト
- grader定義（JSON/YAML）

### 出力

- 検証状態スナップショット（~/.claude/checkpoints/）
- pass@kスコア
- 失敗時のinstinct（継続学習へフィードバック）

## 使うツール・ライブラリ

- pytest/jest/go test等のテストランナー
- graderスクリプト（skills/quality-harness/に同梱）

## コード例

```
# 検証状態保存
/checkpoint

# 検証ループ実行
/verify

# 失敗時のパターン抽出
/learn-eval
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）
