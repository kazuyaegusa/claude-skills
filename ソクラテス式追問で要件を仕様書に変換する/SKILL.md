# ソクラテス式追問で要件を仕様書に変換する

> エージェントが曖昧な要件に対して逆質問を繰り返し、読み通せるサイズのチャンクに分けた設計文書を自動生成する

- 出典: https://x.com/btcqzy1/status/2033116943712993717
- 投稿者: 爱丽丝呀！
- カテゴリ: agent-orchestration

## なぜ使うのか

曖昧な要件のままコーディングを始めると、実装後に「思っていたのと違う」が多発し手戻りコストが膨大になる。先に仕様を固めることで後工程を安定させる

## いつ使うのか

新機能の実装や大規模リファクタリングを開始するとき。要件が頭の中にあるが文書化されていない段階

### 具体的な適用場面

- 長期間・複数ファイルにわたる機能追加をAIエージェントに任せるとき
- AIが書いたコードがすぐにスパゲッティ化するプロジェクトで品質を安定させたいとき
- Claude Code / Cursor / Codex / Gemini CLI を使っているチームがテスト文化を強制したいとき

## やり方

1. エージェントに「○○を作りたい」と伝える
2. SuperPowers のスキルが自動起動し、エージェントが「何のために作るのか」「誰が使うのか」「成功状態はどう見えるか」などソクラテス式に追問してくる
3. 回答を積み上げると、エージェントが設計文書をチャンク単位で提示してくる
4. 開発者が各チャンクをレビューしてOKを出すと次の段階へ進む（承認なしにコーディングフェーズに入らない）

### 入力

- 自然言語での曖昧な要件・アイデア

### 出力

- エージェントが生成した設計文書（開発者が承認済み）

## 使うツール・ライブラリ

- SuperPowers
- Claude Code または対応エージェント

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
