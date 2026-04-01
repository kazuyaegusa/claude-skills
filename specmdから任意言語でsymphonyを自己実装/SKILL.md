# SPEC.mdから任意言語でSymphonyを自己実装

> Symphony公式のSPEC.mdをコーディングエージェントに渡し、好みの言語でSymphony本体を実装させる

- 出典: https://x.com/ai_agent_dev/status/2029406495805440089
- 投稿者: 遠藤巧巳 - AIネイティブな会社の作り方
- カテゴリ: agent-orchestration

## なぜ使うのか

Elixir以外のスタック（Python・TypeScript等）を使うチームでも導入できる。公式参照実装に縛られず既存インフラと統合しやすい言語で実装できる

## いつ使うのか

Elixir環境がなく、PythonやTypeScriptなど既存スタックでSymphonyを動かしたいとき

### 具体的な適用場面

- LinearでタスクトラッキングしているチームがCodexを本格導入する際、エンジニアの監視コストを下げたいとき
- 複数のコーディングタスクを並列で自律実行させ、PR+CI結果を自動生成したいとき

## やり方

1. Claude Code・Cursor・Codex等のコーディングエージェントを開く
2. 以下のプロンプトを送る:
   「Implement Symphony according to the following spec: https://github.com/openai/symphony/blob/main/SPEC.md」
3. エージェントがSPEC.mdを読み込み、指定言語で実装を生成する
4. 生成コードをレビューし、Linear・Codex APIの認証情報を設定して起動する

### 入力

- https://github.com/openai/symphony/blob/main/SPEC.md（仕様書）
- コーディングエージェント（Claude Code・Codex等）

### 出力

- 任意言語で動作するSymphony実装

## 使うツール・ライブラリ

- Symphony SPEC.md (github.com/openai/symphony)
- Claude Code / Cursor / Codex（実装用）

## コード例

```
> Set up Symphony for my repository based on
> https://github.com/openai/symphony/blob/main/elixir/README.md
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
