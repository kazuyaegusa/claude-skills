# Codex環境向けにスキルをローカルインストール

> Codex（Google製CLI AI環境）でTrail of Bitsスキルを利用できるようにする

- 出典: https://github.com/trailofbits/skills
- 投稿者: trailofbits
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Code以外のAI環境でも同じスキルセットを使いたい場合がある。Codexネイティブのスキル検出機能に対応した形でインストールする必要がある

## いつ使うのか

Codex環境でTrail of Bitsのセキュリティスキルを使いたい時、または複数のAI環境で同じスキルセットを統一的に管理したい時

## やり方

1. `git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills` でリポジトリをクローン
2. `~/.codex/trailofbits-skills/.codex/scripts/install-for-codex.sh` を実行
3. Codexの`.codex/skills/`ツリー経由でスキルが検出可能になる

### 入力

- Codex環境
- trailofbits/skillsリポジトリへのアクセス

### 出力

- Codexから利用可能なスキルツリー
- ~/.codex/trailofbits-skills/ 配下のインストール済みスキル

## 使うツール・ライブラリ

- Codex
- git
- install-for-codex.sh スクリプト

## コード例

```
git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills
~/.codex/trailofbits-skills/.codex/scripts/install-for-codex.sh
```

## 前提知識

- Claude CodeまたはCodexのインストールと基本的な使い方
- セキュリティ監査・脆弱性分析の基礎知識
- 静的解析ツール（Semgrep, CodeQL等）の概要理解
- スマートコントラクト監査の場合は対象ブロックチェーンの知識
- 暗号解析スキルを使う場合はサイドチャネル攻撃の基礎知識

## 根拠

> Codex install: `git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills` then run install script
