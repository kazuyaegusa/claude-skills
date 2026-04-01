# IDE内デザインツールでGemini枠を消費する

> Pencil.devをVS Code等のIDEにインストールし、Gemini APIをバックエンドに設定してデザイン生成を行う

- 出典: https://x.com/fumiya_kume/status/2035303547844338168
- 投稿者: Kuu
- カテゴリ: dev-tool

## なぜ使うのか

AI Proで余っているGeminiトークンを有効活用し、外部デザインツールへの移動なくデザイン→コード変換を完結できるため

## いつ使うのか

AI Proプランを契約しており、かつGeminiの月間枠が余っている状況で、小〜中規模のUIデザインが必要になったとき

### 具体的な適用場面

- AI Proプランを契約しているがGeminiの枠を使い切れていない
- Figmaとコードエディタを往復する手間を減らしたい
- 小規模なUIコンポーネントをその場で生成してすぐコード化したい
- デザイナー不在のチームで簡易的なUIプロトタイプが必要

## やり方

1. Pencil.dev の公式サイト（https://pencil.dev）からIDE拡張機能をインストール 2. 設定でLLMバックエンドにGemini APIを選択（AI Pro契約の場合、Geminiの無料枠が利用可能） 3. IDE内でキャンバスを開き、テキストプロンプトでUIコンポーネントを生成 4. 生成されたデザインをそのままコードとしてエクスポート

### 入力

- AI Proプランのアカウント（Gemini無料枠付き）
- Pencil.dev対応IDE（VS Code等）
- デザイン要件のテキストプロンプト

### 出力

- IDE内で生成されたUIデザイン
- 対応するコード（HTML/CSS/React等）
- Geminiトークン消費による枠の有効活用

## 使うツール・ライブラリ

- Pencil.dev
- Gemini API（AI Pro枠）
- VS Code / JetBrains IDE等

## 前提知識

- AI Proプランの契約とGemini無料枠の仕組み理解
- IDE（VS Code等）の基本操作
- Pencil.devの基本的な使い方
- HTMLやReact等のフロントエンド基礎知識

## 根拠

> 「AI Pro で無駄に余ってるGemini のTokenの使い道が決まったこと」

> 「nano bananaも枠内で生成できるのもメリットととして強いな」

> Pencil.dev公式サイト: 'Pencil fundamentally increases your engineering speed by bringing designing directly into your preferred IDE.'
