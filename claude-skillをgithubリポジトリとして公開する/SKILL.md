# Claude SkillをGitHubリポジトリとして公開する

> SKILL.mdファイルを含むGitHubリポジトリを作成し、特定のタスク（例: PDFからテキスト抽出、テスト駆動開発、セキュリティレビュー）を自動化するための手順・ツール呼び出し方法を記述する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code等のAI agentは、SKILL.mdファイルを読み込むことで、そのタスクに特化した振る舞い（ツールの使い方、手順、制約）を学習できる。これにより、ユーザーは同じ指示を毎回繰り返す必要がなくなり、再利用性が高まる

## いつ使うのか

Claude Codeで繰り返し実行するタスク（例: PRレビュー、テスト実行、ドキュメント生成）があり、それをチーム内または公開で共有したい時

## やり方

1. GitHubで新しいリポジトリを作成（例: `your-repo/awesome-claude-skills`）
2. スキルごとにディレクトリを作成し、各ディレクトリ内にSKILL.mdを配置
3. SKILL.mdには以下を記述: スキル名、説明、使用タイミング、必要なツール、手順（チェックリスト形式）、制約事項
4. README.mdでスキルの一覧と使い方を説明
5. リポジトリをpublicに設定し、コミュニティに公開

### 入力

- タスクの定義（何をするか）
- 必要なツール・ライブラリ
- 手順・制約事項

### 出力

- SKILL.mdファイル
- GitHubリポジトリ（public/private）
- README.md（使用方法説明）

## 使うツール・ライブラリ

- GitHub
- Markdown
- Claude Code（スキル読み込み）

## コード例

```
---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development

1. Read existing test suite structure
2. Write failing test for new feature
3. Run test to confirm it fails
4. Write minimal code to make test pass
5. Refactor while keeping tests green
```

## 前提知識

- Claude Code（またはClaude Skills対応のAI agent）の基本的な使い方
- GitHubの基本操作（リポジトリ作成、Fork、Pull Request）
- Markdown記法の理解
- SKILL.mdファイルの構造（name, description等）に関する知識

## 根拠

> >[!Tip] If you use Claude to build web applications, do yourself a favor and use [VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) to avoid getting hacked.

> リポジトリURL: https://github.com/BehiSecc/awesome-claude-skills
