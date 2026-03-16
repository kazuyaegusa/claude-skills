# SuperPowersスキルをエージェントにインストールする

> Claude Code / Cursor / Codex / Gemini CLI に SuperPowers のスキルセットをインストールし、7段階パイプラインを自動有効化する

- 出典: https://x.com/btcqzy1/status/2033116943712993717
- 投稿者: 爱丽丝呀！
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルが自動トリガーするため、開発者が毎回プロンプトを書かなくてもエージェントがSE工程を守るようになる

## いつ使うのか

Claude Code・Cursor・Codex・Gemini CLI でコーディングタスクを開始するとき。特に数時間以上かかる機能実装をエージェントに委任するとき

### 具体的な適用場面

- 長期間・複数ファイルにわたる機能追加をAIエージェントに任せるとき
- AIが書いたコードがすぐにスパゲッティ化するプロジェクトで品質を安定させたいとき
- Claude Code / Cursor / Codex / Gemini CLI を使っているチームがテスト文化を強制したいとき

## やり方

1. Claude Code の場合: 公式プラグインマーケットプレイス（claude.com/plugins/superpowers）からインストール、またはコマンド `claude install obra/superpowers` を実行
2. Cursor の場合: Cursor のプラグインマーケットプレイスから SuperPowers を検索してインストール
3. Codex / OpenCode の場合: GitHubリポジトリ（github.com/obra/superpowers）からスキルファイルを手動でコピーし、設定ファイルに追記
4. インストール後は追加設定不要。エージェントが要件の話をし始めた瞬間から自動的にスキルが起動する

### 入力

- 対応エージェント（Claude Code / Cursor / Codex / Gemini CLI）のインストール済み環境

### 出力

- 7段階パイプラインが自動適用されるエージェント環境

## 使うツール・ライブラリ

- Claude Code
- SuperPowers (github.com/obra/superpowers)
- Cursor
- Codex
- Gemini CLI

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
