# クラウドVMでの長時間生成実行

> 数時間かかるゲーム生成をGCE等のGPU搭載VMで実行し、ローカルマシンを占有せず、チャンネル/リモート制御で進捗確認

- 出典: https://github.com/htdt/godogen
- 投稿者: htdt
- カテゴリ: claude-code-workflow

## なぜ使うのか

ゲーム生成は数時間かかりローカルマシンを占有。VMなら並行作業可能でGPUによるスクリーンショットキャプチャも高速

## いつ使うのか

長時間実行タスクでローカル環境を占有したくない場合、GPUが必要だがローカルにない場合、外出先から進捗確認したい場合

## やり方

1. GCE等でT4/L4 GPU搭載インスタンスを起動
2. Godot、Claude Code、依存パッケージ（mesa-utils, ffmpeg）をインストール
3. API keyを環境変数設定
4. Claude Code channelまたはremote controlで接続
5. スマホ等から `/godogen` コマンドでゲーム生成を投げ、進捗をチャンネル経由で受信

### 入力

- GCEインスタンス（GPU搭載）
- Claude Code channel/remote control設定

### 出力

- 完成したGodotプロジェクト（VM上）
- 進捗通知（Telegram/Slack等）

## 使うツール・ライブラリ

- GCE (or similar cloud VM)
- Claude Code channels
- Claude Code remote control

## 前提知識

- Claude Codeの基本的な使い方とSkills機能の理解
- Godot 4の基礎知識（シーン、ノード、GDScriptの概念）
- API利用のための環境変数設定（GOOGLE_API_KEY, XAI_API_KEY, TRIPO3D_API_KEY）
- Linux/macOSのコマンドライン操作（依存パッケージインストール）
- LLMの文脈窓とトークン制限の理解
- （推奨）GCE等クラウドVM利用経験（長時間実行・GPU利用の場合）

## 根拠

> 「Three Claude Code skills — one orchestrator runs the full pipeline in a single 1M-token context window (planning, building, debugging), while two forked support skills handle Godot API lookup and visual QA without polluting the main context.」

> 「GDScript expertise — custom-built language reference and lazy-loaded API docs for all 850+ Godot classes compensate for LLMs' thin training data on GDScript.」

> 「Visual QA closes the loop — captures actual screenshots from the running game and analyzes them with Gemini Flash and Claude vision. Includes question mode for free-form visual debugging. Catches z-fighting, missing textures, broken physics.」

> 「./publish.sh ~/my-game ... This creates the target directory with `.claude/skills/` and a `CLAUDE.md`, then initializes a git repo.」

> 「2026-04-03 — Single-context architecture (current) - Merged task executor into godogen — full pipeline runs in one 1M-token context window - Added godot-api skill (forked, Sonnet) for Godot class API lookup - Added visual-qa skill (forked) with Gemini Flash, Claude vision, and question mode - Risk-first decomposition replaces task DAG」
