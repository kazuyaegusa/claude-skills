# 継続学習v2（インスティンクトベース）

> セッション中に抽出したパターンを「インスティンクト」として保存し、信頼度スコアで昇格・クラスタリング・スキル化を行う自己改善ループ

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

過去のセッションで学んだベストプラクティスを手動で再入力するのは非効率。自動抽出・評価・昇格により、チーム全体で知見を再利用できる

## いつ使うのか

繰り返し同じパターンを説明している、チームメンバー間でベストプラクティスを共有したい、git履歴からドメイン知識を自動抽出したい場合

## やり方

1. /learn-eval コマンドでセッションからパターンを抽出・評価・保存 2. /instinct-status で学習済みインスティンクトと信頼度を確認 3. /instinct-import <file> で他メンバーのインスティンクトをインポート 4. /evolve で関連インスティンクトをクラスタリングし、SKILL.md として昇格 5. 昇格したスキルは ~/.claude/skills/ に保存され、全プロジェクトで再利用可能に

### 入力

- セッション履歴（.claude/session-context.md等）
- git commit履歴（/skill-create使用時）
- 他メンバーのインスティンクトファイル（インポート時）

### 出力

- ~/.claude/instincts/*.json（インスティンクトストア）
- ~/.claude/skills/<skill-name>/SKILL.md（昇格後）
- 信頼度スコア・使用回数・最終更新日

## 使うツール・ライブラリ

- /learn-eval, /instinct-status, /instinct-import, /instinct-export, /evolve コマンド
- skills/continuous-learning-v2/

## コード例

```
# セッション中にパターン抽出・評価・保存
/learn-eval

# 学習済みインスティンクト確認
/instinct-status

# 他メンバーからインポート
/instinct-import team-patterns.json

# 関連インスティンクトをスキル化
/evolve

# git履歴から自動抽出
/skill-create --instincts
```

## 前提知識

- Claude Code CLI v2.1.0以上の基本操作知識
- 使用する言語スタック（TypeScript/Python/Go等）の基礎知識
- git、npm/pnpm/yarn/bunの基本操作
- JSON/YAML/TOML形式の理解
- CI/CDパイプラインの基礎（AgentShield統合時）
- セキュリティベストプラクティスの基本（OWASP Top 10等）
