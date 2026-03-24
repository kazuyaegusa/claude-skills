# ContributionガイドとContactセクションでコミュニティ参加を促進する

> README末尾にContributionガイドとContactセクションを設け、ユーザーがスキルを追加・修正したり、問題を報告したりできる仕組みを提供する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: other

## なぜ使うのか

Awesome Listの価値は、コミュニティの参加によって維持・拡大される。Contributionガイドを明示することで、ユーザーは「どうやって貢献すればいいか」を理解でき、参加のハードルが下がる

## いつ使うのか

Awesome List等のキュレーションリポジトリを公開し、コミュニティからの貢献を受け入れたい時

## やり方

1. README末尾に## Contributionセクションを作成
2. 貢献方法を3ステップで説明: 1) Fork this repo, 2) Make your changes, 3) Submit a Pull Request
3. Issueでの報告も受け付ける旨を明記
4. ## Contactセクションで、リポジトリ管理者への連絡方法（X/Twitter、メール等）を記載

### 入力

- 貢献プロセス（Fork→変更→PR）
- 連絡先（X/Twitter、メール等）

### 出力

- README.md内のContributionセクション
- README.md内のContactセクション

## 使うツール・ライブラリ

- GitHub（Fork、Pull Request機能）

## コード例

```
## 🤝 Contribution

If you have suggestions, improvements, or new resources to add:

1. Fork this repo
2. Make your changes
3. Submit a Pull Request

You can also open an **Issue** 🐛 if you spot something that needs fixing.

## 📬 Contact

If you want to contact me, you can reach me on [X](https://x.com/Behi_Sec).
```

## 前提知識

- Claude Code（またはClaude Skills対応のAI agent）の基本的な使い方
- GitHubの基本操作（リポジトリ作成、Fork、Pull Request）
- Markdown記法の理解
- SKILL.mdファイルの構造（name, description等）に関する知識

## 根拠

> >[!Tip] If you use Claude to build web applications, do yourself a favor and use [VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) to avoid getting hacked.

> ## 📄 Document Skills - [docx](https://github.com/anthropics/skills/tree/main/skills/docx) - Create, edit, analyze Word docs with tracked changes, comments, formatting.

> ## 🤝 Contribution - If you have suggestions, improvements, or new resources to add: 1. Fork this repo 2. Make your changes 3. Submit a Pull Request
