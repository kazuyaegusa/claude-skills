# 複数LLMの適材適所活用によるコスト最適化

> アセット生成でGemini（精密作業）、Grok（テクスチャ・簡易オブジェクト）、Tripo3D（画像→3Dモデル変換）を使い分け、視覚的インパクト/コスト比を最大化

- 出典: https://github.com/htdt/godogen
- 投稿者: htdt
- カテゴリ: claude-code-workflow

## なぜ使うのか

全てを単一LLMで生成するとコスト高騰。各LLMの得意分野を活用すれば品質とコスト両立

## いつ使うのか

大量アセット生成が必要でAPI利用料を抑えたい場合、各アセットタイプで求められる品質が異なる場合

## やり方

1. キャラクター・精密リファレンス → Gemini image generation
2. テクスチャ・簡易オブジェクト → xAI Grok image generation
3. アニメーションスプライト → Grok video generation（ref→pose→video→frames→loop trim）
4. 2D画像→3Dモデル変換 → Tripo3D API
5. 背景除去 → BiRefNet multi-signal matting

### 入力

- アセット仕様（テキスト記述）
- GOOGLE_API_KEY
- XAI_API_KEY
- TRIPO3D_API_KEY

### 出力

- ゲームアセット（画像、3Dモデル、アニメーションフレーム）

## 使うツール・ライブラリ

- Gemini API
- xAI Grok API
- Tripo3D API
- BiRefNet

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

> 「Asset generation — Gemini creates precise references and characters; xAI Grok handles textures and simple objects; Tripo3D converts images to 3D models. Animated sprites use Grok video generation with loop detection. Budget-aware: maximizes visual impact per cent spent.」

> 「2026-04-03 — Single-context architecture (current) - Merged task executor into godogen — full pipeline runs in one 1M-token context window - Added godot-api skill (forked, Sonnet) for Godot class API lookup - Added visual-qa skill (forked) with Gemini Flash, Claude vision, and question mode - Risk-first decomposition replaces task DAG」
