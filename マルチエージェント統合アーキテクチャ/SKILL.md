# マルチエージェント統合アーキテクチャ

> 1つのブリッジプロセスで複数のAIエージェント（Claude Code、Gemini CLI、Cursor等）を並列管理し、チャットから切り替え可能にする

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: claude-code-workflow

## なぜ使うのか

用途ごとに最適なエージェントを使い分けたいが、それぞれ個別に立ち上げるのは煩雑。統合管理により1つのチャットから全て操作できる

## いつ使うのか

複数AIエージェントを使い分けたい、チーム内で異なるエージェントを試したい場合

## やり方

1. config.tomlで複数プロジェクトを定義（各プロジェクト=エージェント+プラットフォームの組）
2. 各プロジェクトごとにエージェントプロセスをサブプロセスとして起動
3. チャットメッセージを受信したらプロジェクトIDでルーティング
4. `/switch <id>` コマンドでセッションを切り替え
5. 複数ボットを同一グループに参加させてエージェント間会話も可能

### 入力

- 各エージェントの実行パスと設定
- プラットフォームごとのBot認証情報

### 出力

- 統合されたチャットインターフェース
- エージェント間のリレー会話

## 使うツール・ライブラリ

- Go子プロセス管理（os/exec）
- TOML設定パーサー

## コード例

```
[[projects]]
name = "claude-project"
agent = "claude"
platform = "telegram"
work_dir = "/path/to/project"

[[projects]]
name = "gemini-project"
agent = "gemini"
platform = "discord"
work_dir = "/path/to/another"
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法
