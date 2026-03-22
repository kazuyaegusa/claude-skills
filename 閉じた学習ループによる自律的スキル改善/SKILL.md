# 閉じた学習ループによる自律的スキル改善

> エージェントが複雑なタスク完了後に自動でスキルを生成し、使用中に改善し、定期的に記憶を永続化する仕組み

- 出典: https://github.com/NousResearch/hermes-agent
- 投稿者: NousResearch
- カテゴリ: agent-orchestration

## なぜ使うのか

人間が手動でプロンプトやスキルを更新する運用は持続しない。エージェント自身が経験から学習し続ける仕組みがないと、長期利用で陳腐化する

## いつ使うのか

エージェントを数週間〜数ヶ月単位で継続利用し、ユーザー固有の作業パターンに適応させたい場合

## やり方

1. 複雑タスク完了時に自動でスキルをagentskills.io標準形式で生成
2. スキル使用中にLLMが改善案を自己提案・適用
3. 定期的にエージェント自身にメモリ永続化を促すnudge機能
4. FTS5全文検索でセッション横断検索+LLM要約による文脈想起
5. Honcho dialecticでユーザーモデルを会話ごとに深化

### 入力

- タスク実行履歴
- ツール呼び出しトラジェクトリ
- 過去会話のFTS5インデックス

### 出力

- agentskills.io互換スキルファイル
- 改善されたスキルバージョン
- ユーザーモデル（Honcho形式）

## 使うツール・ライブラリ

- agentskills.io（オープン標準）
- Honcho（dialectic user modeling）
- FTS5（SQLite全文検索）

## コード例

```
# スキル自動生成のトリガー例（conceptual）
if task_complexity > threshold and task_success:
    skill = agent.create_skill_from_trajectory()
    agent.skills.save(skill)
# 改善ループ（conceptual）
if skill.usage_count > N:
    improvements = llm.suggest_skill_improvements(skill, recent_failures)
    skill.apply_improvements(improvements)
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

> 「Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. Honcho dialectic user modeling」
