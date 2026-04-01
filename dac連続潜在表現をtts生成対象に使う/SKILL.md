# DAC連続潜在表現をTTS生成対象に使う

> 離散コーデックではなくDACVAE（128次元連続ベクトル）をTTSの生成対象とし、波形再構築品質を向上させる

- 出典: https://x.com/yusuke_kizuna/status/2034831421937000907
- 投稿者: ゆうすけ
- カテゴリ: context-management

## なぜ使うのか

離散トークンは量子化誤差で表現力が制限される。連続潜在表現は韻律・感情の微細な変化を保持でき、48kHz高品質再構築が可能

## いつ使うのか

高品質音声合成が必要で、感情・韻律の細かい制御が求められる場合。EnCodec等の離散コーデックで表現力不足を感じた時

### 具体的な適用場面

- 音声クローニングが必要なコンテンツ生成（ナレーション、キャラクター音声）
- 感情・イントネーション表現が重要な対話システム
- 48kHz高品質音声が必要な商用アプリケーション
- Echo-TTS系モデルをローカルで学習・カスタマイズしたい研究者

## やり方

1. DACVAEエンコーダで音声を128次元連続潜在系列に変換 2. Flow Matching DiTでテキストから潜在系列を生成 3. DACVAEデコーダで48kHz波形に復元。学習時はDACVAE凍結し、DiTのみ最適化

### 入力

- テキスト（トークン系列）
- 参照音声（話者・スタイル情報源）
- 事前学習済みDACVAEモデル

### 出力

- 128次元連続潜在系列
- 48kHz高品質音声波形

## 使うツール・ライブラリ

- DACVAE (facebookresearch/dacvae)
- PyTorch
- HuggingFace Transformers

## コード例

```
# DACVAEエンコーダで潜在表現取得（推測）
latents = dacvae_encoder(audio)  # (B, T, 128)
# Flow Matching DiTで生成
predicted_latents = dit_model(text_tokens, ref_latents, timestep)
# デコードして波形復元
audio_out = dacvae_decoder(predicted_latents)
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
