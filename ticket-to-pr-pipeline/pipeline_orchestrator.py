"""チケット → コード生成 → PR 作成パイプライン"""
from __future__ import annotations

import logging
import os
import re
from typing import Any, Protocol

logger = logging.getLogger(__name__)


class TicketClient(Protocol):
    """チケット管理システムのインターフェース"""

    async def get_issue(self, issue_id: str) -> dict[str, Any]: ...
    async def add_comment(self, issue_id: str, body: str) -> None: ...


class PRClient(Protocol):
    """PR 作成システムのインターフェース"""

    async def create_branch(self, branch_name: str, base: str = "main") -> str: ...
    async def commit_files(
        self, branch: str, files: list[dict[str, str]], message: str
    ) -> str: ...
    async def create_pr(
        self, branch: str, title: str, body: str, base: str = "main"
    ) -> str: ...


class CodeGeneratorProtocol(Protocol):
    def generate(
        self, title: str, description: str, context: str = ""
    ) -> list[dict[str, str]]: ...


class PipelineOrchestrator:
    """チケット → AI コード生成 → PR 作成のパイプライン"""

    def __init__(
        self,
        ticket_client: TicketClient,
        pr_client: PRClient,
        code_generator: CodeGeneratorProtocol,
        branch_prefix: str = "auto",
    ) -> None:
        self.ticket = ticket_client
        self.pr = pr_client
        self.codegen = code_generator
        self.branch_prefix = branch_prefix

    async def handle_issue(self, issue_id: str) -> str | None:
        """チケットを処理し、PR URL を返す（失敗時は None）"""
        issue = await self.ticket.get_issue(issue_id)
        identifier = issue.get("identifier", issue_id[:8])
        title = issue.get("title", "untitled")
        description = issue.get("description", "")

        logger.info(f"Processing: {identifier} - {title}")

        # ブランチ名生成
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:40]
        branch = f"{self.branch_prefix}/{identifier}-{slug}"

        # コード生成
        await self.ticket.add_comment(issue_id, "🤖 コード生成を開始しました...")
        try:
            files = self.codegen.generate(title=title, description=description)
        except Exception as e:
            await self.ticket.add_comment(issue_id, f"❌ コード生成失敗: {e}")
            logger.error(f"Code generation failed: {e}")
            return None

        if not files:
            await self.ticket.add_comment(issue_id, "⚠️ 生成されたファイルがありません")
            return None

        # GitHub 操作
        try:
            await self.pr.create_branch(branch)
            commit_msg = f"feat: {identifier} {title}"
            await self.pr.commit_files(branch, files, commit_msg)

            file_list = "\n".join(f"- `{f['path']}`" for f in files)
            pr_body = (
                f"## {identifier}: {title}\n\n"
                f"{description or 'No description'}\n\n"
                f"### Generated Files\n{file_list}\n\n"
                f"---\n🤖 Auto-generated"
            )
            pr_url = await self.pr.create_pr(
                branch=branch,
                title=f"{identifier}: {title}",
                body=pr_body,
            )
        except Exception as e:
            await self.ticket.add_comment(issue_id, f"❌ PR 作成失敗: {e}")
            logger.error(f"PR creation failed: {e}")
            return None

        await self.ticket.add_comment(
            issue_id,
            f"✅ PR 作成完了: [{branch}]({pr_url})\n\n変更ファイル:\n{file_list}",
        )
        logger.info(f"PR created: {pr_url}")
        return pr_url
