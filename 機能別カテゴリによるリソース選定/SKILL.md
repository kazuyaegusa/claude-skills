# 機能別カテゴリによるリソース選定

> 70以上のClaude Code拡張リソースを8カテゴリ（Agent Skills/Workflows/Tooling/Status Lines/Hooks/Slash-Commands/CLAUDE.md/Alternative Clients）に分類し、目的に応じて選択可能にする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeの拡張は多様だが、無計画に導入すると競合・重複・複雑化を招く。カテゴリ別に整理することで、「何が足りないか」「どれを組み合わせるべきか」を判断できる

## いつ使うのか

Claude Code導入初期、または既存環境の改善時。特に「何が必要か分からない」状態で全体像を把握したい場合

## やり方

1. 自プロジェクトの課題を特定（例：テスト規律が弱い、コスト可視化が必要、セッション継続性が低い）
2. 該当カテゴリを参照（例：TDD→Hooks「TDD Guard」、コスト→Usage Monitors「ccflare」、継続性→Tooling「Claude Session Restore」）
3. 各リソースの説明文から技術スタック・依存関係を確認
4. 競合しない組み合わせを選定（例：Hooks複数は可、Orchestrator複数は競合リスク）
5. 小規模導入→評価→本格展開の順で進める

### 入力

- プロジェクトの開発要件（言語・フレームワーク・チーム規模・品質基準）
- 現在のClaude Code利用状況（素のCLIのみ、一部拡張済み等）
- 解決したい課題（テスト規律・コスト管理・セキュリティ・マルチエージェント等）

### 出力

- 目的別の拡張リソース候補リスト
- 導入優先順位付け
- 競合リスク・依存関係の把握

## 使うツール・ライブラリ

- awesome-claude-code repository
- GitHub（各リソースの詳細確認用）

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ファイル操作承認等）
- gitの基礎知識（branch, commit, PR等）
- 開発ワークフローの基礎（TDD, CI/CD, コードレビュー等の概念）
- JSON/Markdown形式の読み書き（Hooks設定、CLAUDE.md記述に必要）
