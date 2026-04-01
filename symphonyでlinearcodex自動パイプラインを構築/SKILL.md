# SymphonyでLinear→Codex自動パイプラインを構築

> Linearボードを監視し、新しいチケットが作成されると隔離されたCodex実行セッションを自動スポーンするSymphonyをセットアップする

- 出典: https://x.com/ai_agent_dev/status/2029406495805440089
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: agent-orchestration

## なぜ使うのか

エンジニアがエージェントのセッションを一つずつ監視する手間をなくし、タスク管理（Linearチケット更新）に専念できるようになる。エージェントはCI・PRレビュー・複雑度分析・walkthrough動画として証拠を提出し品質を担保する

## いつ使うのか

LinearでプロジェクトトラッキングしているチームがCodexを本格活用し始める段階。エンジニアがエージェントを個別監視することにボトルネックを感じているとき

### 具体的な適用場面

- LinearでタスクトラッキングしているチームがCodexを本格導入する際、エンジニアの監視コストを下げたいとき
- 複数のコーディングタスクを並列で自律実行させ、PR+CI結果を自動生成したいとき

## やり方

1. harness engineeringに対応したコードベースを用意する（エージェントが安全に実行できるCI/テスト環境を整備）
2a. Elixir実装を使う場合: `git clone https://github.com/openai/symphony && cd symphony/elixir` を実行し `README.md` に従ってElixir環境をセットアップして起動する
2b. 好みの言語で実装する場合: コーディングエージェントに「Implement Symphony according to the following spec: https://github.com/openai/symphony/blob/main/SPEC.md」と指示する
3. Linear APIキーとCodex APIキーをSymphonyの設定に渡す
4. Symphonyを起動するとLinearボードの監視が始まる
5. Linearにチケットを作成すると隔離されたCodexエージェントが自動スポーンされタスクを実行
6. 完了後、PR・CI結果・複雑度分析・walkthrough動画が自動生成される

### 入力

- Linear プロジェクトボードのAPIキー
- Codex のAPIアクセス権
- harness engineeringに対応したコードベース（CI/テスト環境が整備済み）

### 出力

- Linearチケットに対応するPR
- CI実行結果
- コード複雑度分析
- 実装walkthrough動画

## 使うツール・ライブラリ

- Symphony (github.com/openai/symphony)
- Linear
- Codex
- Elixir（参照実装使用時）

## コード例

```
> Implement Symphony according to the following spec:
> https://github.com/openai/symphony/blob/main/SPEC.md
```

## 前提知識

- harness engineering（エージェントが安全に実行できるCI/テスト自動化環境）が整備されていること
- Linear のAPIアクセス権
- Codex のAPIアクセス権
- Elixir実行環境（参照実装を使う場合）

## 根拠

> 「Linearにチケットを入れればCodexが裏で動くようになった」

> "Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents."

> "Symphony monitors a Linear board for work and spawns agents to handle the tasks. The agents complete the tasks and provide proof of work: CI status, PR review feedback, complexity analysis, and walkthrough videos."

> "Option 1. Make your own: Tell your favorite coding agent to build Symphony: Implement Symphony according to the following spec: https://github.com/openai/symphony/blob/main/SPEC.md"

> "Symphony works best in codebases that have adopted harness engineering. Symphony is the next step -- moving from managing coding agents to managing work that needs to get done."
