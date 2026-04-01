# TDDを強制してテストなしコードを拒否する

> Red（失敗テスト作成）→Green（テスト通過）→Refactor のサイクルをエージェントに強制し、テストを書かずに実装コードを書いたら削除して最初からやり直させる

- 出典: https://x.com/btcqzy1/status/2033116943712993717
- 投稿者: 爱丽丝呀！
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントはテストを省略して実装コードを先に書く傾向がある。TDDを強制することで仕様の抜け漏れを早期検出し、実装品質を担保する

## いつ使うのか

各タスクの実装フェーズ。特にロジックが複雑で副作用が多い処理を実装するとき

### 具体的な適用場面

- 長期間・複数ファイルにわたる機能追加をAIエージェントに任せるとき
- AIが書いたコードがすぐにスパゲッティ化するプロジェクトで品質を安定させたいとき
- Claude Code / Cursor / Codex / Gemini CLI を使っているチームがテスト文化を強制したいとき

## やり方

1. SuperPowersのTDDスキルがタスク開始時に自動起動
2. エージェントはまず失敗するテストのみを書く（実装コードは書かない）
3. テストを実行してRedを確認する
4. テストが通る最小限の実装コードを書く
5. テストを実行してGreenを確認する
6. リファクタリングを行い、再度Greenを確認する
7. テストなしで実装コードが書かれた場合、SuperPowersスキルが検出して削除・やり直しを指示する

### 入力

- タスク仕様（ファイルパス・コードスニペット単位まで明確化済み）

### 出力

- テストが先に存在する状態で書かれた実装コード
- 全テストがGreenの状態

## 使うツール・ライブラリ

- SuperPowers TDDスキル
- 各言語のテストフレームワーク（Jest / pytest / RSpec 等）

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
