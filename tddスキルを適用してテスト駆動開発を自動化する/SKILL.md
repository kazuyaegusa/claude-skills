# TDDスキルを適用してテスト駆動開発を自動化する

> test-driven-development スキルをClaude Codeに導入し、機能実装前に必ずテストを書かせるワークフローを強制する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはデフォルトでは実装コードを先に書く傾向があるが、TDDスキルを有効化すると「テスト→実装→リファクタ」の順序が自動的に守られ、バグの早期発見と設計品質の向上が実現する

## いつ使うのか

新機能追加やバグ修正など、すべての実装タスクの開始時（スキル説明文: 'Use when implementing any feature or bugfix, before writing implementation code'）

## やり方

1. https://github.com/obra/superpowers/tree/main/skills/test-driven-development からSKILL.mdを取得
2. `~/.claude/skills/test-driven-development/` に配置
3. Claude Codeに「機能Xを実装して」と依頼すると、スキルが発動し「まずテストを書きます」と返答
4. テストが失敗することを確認してから実装コードを書く
5. テストがパスすることを確認してリファクタリング

### 入力

- 実装する機能の仕様
- 既存のテストフレームワーク（Jest, pytest等）

### 出力

- 機能仕様を満たすテストコード
- テストをパスする実装コード
- リファクタリング後のクリーンなコード

## 使うツール・ライブラリ

- test-driven-development skill
- テストフレームワーク（Jest, pytest, JUnit等）

## 前提知識

- Claude Codeの基本的な使い方（スキルの配置場所 ~/.claude/skills/ の理解）
- GitHubリポジトリのクローン方法
- npm/npx の基本操作（一部スキルのインストールに必要）
- MCP（Model Context Protocol）の概念（外部ツール連携スキルを使う場合）

## 根拠

> 投稿タイトル: 'BehiSecc/awesome-claude-skills - A curated list of Claude Skills.'

> 収録スキル例: 'docx - Create, edit, analyze Word docs with tracked changes', 'test-driven-development - Use when implementing any feature or bugfix', 'VibeSec-Skill - VibeSec helps Claude write secure code and prevent common vulnerabilities', 'pm-skills - 24 product management skills across the Triple Diamond lifecycle'

> コレクション例: 'OpenPaw - 38-skill bundle that turns Claude Code into a personal assistant. Run via npx pawmode', 'agentskill.sh - Browse and install 69,000+ AI agent skills'

> Tip: 'If you use Claude to build web applications, do yourself a favor and use VibeSec-Skill to avoid getting hacked.'

> GitHub URL: https://github.com/BehiSecc/awesome-claude-skills
