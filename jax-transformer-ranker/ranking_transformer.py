"""Transformerベースのスコアリングモデル（JAX/Flax実装）"""
from __future__ import annotations

import jax
import jax.numpy as jnp
import flax.linen as nn
import numpy as np
import optax


class MultiHeadSelfAttention(nn.Module):
    num_heads: int = 4
    head_dim: int = 16

    @nn.compact
    def __call__(self, x: jnp.ndarray, training: bool = False) -> jnp.ndarray:
        batch, seq_len, d_model = x.shape
        qkv = nn.Dense(3 * self.num_heads * self.head_dim)(x)
        qkv = qkv.reshape(batch, seq_len, 3, self.num_heads, self.head_dim)
        q, k, v = qkv[:, :, 0], qkv[:, :, 1], qkv[:, :, 2]
        q = q.transpose(0, 2, 1, 3)
        k = k.transpose(0, 2, 1, 3)
        v = v.transpose(0, 2, 1, 3)

        scale = jnp.sqrt(self.head_dim).astype(x.dtype)
        attn = jnp.matmul(q, k.transpose(0, 1, 3, 2)) / scale
        attn = nn.softmax(attn, axis=-1)
        if training:
            attn = nn.Dropout(rate=0.1, deterministic=False)(attn)

        out = jnp.matmul(attn, v)
        out = out.transpose(0, 2, 1, 3).reshape(batch, seq_len, self.num_heads * self.head_dim)
        return nn.Dense(d_model)(out)


class TransformerBlock(nn.Module):
    num_heads: int = 4
    head_dim: int = 16
    ff_dim: int = 128

    @nn.compact
    def __call__(self, x: jnp.ndarray, training: bool = False) -> jnp.ndarray:
        residual = x
        x = nn.LayerNorm()(x)
        x = MultiHeadSelfAttention(self.num_heads, self.head_dim)(x, training)
        x = x + residual

        residual = x
        x = nn.LayerNorm()(x)
        x = nn.Dense(self.ff_dim)(x)
        x = nn.gelu(x)
        x = nn.Dense(residual.shape[-1])(x)
        x = x + residual
        return x


class RankingTransformer(nn.Module):
    """Transformerベースのスコアリングモデル

    入力: (batch, num_candidates, feature_dim)
    出力: (batch, num_candidates) スコア
    """
    feature_dim: int = 96
    d_model: int = 64
    num_layers: int = 3
    num_heads: int = 4

    @nn.compact
    def __call__(self, x: jnp.ndarray, training: bool = False) -> jnp.ndarray:
        x = nn.Dense(self.d_model)(x)
        pos_emb = self.param(
            "pos_embedding",
            nn.initializers.normal(0.02),
            (1, x.shape[1], self.d_model),
        )
        x = x + pos_emb

        for _ in range(self.num_layers):
            x = TransformerBlock(
                num_heads=self.num_heads,
                head_dim=self.d_model // self.num_heads,
                ff_dim=self.d_model * 4,
            )(x, training)

        x = nn.LayerNorm()(x)
        return nn.Dense(1)(x).squeeze(-1)


class Ranker:
    """ランキングモデルのラッパー

    Args:
        feature_dim: 入力特徴量の次元数
        max_candidates: 最大候補数（パディング用）
        d_model: Transformerのモデル次元
        num_layers: Transformer層数
        num_heads: Attentionヘッド数
        learning_rate: 学習率
        seed: 乱数シード
    """

    def __init__(
        self,
        feature_dim: int = 96,
        max_candidates: int = 200,
        d_model: int = 64,
        num_layers: int = 3,
        num_heads: int = 4,
        learning_rate: float = 1e-3,
        seed: int = 42,
    ) -> None:
        self.feature_dim = feature_dim
        self.max_candidates = max_candidates
        self.model = RankingTransformer(
            feature_dim=feature_dim,
            d_model=d_model,
            num_layers=num_layers,
            num_heads=num_heads,
        )
        self.rng = jax.random.PRNGKey(seed)
        dummy = jnp.zeros((1, max_candidates, feature_dim))
        self.params = self.model.init(self.rng, dummy)
        self.optimizer = optax.adam(learning_rate)
        self.opt_state = self.optimizer.init(self.params)

    def score(self, features: np.ndarray) -> np.ndarray:
        """features: (num_candidates, feature_dim) → scores: (num_candidates,)"""
        x = jnp.array(features)[None, ...]
        pad_len = self.max_candidates - x.shape[1]
        if pad_len > 0:
            x = jnp.pad(x, ((0, 0), (0, pad_len), (0, 0)))
        scores = self.model.apply(self.params, x, training=False)
        return np.array(scores[0, : features.shape[0]])

    def train_step(self, features: np.ndarray, labels: np.ndarray) -> float:
        """1ステップ学習。labels: (num_candidates,)"""
        x = jnp.array(features)[None, ...]
        y = jnp.array(labels)[None, ...]
        pad_len = self.max_candidates - x.shape[1]
        if pad_len > 0:
            x = jnp.pad(x, ((0, 0), (0, pad_len), (0, 0)))
            y = jnp.pad(y, ((0, 0), (0, pad_len)))

        def loss_fn(params: dict) -> jnp.ndarray:
            scores = self.model.apply(params, x, training=True, rngs={"dropout": self.rng})
            return optax.sigmoid_binary_cross_entropy(scores, y).mean()

        loss, grads = jax.value_and_grad(loss_fn)(self.params)
        updates, self.opt_state = self.optimizer.update(grads, self.opt_state)
        self.params = optax.apply_updates(self.params, updates)
        self.rng = jax.random.split(self.rng)[0]
        return float(loss)
