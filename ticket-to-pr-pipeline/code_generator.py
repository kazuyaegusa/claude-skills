"""AI コード生成モジュール（LLM プロバイダ差し替え可能）"""
from __future__ import annotations

import json
import os
from abc import ABC, abstractmethod


class CodeGenerator(ABC):
    """コード生成の抽象基底クラス"""

    @abstractmethod
    def generate(
        self,
        title: str,
        description: str,
        context: str = "",
    ) -> list[dict[str, str]]:
        """チケット情報からファイル変更リストを生成

        Returns:
            [{"path": "relative/path", "content": "file content"}, ...]
        """
        ...


class OpenAICodeGenerator(CodeGenerator):
    """OpenAI Responses API を使ったコード生成"""

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
    ) -> None:
        from openai import OpenAI

        key = api_key or os.getenv("OPENAI_API_KEY", "")
        if not key:
            raise ValueError("OPENAI_API_KEY が未設定です")
        self._client = OpenAI(api_key=key)
        self._model = model or os.getenv("CODEX_MODEL", "o4-mini")

    def generate(
        self,
        title: str,
        description: str,
        context: str = "",
    ) -> list[dict[str, str]]:
        system_prompt = (
            "You are a senior software engineer. Given a ticket, "
            "generate the implementation code. Return a JSON array of file changes:\n"
            '[{"path": "relative/file/path", "content": "full file content"}]\n'
            "Only output valid JSON. No explanation."
        )
        user_prompt = f"## Ticket: {title}\n\n{description or 'No description'}"
        if context:
            user_prompt += f"\n\n## Context\n{context}"

        response = self._client.responses.create(
            model=self._model,
            instructions=system_prompt,
            input=user_prompt,
        )
        raw = response.output_text.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1].rsplit("```", 1)[0]
        return json.loads(raw)
