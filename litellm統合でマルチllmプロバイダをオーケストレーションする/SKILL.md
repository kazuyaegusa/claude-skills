# LiteLLM統合でマルチLLMプロバイダをオーケストレーションする

> LiteLLMを使ってAnthropic、OpenAI、Gemini、Ollama等を統一インターフェースで扱い、自動フォールバック・コスト追跡・予算強制を実現

- 出典: https://github.com/gadievron/raptor
- 投稿者: gadievron
- カテゴリ: claude-code-workflow

## なぜ使うのか

複数LLMプロバイダを使い分けることで可用性向上・コスト最適化が可能。特にローカルOllama（無料だが品質低）とクラウドAPI（高品質だが有料）を使い分けたい。PydanticバリデーションでYAML設定の誤りを早期検出できる

## いつ使うのか

複数LLMプロバイダを使い分けたい時、コスト上限を厳守したい時、ローカルとクラウドAPIをフォールバック構成にしたい時

## やり方

1. litellm_config.yamlにmodel_listを定義（Anthropic、OpenAI、Gemini等）
2. LLMConfigでmax_cost_per_scanを設定して予算強制
3. LiteLLMが自動で最適なreasoning/thinkingモデルを選択
4. リアルタイムコールバックでトークン数・コスト・実行時間をログ
5. レート制限検出時にプロバイダ固有のガイダンスを表示

### 入力

- litellm_config.yaml（モデル定義）
- 環境変数（ANTHROPIC_API_KEY、OPENAI_API_KEY等）
- max_cost_per_scan（予算上限）

### 出力

- 統一されたLLMインターフェース
- リアルタイムコスト追跡
- 予算超過時のエラー

## 使うツール・ライブラリ

- LiteLLM
- Pydantic（YAML検証）

## コード例

```
# litellm_config.yaml
model_list:
  - model_name: claude-opus-4.5
    litellm_params:
      model: anthropic/claude-opus-4.5
      api_key: ${ANTHROPIC_API_KEY}
  - model_name: gpt-5.2-thinking
    litellm_params:
      model: openai/gpt-5.2-thinking
      api_key: ${OPENAI_API_KEY}

# Python
from packages.llm_analysis.llm.config import LLMConfig
config = LLMConfig(max_cost_per_scan=1.0)  # $1上限
```

## 前提知識

- Claude Codeの基本操作（コマンド、スキル、エージェントの概念）
- セキュリティツールの基礎知識（Semgrep、CodeQL、AFL、ペネトレーションテスト）
- LLMプロバイダのAPI認証（ANTHROPIC_API_KEY等）
- BigQuery認証（OSS Forensics使用時）
- Dockerまたはdevcontainer環境構築（オプション）
