# Homerowで画面全体をキーボード操作する

> macOS上の全ネイティブアプリのボタン・リンク・UI要素に一時的なキーボードラベルを表示し、ラベルのキーを押すだけでクリック操作を実行する。

- 出典: https://x.com/oikon48/status/2014717709658030202
- 投稿者: Oikon
- カテゴリ: ui-ux

## なぜ使うのか

マウスへの手の移動なしにUIを操作できるため、キーボード中心のワークフロー（Vim等）をアプリ外まで拡張でき、操作速度と集中度が向上する。

## いつ使うのか

ブラウザ・Finder・設定画面など、マウスクリックが必要な場面で手をキーボードから離したくないとき。

### 具体的な適用場面

- コーディング中にブラウザのボタンや設定画面を操作するためにマウスへ手を伸ばす頻度が高い場合
- Vimキーバインドをエディタ以外にも広げたい場合
- プレゼンやデモで画面操作をキーボードだけで完結させたい場合

## やり方

1. https://www.homerow.app からHomerowをダウンロードしてインストール（macOS 13以上が必要）。
2. アクセシビリティ権限をシステム設定→プライバシーとセキュリティ→アクセシビリティでHomerowに付与する。
3. デフォルトのトリガーキー（Space）を押すと画面上の全インタラクティブ要素にアルファベットラベルが表示される。
4. 目的のラベル（例: 'jk'）を入力するとその要素がクリックされる。
5. Shift+Spaceでリンクナビゲーションモード、Shift+J / Shift+/ で別モードに切り替え可能（ランディングページ記載）。

### 入力

- macOS 13 (Ventura) 以上
- アクセシビリティ権限の付与

### 出力

- マウスなしで任意のUIボタン・リンクをクリックできる状態
- キーボード完結のmacOS操作ワークフロー

## 使うツール・ライブラリ

- Homerow (https://www.homerow.app, $49.99 one-time, 50回まで無料試用可)

## 前提知識

- macOS 13 (Ventura) 以上の環境
- キーボードショートカット・Vimキーバインドの基本的な概念の理解

## 根拠

> 「全てキーボードで操作できるところを見せてもらって感動した」

> 「Click anywhere, without a mouse — Navigate buttons, links, and UI elements instantly with keyboard labels」（homerow.app公式）

> 「Works with your favourite apps — Homerow works with most native macOS apps and a growing set of non-native web-based apps」（homerow.app公式）

> 「Nice piece of software for those of us who use vim motions everywhere and always avoid using anything other than the keyboard.」（ユーザーレビュー）
