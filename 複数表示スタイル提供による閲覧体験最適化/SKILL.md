# 複数表示スタイル提供による閲覧体験最適化

> 同一コンテンツを4つの異なるスタイル（Awesome/Extra/Classic/Flat）でレンダリングし、ユーザーが好みに応じて切り替えられるようにする

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーの情報探索スタイルは多様であり、詳細な説明を好む人もいれば、簡潔な一覧を好む人もいる。複数スタイルを提供することで、より広い層にアクセスしやすい形式を提供できる

## いつ使うのか

多様なユーザー層を持つドキュメントやリソース集で、閲覧体験をパーソナライズしたい場合

## やり方

1. メインREADMEを詳細版（Awesome）として作成
2. README_ALTERNATIVES/ディレクトリに他スタイル版を配置
3. 各スタイル用のバッジ画像を作成（assets/badge-style-*.svg）
4. READMEトップに切り替えリンクを配置
5. 自動生成のコメント（<!-- GENERATED FILE: do not edit directly -->）を追加して、手動編集を防止

### 入力

- 同一データソース（リソースリスト）
- 各スタイルの表示ルール定義

### 出力

- メインREADME.md
- README_ALTERNATIVES/README_EXTRA.md
- README_ALTERNATIVES/README_CLASSIC.md
- README_ALTERNATIVES/README_FLAT_ALL_AZ.md

## 使うツール・ライブラリ

- Markdown
- スタイル切り替えバッジ（SVG）
- 自動生成スクリプト（推測）

## コード例

```
<h3 align="center">Pick Your Style:</h3>
<p align="center">
<a href="./"><img src="assets/badge-style-awesome.svg" alt="Awesome" height="28" style="border: 2px solid #cc3366; border-radius: 4px;"></a>
<a href="README_ALTERNATIVES/README_EXTRA.md"><img src="assets/badge-style-extra.svg" alt="Extra" height="28"></a>
...
```

## 前提知識

- Claude Codeの基本的な使い方（CLI、設定ファイル、コマンド実行）
- GitHubの基本操作（リポジトリのクローン、READMEの閲覧）
- Markdownの読解
- AI開発ツールの一般的な概念（エージェント、フック、プロンプト等）

## 根拠

> "Please do not open a PR to submit a recommendation - the only person who is allowed to submit PRs to this repo is Claude" - 品質管理方針
