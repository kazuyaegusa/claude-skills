# 3つの柱（Server/App/Client）で役割分離

> FastMCPをServer（ツール提供）、App（対話UI）、Client（サーバー接続）の3つのモードで使い分ける

- 出典: https://github.com/PrefectHQ/fastmcp
- 投稿者: PrefectHQ
- カテゴリ: dev-tool

## なぜ使うのか

LLMツール公開、UI統合、マルチサーバー接続といった異なる責務を明確に分離し、アーキテクチャの理解とメンテナンスを容易にするため

## いつ使うのか

MCPアプリケーションの設計時、責務を分離したい時

## やり方

1. ツール提供が目的ならServerモードで@mcp.toolを使う
2. 対話UIが必要ならAppモードでコンポーネントをレンダリング
3. 既存MCPサーバーに接続するならClientモードでURL指定

### 入力

- 要件（ツール提供 / UI統合 / サーバー接続）

### 出力

- 明確に役割分離されたアーキテクチャ

## 使うツール・ライブラリ

- fastmcp

## 前提知識

- Python 3.xの基礎知識
- 型ヒント（Type Hints）の理解
- デコレータの基本概念
- Model Context Protocol（MCP）の概要
- LLMツール統合の基本的な動機
