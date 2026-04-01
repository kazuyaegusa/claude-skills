# HuggingFace Hubからチェックポイントを読み込んで推論する

> 学習済みIrodori-TTSモデルをHuggingFace Hubから取得し、CLI/Gradioで推論実行する

- 出典: https://x.com/yusuke_kizuna/status/2034831421937000907
- 投稿者: ゆうすけ
- カテゴリ: dev-tool

## なぜ使うのか

自前学習せずに高品質TTSをすぐ利用でき、カスタマイズのベースラインとして使える

## いつ使うのか

Irodori-TTSを試したい時。自分のデータでfine-tuningする前のベースライン評価

### 具体的な適用場面

- 音声クローニングが必要なコンテンツ生成（ナレーション、キャラクター音声）
- 感情・イントネーション表現が重要な対話システム
- 48kHz高品質音声が必要な商用アプリケーション
- Echo-TTS系モデルをローカルで学習・カスタマイズしたい研究者

## やり方

1. `git clone https://github.com/Aratako/Irodori-TTS.git && cd Irodori-TTS` 2. `uv sync` で依存インストール 3. HuggingFace Hubから `Aratako/Irodori-TTS-500M` をダウンロード（自動または手動） 4. CLI推論: `uv run python inference.py --text "こんにちは" --ref_audio ref.wav --output out.wav` 5. Gradio UI: `uv run python app.py` でブラウザ起動

### 入力

- テキスト文字列
- 参照音声ファイル（話者・スタイル指定用）

### 出力

- 合成音声ファイル（48kHz WAV）

## 使うツール・ライブラリ

- uv (Python環境管理)
- HuggingFace Hub
- Gradio

## コード例

```
# CLI推論例
uv run python inference.py \
  --text "これはテストです" \
  --ref_audio ./samples/ref.wav \
  --output ./output.wav \
  --checkpoint Aratako/Irodori-TTS-500M
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
