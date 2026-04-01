# 事前学習LLM埋め込みをText Encoderに転移学習する

> TTSのText Encoderトークン埋め込みを、事前学習済みLLMの埋め込み層で初期化する

- 出典: https://x.com/yusuke_kizuna/status/2034831421937000907
- 投稿者: ゆうすけ
- カテゴリ: other

## なぜ使うのか

ゼロからの学習より言語理解が早期に獲得され、テキスト→音声のアライメント品質が向上する

## いつ使うのか

言語理解が重要なTTSタスク（多言語、文脈依存韻律）。学習データが限定的で、事前知識を活用したい場合

### 具体的な適用場面

- 音声クローニングが必要なコンテンツ生成（ナレーション、キャラクター音声）
- 感情・イントネーション表現が重要な対話システム
- 48kHz高品質音声が必要な商用アプリケーション
- Echo-TTS系モデルをローカルで学習・カスタマイズしたい研究者

## やり方

1. 事前学習LLM（例: LLaMA, GPT系）のトークン埋め込み層の重みを取得 2. Irodori-TTSのText Encoderの埋め込み層に代入 3. 残りのTransformer層（Self-Attention+SwiGLU）はランダム初期化またはLLM層で初期化 4. TTSタスクでfine-tuning

### 入力

- 事前学習LLMのトークン埋め込み重み
- TTSテキストトークン系列

### 出力

- 言語理解を持つテキスト特徴ベクトル

## 使うツール・ライブラリ

- HuggingFace Transformers
- PyTorch

## コード例

```
# 埋め込み転移の例（疑似コード）
from transformers import AutoModel
llm = AutoModel.from_pretrained('llama-2-7b')
text_encoder.embedding.weight.data = llm.get_input_embeddings().weight.data.clone()
```

## 前提知識

- Flow Matching / Diffusion Modelsの基礎
- Transformerアーキテクチャ（Self-Attention, RoPE, AdaLN）
- 音声コーデック（DAC, EnCodec）の仕組み
- PyTorch分散学習（torchrun, DDP）
- HuggingFace Hubの使い方

## 根拠

> 投稿: 「ちょっと意味が分からないぐらい表現力が高い」→ 音声品質の高さを示唆

> README: 「Flow Matching TTS: Rectified Flow Diffusion Transformer (RF-DiT) over continuous DACVAE latents」

> README: 「Zero-shot voice cloning from reference audio」

> README: 「Multi-GPU Training: Distributed training via `uv run torchrun` with gradient accumulation, mixed precision (bf16)」

> Architecture: 「Audio is represented as continuous latent sequences via the DACVAE codec (128-dim), enabling high-quality 48kHz waveform reconstruction」
