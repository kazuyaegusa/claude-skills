"""GitHub API による PR 自動作成クライアント"""
from __future__ import annotations

import os
from typing import Any

import httpx


class GitHubPRClient:
    """GitHub REST API でブランチ作成・ファイルコミット・PR 作成を行う非同期クライアント"""

    def __init__(self, token: str | None = None, repo: str | None = None) -> None:
        self._token = token or os.getenv("GITHUB_TOKEN", "")
        self._repo = repo or os.getenv("GITHUB_REPO", "")
        if not self._token:
            raise ValueError("GITHUB_TOKEN が未設定です")
        if not self._repo:
            raise ValueError("GITHUB_REPO が未設定です（'owner/repo' 形式）")
        self._base = "https://api.github.com"
        self._headers = {
            "Authorization": f"token {self._token}",
            "Accept": "application/vnd.github.v3+json",
        }

    async def _request(
        self, method: str, path: str, json: dict[str, Any] | None = None
    ) -> dict:
        async with httpx.AsyncClient() as c:
            resp = await c.request(
                method,
                f"{self._base}{path}",
                headers=self._headers,
                json=json,
            )
            resp.raise_for_status()
            return resp.json()

    async def create_branch(self, branch_name: str, base: str = "main") -> str:
        """base ブランチから新しいブランチを作成。作成元の SHA を返す。"""
        ref = await self._request("GET", f"/repos/{self._repo}/git/ref/heads/{base}")
        sha = ref["object"]["sha"]
        await self._request(
            "POST",
            f"/repos/{self._repo}/git/refs",
            {"ref": f"refs/heads/{branch_name}", "sha": sha},
        )
        return sha

    async def commit_files(
        self,
        branch: str,
        files: list[dict[str, str]],
        message: str,
    ) -> str:
        """複数ファイルを一括コミット。コミット SHA を返す。

        Args:
            branch: コミット先ブランチ名
            files: [{"path": "relative/path", "content": "file content"}, ...]
            message: コミットメッセージ
        """
        ref = await self._request("GET", f"/repos/{self._repo}/git/ref/heads/{branch}")
        base_sha = ref["object"]["sha"]
        commit = await self._request(
            "GET", f"/repos/{self._repo}/git/commits/{base_sha}"
        )
        base_tree = commit["tree"]["sha"]

        # Blob + Tree エントリ作成
        tree_entries = []
        for f in files:
            blob = await self._request(
                "POST",
                f"/repos/{self._repo}/git/blobs",
                {"content": f["content"], "encoding": "utf-8"},
            )
            tree_entries.append(
                {
                    "path": f["path"],
                    "mode": "100644",
                    "type": "blob",
                    "sha": blob["sha"],
                }
            )

        tree = await self._request(
            "POST",
            f"/repos/{self._repo}/git/trees",
            {"base_tree": base_tree, "tree": tree_entries},
        )
        new_commit = await self._request(
            "POST",
            f"/repos/{self._repo}/git/commits",
            {"message": message, "tree": tree["sha"], "parents": [base_sha]},
        )
        await self._request(
            "PATCH",
            f"/repos/{self._repo}/git/refs/heads/{branch}",
            {"sha": new_commit["sha"]},
        )
        return new_commit["sha"]

    async def create_pr(
        self,
        branch: str,
        title: str,
        body: str = "",
        base: str = "main",
    ) -> str:
        """PR を作成し、URL を返す。"""
        pr = await self._request(
            "POST",
            f"/repos/{self._repo}/pulls",
            {"title": title, "head": branch, "base": base, "body": body},
        )
        return pr["html_url"]

    async def get_file_content(self, path: str, ref: str = "main") -> str | None:
        """リポジトリ内のファイル内容を取得（存在しなければ None）"""
        try:
            data = await self._request(
                "GET", f"/repos/{self._repo}/contents/{path}?ref={ref}"
            )
            import base64
            return base64.b64decode(data["content"]).decode("utf-8")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
