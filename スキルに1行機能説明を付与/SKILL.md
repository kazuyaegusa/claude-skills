# スキルに1行機能説明を付与

> 各スキルのリンクの後に、そのスキルが何をするのかを簡潔に記述する（例: "Create, edit, analyze Word docs with tracked changes, comments, formatting."）

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

リンク先を開かずに機能を理解でき、ユーザーの認知負荷を削減する。リスト全体をスキャンして目的のスキルを素早く発見できる

## いつ使うのか

スキルカタログを作成・更新する際、全てのエントリに対して実施

## やり方

1. スキルのREADME.mdまたはSKILL.mdから機能概要を抽出
2. 動詞で始まる簡潔な説明文（10-20語）にまとめる
3. 複数機能がある場合はコロン区切りで列挙
4. awesome-listの各エントリに統一フォーマットで付記

### 入力

- スキルのドキュメント（README.md、SKILL.md）
- スキルのコード内容

### 出力

- 各スキルの1行機能説明

## 前提知識

- Claude Codeの基本的な使い方とスキルシステムの理解
- SKILL.mdフォーマットの概念
- GitHubの基本操作（リポジトリ閲覧、PR作成）
- Markdown記法
