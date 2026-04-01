# サブカテゴリー分割による詳細ナビゲーション

> 大きなカテゴリー（例：Slash-Commands）をサブカテゴリー（Version Control & Git、Code Analysis & Testing等）に分割する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

リソース数が多い場合、サブカテゴリーがないと目的のリソースを見つけにくい。機能別に整理することで、特定のニーズに対応するリソースを素早く発見できる

## いつ使うのか

1つのカテゴリーに10個以上のリソースがあり、さらに細分化できる場合

## やり方

1. カテゴリー内のリソースを機能や用途で分類
2. 適切なサブカテゴリー名を付ける（明確で具体的な名前）
3. 各サブカテゴリーを### で表記
4. 目次にサブカテゴリーも含める

### 入力

- リソースの機能・用途情報
- 適切な分類軸

### 出力

- サブカテゴリー構造（###）
- 更新された目次

## 使うツール・ライブラリ

- Markdown

## コード例

```
## Slash-Commands 🔪

> "Slash Commands are customized..."

### General
...

### Version Control & Git
...

### Code Analysis & Testing
...
```

## 前提知識

- Claude Codeの基本的な使い方（CLI、設定ファイル、コマンド実行）
- GitHubの基本操作（リポジトリのクローン、READMEの閲覧）
- Markdownの読解
- AI開発ツールの一般的な概念（エージェント、フック、プロンプト等）

## 根拠

> "Agent Skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks" - カテゴリー定義の例

> Slash-Commandsカテゴリーは7つのサブカテゴリーに分割（General, Version Control & Git, Code Analysis & Testing, Context Loading & Priming, Documentation & Changelogs, CI / Deployment, Project & Task Management, Miscellaneous）
