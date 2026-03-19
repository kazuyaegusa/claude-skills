# クローズドループ学習によるスキル自動生成・改善

> 複雑なタスク完了後にエージェントが自律的にスキル（手続き的記憶）を生成し、使用中に改善し、定期的なナッジで知識を永続化する

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

人間が手動でナレッジベースを整備するのは非効率で継続困難。エージェント自身が経験から学習しスキルを蓄積すれば、時間とともに賢くなり、同様のタスクで再利用可能な知識が自動で増える

## いつ使うのか

同種のタスクを繰り返し実行する運用環境や、エージェントのナレッジベースを人手なしで成長させたいとき

## やり方

1. 複雑なタスクを実行する
2. タスク完了後、エージェントが自動でスキルを生成（agentskills.io標準準拠）
3. スキル使用時、実行結果をもとに自己改善
4. 定期的なナッジでエージェント自身が重要な知識を記憶へ永続化
5. FTS5全文検索でセッション間の過去会話を検索し、LLM要約で関連知識を参照
6. Honcho dialectic user modelingでユーザーモデルをセッション間で深化

### 入力

- 複雑なタスク実行履歴
- ツール呼び出し軌跡
- 会話ログ

### 出力

- 自動生成されたスキル定義（agentskills.io互換）
- 改善されたスキル
- FTS5検索可能なセッションデータベース
- ユーザーモデル（Honcho）

## 使うツール・ライブラリ

- Hermes Agent skill system
- FTS5 (SQLite full-text search)
- Honcho (plastic-labs/honcho)
- agentskills.io standard

## 前提知識

- Linux/macOS/WSL2環境（Windows nativeは非対応）
- git
- LLMプロバイダーAPIキー（OpenRouter/OpenAI/Anthropic/Kimi/MiniMax等のいずれか）
- Python 3.11+ (インストーラーが自動セットアップ)
- Node.js (インストーラーが自動セットアップ)
- Telegram/Discord等のBot Token（メッセージングゲートウェイ利用時）
- Daytona/Modalアカウント（サーバーレス利用時、オプション）

## 根拠

> 「Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling. Compatible with the agentskills.io open standard.」

> 「curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash」
