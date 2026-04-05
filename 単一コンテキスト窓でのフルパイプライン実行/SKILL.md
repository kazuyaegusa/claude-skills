# 単一コンテキスト窓でのフルパイプライン実行

> 計画・ビルド・デバッグを1つの1Mトークンコンテキスト窓で実行し、タスク間の状態共有とコンテキスト保持を最大化

- 出典: https://github.com/htdt/godogen
- 投稿者: htdt
- カテゴリ: claude-code-workflow

## なぜ使うのか

従来のマルチエージェント設計ではコンテキスト分断でエラー伝播と修正が困難になるため。単一窓なら全履歴を参照しながらリアルタイム修正可能

## いつ使うのか

複数工程の相互依存が強く、各工程の出力が後続工程の入力設計に影響する場合（例: アーキテクチャ設計がアセット仕様を決め、アセットがコード実装を制約）

## やり方

1. orchestrator skill (godogen) が全タスクを1つのセッションで実行
2. API検索とビジュアルQAのみフォークスキル（godot-api, visual-qa）で分離し汚染回避
3. risk-first decompositionでタスク依存グラフの代わりにリスク優先順位で実行順序決定

### 入力

- ゲーム説明（自然言語）
- 1Mトークン対応LLM（Claude Opus 4.6推奨）

### 出力

- Godot 4プロジェクト（シーン、スクリプト、アセット構成済み）

## 使うツール・ライブラリ

- Claude Code
- Godot 4

## 前提知識

- Claude Codeの基本的な使い方とSkills機能の理解
- Godot 4の基礎知識（シーン、ノード、GDScriptの概念）
- API利用のための環境変数設定（GOOGLE_API_KEY, XAI_API_KEY, TRIPO3D_API_KEY）
- Linux/macOSのコマンドライン操作（依存パッケージインストール）
- LLMの文脈窓とトークン制限の理解
- （推奨）GCE等クラウドVM利用経験（長時間実行・GPU利用の場合）

## 根拠

> 「Three Claude Code skills — one orchestrator runs the full pipeline in a single 1M-token context window (planning, building, debugging), while two forked support skills handle Godot API lookup and visual QA without polluting the main context.」

> 「./publish.sh ~/my-game ... This creates the target directory with `.claude/skills/` and a `CLAUDE.md`, then initializes a git repo.」

> 「2026-04-03 — Single-context architecture (current) - Merged task executor into godogen — full pipeline runs in one 1M-token context window - Added godot-api skill (forked, Sonnet) for Godot class API lookup - Added visual-qa skill (forked) with Gemini Flash, Claude vision, and question mode - Risk-first decomposition replaces task DAG」
