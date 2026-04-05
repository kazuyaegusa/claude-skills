# カスタムGDScript API参照システムによるLLM知識補完

> GDScriptの850+クラスAPI仕様をカスタムビルドした言語リファレンスとしてlazy-loadし、LLMのGDScript訓練データ不足を補う

- 出典: https://github.com/htdt/godogen
- 投稿者: htdt
- カテゴリ: claude-code-workflow

## なぜ使うのか

LLMのGDScript訓練データは薄く、Godot 4固有APIやクラス仕様を正確に生成できない。外部参照で補完すれば正確性向上

## いつ使うのか

LLMの訓練データが不足している専門ドメイン（ゲームエンジンAPI、特定フレームワーク等）でコード生成品質を上げたい場合

## やり方

1. Godot 4の全クラスAPIドキュメントをカスタム言語リファレンスとして構造化
2. godot-apiスキル（forked, Sonnet）でAPI検索専用コンテキストを作成
3. メインスキル（godogen）から必要時にAPI検索スキルをクエリしlazy-loadで必要情報のみ取得
4. 2階層検索（クラス名→メソッド詳細）で情報過多を回避

### 入力

- Godot 4 APIドキュメント（公式またはスクレイピング）

### 出力

- 正確なGDScriptコード（クラス・メソッド使用法が正しい）

## 使うツール・ライブラリ

- Claude Code Skills（forked skill機能）
- Godot 4 API docs

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

> 「Running on a cloud VM keeps your local machine free and gives the pipeline a GPU for Godot's screenshot capture. A basic GCE instance with a T4 or L4 GPU works well.」

> 「2026-04-03 — Single-context architecture (current) - Merged task executor into godogen — full pipeline runs in one 1M-token context window - Added godot-api skill (forked, Sonnet) for Godot class API lookup - Added visual-qa skill (forked) with Gemini Flash, Claude vision, and question mode - Risk-first decomposition replaces task DAG」
