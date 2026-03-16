# workspace preset自動化

> workspace作成時に環境変数コピー、依存インストール、初期セットアップスクリプトを自動実行し、エージェントが即座に動作可能な状態を構築する

- 出典: https://github.com/superset-sh/superset
- 投稿者: superset-sh
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントごとに手動で.envコピーやnpm installを実行すると時間がかかり、設定漏れも発生する。presetで標準化することで、エージェントが毎回クリーンな環境から開始でき、再現性が保たれる。

## いつ使うのか

複数workspaceで同一の初期化処理が必要な時

## やり方

1. リポジトリルートに`.superset/config.json`を配置
2. `setup`配列にシェルスクリプトパス（例：`.superset/setup.sh`）を記述
3. setup.sh内で`cp ../.env .env`、`bun install`等を記述
4. workspace作成時にSupersetが自動実行
5. 環境変数`SUPERSET_WORKSPACE_NAME`, `SUPERSET_ROOT_PATH`が利用可能

### 入力

- .superset/config.json
- setupスクリプト（.superset/setup.sh等）

### 出力

- 依存インストール済み・環境変数設定済みのworkspace

## 使うツール・ライブラリ

- Superset
- Bash/シェルスクリプト

## コード例

```
# .superset/config.json
{
  "setup": ["./.superset/setup.sh"],
  "teardown": ["./.superset/teardown.sh"]
}

# .superset/setup.sh
#!/bin/bash
cp ../.env .env
bun install
echo "Workspace ready!"
```

## 前提知識

- git 2.20以上（worktree機能）
- CLIベースのAIエージェント（Claude Code, Cursor Agent等）
- macOS環境（Windows/Linuxは未検証）
- 複数タスクを並列実行する意義の理解

## 根拠

> 「.superset/config.json」「setup/teardown scripts」（preset自動化）

> 「Keyboard Shortcuts: ⌘1-9 Switch to workspace 1-9」（高速切り替え）
