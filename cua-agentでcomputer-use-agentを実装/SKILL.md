# Cua AgentでComputer-Use Agentを実装

> Python SDKを使い、スクリーン認識・UI操作・タスク実行を行うLLMエージェントを数行で構築する

- 出典: https://github.com/trycua/cua
- 投稿者: trycua
- カテゴリ: agent-orchestration

## なぜ使うのか

従来はPlaywright等でDOM操作するか、画像認識APIを自前実装する必要があったが、Cuaは「画面を見てクリックする」抽象レイヤーを提供するため

## いつ使うのか

Firefoxを開いて検索する、フォームに入力する等のGUIタスクをLLMに自律実行させたい場合

## やり方

1. `Computer(os_type="linux", provider_type="cloud")` でサンドボックス環境を生成
2. `ComputerAgent(model="anthropic/claude-sonnet-4-5-20250929", computer=computer)` でエージェント初期化
3. `agent.run([{"role": "user", "content": "タスク指示"}])` で実行
4. エージェントがスクリーンショット→LLM判断→UI操作を自律的に繰り返す

### 入力

- Python 3.12または3.13
- タスク記述（自然言語）
- 実行環境種別（linux/macos/windows）

### 出力

- タスク実行結果（非同期ストリーム）
- エージェントの操作ログ

## 使うツール・ライブラリ

- cua-agent
- cua-computer

## コード例

```
from computer import Computer
from agent import ComputerAgent

computer = Computer(os_type="linux", provider_type="cloud")
agent = ComputerAgent(model="anthropic/claude-sonnet-4-5-20250929", computer=computer)

async for result in agent.run([{"role": "user", "content": "Open Firefox and search for Cua"}]):
    print(result)
```

## 前提知識

- Python 3.12または3.13（Cua Agent SDK使用時）
- Node.js環境（CuaBot使用時）
- Apple Silicon Mac（Lume使用時）
- LLM APIアクセス（Anthropic Claude等、エージェント実行時）
- Computer-Use AgentやRPA/自動化の基本概念理解

## 根拠

> 「cuabot gives any coding agent a seamless sandbox for computer-use. Individual windows appear natively on your desktop with H.265, shared clipboard, and audio.」

> コード例: `computer = Computer(os_type="linux", provider_type="cloud")` `agent = ComputerAgent(model="anthropic/claude-sonnet-4-5-20250929", computer=computer)`

> インストール例: `npx cuabot` `lume run macos-sequoia-vanilla:latest`

> ベンチマーク実行例: `cb run dataset datasets/cua-bench-basic --agent cua-agent --max-parallel 4`
