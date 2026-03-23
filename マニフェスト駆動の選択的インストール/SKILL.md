# マニフェスト駆動の選択的インストール

> ユーザーが必要なコンポーネント（agents/commands/skills/rules）だけをインタラクティブに選択してインストール

- 出典: https://github.com/affaan-m/everything-claude-code
- 投稿者: affaan-m
- カテゴリ: agent-orchestration

## なぜ使うのか

全部入りインストールはコンテキストを圧迫し、無関係なスキルがノイズになる。必要なものだけ入れれば、トークン効率が上がる

## いつ使うのか

初回セットアップ、プロジェクト切り替え、不要なスキルを削除したい

## やり方

1. scripts/install-plan.js がインストール済み状態を SQLite で管理
2. scripts/install-apply.js が差分を計算し、増分更新を実行
3. /configure-ecc コマンドで対話的に選択（言語・フレームワーク・ツール）
4. 選択に応じて agents/commands/skills/rules を ~/.claude/ にコピー
5. 状態ストアで追跡し、次回は差分のみ更新

### 入力

- /configure-ecc コマンド
- ユーザーの選択（言語・フレームワーク）

### 出力

- 選択されたコンポーネントのみがインストールされた ~/.claude/
- .claude/state-store.db（インストール履歴）

## 使うツール・ライブラリ

- Node.js (scripts/install-plan.js, scripts/install-apply.js)
- SQLite (state store)

## コード例

```
# /configure-ecc コマンドで対話的にインストール
? Which languages do you use? (typescript, python, golang, swift, php)
? Which frameworks? (react, nextjs, django, laravel, springboot)
? Install security tools? (yes/no)
```

## 前提知識

- Claude Code CLI v2.1.0 以降のインストール
- Node.js 18 以降（hooks/scripts の実行に必要）
- Git の基本操作（clone, commit, PR）
- npm/pnpm/yarn/bun のいずれか
- JSON/YAML/TOML の基本文法
- 使用する言語のツールチェーン（TypeScript なら tsc, Python なら pytest など）
