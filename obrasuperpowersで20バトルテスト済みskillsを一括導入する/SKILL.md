# obra/superpowersで20+バトルテスト済みSkillsを一括導入する

> Jesse Vincentによるコミュニティライブラリ obra/superpowers をマーケットプレイス経由でインストールし、TDD・デバッグ・コラボレーション等の実践的Skillsを利用する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別にSkillを探して導入するより、実績ある統合パッケージで一気に生産性を上げられる。/brainstorm, /write-plan, /execute-planコマンドも含まれる。

## いつ使うのか

Claude Code CLIで即座に実践的なSkillセットを揃えたい時、実績あるベストプラクティスを活用したい時

## やり方

1. `/plugin marketplace add obra/superpowers-marketplace` を実行 2. インストールされた20+のSkillsが自動認識される 3. 必要に応じて /brainstorm や /write-plan コマンドを使う 4. superpowers-skills（コミュニティ編集可能リポジトリ）から追加Skillsを取得可能

### 入力

- Claude Code CLI環境

### 出力

- 20+の実践的Skills（TDD, デバッグ等）
- /brainstorm, /write-plan, /execute-planコマンド

## 使うツール・ライブラリ

- obra/superpowers
- Claude Code CLI Marketplace

## コード例

```
/plugin marketplace add obra/superpowers-marketplace
```

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（SkillsはFree tierでは利用不可）
- YAML基礎知識（フロントマター記述用）
- gitとバージョン管理の基本（Skillsの配布・管理用）
- Python/JavaScriptの基礎（スクリプト含むSkill作成時）
- Claude.ai / Claude Code CLI / Claude APIのいずれかの利用経験

## 根拠

> Claude Code CLI: /plugin marketplace add anthropics/skills OR /plugin add /path/to/skill-directory

> obra/superpowers - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns. Installation: /plugin marketplace add obra/superpowers-marketplace
