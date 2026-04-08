# npx copilotkit init で既存プロジェクトに統合

> 既存のReactプロジェクトにCopilotKitを自動セットアップ

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

手動でのパッケージインストール・設定記述を省略し、数分でエージェント連携UIを導入できる

## いつ使うのか

既存のReactアプリにAIエージェント機能を後付けしたい場合

## やり方

1. プロジェクトルートで `npx copilotkit@latest init` を実行
2. CopilotKitがpackage.json、Providerコンポーネント、エージェント接続設定を自動生成
3. 既存のコンポーネントにuseAgent等のフックを追加してエージェント機能を利用

### 入力

- 既存のReactプロジェクト

### 出力

- CopilotKit設定済みのプロジェクト

## 使うツール・ライブラリ

- npx
- @copilotkit/react-core

## コード例

```
npx copilotkit@latest init
```

## 前提知識

- React（Hooksの基本理解）
- 非同期処理・状態管理の基礎
- LLM・AIエージェントの概念（LangGraph、CrewAI等）
- REST/WebSocket等のクライアント-サーバー通信
