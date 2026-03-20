# スキルをドメイン別に階層化

> スキルを「Document Skills」「Development & Code Tools」「Data & Analysis」「Security & Web Testing」など、利用ドメインで大分類する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

ユーザーは「何をしたいか」からスキルを探す。技術スタックやファイル形式ではなく、タスク領域で分類することで直感的な発見を可能にする

## いつ使うのか

スキル数が20を超えた時点でカテゴリ化を開始。50以上になったらサブカテゴリも検討

## やり方

1. スキルの主要用途を分析
2. 10-15程度の大カテゴリを定義（Document、Development、Data、Scientific、Writing、Learning、Media、Health、Collaboration、Security、Utility等）
3. 各スキルを最も適合するカテゴリに配置
4. Table of Contentsで全カテゴリへのアンカーリンクを提供

### 入力

- 各スキルの機能説明
- 想定利用シーン

### 出力

- ドメイン別セクション構成
- Table of Contents

## 使うツール・ライブラリ

- Markdown見出しとアンカーリンク

## コード例

```
## 📄 Document Skills
- [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.
```

## 前提知識

- Claude Codeの基本的な使い方とスキルシステムの理解
- SKILL.mdフォーマットの概念
- GitHubの基本操作（リポジトリ閲覧、PR作成）
- Markdown記法

## 根拠

> 「📄 Document Skills」「🛠 Development & Code Tools」等の12カテゴリ分類

> 「If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked」- セキュリティスキルの明示的推奨

> 「OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant」- スキルコレクションの事例
