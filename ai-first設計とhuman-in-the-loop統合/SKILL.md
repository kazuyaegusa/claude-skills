# AI-First設計とHuman-in-the-Loop統合

> AIネイティブなpiece（AIプロバイダー統合、AI SDK）を提供し、かつ承認待ち・遅延実行といったHuman-in-the-Loopパターンもpieceとして実装することで、AI自動化と人間判断を柔軟に組み合わせる

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: agent-orchestration

## なぜ使うのか

完全自動化が危険またはコスト高な場合でも、AIによる下書き生成→人間による承認→実行という段階的自動化を実現できる。また、複数AIプロバイダーを試行するような実験的ワークフローもビルダーで構築可能にするため

## いつ使うのか

AIが生成したコンテンツを公開前に人間が確認したい時、高リスク操作（請求書発行、契約書送信等）にワンステップの承認を入れたい時、複数AIプロバイダーで結果を比較実験したい時

## やり方

1. ネイティブAI pieceでOpenAI、Claude等の主要AIプロバイダーと統合
2. AI SDKを使って独自AIエージェントをワークフロー内に組み込む
3. Human-in-the-Loop pieceで「承認待ち」「遅延実行」をワークフローに挿入
4. Chat InterfaceやForm Interfaceを使って人間の入力を受け取る
5. ノーコードビルダーでAI→人間→AIのようなハイブリッドフローを構築

### 入力

- AI provider API（OpenAI、Claude等）
- Human-in-the-Loop piece
- Chat/Form Interface piece

### 出力

- AI生成内容の人間承認フロー
- 遅延実行・条件付き実行ワークフロー
- 複数AIプロバイダーの比較結果

## 使うツール・ライブラリ

- Activepieces AI pieces
- AI SDK
- Human-in-the-Loop piece
- Chat Interface piece
- Form Interface piece

## 前提知識

- TypeScriptの基礎知識（型システム、非同期処理）
- npmパッケージ管理の理解
- REST API/Webhook等の統合パターンの知識
- Model Context Protocol (MCP)の基本概念（LLMがツールを呼び出す仕組み）
- ワークフロー自動化ツール（Zapier等）の利用経験があると理解が早い
