---
name: Linear API Client
version: 1.0.0
description: Linear GraphQL APIを使ってIssueの取得・更新・コメント追加を行う汎用クライアント
author: extracted-from-symphony
tags: [linear, project-management, graphql, api]
---

# Linear API Client

Linear の GraphQL API を操作する非同期 Python クライアント。Issue の取得・ステート更新・コメント追加に対応。

## 依存パッケージ

```
httpx
```

## 環境変数

- `LINEAR_API_KEY` — Linear API キー（必須）

## 使い方

```python
from linear_client import LinearClient

client = LinearClient(os.getenv("LINEAR_API_KEY"))

# Issue取得
issue = await client.get_issue("issue-uuid")

# ステート更新
await client.update_issue_state("issue-uuid", "state-uuid")

# コメント追加
await client.add_comment("issue-uuid", "実装完了しました")

# カスタムGraphQLクエリ
data = await client.query("query { viewer { id name } }")
```

## コマンド例

```bash
# 単体テスト
python -m pytest test_linear_client.py

# スクリプトとして使用
python -c "import asyncio; from linear_client import LinearClient; ..."
```

## 注意事項

- API キーは絶対にハードコードしない（`os.getenv()` を使用）
- レート制限: Linear API は 1500 req/hour
- 非同期専用（`asyncio` が必要）
