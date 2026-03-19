# モノレポでの複数MCPサーバー統合管理

> 単一リポジトリ(microsoft/mcp)内に、コアライブラリ・テストフレームワーク・エンジニアリングシステム・パイプライン・ツールを共有し、複数のMCPサーバー(Azure, Fabric等)を統一的に管理する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: automation-pipeline

## なぜ使うのか

エンジニアリング投資の重複を削減し、バージョン管理・CI/CD・テスト戦略を統一することで、品質とメンテナンス効率を向上させるため。

## いつ使うのか

複数の関連MCPサーバーを開発・保守し、共通インフラ(認証、ロギング、エラーハンドリング等)を統一したい場合

## やり方

1. リポジトリルートに`servers/`ディレクトリを作成
2. 各MCPサーバーを`servers/Azure.Mcp.Server/`, `servers/Fabric.Mcp.Server/`等のサブディレクトリに配置
3. 共通ライブラリ・テストフレームワークをルートまたは`shared/`に配置し、各サーバーから参照
4. CIパイプラインで変更検知(例: Azure.Mcp.Server配下の変更時のみAzure MCPをビルド)を実装
5. リリースタグを`Azure.Mcp.Server-v1.0.0`のようにサーバー名prefixで管理
6. 各サーバーのREADME/CHANGELOG/TROUBLESHOOTING.mdをサブディレクトリに配置し、ルートREADMEからリンク

### 入力

- 各MCPサーバーのソースコード
- 共通ライブラリ・テストフレームワーク
- CI/CDパイプライン設定

### 出力

- 統一されたリポジトリ構造
- サーバーごとの独立したリリース
- 共通ツール・ライブラリの再利用

## 使うツール・ライブラリ

- GitHub Actions (CI/CD)
- Monorepo管理ツール(Nx, Turborepoなど、投稿には明記されていないが推測可能)
- Git Tags

## コード例

```
# リポジトリ構造例
microsoft/mcp/
├── servers/
│   ├── Azure.Mcp.Server/
│   │   ├── README.md
│   │   ├── CHANGELOG.md
│   │   └── src/
│   └── Fabric.Mcp.Server/
│       ├── README.md
│       └── src/
├── shared/
│   ├── core-lib/
│   └── test-framework/
└── README.md (カタログ)
```

## 前提知識

- MCP (Model Context Protocol)の基本概念(Host, Client, Server, Tools, Resources)の理解
- VS Code/Visual Studio等のIDEでのMCP設定方法の基礎知識
- Microsoft Graph APIの基本的な知識(認証、スコープ、エンドポイント構造)
- Azure/M365のテナントID・組織名等の基本的な概念の理解
- npmまたはPython(uvx)を使ったパッケージインストールの経験
