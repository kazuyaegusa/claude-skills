# 既存SDKからFastMCPへ移行

> FastMCP v2、MCP Python SDK、または低レベルSDKからFastMCP v3以降へアップグレードする

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: dev-tool

## なぜ使うのか

FastMCPはMCP公式SDKに統合され、現在は独立プロジェクトとして活発に開発されている（日次100万DL）。最新のベストプラクティスと機能を利用するため移行が推奨される

## いつ使うのか

古いMCP SDK/FastMCPバージョンを使っている既存プロジェクトを最新版に移行したい時

## やり方

1. 現在使用中のSDKバージョンを確認
2. 該当する移行ガイドを参照（from-fastmcp-2, from-mcp-sdk, from-low-level-sdk）
3. ガイドに従いコードを更新
4. テストして動作確認

### 入力

- 既存のMCP SDK/FastMCPコードベース
- 移行ガイド（gofastmcp.com/getting-started/upgrading/）

### 出力

- FastMCP v3以降対応のコード

## 使うツール・ライブラリ

- fastmcp v3+

## コード例

```
# 移行ガイド参照（具体的なコード変更は各ガイドに記載）
```

## 前提知識

- Python 3.x基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol (MCP)の概要理解
- 非同期プログラミング（async/await）の基礎（応用時）

## 根拠

> 「FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024」

> 「some version of FastMCP powers 70% of MCP servers across all languages」

> 「Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically」

> 「with FastMCP, best practices are built in」

> 「When you're ready to deploy, Prefect Horizon offers free hosting for FastMCP users」
