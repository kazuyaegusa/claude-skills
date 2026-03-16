# 2-Actionルールによる発見保存

> view や browser 操作を2回実行するごとに、発見した情報を findings.md に保存する。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: context-management

## なぜ使うのか

調査タスクでは情報をコンテキストに詰め込みすぎるとトークン上限に達しやすい。定期的に外部ファイルへ保存することで、コンテキストを圧迫せず、後から参照可能な知識ベースを構築できる。

## いつ使うのか

リサーチタスク、複数ソースからの情報収集、長時間の調査が必要な場合。

## やり方

1. view、WebFetch、Readなどの情報取得ツールを2回実行
2. 得られた情報を findings.md に記録（日時、ソース、内容）
3. 次の2回の操作後も同様に追記
4. コンテキストには最小限の要約のみ保持

### 入力

- view/browser/Readツールの実行結果

### 出力

- findings.md（調査結果の蓄積）

## 前提知識

- Claude CodeまたはAgent Skills対応IDE（Cursor、Gemini CLI、Kiro、OpenClaw等）の基本操作
- markdownファイルの読み書き
- hookの概念（PreToolUse、PostToolUse、Stop）の理解
- bash または PowerShell の基本知識（hookスクリプトカスタマイズ時）
- gitの基本操作（セッションリカバリー機能利用時）

## 根拠

> The 2-Action Rule — Save findings after every 2 view/browser operations
