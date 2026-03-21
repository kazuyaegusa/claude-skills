# TDDスキルで実装前にテストを自動生成する

> test-driven-developmentスキルを使い、機能実装の前に必ずテストケースを先に書くワークフローを強制する

- 出典: https://github.com/BehiSecc/awesome-claude-skills
- 投稿者: BehiSecc
- カテゴリ: claude-code-workflow

## なぜ使うのか

TDDはバグを早期発見し、リファクタリングを安全にする。スキルとして組み込むことで、Claude Codeが常にテストファーストで実装するようになる

## いつ使うのか

新機能追加、バグ修正、リファクタリング等、コード変更を伴うすべてのタスクで使用すべき

## やり方

1. test-driven-developmentスキル（https://github.com/obra/superpowers/tree/main/skills/test-driven-development）を導入
2. 新機能・バグ修正をClaude Codeに依頼
3. スキルが自動起動し、実装コード生成前にテストケース生成を要求
4. テストが失敗することを確認（Red）
5. 最小限の実装でテストをパス（Green）
6. リファクタリング（Refactor）
7. すべてのステップをTodoWriteで追跡

### 入力

- 実装する機能の仕様
- test-driven-developmentスキル

### 出力

- テストコード（先行生成）
- テストをパスする実装コード
- リファクタリング済みコード

## 使うツール・ライブラリ

- test-driven-developmentスキル
- pytest, jest等のテストフレームワーク
- TodoWrite

## 前提知識

- Claude Codeの基本的な使い方（スキルのロード・呼び出し方法）
- GitHubの基本操作（リポジトリのクローン、ファイル取得）
- Markdownの読み書き
- ~/.claude/skills/ディレクトリの存在と役割の理解
