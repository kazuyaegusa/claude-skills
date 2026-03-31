# コンテナ単位でのAgent分離実行

> 各グループのAI AgentをLinuxコンテナ（macOSならApple Container、Linux/WindowsならDocker）で独立実行し、明示的にマウントしたディレクトリのみアクセス可能にする

- 出典: https://github.com/qwibitai/nanoclaw
- 投稿者: qwibitai
- カテゴリ: claude-code-workflow

## なぜ使うのか

アプリケーションレベルの権限チェック（allowlist、ペアリングコード）ではなく、OSレベルのファイルシステム分離により、Agentが予期しないデータにアクセスするリスクを根本的に排除できる

## いつ使うのか

複数のAI Agentを同一ホストで安全に実行したい時、Agentにファイルアクセスやコマンド実行権限を与えつつホスト環境を保護したい時

## やり方

1. グループごとに`groups/{group-id}/`ディレクトリを作成
2. そのディレクトリだけをコンテナにマウント
3. `src/container-runner.ts`がClaude Agent SDKを実行するコンテナをspawn
4. コンテナ内のBashコマンドはホストではなくコンテナ内で実行される
5. Credential等の機密情報はコンテナに渡さず、OneCLI Agent Vaultがプロキシ時に注入

### 入力

- グループID
- グループ専用ディレクトリ（CLAUDE.md含む）
- コンテナランタイム（Docker / Apple Container）

### 出力

- ファイルシステム分離されたAgent実行環境
- グループごとの独立したメモリ・状態

## 使うツール・ライブラリ

- Docker / Apple Container
- Claude Agent SDK
- OneCLI Agent Vault（クレデンシャル管理）

## コード例

```
// src/container-runner.ts がコンテナをspawnする実装
// groups/{group-id}/ のみをマウント
// Bashコマンドはコンテナ内で実行
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
