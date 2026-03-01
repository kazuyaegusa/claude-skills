---
name: JAX Transformer Ranker
description: JAX/FlaxによるTransformerスコアリングモデルの実装テンプレート
tools: [Read, Edit, Write, Bash]
---

# JAX Transformer Ranker

JAX/Flaxを使ったTransformerベースのスコアリング・ランキングモデルを構築するスキル。

## ユースケース

- コンテンツランキング（推薦、検索結果の並び替え）
- ペアワイズ/リストワイズのスコアリング
- 特徴量ベクトルの集合に対するattention集約

## コマンド例

```
/jax-transformer-ranker  # ランキングモデルのテンプレートを生成
```

## 依存パッケージ

- `jax[cpu]>=0.4.20`（GPU使用時は`jax[cuda12]`）
- `flax>=0.8.0`
- `optax>=0.1.7`
- `numpy>=1.24.0`

## アーキテクチャ

1. 入力射影: `(batch, seq, feature_dim)` → `(batch, seq, d_model)`
2. 学習可能な位置エンコーディング
3. N層のTransformerブロック（Multi-Head Self-Attention + FFN + LayerNorm + Residual）
4. 出力ヘッド: `(batch, seq, d_model)` → `(batch, seq)` スコア

## 使い方

```python
from ranking_transformer import RankingTransformer, Ranker

ranker = Ranker(feature_dim=96, max_candidates=200)
scores = ranker.score(features)  # (num_candidates,)
loss = ranker.train_step(features, labels)
```

## カスタマイズポイント

- `d_model`: モデル次元（デフォルト64）
- `num_layers`: Transformer層数（デフォルト3）
- `num_heads`: Attention ヘッド数（デフォルト4）
- `ff_dim`: FFN中間次元（デフォルト`d_model * 4`）
- 損失関数: デフォルトはbinary cross-entropy。listwise softmax等に変更可能

## 注意事項

- JAXは初回JITコンパイルに時間がかかる
- `max_candidates`を変えるとパラメータ再初期化が必要（位置エンコーディングのサイズ依存）
- GPU使用時は`jax[cuda12]`をインストールすること