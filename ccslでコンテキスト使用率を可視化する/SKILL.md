# ccslでコンテキスト使用率を可視化する

> Claude Codeのターミナルステータスラインに、コンテキストウィンドウの使用率をプログレスバー形式でリアルタイム表示する。

- 出典: https://x.com/masahirochaen/status/2038735267117346923
- 投稿者: チャエン | デジライズ CEO《重要AIニュースを毎日最速で発信》
- カテゴリ: claude-code-workflow

## なぜ使うのか

コンテキストが肥大化するほど精度が落ちるが、標準のUIでは使用量が見えないため、劣化に気づかないまま作業を続けてしまう。数値で見えることで適切なタイミングでリセットの判断ができる。

## いつ使うのか

Claude Codeで30分以上の連続作業をするとき。コンテキスト使用量を把握したいあらゆる場面。

### 具体的な適用場面

- 1時間以上のデバッグや機能実装セッションで、途中からClaude の回答精度が落ちてきた気がするとき
- コード量の多いリポジトリでClaude Codeを使っており、コンテキスト超過エラーや品質ムラが頻発しているとき

## やり方

1. `brew install usedhonda/tap/ccsl` でインストール（またはpip: `pip install ccsl`）
2. `ccsl --setup` を実行してClaude Code設定に組み込む
3. Claude Codeを再起動
4. ステータスラインに以下が表示される：
   - 1行目: モデル名、gitブランチ、ディレクトリ、メッセージ数、コスト
   - 2行目: `Context: ████████▒▒▒▒ [49%] 98.4K/200.0K` の形式でコンテキスト使用率
   - 3行目: セッションのスパークライン（5時間分、15分刻み）
   - 4行目: 週次スパークライン＋残り時間・予算
5. 表示行を絞る場合は `ccsl --show simple`（2・3行目のみ）または `ccsl --show 1,2`（指定行）

### 入力

- Python 3.9以上
- Claude Code（インストール済み）
- macOS（brewの場合）またはpip環境

### 出力

- ターミナルステータスラインへのリアルタイムコンテキスト使用率表示
- 80%で黄色、90%で赤色の色付き警告

## 使うツール・ライブラリ

- ccsl
- brew（macOS）または pip

## コード例

```
brew install usedhonda/tap/ccsl
ccsl --setup
# → Claude Code再起動で有効化
```

## 前提知識

- Claude Codeがインストール済みであること
- Python 3.9以上（pip経由でインストールする場合）
- macOS（brew経由の場合）

## 根拠

> 「長時間セッションでコンテキストが肥大すると、精度が落ちるので」

> 「コンテキスト使用率を常に可視化しつつ、80%超えたら強制リセットする運用」

> 「Context: ████████▒▒▒▒▒▒▒▒▒▒▒▒ [49%] 98.4K/200.0K」（README より）

> 「Context window progress bar with color warnings (yellow 80%, red 90%)」（README Features より）

> 「brew install usedhonda/tap/ccsl && ccsl --setup」（README Install より）
