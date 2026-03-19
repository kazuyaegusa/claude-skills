# workspace presetで環境構築を自動化する

> 新しいworkspaceを作った瞬間に、環境変数コピー・依存インストール・初期設定を自動実行する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

手動でcp .env, bun installを毎回やると時間の無駄。setupスクリプトで統一すれば、agentが即座に作業開始できる

## いつ使うのか

複数のプロジェクトや環境（dev/staging/test）を素早く切り替えたい時

## やり方

1. `.superset/config.json` で setup/teardown配列を定義
2. setupスクリプト（例: .superset/setup.sh）で必要なコマンドを列挙
3. Superset内で「New workspace」すると自動実行
4. Ctrl+1-9でpreset番号を指定すれば特定の環境を即起動

### 入力

- .superset/config.json
- setup/teardownシェルスクリプト
- 環境変数SUPERSET_WORKSPACE_NAME, SUPERSET_ROOT_PATH

### 出力

- 即座に利用可能なworkspace
- コピーされた.env
- インストール済み依存

## 使うツール・ライブラリ

- bash/zsh
- .superset/config.json
- Superset（preset機能）

## コード例

```
# .superset/setup.sh
#!/bin/bash
cp ../.env .env
bun install
echo "Workspace ready!"
```

## 前提知識

- git 2.20+の基本操作知識
- git worktreeの概念
- ターミナルでのagent CLI実行経験
- macOS環境（Windows/Linux未検証）
- Bun, gh, Caddyのインストール方法

## 根拠

> ⌘1-9 to switch workspaces, ⌘L to toggle changes panel, Ctrl+1-9 to open preset
