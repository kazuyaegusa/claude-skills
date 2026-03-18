# セルフホスト&ネットワークギャップ運用

> Activepiecesをオンプレミスまたはプライベートクラウドにセルフホストし、外部ネットワークと隔離した環境で運用

- 出典: https://github.com/activepieces/activepieces
- 投稿者: activepieces
- カテゴリ: automation-pipeline

## なぜ使うのか

機密データや規制対象データを扱う環境で、外部SaaSに依存せずワークフロー自動化とMCP統合を実現するため

## いつ使うのか

GDPR、HIPAA等の規制対象データを扱う場合、または外部SaaSへの依存を避けたい場合

## やり方

1. Activepiecesのセルフホスト用Dockerイメージを取得
2. docker-compose.ymlで環境変数を設定(DB、認証、ブランディング等)
3. プライベートネットワーク内でコンテナを起動
4. ファイアウォールでインターネットアクセスを制限(必要な場合のみプロキシ経由)
5. 開発者は統合をローカルまたはプライベートnpmレジストリで管理
6. 非技術者はビルダーUIで自動化フローを構築
7. Claude Desktop等のMCPクライアントもプライベートネットワーク内で設定

### 入力

- Dockerホスト環境
- プライベートネットワーク
- 認証基盤(OAuth/SAML等)

### 出力

- オンプレミスActivepieces環境
- ネットワーク隔離されたMCPサーバー

## 使うツール・ライブラリ

- Docker
- docker-compose
- PostgreSQL等のDB
- プライベートnpmレジストリ(Verdaccio等)

## コード例

```
# docker-compose例
version: '3'
services:
  activepieces:
    image: activepieces/activepieces:latest
    environment:
      - AP_DB_URL=postgres://...
      - AP_EXECUTION_MODE=SANDBOXED
      - AP_TELEMETRY_ENABLED=false
    networks:
      - private_net
networks:
  private_net:
    driver: bridge
```

## 前提知識

- TypeScript基礎知識
- REST API統合の基本理解
- Docker/npmの基本操作
- MCPプロトコルの概念(Claude Desktop等LLMツールとの統合前提)
- ワークフロー自動化の基礎(トリガー、アクション、条件分岐)
- オープンソースプロジェクトへのコントリビューション経験(任意)

## 根拠

> When you contribute pieces to Activepieces they become automatically available as MCP servers that you can use with LLMs through Claude Desktop, Cursor or Windsurf!

> **🛠️ Largest open source MCP toolkit**: All our pieces (280+) are available as MCP that you can use with LLMs on Claude Desktop, Cursor or Windsurf.
