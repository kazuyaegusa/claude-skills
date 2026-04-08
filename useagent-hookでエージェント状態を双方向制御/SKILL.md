# useAgent Hookでエージェント状態を双方向制御

> React Hook経由でエージェントの状態を読み書きし、UI更新をトリガーする

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントの内部状態（例: 選択中の都市、検索フィルター）をUIコンポーネント側から直接操作可能にすることで、ユーザーの明示的な入力とエージェントの推論を統合できる

## いつ使うのか

ユーザーがUIで設定を変更したら即座にエージェントの推論をリセット・再開したい場合

## やり方

1. `const { agent } = useAgent({ agentId: 'my_agent' })` でエージェントインスタンス取得
2. `agent.state.city` で状態を読み取りレンダリング
3. `agent.setState({ city: 'NYC' })` でUI側から状態を書き換え
4. エージェントはこの変更を検知して次のアクションを実行

### 入力

- agentId（エージェント識別子）

### 出力

- agent.state（現在のエージェント状態オブジェクト）
- agent.setState（状態更新関数）

## 使うツール・ライブラリ

- @copilotkit/react-core

## コード例

```
const { agent } = useAgent({ agentId: 'my_agent' });
return (
  <div>
    <h1>{agent.state.city}</h1>
    <button onClick={() => agent.setState({ city: 'NYC' })}>
      Set City
    </button>
  </div>
);
```

## 前提知識

- React（Hooksの基本理解）
- 非同期処理・状態管理の基礎
- LLM・AIエージェントの概念（LangGraph、CrewAI等）
- REST/WebSocket等のクライアント-サーバー通信

## 根拠

> 「Build agent-native applications with generative UI, shared state, and human-in-the-loop workflows.」

> 「Backend Tool Rendering – Enables agents to call backend tools that return UI components rendered directly in the client.」

> 「Shared State – A synchronized state layer that both agents and UI components can read from and write to in real time.」

> 「Human-in-the-Loop – Lets agents pause execution to request user input, confirmation, or edits before continuing.」

> コードスニペット: `const { agent } = useAgent({ agentId: 'my_agent' }); ... agent.setState({ city: 'NYC' })`
