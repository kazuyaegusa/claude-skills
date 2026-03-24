# ローカル開発環境でマーケットプレイスをテスト

> 自作スキルをマーケットプレイスに公開する前にローカルで動作確認する

- 出典: https://github.com/trailofbits/skills
- 投稿者: trailofbits
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキルを公開前にテストしないと、他のユーザーに壊れたスキルを配布してしまう。ローカルマーケットプレイス追加機能で安全に開発できる

## いつ使うのか

新しいスキルを開発している時、または既存スキルを改善してプルリクエストを出す前

## やり方

1. スキルリポジトリの親ディレクトリに移動（例: ~/projectsにいて、~/projects/skillsがリポジトリなら~/projectsへ）
2. `/plugins marketplace add ./skills` で相対パス指定
3. Claude Codeでスキルをテスト
4. 問題があれば修正して再テスト
5. 動作確認後にGitHubへpush

### 入力

- ローカルのスキルリポジトリ（git管理下）
- Claude Code環境

### 出力

- ローカルでテスト済みのスキル
- 動作確認済みのマーケットプレイス設定

## 使うツール・ライブラリ

- Claude Code
- git

## コード例

```
cd /path/to/parent
/plugins marketplace add ./skills
```

## 前提知識

- Claude CodeまたはCodexのインストールと基本的な使い方
- セキュリティ監査・脆弱性分析の基礎知識
- 静的解析ツール（Semgrep, CodeQL等）の概要理解
- スマートコントラクト監査の場合は対象ブロックチェーンの知識
- 暗号解析スキルを使う場合はサイドチャネル攻撃の基礎知識

## 根拠

> Installation: `/plugin marketplace add trailofbits/skills` followed by `/plugin menu`

> Local development: `cd /path/to/parent` then `/plugins marketplace add ./skills`
