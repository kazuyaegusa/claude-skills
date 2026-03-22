# Deep Interviewで要件を事前明確化

> 曖昧な要求に対してソクラテス式質問で段階的に要件を掘り下げ、実装前に明確性を測定する

- 出典: https://github.com/Yeachan-Heo/oh-my-claudecode
- 投稿者: Yeachan-Heo
- カテゴリ: claude-code-workflow

## なぜ使うのか

曖昧な要件のまま実装すると手戻りが発生する。Deep Interviewは隠れた前提を顕在化し、weighted dimensionsで明確度を定量評価してから実装開始できる

## いつ使うのか

要件が曖昧、または設計を細かく管理したい時、チーム内で認識齟齬を防ぎたい時

## やり方

1. `/deep-interview "I want to build a task management app"` を実行
2. システムが目的・ユーザー・成功条件・制約等を順次質問
3. 回答に応じて追加の深堀り質問
4. 明確性スコアが閾値を超えたら実装フェーズへ移行
5. 途中で不明点が再浮上しても再質問可能

### 入力

- 大まかなアイデアまたは要望（1文でも可）

### 出力

- 明確化された要件定義
- weighted dimensionsでの明確性スコア
- 実装可能な詳細仕様

## 使うツール・ライブラリ

- oh-my-claudecode deep-interview skill

## コード例

```
/deep-interview "I want to build a task management app"
```

## 前提知識

- Claude Code CLIの基本操作（インストール・起動）
- Claude Max/ProサブスクリプションまたはAnthropic APIキー
- tmux（CLI workers使用時）
- Node.js/npm（プラグインインストール時）
- Git（スキルのバージョン管理時）

## 根拠

> 「Workers spawn on-demand and die when their task completes — no idle resource usage」

> 「autopilot: build a REST API for managing tasks - That's it. Everything else is automatic.」

> 「The deep interview uses Socratic questioning to clarify your thinking before any code is written」
