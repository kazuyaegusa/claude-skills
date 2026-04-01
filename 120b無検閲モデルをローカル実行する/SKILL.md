# 120B無検閲モデルをローカル実行する

> GPTOSS-120B-Uncensoredモデルをダウンロードし、ローカル環境で推論実行する

- 出典: https://x.com/huggingmodels/status/2035514556722925995
- 投稿者: Hugging Models
- カテゴリ: other

## なぜ使うのか

クラウドAPIの利用規約や検閲機構に制約されず、研究・創作で完全な表現の自由を確保するため

## いつ使うのか

商用LLM APIの利用規約で禁止されるクエリを扱う必要がある時、またはプライバシー上の理由でクラウドに送信できないデータを処理する時

### 具体的な適用場面

- 倫理的に曖昧だが学術的に重要な研究トピック（セキュリティ脆弱性分析、法律グレーゾーン、医療シミュレーション等）でLLMを使いたい場合
- 創作活動（小説、ゲームシナリオ、映画脚本等）で表現の自由を最大化したい場合
- 既存のフィルタリング機構が過剰反応して正当なクエリまでブロックされる問題を回避したい場合
- プライバシー重視でローカル環境で大規模LLMを動かしたいが、クラウドAPIの検閲を避けたい場合

## やり方

1. Hugging Face等からGPTOSS-120B-Uncensoredのモデルウェイトをダウンロード（要十分なストレージ、~240GB想定） 2. vLLM、llama.cpp、text-generation-webui等の推論エンジンをインストール 3. GPUメモリ要件を確認（A100 80GB×2台以上、またはQuantization適用） 4. `vllm serve GPTOSS-120B-Uncensored --tensor-parallel-size 2` のようにモデルをロード 5. OpenAI互換APIエンドポイント経由またはCLIで推論実行

### 入力

- 120B規模のモデルウェイトを保存できるストレージ（~240GB）
- 高性能GPU（A100 80GB×2台以上推奨、またはQuantization利用）
- 推論エンジン（vLLM/llama.cpp/text-generation-webui等）
- 推論対象のプロンプト

### 出力

- 検閲フィルタなしのLLM応答
- ローカルで完結した推論結果

## 使うツール・ライブラリ

- GPTOSS-120B-Uncensored
- vLLM
- llama.cpp
- text-generation-webui
- Hugging Face Transformers

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
