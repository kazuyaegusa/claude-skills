# Web UIでSkillsトグルを有効化・管理する

> Claude.ai Web インターフェースの Settings > Capabilities でSkillsを有効化し、利用可能なSkillを追加する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: ui-ux

## なぜ使うのか

Web UI利用者がGUIで簡単にSkillsを管理できる。Team/Enterprise環境では管理者が組織全体で有効化する必要がある。

## いつ使うのか

Claude.ai WebでSkillsを使い始める時、組織全体で導入する時

## やり方

1. https://claude.ai/settings/capabilities にアクセス 2. Skillsトグルを有効化 3. 利用可能なSkillを閲覧またはカスタムSkillをアップロード 4. Team/Enterprise: 管理者が組織全体で有効化してから個別ユーザーが利用

### 入力

- Claudeアカウント（Pro/Max/Team/Enterprise）
- アップロードするカスタムSkillフォルダ（任意）

### 出力

- 有効化されたSkills
- Claudeが自動認識して関連タスクで利用

## 使うツール・ライブラリ

- Claude.ai Web UI

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験
