# ECCを1コマンドでインストールしてClaude Codeを拡張する

> npmパッケージ `ecc-universal` をnpx経由で実行することで、Claude Code / Cursor に30エージェント・136スキル・60コマンドを一括追加する

- 出典: https://x.com/btcqzy1/status/2038853050643980475
- 投稿者: 爱丽丝呀！
- カテゴリ: claude-code-workflow

## なぜ使うのか

個別にエージェントやスキルを設定するのは手間がかかり、整合性も取れないため、動作検証済みのフルセットをパッケージとして導入することで即戦力化できる

## いつ使うのか

Claude Codeで複雑なプロジェクトを始めるとき、またはデフォルトのClaude Codeの品質に限界を感じたとき

### 具体的な適用場面

- Claude Codeで複雑なプロジェクトを開発しており、コードレビューやセキュリティスキャンを手動でやっていて時間が取られているとき
- PyTorch・Next.js等の特定フレームワークでの実装中に、AIが一般的すぎる・品質の低いコードを出力してくることが問題になっているとき
- 長時間セッションでコンテキスト上限に達してAPI費用が嵩んでいるとき

## やり方

1. Node.js環境で `npx ecc-universal` を実行（または `npm install -g ecc-universal` でグローバルインストール後に `ecc-universal` を実行）
2. Claude Code / Cursor のプロジェクトディレクトリで設定を適用
3. Claude Codeを再起動してエージェント・スキル・コマンドが認識されていることを確認
4. `/help` や `/review` などのコマンドが使えれば導入完了

### 入力

- Node.js環境
- Claude Code または Cursor のインストール済み環境

### 出力

- 30の専門エージェントが有効化されたClaude Code環境
- 136のスキル（PyTorch・Next.js等）が利用可能な状態
- 60のカスタムコマンド（/review等）が使えるClaude Code

## 使うツール・ライブラリ

- ecc-universal (npm)
- Claude Code
- Cursor

## コード例

```
npx ecc-universal
```

## 前提知識

- Claude Code または Cursor がインストールされていること
- Node.js（npx実行環境）が利用可能であること
- Claude Codeの基本操作（チャットでのコード依頼・スラッシュコマンド）を理解していること

## 根拠

> 「最新版内置了 30 个专属 Agent、136 项专业技能（Skills）和 60 个高阶命令」（30エージェント・136スキル・60コマンド）

> 「写完代码一个 /review 指令，AI 就会按生产级标准帮你挑刺、扫漏洞」（コードを書いた後に /review を実行すると本番基準でレビュー・脆弱性スキャン）

> 「预置了 Reviewer（审查者）、Security Scan（安全扫描） 等角格」（ReviewerとSecurity Scanエージェントが内蔵）

> 「智能提醒 /compact 压缩上下文，实测能省下大笔 API 费用」（/compactでコンテキスト圧縮・APIコスト削減を実測確認）

> GitHub README: '50K+ stars | 6K+ forks | 30 contributors | Anthropic Hackathon Winner'
