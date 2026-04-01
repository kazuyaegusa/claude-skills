# 大規模モデルのQuantizationで推論可能にする

> 120Bモデルを4bit/8bit量子化して、より少ないGPUメモリで動作させる

- 出典: https://x.com/huggingmodels/status/2035514556722925995
- 投稿者: Hugging Models
- カテゴリ: other

## なぜ使うのか

120B FP16モデルは~240GB必要だが、量子化により60GB以下（4bit時）に圧縮でき、A100 1台やRTX 4090等の民生GPUでも推論可能になるため

## いつ使うのか

GPU予算が限られているが大規模無検閲モデルを使いたい時、または推論速度を優先したい時

### 具体的な適用場面

- 倫理的に曖昧だが学術的に重要な研究トピック（セキュリティ脆弱性分析、法律グレーゾーン、医療シミュレーション等）でLLMを使いたい場合
- 創作活動（小説、ゲームシナリオ、映画脚本等）で表現の自由を最大化したい場合
- 既存のフィルタリング機構が過剰反応して正当なクエリまでブロックされる問題を回避したい場合
- プライバシー重視でローカル環境で大規模LLMを動かしたいが、クラウドAPIの検閲を避けたい場合

## やり方

1. GPTQ、AWQ、bitsandbytes等の量子化ライブラリを選択 2. `auto-gptq`等で事前量子化されたウェイトをダウンロード、または自分で量子化実行 3. llama.cppなら `-ngl 64 -c 4096` のようなオプションでGPUオフロード設定 4. vLLMなら `--quantization awq` オプション指定 5. 推論速度・品質のトレードオフを確認しながらbit数調整

### 入力

- 量子化前のFP16モデルまたは量子化済みウェイト
- 量子化ライブラリ（GPTQ/AWQ/bitsandbytes）
- 60GB程度のGPUメモリ（4bit時）

### 出力

- メモリ使用量を1/4〜1/2に削減したモデル
- 推論速度向上（場合により）
- 若干の品質劣化（通常は許容範囲）

## 使うツール・ライブラリ

- auto-gptq
- AutoAWQ
- bitsandbytes
- llama.cpp
- vLLM

## コード例

```
# vLLM + AWQ quantization
vllm serve GPTOSS-120B-Uncensored-AWQ --quantization awq --tensor-parallel-size 1

# llama.cpp
./main -m gptoss-120b-uncensored.Q4_K_M.gguf -ngl 64 -c 4096 -p "Your prompt"
```

## 前提知識

- LLMの基本的な仕組み（パラメータ数、推論、ガードレールの概念）
- GPUメモリ要件とモデルサイズの関係（FP16で1Bパラメータ≒2GB）
- 量子化の基礎知識（4bit/8bit、精度とメモリのトレードオフ）
- 推論エンジン（vLLM、llama.cpp等）の基本的な使い方
- 無検閲モデルの法的・倫理的リスク理解（悪用厳禁）

## 根拠

> Meet GPTOSS-120B-Uncensored: a massive 120B parameter model that's completely uncensored.

> This open-source powerhouse is designed for raw, unfiltered AI interactions.

> It's causing buzz because it removes guardrails while maintaining high-quality outputs.
