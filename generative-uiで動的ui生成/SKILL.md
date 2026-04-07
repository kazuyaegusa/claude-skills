# Generative UIで動的UI生成

> エージェントがユーザーの意図・実行状態に応じてUIコンポーネントを実行時に生成・更新する

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

静的なUIでは多様なエージェントの出力パターンに対応しきれず、すべてのケースを事前定義するのは非現実的

## いつ使うのか

エージェントの出力が多様で事前に全パターンを定義できない場合、ユーザーごとにパーソナライズされたUIを動的生成したい場合

## やり方

1. エージェントがUIスキーマ（AG-UI/A2UI/MCP Apps）を生成
2. CopilotKitがスキーマを解釈してReactコンポーネントをレンダリング
3. ユーザーの操作に応じてエージェントがUIを再生成・更新
4. 状態変化がシームレスにUIに反映される

### 入力

- ユーザーの意図
- エージェントの内部状態
- UIスキーマ定義

### 出力

- 動的生成されたUIコンポーネント

## 使うツール・ライブラリ

- AG-UIプロトコル
- A2UI
- MCP Apps

## 前提知識

- React/Angularの基礎知識
- Hooksの理解（useStateなど）
- エージェント・LLMアプリケーションの基本概念
- 非同期処理・ストリーミングの理解

## 根拠

> Build **agent-native applications** with generative UI, shared state, and human-in-the-loop workflows.
