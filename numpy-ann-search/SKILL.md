---
name: NumPy ANN Search
description: LSH(Locality-Sensitive Hashing)ベースの近似最近傍探索をNumPyのみで実装するスキル
tools: [Read, Edit, Write, Bash]
---

# NumPy ANN Search

FAISS等の外部ライブラリなしで近似最近傍探索を実装するスキル。

## ユースケース

- embedding類似検索（ユーザー推薦、文書検索、画像検索）
- プロトタイプ段階でFAISS依存を避けたい場合
- 小〜中規模データ（〜100万件）の類似検索

## コマンド例

```
/numpy-ann-search  # 現在のプロジェクトにANNインデックスを追加
```

## 依存パッケージ

- `numpy>=1.24.0`

## アルゴリズム

1. 複数のランダム射影行列でハッシュテーブルを構築（LSH）
2. クエリ時は各テーブルのバケットから候補を収集
3. 候補に対してコサイン類似度で正確なスコアリング
4. 候補が空の場合は全探索にフォールバック

## パラメータガイド

| パラメータ | デフォルト | 用途 |
|-----------|-----------|------|
| `dim` | 32 | embedding次元数 |
| `num_tables` | 8 | ハッシュテーブル数（多いほど再現率↑、メモリ↑） |
| `num_bits` | 12 | ハッシュビット数（多いほど精度↑、候補数↓） |

## 使い方

```python
from ann_index import ANNIndex

index = ANNIndex(dim=128, num_tables=10, num_bits=16)
index.add(item_id=1, vector=embedding)
results = index.query(query_vector, k=50)  # [(id, similarity), ...]
```

## 注意事項

- 100万件超のデータにはFAISS/ScaNN等の専用ライブラリを推奨
- `num_tables`を増やすとメモリ使用量が線形に増加
- スレッドセーフではない。並行書き込みにはロックが必要