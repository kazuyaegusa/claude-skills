# 継続学習によるスキル自動生成

> セッション終了時にLLMがパターンを抽出し、instinct（学習済みパターン）として保存。関連するinstinctをクラスタリングしてスキルに昇格

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

繰り返し使うパターンを毎回ゼロから指示する非効率を排除。チーム内でベストプラクティスを自動蓄積・共有できる

## いつ使うのか

新しいフレームワーク・ライブラリを学習中、またはチーム固有のパターンを標準化したい時

## やり方

1. /learn-eval コマンドでセッション内容を分析し、再利用可能なパターンを抽出
2. scripts/hooks/evaluate-session.js が実行され、instinctファイル（YAML frontmatter付きMarkdown）を ~/.claude/instincts/ に保存
3. 各instinctにconfidenceスコア（0.0-1.0）とtrigger条件を付与
4. /evolve コマンドで類似instinctをクラスタリングし、SKILL.md として ~/.claude/skills/ に昇格
5. 30日間使われなかったpending instinctは /prune で自動削除

### 入力

- セッション履歴
- LLMアクセス（claude -p）

### 出力

- ~/.claude/instincts/*.md（個別パターン）
- ~/.claude/skills/*.md（昇格後のスキル）

## 使うツール・ライブラリ

- claude -p（サブスクリプション認証優先）
- scripts/hooks/evaluate-session.js

## コード例

```
# セッション終了時にパターン抽出
/learn-eval

# instinctをスキルに昇格
/evolve

# 期限切れinstinct削除
/prune
```

## 前提知識

- Claude Code CLI v2.1.0以降、またはCursor/OpenCode/Codexのいずれか
- npm/pnpm/yarn/bunのいずれかのパッケージマネージャー
- Gitの基本操作（クローン、コミット）
- JSON/YAML形式の理解
- 対象言語のテストフレームワーク（pytest/jest/go test等）の基礎知識
- （オプション）claude -p サブスクリプション認証（継続学習に必要）
