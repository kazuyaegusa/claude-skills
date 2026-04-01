# bit-vcs/bitをJSビルドしてブラウザ埋め込みする

> bit-vcs/bitリポジトリをJavaScriptにビルドし、67kbのバンドルとしてブラウザに埋め込む

- 出典: https://x.com/mizchi/status/2035027196788842661
- 投稿者: mizchi
- カテゴリ: other

## なぜ使うのか

従来のlibgit2（数MB）やisomorphic-git（数百kb）より軽量で、バンドルサイズを最小化しながらGit機能を提供できる

## いつ使うのか

バンドルサイズを最小限に抑えながらブラウザでGit操作を実装したい場合

### 具体的な適用場面

- オフライン動作するWebエディタにバージョン管理機能を追加したい
- プライバシー重視でサーバーにデータを送らずローカルでGit操作したい
- 教育目的でGitの動作原理を軽量実装で理解したい
- モバイルブラウザで動作する最小限のGitクライアントを実装したい

## やり方

1. bit-vcs/bitリポジトリをクローン（git clone https://github.com/bit-vcs/bit） 2. ビルドツール（webpack/rollup等）でJSバンドル生成 3. HTML内で<script>タグで読み込み、bitのAPIを呼び出し（例: bit.commit(), bit.checkout()） 4. 最終バンドルサイズが67kb前後になることを確認

### 入力

- bit-vcs/bitソースコード
- JavaScriptビルド環境（Node.js, webpack/rollup等）

### 出力

- 67kb程度のJSバンドルファイル
- ブラウザで動作するGit操作API

## 使うツール・ライブラリ

- bit-vcs/bit
- webpack または rollup（ビルド用）

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
