# Rectified Flow Diffusion Transformerで音声潜在表現を生成する

> Flow Matchingベースの拡散Transformer（RF-DiT）を使い、テキストと参照音声から連続潜在系列を生成する

- 出典: https://x.com/yusuke_kizuna/status/2034831421937000907
- 投稿者: ゆうすけ
- カテゴリ: other

## なぜ使うのか

通常の拡散モデルより学習が安定し、サンプリングステップを削減できる。Transformerアーキテクチャで長文対応とスケーラビリティを確保

## いつ使うのか

ゼロショット音声クローニングが必要な場合。複数GPUで大規模TTSモデルを学習したい時

### 具体的な適用場面

- 音声クローニングが必要なコンテンツ生成（ナレーション、キャラクター音声）
- 感情・イントネーション表現が重要な対話システム
- 48kHz高品質音声が必要な商用アプリケーション
- Echo-TTS系モデルをローカルで学習・カスタマイズしたい研究者

## やり方

1. Text Encoder: 事前学習LLMの埋め込みを初期化、RoPE付きSelf-Attention+SwiGLU層でテキスト特徴抽出 2. Reference Latent Encoder: パッチ化した参照音声潜在をSelf-Attention+SwiGLUでエンコード 3. Diffusion Transformer: Joint-Attention DiTブロック、Low-Rank AdaLN（timestep条件付き）、half-RoPE、SwiGLU MLPで潜在系列生成。学習は `uv run torchrun` で分散、bf16混合精度、勾配累積

### 入力

- テキストトークン埋め込み
- 参照音声のDAC潜在表現
- タイムステップ（Flow Matching用）

### 出力

- 生成された音声潜在系列（128次元×T）

## 使うツール・ライブラリ

- PyTorch (torchrun)
- RoPE (Rotary Position Embedding)
- uv (パッケージ管理)

## コード例

```
# 学習起動例
uv run torchrun --nproc_per_node=4 train.py \
  --batch_size 8 \
  --grad_accum_steps 4 \
  --precision bf16 \
  --wandb_project irodori-tts
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
