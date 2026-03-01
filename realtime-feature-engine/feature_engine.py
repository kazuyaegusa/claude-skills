"""時間減衰付きリアルタイム特徴量エンジン"""
from __future__ import annotations

import time
from collections import defaultdict
from dataclasses import dataclass, field

import numpy as np


@dataclass
class EngagementEvent:
    """エンゲージメントイベント"""
    entity_id: str
    item_id: int
    event_type: str
    timestamp: float = field(default_factory=time.time)
    metadata: dict = field(default_factory=dict)


class FeatureEngine:
    """時間減衰付きリアルタイム特徴量集計エンジン

    Args:
        feature_dim: 出力特徴量の次元数
        decay_half_life: 減衰の半減期（秒）
        event_weights: イベント種別ごとの重み
        max_events_per_entity: エンティティあたりの最大イベント保持数
        seed: 乱数シード
    """

    DEFAULT_WEIGHTS: dict[str, float] = {
        "click": 1.0,
        "like": 1.0,
        "share": 2.0,
        "comment": 3.0,
        "impression": 0.1,
        "dwell": 0.5,
    }

    def __init__(
        self,
        feature_dim: int = 32,
        decay_half_life: float = 3600.0,
        event_weights: dict[str, float] | None = None,
        max_events_per_entity: int = 500,
        seed: int = 42,
    ) -> None:
        self.feature_dim = feature_dim
        self.decay_half_life = decay_half_life
        self.event_weights = event_weights or self.DEFAULT_WEIGHTS
        self.max_events = max_events_per_entity
        self._entity_events: dict[str, list[EngagementEvent]] = defaultdict(list)
        self._item_events: dict[int, list[EngagementEvent]] = defaultdict(list)
        self._entity_embeddings: dict[str, np.ndarray] = {}
        self._rng = np.random.default_rng(seed)

    def ingest(self, event: EngagementEvent) -> None:
        """イベントを取り込む"""
        events = self._entity_events[event.entity_id]
        events.append(event)
        if len(events) > self.max_events:
            self._entity_events[event.entity_id] = events[-self.max_events:]

        items = self._item_events[event.item_id]
        items.append(event)
        if len(items) > self.max_events:
            self._item_events[event.item_id] = items[-self.max_events:]

    def ingest_batch(self, events: list[EngagementEvent]) -> None:
        """バッチ取り込み"""
        for event in events:
            self.ingest(event)

    def _time_decay(self, elapsed: float) -> float:
        return 2.0 ** (-elapsed / self.decay_half_life)

    def entity_features(self, entity_id: str) -> np.ndarray:
        """エンティティの集計特徴量ベクトル"""
        events = self._entity_events.get(entity_id, [])
        base = self._get_or_create_embedding(entity_id)
        if not events:
            return base

        now = time.time()
        weight_keys = list(self.event_weights.keys())
        type_scores = np.zeros(len(weight_keys))
        for ev in events[-self.max_events:]:
            w = self.event_weights.get(ev.event_type, 0.1)
            decay = self._time_decay(now - ev.timestamp)
            if ev.event_type in weight_keys:
                idx = weight_keys.index(ev.event_type)
                type_scores[idx] += w * decay

        stats = np.zeros(self.feature_dim, dtype=np.float32)
        stats[:len(type_scores)] = type_scores / (type_scores.sum() + 1e-8)
        return (base + stats * 0.3).astype(np.float32)

    def item_features(self, item_id: int) -> np.ndarray:
        """アイテムの集計特徴量ベクトル"""
        events = self._item_events.get(item_id, [])
        feat = np.zeros(self.feature_dim, dtype=np.float32)
        if not events:
            return feat

        now = time.time()
        for ev in events[-self.max_events:]:
            w = self.event_weights.get(ev.event_type, 0.1)
            decay = self._time_decay(now - ev.timestamp)
            idx = hash(ev.entity_id) % self.feature_dim
            feat[idx] += w * decay

        norm = np.linalg.norm(feat) + 1e-8
        return feat / norm

    def pair_features(self, entity_id: str, item_id: int) -> np.ndarray:
        """エンティティ×アイテムの組み合わせ特徴量"""
        u = self.entity_features(entity_id)
        t = self.item_features(item_id)
        cross = u * t
        return np.concatenate([u, t, cross]).astype(np.float32)

    def _get_or_create_embedding(self, entity_id: str) -> np.ndarray:
        if entity_id not in self._entity_embeddings:
            self._entity_embeddings[entity_id] = (
                self._rng.standard_normal(self.feature_dim).astype(np.float32) * 0.1
            )
        return self._entity_embeddings[entity_id]
