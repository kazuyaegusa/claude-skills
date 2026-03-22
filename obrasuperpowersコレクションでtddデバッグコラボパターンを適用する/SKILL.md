# obra/superpowersコレクションでTDD/デバッグ/コラボパターンを適用する

> obra氏のsuperpowersライブラリ（20+の実戦検証済みSkill）を導入し、`/brainstorm`、`/write-plan`、`/execute-plan`コマンドでタスク分解・計画・実行を体系化する。

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

公式Skillは汎用的だが、開発現場の反復パターン（TDD、デバッグ、計画立案）は別途整備が必要。superpowersはこれらを統合し、コミュニティ編集可能なリポジトリで継続改善される。

## いつ使うのか

複雑な開発タスクをTDD・計画駆動で進めたい時、チーム全体で統一したデバッグ手順を適用したい時。

## やり方

1. `/plugin marketplace add obra/superpowers-marketplace`でインストール
2. タスク受領時に`/brainstorm`で要件・制約・成功条件を明確化
3. `/write-plan`で実装計画を段階的に作成
4. `/execute-plan`でTODOリストベースで実行・テスト
5. デバッグ時は専用Skillが自動発動（仮説検証サイクル）
6. 必要に応じてsuperpowers-skills（コミュニティ版）から追加Skillを取得

### 入力

- 開発タスク要件
- obra/superpowers-marketplace plugin

### 出力

- 構造化された計画（/write-plan）
- TODOリストベースの実行ログ（/execute-plan）
- TDD/デバッグパターンの自動適用

## 使うツール・ライブラリ

- obra/superpowers
- obra/superpowers-skills
- Claude Code CLI

## コード例

```
/plugin marketplace add obra/superpowers-marketplace
```

## 前提知識

- Claude Pro/Max/Team/Enterprise契約（Free tierではSkills利用不可）
- YAML frontmatter、Markdownの基本文法
- gitによるバージョン管理の知識（Skill配布・更新管理に必要）
- Claude.ai/Code/APIのいずれかの使用経験
- （開発系Skillの場合）対象フレームワーク・ライブラリの基礎知識
