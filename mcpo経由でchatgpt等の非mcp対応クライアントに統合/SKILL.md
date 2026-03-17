# mcpo経由でChatGPT等の非MCP対応クライアントに統合

> mcpo（MCP to OpenAPI変換ツール）を使い、MCPをサポートしないクライアント（ChatGPT等）でもSerenaツールを利用可能にする

- 出典: https://github.com/oraios/serena
- 投稿者: oraios
- カテゴリ: agent-orchestration

## なぜ使うのか

MCPネイティブサポートがないLLMサービスでも、OpenAPIツール呼び出しインターフェースがあればSerenaの機能を活用できるため

## いつ使うのか

ChatGPTやMCP非対応のLLMサービスで高度なコード編集を行いたい場合

## やり方

1. mcpoをインストール
2. SerenaをMCPサーバーとして起動
3. mcpoでSerena MCPサーバーをOpenAPIエンドポイントとして公開
4. ChatGPT等のクライアントにOpenAPI定義を登録
5. LLMがツールを呼び出すとmcpo経由でSerenaに転送される（詳細: https://github.com/oraios/serena/blob/main/docs/03-special-guides/serena_on_chatgpt.md）

### 入力

- mcpoツール
- Serena MCPサーバー
- OpenAPIツール呼び出し対応のLLMクライアント

### 出力

- OpenAPIエンドポイント経由で利用可能なSerenaツール

## 使うツール・ライブラリ

- mcpo
- Serena

## 前提知識

- MCPの概念と動作原理
- Language Server Protocol（LSP）の基礎知識
- LLMエージェントのツール呼び出しメカニズム
- Python環境管理（uv）の基本操作
- 対象言語のLanguage Serverインストール方法（LSPバックエンド使用時）
- JetBrains IDE操作の基礎（JetBrainsバックエンド使用時）
