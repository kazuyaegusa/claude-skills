# SuperPowersプラグインをインストールしてワークフローを自動強制する

> SuperPowersをClaude CodeまたはCursorにインストールすることで、AIエージェントが自動的に要件深掘り→設計文書生成→実装計画→TDD→二重審査のフローに従うようになる

- 出典: https://x.com/jiroucaigou/status/2035964407201849564
- 投稿者: 努力赚钱的菜狗
- カテゴリ: claude-code-workflow

## なぜ使うのか

ユーザーが毎回プロンプトで「まず要件を整理して」と指示しなくても、スキルが自動トリガーされるためワークフローが再現可能になる。プロジェクト規模が大きくなっても設計崩壊を防げる

## いつ使うのか

新しいClaude Code / Cursorプロジェクトを開始するとき、またはAIが設計を無視してコードを書き始めることへの対策が必要なとき

### 具体的な適用場面

- Claude Code / Cursorで新機能を実装しようとするたびにAIが設計なしに書き始めて後悔する状況
- チームでAIコーディングを使っているが、各人がバラバラなプロンプト戦略を取っていて品質が安定しない状況
- AIが生成したコードが動くが後のリファクタ・バグ修正が困難になっているプロジェクト

## やり方

1. Claude Code公式マーケットプレイス経由: https://claude.com/plugins/superpowers からインストール
2. CLIで直接インストール: `npx @obra/superpowers install`
3. インストール後は特別な操作不要。次回コーディングタスクを与えるとスキルが自動起動する

### 入力

- Claude Code または Cursor の動作環境
- Node.js（npxが使える状態）

### 出力

- スキル群が~/.claude/skills/配下に配置された状態
- 次回のコーディング依頼からワークフローが自動起動

## 使うツール・ライブラリ

- obra/superpowers
- Claude Code plugin marketplace
- npx

## コード例

```
npx @obra/superpowers install
```

## 前提知識

- Claude Code または Cursor が動作する環境
- Node.js / npx が使える環境（CLIインストールの場合）
- git が使える環境（worktree機能のため）
- AIコーディングエージェントの基本的な使い方を知っていること

## 根拠

> 「SuperPowers制定了一套规则，让AI可以像资深团队一样有一套标准的开发流程。目前已在Github斩获106kstars」

> 「1.先疯狂提问，把你的需求完全理解，你同意后并生成标准设计文档」

> 「2.开新分支+隔离工作区，确保不会搞乱主代码」

> 「3.把任务拆分成最小子任务」

> 「4.交给子Agent执行并强制测试，最小代码也要通过测试」
