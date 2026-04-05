# マジックワードによる機能自動適用

> プロンプトに`ultrawork`または`ulw`を含めるだけで、全ての最適化機能(並列エージェント、バックグラウンドタスク、継続強制等)を自動有効化

- 出典: https://github.com/code-yeongyu/oh-my-openagent
- 投稿者: code-yeongyu
- カテゴリ: agent-orchestration

## なぜ使うのか

ユーザーが複雑な設定や指示を書かなくても、キーワード一つで全機能が協調動作する。認知負荷を最小化

## いつ使うのか

複雑なタスクを簡潔に依頼したい場合、または設定を考えたくない場合

## やり方

1. ユーザーがプロンプトに`ultrawork`または`ulw`を含める
2. システムがキーワードを検出
3. プリセット最適化設定を自動適用(エージェント編成、並列実行、TODO強制等)
4. エージェントが自動的に構造分析→コンテキスト収集→実装→完遂まで実行

### 入力

- タスク説明 + `ultrawork`または`ulw`

### 出力

- 完遂されたタスク

## 使うツール・ライブラリ

- oh-my-opencode の ultrawork feature

## コード例

```
// プロンプト例
"ulw - Implement user authentication with OAuth2 and JWT"
```

## 前提知識

- OpenCodeまたはClaude Code等のLLMエージェント環境の基本理解
- 複数LLMサブスクリプション(推奨: Claude Pro, ChatGPT Plus, Gemini Advanced)
- コマンドライン操作の基礎知識
- JSONまたはJSONC設定ファイルの編集スキル
- エージェント型開発の概念(プロンプトエンジニアリング、コンテキスト管理等)
