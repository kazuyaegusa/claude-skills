# EWC++による忘却防止と継続学習

> Elastic Weight Consolidation++で重要な重みを固定し、新しいパターン学習時に過去の知識を忘れないようにする

- 出典: https://github.com/ruvnet/ruflo
- 投稿者: ruvnet
- カテゴリ: agent-orchestration

## なぜ使うのか

ニューラルネットワークは新しいタスクを学習すると過去の知識を上書きする（壊滅的忘却）。EWC++は重要な重みにペナルティをかけ、新旧両方の知識を保持する

## いつ使うのか

長期運用でパターンが蓄積していくシナリオ（数ヶ月〜数年）で、初期に学習した重要パターンを保持したい場合

## やり方

1. 初回学習完了後、`consolidate()`で重要度行列（Fisher Information）を計算
2. 新しいタスク学習時、損失関数に`λ * Σ F_i (θ_i - θ*_i)^2`項を追加（重要な重みの変更を抑制）
3. 定期的に`hooks post-task`で自動consolidation実行
4. 学習済みパターンの精度を維持したまま新パターンを追加

### 入力

- 新しいトレーニングデータ
- consolidation頻度（例: 10エポックごと）
- λ（正則化強度、デフォルト0.4）

### 出力

- 更新された重み（過去+新規知識）
- Fisher Information行列

## 使うツール・ライブラリ

- @ruvector/sona（SONA + EWC++実装）
- @claude-flow/neural

## コード例

```
const sona = new SONA({ enableEWC: true, learningRate: 0.001 });
const trajectory = sona.startTrajectory('task-123');
// ... タスク実行 ...
await trajectory.complete('success');
await sona.consolidate(); // EWC++でFisher Information更新、重要な重みを保護
```

## 前提知識

- Node.js 20+とnpm 9+
- Claude Code CLIのインストール（`npm install -g @anthropic-ai/claude-code`）
- Anthropic APIキー（Claude利用時）またはClaude Codeサブスクリプション
- 基本的なTypeScript/JavaScriptの知識
- （オプション）Docker（RuVector PostgreSQL利用時）
- （オプション）Git、GitHub CLI（GitHub統合時）
- マルチエージェントシステムの基本概念理解（推奨）
