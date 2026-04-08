# Generative UIで動的にコンポーネント生成

> エージェントがユーザーの意図に基づき、実行時に新しいUIコンポーネントを生成・更新

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

予め定義されたUIでは対応できない多様なユースケースに対し、エージェントがその場で最適なUIを組み立てることで柔軟性を最大化

## いつ使うのか

ユーザーのリクエストが多様でUI構造を事前に固定できない場合（例: 「売上推移を可視化して」→棒グラフか折れ線グラフか動的に決定）

## やり方

1. Static (AG-UI Protocol): エージェントが定義済みのコンポーネントをパラメータ付きで呼び出す
2. Declarative (A2UI): エージェントがJSONでUI構造を宣言し、CopilotKitがレンダリング
3. Open-Ended (MCP Apps & Open JSON): エージェントが任意のJSON形式を返し、アプリ側でカスタムレンダラーを実装

### 入力

- ユーザーの自然言語指示
- エージェントのコンテキスト

### 出力

- React要素（動的生成されたコンポーネント）

## 使うツール・ライブラリ

- @copilotkit/react-core
- AG-UI Protocol
- A2UI
- MCP Apps

## 前提知識

- React（Hooksの基本理解）
- 非同期処理・状態管理の基礎
- LLM・AIエージェントの概念（LangGraph、CrewAI等）
- REST/WebSocket等のクライアント-サーバー通信

## 根拠

> 「Build agent-native applications with generative UI, shared state, and human-in-the-loop workflows.」
