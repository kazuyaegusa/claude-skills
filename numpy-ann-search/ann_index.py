"""LSH(Locality-Sensitive Hashing)ベースの近似最近傍探索インデックス"""
from __future__ import annotations

import numpy as np


class ANNIndex:
    """LSHベースの近似最近傍インデックス

    Args:
        dim: ベクトル次元数
        num_tables: ハッシュテーブル数（多いほど再現率↑）
        num_bits: ハッシュビット数（多いほど精度↑）
        seed: 乱数シード
    """

    def __init__(
        self,
        dim: int = 32,
        num_tables: int = 8,
        num_bits: int = 12,
        seed: int = 0,
    ) -> None:
        self.dim = dim
        self.num_tables = num_tables
        self.num_bits = num_bits
        self._rng = np.random.default_rng(seed)
        self._projections = [
            self._rng.standard_normal((num_bits, dim)).astype(np.float32)
            for _ in range(num_tables)
        ]
        self._tables: list[dict[int, list[int]]] = [
            {} for _ in range(num_tables)
        ]
        self._vectors: dict[int, np.ndarray] = {}

    def _hash(self, vec: np.ndarray, table_idx: int) -> int:
        projected = self._projections[table_idx] @ vec
        bits = (projected > 0).astype(int)
        return int(bits.dot(1 << np.arange(self.num_bits)))

    def add(self, item_id: int, vector: np.ndarray) -> None:
        """1件追加"""
        self._vectors[item_id] = vector.astype(np.float32)
        for i in range(self.num_tables):
            h = self._hash(vector, i)
            self._tables[i].setdefault(h, []).append(item_id)

    def add_batch(self, item_ids: list[int], vectors: np.ndarray) -> None:
        """バッチ追加"""
        for item_id, vec in zip(item_ids, vectors):
            self.add(item_id, vec)

    def query(self, vector: np.ndarray, k: int = 100) -> list[tuple[int, float]]:
        """近似k近傍を返す: list of (item_id, cosine_similarity)"""
        candidates: set[int] = set()
        for i in range(self.num_tables):
            h = self._hash(vector, i)
            candidates.update(self._tables[i].get(h, []))

        if not candidates:
            candidates = set(self._vectors.keys())

        vec_norm = vector / (np.linalg.norm(vector) + 1e-8)
        scored: list[tuple[int, float]] = []
        for cid in candidates:
            cv = self._vectors[cid]
            cv_norm = cv / (np.linalg.norm(cv) + 1e-8)
            scored.append((cid, float(np.dot(vec_norm, cv_norm))))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]

    def remove(self, item_id: int) -> None:
        """アイテム削除"""
        if item_id not in self._vectors:
            return
        vec = self._vectors.pop(item_id)
        for i in range(self.num_tables):
            h = self._hash(vec, i)
            bucket = self._tables[i].get(h, [])
            if item_id in bucket:
                bucket.remove(item_id)

    def __len__(self) -> int:
        return len(self._vectors)
