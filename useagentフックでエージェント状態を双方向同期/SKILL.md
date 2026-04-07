# useAgentフックでエージェント状態を双方向同期

> React Hooksを使ってエージェントの内部状態を読み取り・更新し、UI再レンダリングとエージェント実行を同期する

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントの状態とUIコンポーネントのステートが独立していると、ユーザーの操作がエージェントに伝わらず、エージェントの変更がUIに反映されない。双方向同期により常に一貫した状態を保つ

## いつ使うのか

エージェントの推論結果をUIで編集可能にしたい、UIの操作でエージェントのワークフローを制御したい場合

## やり方

1. `useAgent({ agentId: "my_agent" })` でエージェントインスタンスを取得
2. `agent.state.city` でエージェントの現在状態を読み取りUIに表示
3. `agent.setState({ city: "NYC" })` でUIからエージェント状態を更新
4. 状態変更はAG-UIプロトコル経由でバックエンドエージェントに伝播

### 入力

- エージェントID
- CopilotKitProviderでラップされたReactアプリ

### 出力

- リアルタイム同期されたエージェント状態
- setState関数

## 使うツール・ライブラリ

- @copilotkit/react-core

## コード例

```
const { agent } = useAgent({ agentId: "my_agent" });
return <div>
  <h1>{agent.state.city}</h1>
  <button onClick={() => agent.setState({ city: "NYC" })}>
    Set City
  </button>
</div>
```

## 前提知識

- React/Angularの基礎知識
- Hooksの理解（useStateなど）
- エージェント・LLMアプリケーションの基本概念
- 非同期処理・ストリーミングの理解

## 根拠

> const { agent } = useAgent({ agentId: "my_agent" }); ... agent.setState({ city: "NYC" })
