# (解析失敗)

> Claude Code 2.1.83 (抜粋)

・`managed-settings.json` に加え、`managed-settings.d/` のドロッ

- 出典: https://x.com/oikon48/status/2036703443453374878
- 投稿者: Oikon
- カテゴリ: claude-code-workflow

## なぜ使うのか

(未記載)

## いつ使うのか

(未記載)

## やり方

(投稿参照)

## 根拠

> Claude Code 2.1.83 (抜粋)

・`managed-settings.json` に加え、`managed-settings.d/` のドロップインディレクトリを追加。複数チームが独立したポリシー断片を配置し、それらをアルファベット順でマージできるようになる。

・リアクティブな環境管理のため、`CwdChanged` と `FileChanged` のフックイベントを追加。(例
