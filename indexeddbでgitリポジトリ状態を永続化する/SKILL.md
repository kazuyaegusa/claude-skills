# IndexedDBでGitリポジトリ状態を永続化する

> ブラウザのIndexedDBにGitオブジェクト（コミット、ツリー、ブロブ）とブランチ情報を保存し、リロード後も復元可能にする

- 出典: https://x.com/mizchi/status/2035027196788842661
- 投稿者: mizchi
- カテゴリ: other

## なぜ使うのか

ブラウザメモリのみの実装では、リロード時にリポジトリ状態が失われるため、実用的なバージョン管理には永続化が必須

## いつ使うのか

ブラウザリロード後もGitリポジトリの履歴を保持したい場合

### 具体的な適用場面

- オフライン動作するWebエディタにバージョン管理機能を追加したい
- プライバシー重視でサーバーにデータを送らずローカルでGit操作したい
- 教育目的でGitの動作原理を軽量実装で理解したい
- モバイルブラウザで動作する最小限のGitクライアントを実装したい

## やり方

1. IndexedDB APIでデータベースを作成（例: const db = await indexedDB.open('bit-repo', 1)） 2. Gitオブジェクトストア（commits, trees, blobs）とrefs（ブランチ参照）を定義 3. コミット時にオブジェクトをIndexedDBに保存（例: db.transaction('commits', 'readwrite').objectStore('commits').add(commitObj)） 4. 起動時にIndexedDBから状態を読み込み、リポジトリを復元 5. デモページの「Reset sample repo」「Loading saved repo」フローを参考に実装

### 入力

- Gitオブジェクト（コミット、ツリー、ブロブ）のデータ構造
- ブランチ参照情報（refs/heads/*）

### 出力

- IndexedDBに永続化されたGitリポジトリデータ
- リロード後も復元可能なコミット履歴

## 使うツール・ライブラリ

- IndexedDB API（ブラウザ標準）

## 前提知識

- GitのオブジェクトモデルとGitフロー（コミット、ツリー、ブロブ、refs）の基礎理解
- JavaScriptビルドツール（webpack/rollup）の基本操作
- IndexedDB APIの基本的な使い方（open, transaction, objectStore）
- ブラウザのストレージ制限とクォータ管理の知識

## 根拠

> 投稿本文: 「ブラウザで 67kb で埋め込み git が動く」

> 投稿本文: 「bit-vcs/bit をjsビルドして埋め込んだやつ」

> デモページ: 「IndexedDB demo」「Loading saved repo」「Reset sample repo」

> デモページ: 「Stage file」「Commit staged changes」「Create branch」「Checkout branch」のUI要素

> デモページ: 「Recent History」「Storage details and event log」の機能実装
