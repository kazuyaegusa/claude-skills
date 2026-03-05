"""汎用 Webhook サーバー（HMAC 署名検証付き）"""
from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
from typing import Any, Awaitable, Callable

from aiohttp import web

logger = logging.getLogger(__name__)


class WebhookServer:
    """HMAC 署名検証付きの汎用 Webhook 受信サーバー"""

    def __init__(
        self,
        secret: str = "",
        port: int = 8000,
        signature_header: str = "X-Signature",
    ) -> None:
        self._secret = secret
        self._port = port
        self._signature_header = signature_header
        self._handlers: dict[str, Callable[[dict[str, Any]], Awaitable[None]]] = {}
        self.app = web.Application()
        self.app.router.add_post("/webhook", self._handle)
        self.app.router.add_get("/health", self._health)

    def on_event(
        self, event_type: str
    ) -> Callable[
        [Callable[[dict[str, Any]], Awaitable[None]]],
        Callable[[dict[str, Any]], Awaitable[None]],
    ]:
        """イベントタイプごとのハンドラを登録するデコレータ"""
        def decorator(
            func: Callable[[dict[str, Any]], Awaitable[None]]
        ) -> Callable[[dict[str, Any]], Awaitable[None]]:
            self._handlers[event_type] = func
            return func
        return decorator

    def verify_signature(self, body: bytes, signature: str) -> bool:
        if not self._secret:
            return True
        expected = hmac.new(
            self._secret.encode(), body, hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, signature)

    async def _handle(self, request: web.Request) -> web.Response:
        body = await request.read()
        signature = request.headers.get(self._signature_header, "")
        if not self.verify_signature(body, signature):
            return web.Response(status=401, text="Invalid signature")

        payload = json.loads(body)
        event_type = payload.get("type", payload.get("event", "unknown"))

        handler = self._handlers.get(event_type)
        if handler:
            import asyncio
            asyncio.create_task(handler(payload))
            logger.info(f"Event '{event_type}' dispatched")
        else:
            logger.debug(f"No handler for event type: {event_type}")

        return web.Response(status=200, text="OK")

    async def _health(self, _: web.Request) -> web.Response:
        return web.json_response({"status": "ok"})

    def run(self) -> None:
        """サーバーを起動"""
        logger.info(f"Webhook server starting on port {self._port}")
        web.run_app(self.app, port=self._port)
