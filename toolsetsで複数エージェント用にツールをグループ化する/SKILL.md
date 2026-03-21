# toolsetsで複数エージェント用にツールをグループ化する

> tools.yamlのtoolsetsセクションで、ツールを名前付きグループに分け、エージェントやアプリケーションごとに必要なツールだけを読み込む

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

全ツールを全エージェントに渡すとコンテキストが肥大化し、不要なツールが呼ばれるリスクがある。用途別にツールセットを分けることで、エージェントの専門性を保ち、パフォーマンスとセキュリティを向上させる

## いつ使うのか

複数のエージェントが異なる役割を持つ時、セキュリティ上特定ツールへのアクセスを制限したい時、コンテキストサイズを最適化したい時

## やり方

1. tools.yamlのtoolsetsセクションでツールをグループ化
2. 各toolsetに名前を付け、含めるツール名をリスト化
3. SDK側で `client.load_toolset('toolset_name')` として特定のツールセットのみ読み込む
4. 引数なしで呼ぶと全ツールを読み込む

### 入力

- tools.yaml内のtoolsets定義

### 出力

- 指定したtoolsetに含まれるツールのみのリスト

## 使うツール・ライブラリ

- Toolbox SDK（全言語共通機能）

## コード例

```
# tools.yaml
toolsets:
  my_first_toolset:
    - my_first_tool
    - my_second_tool
  my_second_toolset:
    - my_second_tool
    - my_third_tool

# Python
all_tools = client.load_toolset()  # 全ツール
my_second_toolset = client.load_toolset("my_second_toolset")  # 特定ツールセットのみ
```

## 前提知識

- MCPプロトコルの基本概念（サーバー・クライアント・ツール）
- 使用するデータベース（PostgreSQL/MySQL/BigQuery等）の接続情報
- AIフレームワーク（LangChain/LlamaIndex/Genkit等）の基本的な使い方
- YAML形式の理解
- 非同期処理（async/await）の理解（Python/JS SDKを使う場合）
