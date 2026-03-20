# obra/superpowersで20+の実践スキルライブラリを一括導入する

> obra/superpowersコミュニティスキルパックをインストールし、TDD/デバッグ/コラボレーションパターン等20以上のスキルを利用可能にする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別にスキルを探して導入するより、実戦検証済みのスキルセットを一括で得られるため

## いつ使うのか

Claude Codeで本格的な開発ワークフローを構築したい時

## やり方

1. `/plugin marketplace add obra/superpowers-marketplace` でインストール
2. /brainstorm, /write-plan, /execute-planコマンドとskills-searchツールが利用可能になる
3. 必要に応じてobra/superpowers-labで実験的スキルも導入可能

### 入力

- Claude Code環境

### 出力

- 20+のスキル（TDD, debugging, collaboration等）
- brainstorm/write-plan/execute-planコマンド

## 使うツール・ライブラリ

- obra/superpowers
- obra/superpowers-marketplace
- Claude Code CLI

## コード例

```
/plugin marketplace add obra/superpowers-marketplace
```

## 前提知識

- Claude.ai Pro/Max/Team/Enterpriseアカウント（Freeユーザーはスキル利用不可）
- YAML frontmatter、Markdownの基本知識
- （API利用の場合）Anthropic APIキーとAPI仕様の理解
- （Claude Code利用の場合）Claude Code CLIのインストール
