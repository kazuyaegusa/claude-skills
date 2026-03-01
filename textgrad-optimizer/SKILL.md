---
title: TextGrad テキスト最適化
version: 1.0.0
author: auto-extracted
tags: [optimization, prompt-engineering, llm, textgrad]
---

# TextGrad テキスト最適化スキル

LLMのフィードバックを「テキスト勾配」として扱い、プロンプト・コード・文章を反復的に自動最適化する。
PyTorchの自動微分に着想を得た最適化ループ（評価→フィードバック→改善）を実行する。

## コマンド

```
/textgrad-optimizer <対象テキストファイル> [--criteria "評価基準"] [--steps 3]
```

## 使い方

1. 最適化対象のテキスト（プロンプト、コード、文章）を指定
2. 評価基準を自然言語で記述（省略時はデフォルト基準を使用）
3. 指定ステップ数だけ「評価→フィードバック生成→改善」を繰り返す
4. 各ステップの変更差分と最終結果を出力

## 最適化対象の例

- **プロンプト最適化**: LLMへの指示文を具体的・効果的に改善
- **コード改善**: 可読性・パフォーマンス・エラーハンドリングを反復改善
- **文章推敲**: ビジネス文書・技術文書の明確さ・簡潔さを向上

## 依存パッケージ

なし（`claude -p` を内部で使用）

## 実装パターン

```python
# 基本的な最適化ループ
for step in range(max_steps):
    feedback = evaluate(current_text, criteria)  # LLMで評価
    gradient = extract_improvements(feedback)      # 改善点を抽出
    current_text = apply_gradient(current_text, gradient)  # 改善を適用
```

## スクリプト実行

```bash
python3 ~/.claude/skills/textgrad-optimizer/textgrad_optimize.py \
  --input target.txt \
  --criteria "明確さ、具体性、実行可能性" \
  --steps 3 \
  --output optimized.txt
```

## 注意事項

- APIキーは環境変数 `ANTHROPIC_API_KEY` から取得（ハードコード禁止）
- 各ステップの差分を保存し、改悪を検知した場合はロールバック可能
- `--dry-run` で評価フィードバックのみ取得（テキスト変更なし）
