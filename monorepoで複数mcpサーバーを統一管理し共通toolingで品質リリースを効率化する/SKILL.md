# monorepoで複数MCPサーバーを統一管理し、共通toolingで品質・リリースを効率化する

> microsoft/mcpリポジトリで、Azure MCP, Fabric MCP等のサーバー実装をまとめて管理し、core libraries, test frameworks, pipelines, toolingを共有する

- 出典: https://github.com/microsoft/mcp
- 投稿者: microsoft
- カテゴリ: automation-pipeline

## なぜ使うのか

各サーバーを別リポジトリで管理すると、テスト基盤・CI/CD・ドキュメント構造が分散し、重複投資・品質のばらつきが発生する。monorepoで統一すれば、共通基盤の改善が全サーバーに波及し、エンジニアリングコストを削減できる

## いつ使うのか

組織が複数のMCPサーバーを提供する際、品質・メンテナンス効率を高めたいとき

## やり方

1. microsoft/mcpリポジトリを作成
2. servers/ディレクトリ配下に各サーバー（Azure.Mcp.Server, Fabric.Mcp.Server等）を配置
3. 共通ライブラリをルート階層またはsharedディレクトリで管理
4. 統一テストフレームワークで各サーバーのCI実行
5. 統一リリースパイプラインでバージョン管理・GitHub Releases発行
6. 各サーバーのREADME, CHANGELOG, TROUBLESHOOTING, SUPPORTを標準フォーマットで用意

### 入力

- 複数のMCPサーバー実装
- 共通テスト要件・品質基準
- CI/CDパイプライン定義

### 出力

- 統一されたリポジトリ構造
- 共通tooling（test, build, release）
- 一貫したドキュメント体系

## 使うツール・ライブラリ

- GitHub monorepo管理（Actions, Releases）
- 共通test frameworks（言語依存）
- 統一CI/CDパイプライン

## 前提知識

- Model Context Protocol (MCP)の基本概念（クライアント・サーバーアーキテクチャ、ツール・リソース・プロンプトの違い）
- MCPホスト（Claude Desktop, VS Code, GitHub Copilot等）の使用経験
- Azure/Microsoft 365の基本サービス理解（必要に応じてAzure subscription, M365 tenant）
- JSON設定ファイル編集、環境変数・認証の基礎知識
- （開発者向け）TypeScript/Python等のMCP SDK、npm/pip等パッケージマネージャ使用経験

## 根拠

> "This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence"
