# セキュリティ監査を実施してからスキルをインストールする

> スキルの SKILL.md と全スクリプトを精査し、任意コード実行のリスクがないか確認してから有効化する

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルは Claude の実行環境で任意のコードを実行できるため、悪意あるスキルはデータ流出・プロンプトインジェクション攻撃・脆弱性導入のリスクがある

## いつ使うのか

未検証のコミュニティスキルをインストールする前、または Enterprise 環境で承認プロセスを実施する場合

## やり方

1. SKILL.md を開いて指示内容を確認
2. scripts/ 内の全ファイル（.py, .js 等）をコードレビュー
3. 機密データアクセスや外部通信の有無をチェック
4. 信頼できるソース（公式リポジトリ、検証済みコミュニティ）からのみインストール
5. 本番環境適用前に非本番環境でテスト
6. git タグでバージョン管理し、変更履歴を追跡

### 入力

- スキルフォルダ（SKILL.md + scripts/）
- セキュリティチェックリスト

### 出力

- 安全性が確認されたスキル
- 監査レポート（Enterprise の場合）

## 使うツール・ライブラリ

- コードレビューツール
- git（バージョン管理）

## コード例

```
# 例: スクリプト内の外部通信チェック
grep -r "requests\." scripts/
grep -r "urllib" scripts/
grep -r "subprocess" scripts/
```

## 前提知識

- Claude Pro, Max, Team, または Enterprise サブスクリプション（Free tier ではスキル利用不可）
- Claude.ai Web / Claude Code CLI / Claude API のいずれかへのアクセス
- YAMLとMarkdownの基本構文（スキル作成時）
- git の基本操作（チーム配布時）
