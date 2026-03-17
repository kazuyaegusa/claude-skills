# Cua-Benchで既存ベンチマーク実行

> OSWorld、ScreenSpot、Windows Arena等の公開データセットで自作エージェントを評価する

- 出典: https://github.com/trycua/cua
- 投稿者: trycua
- カテゴリ: agent-orchestration

## なぜ使うのか

エージェントの性能を標準化された指標で測定し、他手法と比較可能にするため

## いつ使うのか

自社エージェントが既存手法と比べてどれだけ優れているかを定量評価したい場合

## やり方

1. `uv tool install -e .` でCua-Bench CLIインストール
2. `cb image create linux-docker` でベンチマーク用ベースイメージ作成
3. `cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4` で並列実行
4. 結果が自動集計され、タスク成功率・操作軌跡が保存される

### 入力

- 評価対象エージェント実装
- ベンチマークデータセット名

### 出力

- タスク成功率スコア
- エージェント操作軌跡（RL学習用にエクスポート可能）

## 使うツール・ライブラリ

- cua-bench
- uv

## コード例

```
cd cua-bench
uv tool install -e . && cb image create linux-docker
cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4
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
