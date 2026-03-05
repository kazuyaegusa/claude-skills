---
name: GitHub PR Automation
version: 1.0.0
description: GitHub APIでブランチ作成・ファイルコミット・PR作成を自動化する汎用クライアント
author: extracted-from-symphony
tags: [github, pr, automation, git, api]
---

# GitHub PR Automation

GitHub REST API を使って、ブランチ作成 → ファイルコミット → PR 作成を完全自動化する非同期 Python クライアント。

ローカルに git clone 不要。API 経由でリモートリポジトリに直接コミット・PR 作成が可能。

## 依存パッケージ

```
httpx
```

## 環境変数

- `GITHUB_TOKEN` — GitHub Personal Access Token（必須、`repo` スコープ）
- `GITHUB_REPO` — 対象リポジトリ `owner/repo` 形式（必須）

## 使い方

```python
from github_pr_client import GitHubPRClient

client = GitHubPRClient(
    token=os.getenv("GITHUB_TOKEN"),
    repo=os.getenv("GITHUB_REPO"),  # "owner/repo"
)

# ブランチ作成
await client.create_branch("feature/my-change")

# ファイルをコミット
files = [
    {"path": "src/hello.py", "content": "print('hello')\n"},
    {"path": "README.md", "content": "# Updated\n"},
]
await client.commit_files("feature/my-change", files, "feat: add hello")

# PR作成
pr_url = await client.create_pr(
    branch="feature/my-change",
    title="Add hello feature",
    body="Auto-generated PR",
)
print(pr_url)
```

## コマンド例

```bash
# テスト実行
python -m pytest test_github_pr_client.py
```

## ユースケース

- AI が生成したコードを自動的に PR にする
- CI/CD パイプラインからプログラム的に PR を作成
- バッチ処理でファイル更新を PR にまとめる

## 注意事項

- トークンは絶対にハードコードしない
- `repo` スコープが必要（Fine-grained token の場合は Contents + Pull requests 権限）
- GitHub API レート制限: 5000 req/hour（認証済み）
