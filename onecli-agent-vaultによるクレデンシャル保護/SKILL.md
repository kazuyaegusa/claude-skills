# OneCLI Agent Vaultによるクレデンシャル保護

> API keyをコンテナに渡さず、外向きリクエスト時にプロキシ層（OneCLI Agent Vault）がクレデンシャルを注入する

- 出典: https://github.com/qwibitai/nanoclaw
- 投稿者: qwibitai
- カテゴリ: agent-orchestration

## なぜ使うのか

コンテナ内にAPIキーを環境変数やファイルとして渡すと、Agentが意図せず漏洩させるリスクがある。プロキシ層で注入すればAgentはキーを保持せず、アクセスポリシーやレート制限も集中管理できる

## いつ使うのか

AI Agentに外部API（GitHub, AWS等）へのアクセスを許可したいが、クレデンシャル漏洩リスクを最小化したい時

## やり方

1. AgentからのHTTPリクエストをOneCLI Agent Vaultにルーティング
2. Vaultがリクエストを検証し、Agent IDに応じたクレデンシャルを注入
3. 外部APIへリクエストを転送
4. レスポンスをAgentに返す
5. Agentは生のAPIキーを扱わない

### 入力

- Agent ID
- 外向きHTTPリクエスト
- OneCLI Agent Vault設定

### 出力

- クレデンシャル注入済みリクエスト
- アクセスポリシー・レート制限の適用

## 使うツール・ライブラリ

- OneCLI Agent Vault

## コード例

```
// Agentはraw API keyを持たない
// 外向きリクエストはOneCLI Vaultを経由
// Vaultがリクエスト時にクレデンシャル注入
```

## 前提知識

- Claude Codeの基本的な使い方（スキル実行、自然言語でのコード変更依頼）
- Dockerまたはコンテナ技術の基礎知識（なぜファイルシステム分離がセキュリティに有効か）
- Node.js基礎（このプロジェクトはNode.js 20+で実装）
- Claude Agent SDKの概要（Anthropic公式のAgent実行ハーネス）
- フォーク＆ブランチベースのGitワークフロー

## 根拠

> NanoClaw provides that same core functionality, but in a codebase small enough to understand: one process and a handful of files. Claude agents run in their own Linux containers with filesystem isolation, not merely behind permission checks.

> Agents never hold raw API keys. Outbound requests route through OneCLI's Agent Vault, which injects credentials at request time and enforces per-agent policies and rate limits.
