# 双段階コードレビューで品質ゲートを設ける

> タスク完了後に「仕様適合チェック（設計文書との差異確認）」と「コード品質チェック（可読性・DRY・YAGNI違反）」の2段階レビューをエージェントに自動実行させる

- 出典: https://x.com/btcqzy1/status/2033116943712993717
- 投稿者: 爱丽丝呀！
- カテゴリ: agent-orchestration

## なぜ使うのか

1段階のレビューでは仕様通りかどうかとコード品質のどちらかが漏れやすい。段階を分けることでCritical問題の見落としを防ぎ、次タスクへの汚染を防止する

## いつ使うのか

各タスクの実装・TDDサイクル完了後。次のタスクへ進む前のゲートとして

### 具体的な適用場面

- 長期間・複数ファイルにわたる機能追加をAIエージェントに任せるとき
- AIが書いたコードがすぐにスパゲッティ化するプロジェクトで品質を安定させたいとき
- Claude Code / Cursor / Codex / Gemini CLI を使っているチームがテスト文化を強制したいとき

## やり方

1. 各タスクの実装完了後、SuperPowersが自動的に第1フェーズレビューを起動
2. 第1フェーズ: 設計文書と実装の差異をチェック（仕様適合度）。Criticalな乖離があれば実装へ差し戻し
3. 第1フェーズ通過後、第2フェーズへ自動移行
4. 第2フェーズ: コード品質チェック（DRY違反・YAGNI違反・命名・複雑度等）
5. Criticalな問題が残っている場合は次タスクへの進行をブロックする
6. 両フェーズ通過後のみ次タスクまたはPR作成へ進む

### 入力

- 実装コード
- 元の設計文書・タスク仕様

### 出力

- レビュー結果レポート
- Criticalなし確認済みのコード

## 使うツール・ライブラリ

- SuperPowers レビュースキル

## 前提知識

- Claude Code・Cursor・Codex・Gemini CLI のいずれかのインストールと基本操作の習得
- git の基本操作（ブランチ・PR・worktree）
- TDD（テスト駆動開発）の概念理解

## 根拠

> 「7阶段强制流水线，缺一不可。脑暴+设计验证 → git worktree → 计划拆分 → 子Agent执行+TDD → 审查 → 完成分支/PR」

> 「先写测试、看它失败、再写代码、看它通过——跳过测试的代码直接删掉重来」

> 「每个任务完成后触发双阶段代码审查，先查规格符合度，再查代码质量，Critical 问题不解决不许前进」

> GitHub README: 「it launches a subagent-driven-development process, having agents work through each engineering task, inspecting and reviewing their work」

> GitHub README: 「It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY」
