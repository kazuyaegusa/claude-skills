# CLAUDE.mdで条件付き重要ブロックを指定する

> 特定の状況でのみ重要な指示をCLAUDE.md内で条件付きブロックとして明示し、Claudeに確実に遵守させる

- 出典: https://x.com/ai_masaou/status/2035288249581617200
- 投稿者: まさお@AI駆動開発
- カテゴリ: claude-code-workflow

## なぜ使うのか

CLAUDE.mdが長くなると内容が「任意の参考情報」として流される。システムリマインダーにも「関連性があるかもしれないし、ないかもしれない」と書かれており、特定場面での重要指示が無視されやすい

## いつ使うのか

CLAUDE.mdが長くなり、テスト設定・デプロイ手順・特定フレームワークの使い方など「特定の状況でのみ重要な指示」が守られなくなった時

### 具体的な適用場面

- CLAUDE.mdが長くなり、重要な指示が守られなくなった時
- PRレビュー時に最新のdiffを自動で読み込ませたい時
- CI/CD結果やエラー通知をClaude Codeセッションに直接流し込みたい時
- スマホから自宅PCのClaude Codeを操作して作業させたい時
- 他人が作ったスキルをインストールする前に安全性を確認したい時

## やり方

1. CLAUDE.mdに `<important if="テストを書いている時">` のように条件を指定したブロックを作成
2. ブロック内に特定場面でのみ重要な指示を記述（例: `createTestApp()ヘルパーを使う`、`packages/db/testのdbMockでモック`）
3. 常時重要な情報（プロジェクト構造・技術スタック）は条件ブロック外に通常記述
4. 使い分けルール: 常時重要=そのまま、特定場面のみ重要=important ifで囲う

### 入力

- 長くなったCLAUDE.md
- 特定場面でのみ重要な指示（テスト設定、デプロイ手順等）

### 出力

- 条件に応じて確実に遵守されるCLAUDE.md
- 遵守率の向上

## 使うツール・ライブラリ

- Claude Code
- CLAUDE.md

## コード例

```
<important if="テストを書いている時">
・createTestApp()ヘルパーを使う
・packages/db/testのdbMockでモック
</important>
```

## 前提知識

- Claude Codeの基本的な使い方
- CLAUDE.mdの役割と記述方法
- Skillsの基本的な作成・インストール方法
- Telegram/Discordアカウント（Channels利用時）
- Claude Coworkデスクトップ版（Dispatch利用時）

## 根拠

> HumanLayerのブログで紹介された対策がこれ <important if="テストを書いている時">

> スキルMD内に !`gh pr diff` のように書くと読み込み時にコマンドが自動実行され、出力がコンテキストに注入される

> Telegram/Discordから、動いているClaude Codeセッションにメッセージをプッシュできる

> Claude Coworkのデスクトップアプリに追加されたリモートコントロール機能 スマホアプリからデスクトップのCoworkを操作できる「トランシーバー」

> ターミナルのClaude Codeを外から操作したい → Channels / デスクトップのClaude Coworkを外から操作したい → Dispatch
