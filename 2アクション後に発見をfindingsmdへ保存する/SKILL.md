# 2アクション後に発見をfindings.mdへ保存する

> ブラウザ操作やファイル閲覧を2回実行したら、その発見を必ずfindings.mdに書き出す（The 2-Action Rule）。

- 出典: https://github.com/OthmanAdi/planning-with-files
- 投稿者: OthmanAdi
- カテゴリ: context-management

## なぜ使うのか

コンテキストに情報を溜め続けると上限（200kトークン等）に達し、古い情報が押し出される。定期的にディスクへ退避することで、コンテキストを圧縮し、情報を永続化できる。

## いつ使うのか

調査タスク、APIドキュメント読解、複数ページのスクレイピング、設計ドキュメント作成

## やり方

1. WebFetch / Readツール等でデータを取得
2. 2回目の取得完了時、findings.mdを開く（Editツール）
3. 「## [日時] 調査結果」セクションを追加し、発見内容を箇条書きで記載
4. コードスニペット・URL・重要な引用を含める
5. PostToolUseフックが「findings更新を忘れていないか？」とリマインド

### 入力

- WebFetch / Read等で取得したデータ
- findings.md（追記対象）

### 出力

- 更新されたfindings.md（調査履歴が蓄積）

## 使うツール・ライブラリ

- Edit（ファイル編集ツール）
- WebFetch / Read / Bash等（情報取得ツール）

## コード例

```
## 2026-03-20 14:30 調査結果
- vxtwitter APIは認証不要で画像取得可能
- https://github.com/dylanpdx/BetterTwitFix
- レート制限: 300req/15min
```

## 前提知識

- Claude Code / Cursor / Gemini CLI / Codex等のAIエージェント環境
- Node.js（npx skills addコマンド実行用）
- bash（macOS/Linux）またはPowerShell（Windows）
- Agent Skills仕様の基本理解（SKILL.md, hooks.json等）
- Markdownフォーマットの理解（チェックボックス [ ] / [x] 記法）

## 根拠

> The 2-Action Rule — Save findings after every 2 view/browser operations
