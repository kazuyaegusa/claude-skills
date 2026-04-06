# awesome-* 形式によるコミュニティキュレーション

> GitHub の awesome-* リスト形式（awesome-python, awesome-go など）を Claude Skills に適用し、PR ベースでコミュニティがスキルを追加・更新できる仕組みを構築

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

単一の管理者では全スキルを追跡できないため、コミュニティ全体で知識を集約し、品質を相互レビューする必要がある

## いつ使うのか

スキルエコシステムが成長期に入り、新規スキルが頻繁に追加される時、または品質のばらつきが問題になった時

## やり方

1. awesome-claude-skills リポジトリを作成
2. README.md に Contribution ガイドを明記（Fork → 変更 → PR の流れ）
3. 各スキルエントリは [名前](URL) - 説明 の形式で統一
4. PR で新規スキル追加や説明改善を受け付け
5. メンテナーがレビュー・マージ

### 入力

- コミュニティからの PR（新規スキル、説明改善）
- スキルリポジトリの品質基準

### 出力

- 継続的に更新される awesome リスト
- コミュニティによる品質レビュー

## 使うツール・ライブラリ

- GitHub
- Pull Request ワークフロー

## コード例

```
## 🤝 Contribution

If you have suggestions, improvements, or new resources to add:

1. Fork this repo
2. Make your changes
3. Submit a Pull Request
```

## 前提知識

- Claude Code の基本的な使い方（スキルのインストール方法）
- GitHub リポジトリの構造と README.md の役割
- Markdown 記法
- awesome-* リストの概念（例: awesome-python, awesome-go）

## 根拠

> ## 🤝 Contribution - Fork → 変更 → PR の標準的なコントリビューションフローを明記

> [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs - 1行説明の実例
