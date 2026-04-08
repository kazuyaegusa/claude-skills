# Human-in-the-Loopでエージェント実行を一時停止

> エージェントがタスク途中でユーザーの確認・入力・編集を待つフローを実装

- 出典: https://github.com/CopilotKit/CopilotKit
- 投稿者: CopilotKit
- カテゴリ: agent-orchestration

## なぜ使うのか

重要な判断をエージェントに完全委任せず、ユーザーが介入できるポイントを設けることで信頼性と制御性を確保

## いつ使うのか

削除・送信・決済など不可逆な操作を実行前に確認したい場合、またはエージェントが判断できない情報をユーザーに問い合わせたい場合

## やり方

1. エージェント側で `await requestUserInput('承認しますか？')` のような関数を呼び出す
2. CopilotKitがUI側にモーダル・プロンプトを表示
3. ユーザーが応答するとその値がエージェントに返り、処理を再開

### 入力

- エージェント側のrequestUserInput呼び出し

### 出力

- ユーザーの入力値・選択結果

## 使うツール・ライブラリ

- @copilotkit/react-core
- LangGraph等のエージェントフレームワーク

## 前提知識

- React（Hooksの基本理解）
- 非同期処理・状態管理の基礎
- LLM・AIエージェントの概念（LangGraph、CrewAI等）
- REST/WebSocket等のクライアント-サーバー通信
