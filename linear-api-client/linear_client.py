"""Linear GraphQL API 汎用クライアント"""
from __future__ import annotations

import os
from typing import Any

import httpx

GRAPHQL_URL = "https://api.linear.app/graphql"


class LinearClient:
    """Linear GraphQL API の非同期クライアント"""

    def __init__(self, api_key: str | None = None) -> None:
        key = api_key or os.getenv("LINEAR_API_KEY", "")
        if not key:
            raise ValueError("LINEAR_API_KEY が未設定です")
        self._headers = {
            "Authorization": key,
            "Content-Type": "application/json",
        }

    async def query(self, query: str, variables: dict[str, Any] | None = None) -> dict:
        """任意の GraphQL クエリを実行"""
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                GRAPHQL_URL,
                json={"query": query, "variables": variables or {}},
                headers=self._headers,
            )
            resp.raise_for_status()
            data = resp.json()
            if "errors" in data:
                raise RuntimeError(f"GraphQL errors: {data['errors']}")
            return data["data"]

    async def get_issue(self, issue_id: str) -> dict:
        """Issue の詳細を取得"""
        data = await self.query(
            """
            query($id: String!) {
                issue(id: $id) {
                    id
                    identifier
                    title
                    description
                    priority
                    state { id name }
                    labels { nodes { name } }
                    project { name }
                    assignee { name email }
                }
            }
            """,
            {"id": issue_id},
        )
        return data["issue"]

    async def list_issues(
        self,
        team_id: str | None = None,
        state_filter: str | None = None,
        limit: int = 50,
    ) -> list[dict]:
        """Issue 一覧を取得（フィルタ付き）"""
        filters: list[str] = []
        variables: dict[str, Any] = {"first": limit}
        if team_id:
            filters.append('team: { id: { eq: $teamId } }')
            variables["teamId"] = team_id
        if state_filter:
            filters.append('state: { name: { eq: $stateName } }')
            variables["stateName"] = state_filter

        filter_clause = f'filter: {{ {" ".join(filters)} }}' if filters else ""

        # 動的変数宣言の構築
        var_decls = ["$first: Int!"]
        if team_id:
            var_decls.append("$teamId: String!")
        if state_filter:
            var_decls.append("$stateName: String!")
        var_str = ", ".join(var_decls)

        data = await self.query(
            f"""
            query({var_str}) {{
                issues(first: $first, {filter_clause}) {{
                    nodes {{
                        id
                        identifier
                        title
                        state {{ name }}
                        priority
                        assignee {{ name }}
                    }}
                }}
            }}
            """,
            variables,
        )
        return data["issues"]["nodes"]

    async def update_issue_state(self, issue_id: str, state_id: str) -> None:
        """Issue のステートを更新"""
        await self.query(
            """
            mutation($id: String!, $stateId: String!) {
                issueUpdate(id: $id, input: { stateId: $stateId }) {
                    success
                }
            }
            """,
            {"id": issue_id, "stateId": state_id},
        )

    async def add_comment(self, issue_id: str, body: str) -> None:
        """Issue にコメントを追加"""
        await self.query(
            """
            mutation($issueId: String!, $body: String!) {
                commentCreate(input: { issueId: $issueId, body: $body }) {
                    success
                }
            }
            """,
            {"issueId": issue_id, "body": body},
        )

    async def create_issue(
        self,
        team_id: str,
        title: str,
        description: str = "",
        priority: int = 0,
        label_ids: list[str] | None = None,
    ) -> dict:
        """新規 Issue を作成"""
        variables: dict[str, Any] = {
            "teamId": team_id,
            "title": title,
            "description": description,
            "priority": priority,
        }
        label_input = ""
        if label_ids:
            variables["labelIds"] = label_ids
            label_input = ", labelIds: $labelIds"

        data = await self.query(
            f"""
            mutation($teamId: String!, $title: String!, $description: String!, $priority: Int!{', $labelIds: [String!]' if label_ids else ''}) {{
                issueCreate(input: {{
                    teamId: $teamId
                    title: $title
                    description: $description
                    priority: $priority
                    {('labelIds: $labelIds' if label_ids else '')}
                }}) {{
                    success
                    issue {{
                        id
                        identifier
                        url
                    }}
                }}
            }}
            """,
            variables,
        )
        return data["issueCreate"]["issue"]
