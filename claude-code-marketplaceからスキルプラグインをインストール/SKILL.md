# Claude Code Marketplaceからスキルプラグインをインストール

> Trail of BitsのセキュリティスキルリポジトリをClaude Codeのプラグインマーケットプレイスとして追加し、必要なスキルを選択的にインストールする

- 出典: https://github.com/trailofbits/skills
- 投稿者: trailofbits
- カテゴリ: claude-code-workflow

## なぜ使うのか

セキュリティ監査では専門的なワークフローが必要だが、毎回プロンプトを作るのは非効率。プラグイン化されたスキルを使うことで、専門家が設計した分析手法を即座に利用できる

## いつ使うのか

セキュリティ監査・脆弱性分析・コードレビューなどの専門的なタスクを開始する前に、関連するスキルセットを環境にセットアップしたい時

## やり方

1. `/plugin marketplace add trailofbits/skills` でマーケットプレイスを追加
2. `/plugin menu` でプラグイン一覧を表示
3. 必要なプラグイン（例: static-analysis, variant-analysis等）を選択してインストール
4. インストールしたスキルをClaude Codeセッション内で呼び出す

### 入力

- Claude Code環境
- 実施したいセキュリティタスクの種類（監査、脆弱性検出、ルール作成等）

### 出力

- インストール済みのセキュリティスキルプラグイン
- Claude Codeから呼び出し可能なドメイン特化ワークフロー

## 使うツール・ライブラリ

- Claude Code
- trailofbits/skills リポジトリ

## コード例

```
/plugin marketplace add trailofbits/skills
/plugin menu
```

## 前提知識

- Claude CodeまたはCodexのインストールと基本的な使い方
- セキュリティ監査・脆弱性分析の基礎知識
- 静的解析ツール（Semgrep, CodeQL等）の概要理解
- スマートコントラクト監査の場合は対象ブロックチェーンの知識
- 暗号解析スキルを使う場合はサイドチャネル攻撃の基礎知識

## 根拠

> Installation: `/plugin marketplace add trailofbits/skills` followed by `/plugin menu`

> Codex install: `git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills` then run install script

> 30+ plugins across categories: Smart Contract Security, Code Auditing, Malware Analysis, Verification, Reverse Engineering, Mobile Security, Development

> Local development: `cd /path/to/parent` then `/plugins marketplace add ./skills`

> Notable plugins: variant-analysis (find similar vulnerabilities), semgrep-rule-creator (custom detection), fp-check (false positive verification), constant-time-analysis (timing side-channels), static-analysis (CodeQL/Semgrep/SARIF)
