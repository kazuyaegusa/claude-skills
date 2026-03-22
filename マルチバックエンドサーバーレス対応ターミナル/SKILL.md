# マルチバックエンド・サーバーレス対応ターミナル

> local/Docker/SSH/Daytona/Singularity/Modalの6種類のターミナルバックエンドを切り替え可能にし、アイドル時休止・オンデマンド起動を実現

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

ノートPCだけで動かすとオフライン時使えず、常時稼働VMは月額コストが嵩む。サーバーレス環境で休止・起動を自動化すれば実質無料で常駐エージェントを運用できる

## いつ使うのか

個人開発で$5/月以下に抑えたいが24/7稼働エージェントが欲しい場合、またはGPUクラスタとVPSを状況で切り替えたい場合

## やり方

1. hermes model/hermes setup でバックエンドを選択
2. Daytona/Modal選択時はワークスペース休止API統合
3. メッセージ受信時にバックエンドを自動wake
4. アイドル時に自動sleep（コスト最小化）
5. 各バックエンドで統一インターフェース（ターミナル操作/ファイルアクセス）

### 入力

- バックエンド選択（CLI設定）
- 各バックエンドのAPI認証情報

### 出力

- 統一ターミナルインターフェース
- アイドル時の自動休止・起動

## 使うツール・ライブラリ

- Daytona
- Modal
- Docker
- SSH
- Singularity

## コード例

```
# バックエンド切り替え（conceptual）
hermes config set terminal_backend modal
# Modalサーバーレス起動例（conceptual）
@modal.cls(gpu="A100", idle_timeout=300)
class HermesBackend:
    def execute_command(self, cmd): ...
```

## 前提知識

- Linux/macOS/WSL2環境（Windowsネイティブ非対応）
- gitインストール済み
- AIエージェント・LLM基礎知識（tool calling, context window等）
- ターミナル操作の基本（bash, curl等）
- 各メッセージングプラットフォームのBot API取得方法（Telegram/Discord等）
- （サーバーレス利用時）Daytona/ModalアカウントとAPI認証
- （LLM利用）OpenRouter/OpenAI等のAPIキー

## 根拠

> 「Use any model you want — Nous Portal, OpenRouter (200+ models), z.ai/GLM, Kimi/Moonshot, MiniMax, OpenAI, or your own endpoint. Switch with hermes model — no code changes, no lock-in」

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」

> 「hermes claw migrate — Interactive migration (full preset) from OpenClaw」
