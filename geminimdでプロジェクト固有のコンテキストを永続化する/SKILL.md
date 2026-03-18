# GEMINI.mdでプロジェクト固有のコンテキストを永続化する

> リポジトリルートまたはホームディレクトリに`GEMINI.md`を配置し、プロジェクトのアーキテクチャ・コーディング規約・制約条件をGemini CLIに常時認識させる

- 出典: https://github.com/google-gemini/gemini-cli
- 投稿者: google-gemini
- カテゴリ: claude-code-workflow

## なぜ使うのか

セッション毎にコンテキストを説明し直す手間を削減し、チーム全体で一貫したAI挙動を担保できる。リポジトリ内で管理すればバージョン管理とレビューの対象にもなる。

## いつ使うのか

複数人で同じリポジトリを触る、AIにプロジェクト固有のルール（認証方式、LLMバックエンド選択等）を守らせたい、オンボーディング時の説明コストを削減したい場合

## やり方

1. プロジェクトルートに`GEMINI.md`を作成 2. アーキテクチャ図、使用技術スタック、禁止事項（例: 「絶対にAPIキーをコミットしない」）を記述 3. `gemini`コマンド実行時、自動的にこのファイルがコンテキストに追加される 4. グローバル設定は`~/.gemini/GEMINI.md`に配置可能

### 入力

- GEMINI.mdファイル（Markdown形式）
- プロジェクトルートまたは~/.geminiディレクトリ

### 出力

- 全セッションで自動適用されるコンテキスト
- AIの応答がプロジェクトルールに準拠

## 使うツール・ライブラリ

- gemini-cli
- Markdown

## コード例

```
# プロジェクトルート/GEMINI.md
## Architecture
- Backend: Python 3.12, async/await統一
- LLM: `claude -p` のみ（APIキー不要）
- 禁止: ANTHROPIC_API_KEYの子プロセス渡し

## Rules
- 大きなタスクは分割してcommit
- コーディング前に目的・影響範囲を確認
```

## 前提知識

- Node.js環境の基本操作（npmまたはnpxの使用経験）
- ターミナル/コマンドラインの基礎知識
- Git操作の基本（GitHub連携を使う場合）
- JSON-RPC 2.0の基礎（MCP Server自作時）
- Google Cloud Projectの概念（Code Assistライセンス利用時）
- CI/CDパイプラインの基礎（GitHub Actions統合時）
