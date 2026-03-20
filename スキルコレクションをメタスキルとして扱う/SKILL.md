# スキルコレクションをメタスキルとして扱う

> 個別スキルだけでなく、複数スキルをバンドルした「コレクション」（例: OpenPaw、claude-starter）も1エントリとして掲載する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

特定ユースケース（個人アシスタント、科学計算、プロダクトマネジメント等）には複数スキルの組み合わせが必要。コレクションを提供することで、ユーザーは初期設定の手間を削減できる

## いつ使うのか

5つ以上のスキルを含むバンドルが登場した時点で専用セクションを作成

## やり方

1. 複数スキルをパッケージしたリポジトリを「Collections」セクションに分類
2. 含まれるスキル数と対象ドメインを説明に明記
3. インストール方法（npxコマンド等）があれば併記

### 入力

- スキルコレクションのリポジトリ
- 含まれるスキルリストと説明

### 出力

- Collectionsセクション
- 各コレクションの説明とインストール手順

## コード例

```
- [OpenPaw](https://github.com/daxaur/openpaw) - 38-skill bundle that turns Claude Code into a personal assistant. Includes git, Telegram, Discord, Obsidian, daily briefing, and more. Run via `npx pawmode`.
```

## 前提知識

- Claude Codeの基本的な使い方とスキルシステムの理解
- SKILL.mdフォーマットの概念
- GitHubの基本操作（リポジトリ閲覧、PR作成）
- Markdown記法
