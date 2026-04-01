# 設計仕様+コード品質の二重レビューを実施する

> 各タスク完了後に「設計仕様との適合確認」と「コード品質チェック」の両方を自動実行し、どちらか一方でも不合格なら差し戻す

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: other

## なぜ使うのか

「動くが汚い」コードの蓄積がプロジェクト崩壊の原因。設計仕様適合だけでなくコード品質（YAGNI・DRY等の原則適用）も自動ゲートとして設けることで、長期的な保守性を担保する

## いつ使うのか

各サブエージェントがタスクを完了したと報告したとき

### 具体的な適用場面

- プロジェクトが大きくなるにつれてAI生成コードの整合性が崩れてきた場合
- Claude CodeやCursorでエージェントに長時間タスクを委任したいが、途中で脱線するのを防ぎたい場合
- チームでAIコーディングを使うが、各自が独自プロセスで動いていて品質がばらつく場合

## やり方

1. サブエージェントがタスク完了を報告すると、`requesting-code-review`スキルが自動発火
2. レビュアーエージェントが設計仕様文書と実装を照合（要件の充足確認）
3. 次に`verification-before-completion`スキルでコード品質を確認（YAGNI・DRY・テストカバレッジ）
4. 両方パスした場合のみ次のタスクへ進む
5. 不合格の場合は`receiving-code-review`スキルでフィードバックを受けて修正

### 入力

- 承認済み設計仕様文書
- サブエージェントが実装したコード
- テスト結果

### 出力

- 設計仕様適合確認レポート
- コード品質スコア
- 差し戻しフィードバックまたは承認

## 使うツール・ライブラリ

- superpowers requesting-code-review skill
- superpowers verification-before-completion skill
- superpowers receiving-code-review skill

## 前提知識

- Claude CodeまたはCursorのインストール
- gitの基本操作（branch・worktree）の理解
- TDD（テスト駆動開発）の基本概念

## 根拠

> SuperPowers is a complete software development workflow for your coding agents, built on top of a set of composable 'skills'

> it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do

> It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY

> it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work

> It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan
