# EXTEND.mdによるスキルカスタマイズ

> 各スキルの動作を `EXTEND.md` ファイルで上書き・拡張し、デフォルト設定を変更せずにカスタマイズする

- 出典: https://github.com/JimLiu/baoyu-skills
- 投稿者: JimLiu
- カテゴリ: claude-code-workflow

## なぜ使うのか

スキル本体のSKILL.mdを変更するとアップデート時にコンフリクトが発生する。EXTEND.mdを別ファイルとして用意することで、アップデートとカスタマイズを両立

## いつ使うのか

ブランドカラーや独自用語集を使いたい場合、チーム固有のスタイルプリセットを定義したい場合

## やり方

1. プロジェクトレベル: `.baoyu-skills/<skill-name>/EXTEND.md` を作成
2. ユーザーレベル: `~/.baoyu-skills/<skill-name>/EXTEND.md` を作成
3. EXTEND.mdにカスタムパレット、スタイル、用語集などを記述
4. スキル実行時、EXTEND.mdの内容が読み込まれ、デフォルト設定を上書き

### 入力

- EXTEND.md(カスタム設定)
- スキル本体のSKILL.md

### 出力

- カスタマイズされたスキル動作

## コード例

```
mkdir -p .baoyu-skills/baoyu-cover-image
# Then create .baoyu-skills/baoyu-cover-image/EXTEND.md
## Custom Palettes
### corporate-tech
- Primary colors: #1a73e8, #4A90D9
```

## 前提知識

- Claude Codeの基本的な使い方とスキルの概念
- GitHubリポジトリの作成・管理
- JSON形式の理解(plugin-marketplace.json作成のため)
- 環境変数と.envファイルの扱い方
- Bashスクリプトの基本(ClawHub公開スクリプト利用時)
