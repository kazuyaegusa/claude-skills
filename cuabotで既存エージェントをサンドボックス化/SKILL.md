# CuaBotで既存エージェントをサンドボックス化

> Claude CodeやOpenClaw等の任意のコーディングエージェントを、分離された仮想デスクトップ環境で動かす

- 出典: https://github.com/trycua/cua
- 投稿者: trycua
- カテゴリ: claude-code-workflow

## なぜ使うのか

ホストマシンへの影響を防ぎつつ、エージェントが自由にファイル操作・ブラウザ起動・GUI操作できる環境を提供するため

## いつ使うのか

エージェントにブラウザ操作やGUIツール実行をさせたいが、ホスト環境を汚したくない場合

## やり方

1. `npx cuabot` で初回セットアップ実行
2. `cuabot claude` でClaude Codeをサンドボックス内起動
3. エージェントが操作するウィンドウがホストデスクトップにH.265でストリーミング表示される
4. クリップボード・音声は自動的にホストと共有

### 入力

- Node.js環境（npx実行可能）
- 起動したいエージェント名（claude, openclaw等）

### 出力

- サンドボックス化されたエージェント実行環境
- ホストに表示される仮想デスクトップウィンドウ

## 使うツール・ライブラリ

- cuabot（npm package）

## コード例

```
npx cuabot
cuabot claude
cuabot openclaw
```

## 前提知識

- Python 3.12または3.13（Cua Agent SDK使用時）
- Node.js環境（CuaBot使用時）
- Apple Silicon Mac（Lume使用時）
- LLM APIアクセス（Anthropic Claude等、エージェント実行時）
- Computer-Use AgentやRPA/自動化の基本概念理解

## 根拠

> 「Build agents that see screens, click buttons, and complete tasks autonomously. Run isolated code execution environments for AI coding assistants like Claude Code, Codex CLI, or OpenCode.」

> コード例: `computer = Computer(os_type="linux", provider_type="cloud")` `agent = ComputerAgent(model="anthropic/claude-sonnet-4-5-20250929", computer=computer)`

> インストール例: `npx cuabot` `lume run macos-sequoia-vanilla:latest`
