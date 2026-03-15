# コンテキスト50%でmanual /compactを実行する

> コンテキスト使用率が50%に達したタイミングで手動で `/compact` を実行し、新タスクに切り替える時は `/clear` でリセットする

- 出典: https://x.com/labelmake/status/2032652943250338098
- 投稿者: Kyohei - OSS, 外資IT
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキストが膨らむと「agent dumb zone」に入り、応答品質が著しく低下する。早めの圧縮で品質を維持できる

## いつ使うのか

長時間のセッションで応答が鈍くなったと感じた時、または新しいタスクに切り替える時

## やり方

1. `/context` コマンドでコンテキスト使用率を確認
2. 50%前後で `/compact` を実行してサマリー圧縮
3. 全く別のタスクに切り替える場合は `/clear` でコンテキスト全リセット
4. ステータスラインを設定してコンテキスト使用率を常時表示（`github.com/shanraisshan/claude-code-status-line`）

### 入力

- 進行中のClaude Codeセッション

### 出力

- 圧縮されたコンテキスト
- リフレッシュされた応答品質

## 使うツール・ライブラリ

- /compact
- /clear
- /context
- claude-code-status-line

## 前提知識

- Claude Code CLIの基本操作（起動、プロンプト入力、コマンド実行）
- GitおよびGitHubの基本知識
- CLAUDE.md、.claude/ディレクトリ構造の理解
- Claude CodeのPlan Mode、Command、Agent、Skillの概念的な区別

## 根拠

> 「公式・コミュニティのClaude Codeベストプラクティスを1箇所にまとめたリポジトリがGitHub月間トレンド入り」

> 「プログラムではなく、情報をまとめたマークダウンがトレンド入りするのがまさに今っぽい。最もレバレッジが効く場所がプログラムではなく、ナレッジになった感」
