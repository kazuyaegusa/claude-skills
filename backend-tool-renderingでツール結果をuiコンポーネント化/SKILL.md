# Backend Tool Renderingでツール結果をUIコンポーネント化

> エージェントがバックエンドツールを呼び出した際、返り値をReactコンポーネントとしてクライアントでレンダリング

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

ツールの出力をテキストではなくインタラクティブなUI（グラフ、表、フォーム等）で表現することで、ユーザーが結果を直感的に操作・編集できる

## いつ使うのか

APIから取得したデータをそのままUIに埋め込みたい、またはツール実行結果をユーザーに確認・編集させたい場合

## やり方

1. バックエンドツール定義時に返り値として `{ type: 'ui', component: 'ChartWidget', props: {...} }` 形式を返す
2. CopilotKitがこのメタデータを検出し、フロントエンド側で `ChartWidget` コンポーネントをレンダリング
3. ユーザーがそのUIを操作するとイベントが再度エージェントに渡される

### 入力

- ツール定義（バックエンド関数）
- UIコンポーネント登録（フロントエンド）

### 出力

- レンダリング可能なReactコンポーネントとprops

## 使うツール・ライブラリ

- @copilotkit/react-core
- AG-UI Protocol

## 前提知識

- React（Hooksの基本理解）
- 非同期処理・状態管理の基礎
- LLM・AIエージェントの概念（LangGraph、CrewAI等）
- REST/WebSocket等のクライアント-サーバー通信

## 根拠

> 「Backend Tool Rendering – Enables agents to call backend tools that return UI components rendered directly in the client.」
