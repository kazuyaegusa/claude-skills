# PRベースでコミュニティ貢献を受け付ける

> Contribution セクションを設け、Fork→変更→PR の標準的なGitHubワークフローを明示してコミュニティからの追加を促す

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

メンテナーだけでは全スキルを把握しきれないため、コミュニティの知見を集約する仕組みが必要。PRベースにすることでレビュー・品質管理が可能になる

## いつ使うのか

リストが公開され、外部からの追加依頼が来るようになった時

## やり方

1. README末尾に ## 🤝 Contribution セクションを追加
2. Fork→変更→PR の3ステップを明記
3. Issue報告も受け付ける旨を記載
4. PRテンプレートで必須情報（リポジトリURL、説明、カテゴリ）を定義する

### 入力

- 新規スキルのリポジトリURL
- 説明文
- カテゴリ

### 出力

- 更新されたREADME.md
- PRマージ履歴

## 使うツール・ライブラリ

- GitHub PR
- GitHub Issues

## コード例

```
## 🤝 Contribution

If you have suggestions, improvements, or new resources to add:

1. Fork this repo
2. Make your changes
3. Submit a Pull Request
```

## 前提知識

- Claude Code / Claude Skills の基本概念
- GitHubの基本操作（Fork, PR）
- Markdownの記法

## 根拠

> 🤝 Contribution - Fork this repo, Make your changes, Submit a Pull Request
