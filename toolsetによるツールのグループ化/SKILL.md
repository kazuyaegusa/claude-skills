# Toolsetによるツールのグループ化

> 複数のツールをtoolsetとして名前付きグループ化し、エージェントごとに必要なツールセットだけをロードする

- 出典: https://github.com/googleapis/genai-toolbox
- 投稿者: googleapis
- カテゴリ: agent-orchestration

## なぜ使うのか

全てのツールを全エージェントに渡すとコンテキスト汚染やコスト増大が起きるため、エージェントの役割に応じて必要最小限のツールセットを渡す

## いつ使うのか

複数の専門エージェント（検索専用・更新専用など）を運用する時、エージェントごとに権限を分けたい時

## やり方

1. tools.yamlの`toolsets:`セクションに名前とツールリストを定義
2. SDK側で`client.load_toolset("my_first_toolset")`のように名前指定でロード
3. 名前省略時は全ツールがロードされる

### 入力

- tools.yamlのtoolsetsセクション定義
- 各ツールの定義

### 出力

- 指定したtoolsetに含まれるツールのリスト

## 使うツール・ライブラリ

- tools.yaml
- ToolboxClient SDK

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
my_second_toolset = client.load_toolset("my_second_toolset")
```

## 前提知識

- MCPプロトコルの基本概念（Model Context Protocol）
- LLMエージェントフレームワークの基礎（LangChain/LlamaIndex/Genkit等のいずれか）
- データベース接続の基本（PostgreSQL/MySQL等の接続文字列）
- YAMLの基本文法
- ツール呼び出しの仕組み（Function Calling）
