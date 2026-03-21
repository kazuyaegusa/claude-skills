# skill-creatorテンプレートで新規スキルを標準化して作成する

> Anthropic公式のskill-creatorテンプレートを使い、SKILL.md標準に準拠した新しいスキルを作成・公開する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

独自フォーマットで作成すると、他のユーザーやツールとの互換性がなくなる。公式テンプレートを使うことで、エコシステムに貢献できる再利用可能なスキルになる

## いつ使うのか

既存スキルにない新しいワークフロー・知識を発見し、コミュニティに共有したい場合

## やり方

1. skill-creatorスキル（https://github.com/anthropics/skills/tree/main/skills/skill-creator）をダウンロード
2. テンプレートのSKILL.mdを開き、必須セクション（name, description, how, when_to_use等）を埋める
3. スキルが必要とするツール・ライブラリをtools_or_libsに記載
4. （あれば）サンプルコード、チェックリスト、トラブルシューティングを追加
5. `~/.claude/skills/your-skill-name/`に配置してローカルテスト
6. GitHubリポジトリを作成してpush
7. awesome-claude-skillsにPRを送って掲載依頼

### 入力

- 新しく作成したいスキルの内容
- skill-creatorテンプレート

### 出力

- 標準準拠のSKILL.mdファイル
- GitHubリポジトリ
- awesome-claude-skillsへのPR

## 使うツール・ライブラリ

- skill-creator
- GitHub
- Markdown

## 前提知識

- Claude Codeの基本的な使い方（スキルのロード・呼び出し方法）
- GitHubの基本操作（リポジトリのクローン、ファイル取得）
- Markdownの読み書き
- ~/.claude/skills/ディレクトリの存在と役割の理解
