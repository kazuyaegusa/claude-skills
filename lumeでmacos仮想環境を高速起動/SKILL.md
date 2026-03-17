# LumeでmacOS仮想環境を高速起動

> Apple Silicon Mac上でmacOS VMを数秒で起動し、エージェント開発・テストに使う

- 出典: https://github.com/trycua/cua
- 投稿者: trycua
- カテゴリ: agent-orchestration

## なぜ使うのか

macOS特有のUI（Finder、Spotlight等）を操作するエージェントを開発する際、ホスト環境を汚さず、かつDocker等のLinuxコンテナでは実現できないため

## いつ使うのか

macOS GUIアプリケーション操作をエージェントで自動化したいが、ホストmacOSを直接触りたくない場合

## やり方

1. インストールスクリプト実行: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"`
2. `lume run macos-sequoia-vanilla:latest` でmacOS Sequoia VMを起動
3. Apple Virtualization.Framework経由でネイティブに近い速度で動作
4. lumierコマンドでDocker CLI互換インターフェース利用可能

### 入力

- Apple Silicon Mac（M1以降）
- macOSイメージ名（タグ指定）

### 出力

- 起動したmacOS仮想マシン
- ネイティブ並みの実行速度

## 使うツール・ライブラリ

- lume
- Apple Virtualization.Framework

## コード例

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
lume run macos-sequoia-vanilla:latest
```

## 前提知識

- Python 3.12または3.13（Cua Agent SDK使用時）
- Node.js環境（CuaBot使用時）
- Apple Silicon Mac（Lume使用時）
- LLM APIアクセス（Anthropic Claude等、エージェント実行時）
- Computer-Use AgentやRPA/自動化の基本概念理解

## 根拠

> 「Build agents that see screens, click buttons, and complete tasks autonomously. Run isolated code execution environments for AI coding assistants like Claude Code, Codex CLI, or OpenCode.」

> 「Create and manage macOS/Linux VMs with near-native performance on Apple Silicon using Apple's Virtualization.Framework.」

> インストール例: `npx cuabot` `lume run macos-sequoia-vanilla:latest`

> ベンチマーク実行例: `cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4`
