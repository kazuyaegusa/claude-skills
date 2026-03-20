# セキュリティスキルを明示的に推奨

> READMEの冒頭にTipセクションを配置し、Web開発者向けにセキュリティスキル（VibeSec-Skill）の利用を強く推奨する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: ui-ux

## なぜ使うのか

LLMが生成するコードは脆弱性を含みやすい。セキュリティベストプラクティスをスキル化し、デフォルトで組み込むことで被害を防ぐ

## いつ使うのか

スキルカタログを公開する際、特にコード生成用途の場合は必須で実施

## やり方

1. README冒頭に目立つTip/Warning blockquoteを配置
2. 「Webアプリを作るならVibeSec-Skillを使え」と明示
3. 該当スキルへの直接リンクを提供

### 入力

- 推奨するセキュリティスキルのリポジトリURL

### 出力

- READMEのTipセクション

## 使うツール・ライブラリ

- Markdown blockquote記法

## コード例

```
>[!Tip]
>If you use Claude to build web applications, do yourself a favor and use [VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) to avoid getting hacked.
```

## 前提知識

- Claude Codeの基本的な使い方とスキルシステムの理解
- SKILL.mdフォーマットの概念
- GitHubの基本操作（リポジトリ閲覧、PR作成）
- Markdown記法
