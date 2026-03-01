---
name: Realtime Feature Engine
description: イベントストリームから時間減衰付き特徴量をリアルタイム集計するエンジン
tools: [Read, Edit, Write, Bash]
---

# Realtime Feature Engine

ユーザーアクションやイベントストリームから、時間減衰（exponential decay）付きの特徴量ベクトルをリアルタイム生成するスキル。

## ユースケース

- 推薦システムのユーザー/アイテム特徴量
- リアルタイムスコアリング（広告、コンテンツランキング）
- ユーザー行動分析のオンライン特徴量

## コマンド例

```
/realtime-feature-engine  # 特徴量エンジンのテンプレートを生成
```

## 依存パッケージ

- `numpy>=1.24.0`

## 設計パターン

1. **イベント取り込み**: 型付きイベント（like, click, view等）を蓄積
2. **時間減衰**: 半減期ベースの指数減衰で古いイベントの影響を低減
3. **エンティティ特徴量**: ユーザー/アイテム単体の集計特徴量
4. **ペア特徴量**: ユーザー×アイテムのelement-wise interaction

## 使い方

```python
from feature_engine import FeatureEngine, EngagementEvent

engine = FeatureEngine(feature_dim=64, decay_half_life=1800.0)
engine.ingest(EngagementEvent(entity_id="user_1", item_id=42, event_type="click"))

user_feat = engine.entity_features("user_1")     # (64,)
item_feat = engine.item_features(42)               # (64,)
pair_feat = engine.pair_features("user_1", 42)     # (192,) = user + item + cross
```

## カスタマイズポイント

- `event_weights`: イベント種別ごとの重み
- `decay_half_life`: 減衰の半減期（秒）
- `feature_dim`: 出力特徴量の次元数
- `max_events_per_entity`: メモリ制限用の最大イベント保持数

## 注意事項

- インメモリ実装のため、大規模データにはRedis等の外部ストアを検討
- スレッドセーフではない。並行アクセスにはロックが必要
- `max_events_per_entity`で古いイベントを自動切り捨て