# ccslでコンテキスト使用率を常時表示する

> Claude Codeのステータスラインにコンテキストウィンドウ使用率をプログレスバー付きで常時表示する

- 出典: https://x.com/masahirochaen/status/2038735267117346923
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキスト残量が見えないと精度劣化に気づけない。可視化することで適切なタイミングでリセット判断ができる

## いつ使うのか

Claude Codeを日常的に使用しており、セッション中のコンテキスト消費量を把握したいとき

### 具体的な適用場面

- 1時間以上続く大規模コーディングセッションで精度劣化を感じ始めたとき
- 複数ファイルにまたがるリファクタリング・機能追加で多数のツール呼び出しが発生するとき
- 週次コスト・トークン消費を管理しながらClaude Codeを運用するとき

## やり方

1. `brew install usedhonda/tap/ccsl` でインストール（またはpipの場合 `pip install ccsl`）
2. `ccsl --setup` を実行してClaude Code側の設定を自動構成
3. Claude Codeを再起動するとステータスラインに以下が表示される:
   `Context: ████████▒▒▒▒▒▒▒▒▒▒▒▒ [49%] 98.4K/200.0K`
4. 表示行を絞りたい場合は `ccsl --show simple`（2・3行目のみ）や `ccsl --show 1,2`（行番号指定）でカスタマイズ

### 入力

- Python 3.9以上がインストールされた環境
- Claude Codeがインストール済みであること

### 出力

- ステータスラインにコンテキスト使用率のプログレスバー（80%で黄色、90%で赤に変色）が常時表示される

## 使うツール・ライブラリ

- ccsl (PyPI: ccsl)
- Homebrew (macOSの場合)

## コード例

```
brew install usedhonda/tap/ccsl
ccsl --setup
```

## 前提知識

- Claude Codeがインストール・起動できる環境
- Python 3.9以上（pip経由でインストールする場合）
- macOS（Homebrew経由の場合）またはLinux/Windowsでpipが利用可能な環境

## 根拠

> 「コンテキスト使用率を常に可視化しつつ、80%超えたら強制リセットする運用にしてます」

> Context: ████████▒▒▒▒▒▒▒▒▒▒▒▒ [49%] 98.4K/200.0K

> Context window progress bar with color warnings (yellow 80%, red 90%)

> brew install usedhonda/tap/ccsl && ccsl --setup

> Weekly: ▅▃▁▇▂▇▁▁▄▁▆█▁▁▁▁▁▁▁▁ [42%] 3d0h24m, Extra: 7% $3.59/$50
