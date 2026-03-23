# 継続学習 v2（Instinct ベース）

> セッションから自動的にパターンを抽出し、信頼度スコア付きで蓄積。関連するパターンをクラスタリングして再利用可能なスキルに昇華

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: claude-code-workflow

## なぜ使うのか

毎回同じことを教え直すのは非効率。成功パターンを自動記憶し、次回から自動適用すれば、品質と速度が向上

## いつ使うのか

同じタイプのタスクを繰り返す、チーム知識を蓄積したい、プロジェクト固有のベストプラクティスを定着させたい

## やり方

1. /learn-eval コマンドでセッション終了時にパターンを抽出・評価
2. .claude/instincts/ に YAML 形式で保存（name, description, action, evidence, confidence）
3. /instinct-status で学習済みパターンを確認
4. /evolve で関連パターンをクラスタリングし、skills/ に SKILL.md として生成
5. 次回セッションで自動適用

### 入力

- セッション履歴
- /learn-eval, /instinct-status, /evolve コマンド

### 出力

- .claude/instincts/*.yaml（パターン定義）
- skills/*.md（再利用可能なスキル）
- 次回セッションでの自動適用

## 使うツール・ライブラリ

- Claude Code continuous-learning-v2 skill
- YAML parser

## コード例

```
# .claude/instincts/use-immutable-updates.yaml
name: use-immutable-updates
description: Always use spread operators for state updates
action: Replace mutating array/object updates with spread syntax
evidence: ["PR #123", "session 2025-03-15"]
confidence: 0.85
```

## 前提知識

- Claude Code CLI v2.1.0 以降のインストール
- Node.js 18 以降（hooks/scripts の実行に必要）
- Git の基本操作（clone, commit, PR）
- npm/pnpm/yarn/bun のいずれか
- JSON/YAML/TOML の基本文法
- 使用する言語のツールチェーン（TypeScript なら tsc, Python なら pytest など）
