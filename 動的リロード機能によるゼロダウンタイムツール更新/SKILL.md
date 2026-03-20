# 動的リロード機能によるゼロダウンタイムツール更新

> Toolboxサーバーの起動中に`tools.yaml`を編集すると、サーバー再起動なしで新しいツール定義が反映される

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: other

## なぜ使うのか

本番環境でのツール更新時にダウンタイムを発生させず、アプリケーション再デプロイも不要なため、迅速なイテレーションが可能

## いつ使うのか

ツールのSQL文やパラメータを頻繁に調整する開発フェーズ、本番環境での緊急修正、A/Bテストでツールバリエーションを試したい時

## やり方

1. Toolboxサーバーをデフォルト設定で起動（`--disable-reload`フラグなし）
2. `tools.yaml`を編集してツールの定義・パラメータ・SQLクエリ等を変更
3. ファイル保存時にToolboxサーバーが自動検出してリロード
4. 次回のクライアント呼び出しから新しい定義が適用される

### 入力

- 編集された`tools.yaml`

### 出力

- 更新されたツール定義（ダウンタイムなし）

## 使うツール・ライブラリ

- MCP Toolbox server（デフォルトで有効）

## コード例

```
# サーバー起動時にデフォルトで動的リロード有効
./toolbox --tools-file tools.yaml

# 無効化する場合のみ
./toolbox --tools-file tools.yaml --disable-reload
```

## 前提知識

- Model Context Protocol (MCP)の基本概念
- AIエージェントフレームワーク（LangChain、LlamaIndex、Genkit等）の基礎知識
- データベース接続の基本（PostgreSQL、MySQL、Spanner、BigQuery等）
- YAML形式の読み書き
- Docker/コンテナ技術の基礎（本番デプロイ時）
- OpenTelemetryによる可観測性の概念（本番運用時）
