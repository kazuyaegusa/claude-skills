# Agent Skillsによる専門能力の注入

> Claude Codeに特定タスク（セキュリティ監査、ドキュメント生成、コード最適化等）を実行する専門知識とプロンプトをSKILL.mdファイルとして追加する

- 出典: https://github.com/hesreallyhim/awesome-claude-code
- 投稿者: hesreallyhim
- カテゴリ: claude-code-workflow

## なぜ使うのか

Claude Codeはデフォルトでは汎用的だが、ドメイン固有の深い知識や手順を持たない。Skillファイルを読み込ませることで、専門家レベルの分析・実装を再現可能にする

## いつ使うのか

特定の技術スタック（Rust、Go、TypeScript等）やタスク（セキュリティ監査、TDD、PRレビュー）に特化した処理を繰り返し実行する必要がある時

## やり方

1. `~/.claude/skills/` ディレクトリに `SKILL.md` を配置
2. ファイル内に「このスキルが適用される条件」「実行手順」「使用するツール」を明記
3. Claude Code起動時に自動読み込み、または `/skill-name` で明示的に呼び出し
4. 複数スキルを組み合わせてワークフロー全体を自動化

### 入力

- SKILL.mdファイル（マークダウン形式のプロンプト定義）
- 必要に応じてスクリプトやツール設定

### 出力

- Claude Codeが専門知識を持った状態で動作
- 再現性の高い高品質なコード・ドキュメント

## 使うツール・ライブラリ

- Trail of Bits Security Skills（セキュリティ監査）
- Superpowers（TDD、デバッグ、レビュー）
- AgentSys（ワークフロー自動化）

## コード例

```
# 例: ~/.claude/skills/security-audit/SKILL.md
---
name: security-audit
description: CodeQL/Semgrepによる脆弱性検出
---
1. `semgrep --config auto .` 実行
2. 検出された問題を分類
3. 修正案を提示
4. 再スキャンで検証
```

## 前提知識

- Claude Codeの基本的な使い方（CLI起動、プロンプト入力、ツール実行）
- Git/GitHubの基礎知識（ブランチ、コミット、PR）
- ターミナル操作とシェルスクリプトの基本
- Markdown記法の理解
- 使用する言語・フレームワークの基礎知識（TypeScript、Python、Go等）

## 根拠

> 「A selectively curated list of skills, agents, plugins, hooks, and other amazing tools for enhancing your Claude Code workflow」

> 「Agent skills are model-controlled configurations (files, scripts, resources, etc.) that enable Claude Code to perform specialized tasks requiring specific knowledge or capabilities」

> 「Hooks are a powerful API for Claude Code that allows users to activate commands and run scripts at different points in Claude's agentic lifecycle」

> 「Slash Commands are customized, carefully refined prompts that control Claude's behavior in order to perform a specific task」

> 「CLAUDE.md files are files that contain important guidelines and context-specific information or instructions that help Claude Code to better understand your project and your coding standards」
