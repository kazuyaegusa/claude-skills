# nano bananaサイズのデザインを枠内生成する

> 小規模なUIコンポーネント（ボタン、アイコン、カード等）をPencil.devの無料枠内で生成し、即座にコード化する

- 出典: https://x.com/fumiya_kume/status/2035303547844338168
- 投稿者: Kuu
- カテゴリ: dev-tool

## なぜ使うのか

従来は有料プランが必要だった小規模デザイン生成が枠内で可能になり、コスト削減とイテレーション速度向上を両立できるため

## いつ使うのか

ボタン、アイコン、ラベル等の単一UI要素が必要で、手書きCSSよりも視覚的確認しながら調整したいとき

### 具体的な適用場面

- AI Proプランを契約しているがGeminiの枠を使い切れていない
- Figmaとコードエディタを往復する手間を減らしたい
- 小規模なUIコンポーネントをその場で生成してすぐコード化したい
- デザイナー不在のチームで簡易的なUIプロトタイプが必要

## やり方

1. Pencil.devでキャンバスを開く 2. 「nano banana」サイズ相当（ボタン1個、アイコン等の小要素）のプロンプトを入力 3. 生成されたデザインをプレビュー 4. 満足できればコードとしてエクスポート、不満があれば再生成（枠内で反復可能）

### 入力

- 小規模UIコンポーネントの要件（色、サイズ、テキスト等）
- Pencil.devの無料枠

### 出力

- nano bananaサイズのUIコンポーネント
- 対応するコード（CSS/React/Vue等）

## 使うツール・ライブラリ

- Pencil.dev

## 前提知識

- AI Proプランの契約とGemini無料枠の仕組み理解
- IDE（VS Code等）の基本操作
- Pencil.devの基本的な使い方
- HTMLやReact等のフロントエンド基礎知識

## 根拠

> 「AI Pro で無駄に余ってるGemini のTokenの使い道が決まったこと」

> 「nano bananaも枠内で生成できるのもメリットととして強いな」

> Pencil.dev公式サイト: 'Pencil fundamentally increases your engineering speed by bringing designing directly into your preferred IDE.'
