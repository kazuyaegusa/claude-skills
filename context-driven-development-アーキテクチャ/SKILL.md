# Context-Driven Development アーキテクチャ

> Skills(知識) + MCP servers(ツール) + Custom Agents(役割) + AGENTS.md(振る舞い設定)を組み合わせ、AI Agentが自律的にコード生成・ドキュメント参照・デプロイを行う開発スタイル

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

従来のAI支援開発は「都度プロンプトを書く」ものだったが、Context-Driven Developmentでは「適切なコンテキストをリポジトリに埋め込む」ことで、Agentが自動的に最適な行動を選ぶ。結果、開発者はWHATを指示するだけでよく、HOWはAgentが判断する

## いつ使うのか

Azure/Foundry等のエコシステムを使う大規模プロジェクトで、複数開発者が異なるAgent(Copilot/Claude等)を使う時。チーム全体で「Agentにどう振る舞ってほしいか」を統一したい時

## やり方

1. **Skills**: `.github/skills/` にSDK/ライブラリ使用法を定義 2. **MCP servers**: `.vscode/mcp.json` でドキュメント検索・GitHub操作等のツールを登録 3. **Custom Agents**: `.github/agents/` にbackend/frontend/infrastructure等の役割別Agentを定義 4. **AGENTS.md**: プロジェクトルートに配置し、「このプロジェクトではどのAgentをいつ使うか」を宣言 5. 開発者が「Cosmos DBでユーザー管理APIを作って」と指示 → backend agentが azure-cosmos-db-py skill参照 → microsoft-docs MCPでドキュメント確認 → コード生成 → テスト → デプロイ

### 入力

- Skills (知識)
- MCP servers (ツール)
- Custom Agents (役割)
- AGENTS.md (振る舞い設定)

### 出力

- Agentが自律的にコード生成・ドキュメント参照・デプロイを実行
- 開発者はWHATを指示するだけでよい開発体験

## 使うツール・ライブラリ

- GitHub Copilot / Claude / Gemini
- MCP protocol
- Skills repository

## コード例

```
# AGENTS.md
---
backend:
  role: FastAPI + Cosmos DB backend developer
  skills:
    - azure-cosmos-db-py
    - fastapi-router-py
    - pydantic-models-py
  mcp_servers:
    - microsoft-docs
    - github
  triggers:
    - "create API"
    - "add endpoint"
---

# 開発者の指示
"Create a user management API with Cosmos DB"

# Agentの動作
1. AGENTS.mdでbackend agentを選択
2. azure-cosmos-db-py skillを参照
3. microsoft-docs MCPでCosmos DB公式ドキュメント検索
4. FastAPI + Pydantic + Cosmos DB のコード生成
5. pytest-asyncioでテスト生成
6. github MCPでPR作成
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "Skills, custom agents, AGENTS.md templates, and MCP configurations for AI coding agents working with Azure SDKs and Microsoft AI Foundry."

> "132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery"

> "Context-Driven Development: Agent Skills for Microsoft Foundry and Azure (Blog post)"
