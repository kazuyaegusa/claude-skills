# 視覚的フィードバックループによるQA自動化

> 実行中ゲームのスクリーンショットをキャプチャし、Vision LLMで解析して不具合（z-fighting、テクスチャ欠損、物理挙動異常）を検出・修正

- 出典: https://github.com/htdt/godogen
- 投稿者: htdt
- カテゴリ: claude-code-workflow

## なぜ使うのか

GDScriptやシーン設定のバグは実行画面を見ないと検出困難。テキストベースのテストでは見た目の問題を捉えられない

## いつ使うのか

3Dゲームでレンダリング問題が懸念される場合、物理演算の妥当性確認が必要な場合、UI配置の視覚的検証が必要な場合

## やり方

1. Godot Engineをヘッドレスまたはエディタモードで起動
2. 実行中ゲームのスクリーンショット/動画をキャプチャ
3. Gemini FlashとClaude Visionで画像解析（question modeで自由形式デバッグも可）
4. 検出した問題（z-fighting等）をGDScriptコードやシーン設定に反映して修正
5. 再キャプチャして検証

### 入力

- 実行可能なGodotプロジェクト
- スクリーンショットキャプチャ環境（GPUアクセス推奨）

### 出力

- 視覚的不具合の検出レポート
- 修正適用済みコード

## 使うツール・ライブラリ

- Godot Engine (headless/editor)
- Gemini Flash
- Claude Vision
- mesa-utils
- ffmpeg

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

> 「Running on a cloud VM keeps your local machine free and gives the pipeline a GPU for Godot's screenshot capture. A basic GCE instance with a T4 or L4 GPU works well.」
