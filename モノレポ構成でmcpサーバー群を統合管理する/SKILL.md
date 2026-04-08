# モノレポ構成でMCPサーバー群を統合管理する

> microsoft/mcp リポジトリのように、複数のMCPサーバー実装を1つのリポジトリで管理し、共通のライブラリ・テストフレームワーク・パイプライン・エンジニアリングシステムを統一する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: automation-pipeline

## なぜ使うのか

個別リポジトリで管理すると、依存ライブラリのバージョン不整合・テスト品質のばらつき・CI/CDの重複実装が発生する。モノレポ化により「unify engineering investments; reduce duplication and divergence」を実現し、開発効率と品質を向上

## いつ使うのか

組織内で複数のMCPサーバーを開発・保守する場合。特にサーバー間で共通のロジック（認証、ログ、エラーハンドリング等）がある場合に有効

## やり方

1. リポジトリルートに共通ライブラリ（core libraries）を配置 2. servers/ ディレクトリ配下に各MCPサーバーをサブディレクトリとして配置（例: servers/Azure.Mcp.Server/、servers/Fabric.Mcp.Server/） 3. 各サーバーディレクトリに README.md / CHANGELOG.md / TROUBLESHOOTING.md / SUPPORT.md を標準化 4. 統一テストフレームワークでE2Eテスト・単体テストを実行 5. 共通パイプラインで各サーバーのビルド・リリースを自動化

### 入力

- 複数のMCPサーバー実装
- 共通ライブラリ（認証、通信、スキーマ定義等）
- 統合テストスイート

### 出力

- 統一された品質基準を満たすMCPサーバー群
- 共通ドキュメント構成（README / CHANGELOG / TROUBLESHOOTING / SUPPORT）
- 自動化されたリリースパイプライン

## 使うツール・ライブラリ

- monorepo管理ツール（Nx / Turborepo / Lerna等、リポジトリ固有）
- 共通CI/CDパイプライン（GitHub Actions等）
- 共通テストフレームワーク

## コード例

```
// リポジトリ構成例
microsoft/mcp/
├── servers/
│   ├── Azure.Mcp.Server/
│   │   ├── README.md
│   │   ├── CHANGELOG.md
│   │   ├── TROUBLESHOOTING.md
│   │   ├── SUPPORT.md
│   │   └── src/
│   ├── Fabric.Mcp.Server/
│   │   └── ...
├── core-libraries/
│   ├── auth/
│   ├── transport/
│   └── schemas/
├── tests/
│   ├── integration/
│   └── e2e/
└── pipelines/
```

## 前提知識

- Model Context Protocol (MCP) の基本概念（Host / Client / Server アーキテクチャ）の理解
- VS Code / Visual Studio / Claude Desktop 等の MCP Host 対応アプリケーションの使用経験
- Microsoft Azure / Microsoft 365 / GitHub 等のサービスへのアクセス権限（該当サーバーを利用する場合）
- Node.js / Python / .NET 等のランタイム環境（Local型MCPサーバーを利用する場合）
- OAuth 2.0 / Microsoft Entra ID 等の認証フローの基礎知識（Remote型MCPサーバーを利用する場合）

## 根拠

> 「Microsoft 365 Calendar / Mail / User / Teams / Word / Admin Center / Copilot Chat 等の M365系MCPサーバーは全て Remote型（https://agent365.svc.cloud.microsoft/agents/tenants/{tenant_id}/servers/...）」
