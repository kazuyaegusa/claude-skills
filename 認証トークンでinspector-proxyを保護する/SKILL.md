# 認証トークンでInspector Proxyを保護する

> Inspector起動時に自動生成されるセッショントークンをブラウザに入力またはURL経由で渡し、プロキシサーバーへの不正アクセスを防ぐ

- 出典: https://github.com/modelcontextprotocol/inspector
- 投稿者: modelcontextprotocol
- カテゴリ: ui-ux

## なぜ使うのか

Inspectorのプロキシサーバーはローカルプロセス実行権限を持つため、認証なしではDNSリバインディング攻撃やブラウザ経由のRCE（CVE-2025-49596）のリスクがある。トークン認証により安全性を確保する

## いつ使うのか

Inspectorをデフォルト設定で起動する全ての場合（認証はデフォルト有効）。特に信頼できないネットワークやリモートアクセスが可能な環境では必須

## やり方

1. `npx @modelcontextprotocol/inspector` 起動時にコンソールに出力されるトークンとURLを確認
2. 自動的に開くブラウザでトークンがURL事前入力済み
3. 手動設定の場合はUI右上「Configuration」→「Proxy Session Token」にトークンを入力→Save
4. 環境変数 `MCP_PROXY_AUTH_TOKEN` で事前設定も可能

### 入力

- Inspector起動時にコンソール出力されるセッショントークン（ランダム生成）
- または環境変数 MCP_PROXY_AUTH_TOKEN

### 出力

- 認証済みInspector Proxy接続
- RCE攻撃からの保護

## 使うツール・ライブラリ

- MCP Inspector
- Bearer token認証

## コード例

```
# 起動時のコンソール出力例
🔑 Session token: 3a1c267fad21f7150b7d624c160b7f09b0b8c4f623c7107bbf13378f051538d4

🔗 Open inspector with token pre-filled:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=3a1c267fad21f7150b7d624c160b7f09b0b8c4f623c7107bbf13378f051538d4

# 環境変数で事前設定
MCP_PROXY_AUTH_TOKEN=$(openssl rand -hex 32) npm start

# 🚨警告: 認証無効化は危険（非推奨）
DANGEROUSLY_OMIT_AUTH=true npm start
```

## 前提知識

- Node.js ^22.7.5以上
- MCPサーバーの基本概念（tools/resources/prompts）の理解
- MCPのトランスポート種別（stdio/SSE/Streamable HTTP）の違い
- JSON形式の設定ファイル記述能力（mcp.json）
