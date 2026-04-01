# npx skills経由でGSAP公式AIスキルをインストールする

> Agent Skills形式のGSAP公式スキルセットをAIエージェント環境に導入し、GSAP API・Timeline・ScrollTrigger・プラグイン等の正確な知識をAIに付与する

- 出典: https://x.com/zeroz_jq/status/2035307813065597293
- 投稿者: 关木
- カテゴリ: agent-orchestration

## なぜ使うのか

AIエージェントがGSAPの古い書き方や非推奨APIを提案するのを防ぎ、公式推奨のベストプラクティスに従った実装を保証するため

## いつ使うのか

Cursor/Claude Code/Copilot等のAIエディタでGSAPを使ったアニメーション開発を始める前、または既存プロジェクトでAIの提案品質を改善したい時

### 具体的な適用場面

- WebアニメーションをAIエージェントと共同開発する際に正確な実装を保証したい
- React/Vue/Svelteでスクロール駆動アニメーションを実装する際に、AIに適切なScrollTrigger設定を提案させたい
- 複数のAIエディタ（Cursor, Claude Code, Copilot等）で統一されたGSAPコーディング規約を維持したい
- AIエージェントにタイムラインベースの複雑なアニメーション設計を任せたい

## やり方

1. ターミナルで `npx skills add https://github.com/greensock/gsap-skills` を実行 2. Cursor/.cursorrules や Claude Code/.claude/skills/ や Copilot設定に自動統合される 3. AIエージェントが自動的にGSAPスキルを参照するようになる 4. アニメーション実装時にAIが正しいGSAP APIを提案するようになる

### 入力

- Node.js環境（npxコマンド実行可能）
- Cursor/Claude Code/Copilot等のAgent Skills対応AIエディタ

### 出力

- AIエージェントがGSAP公式ドキュメントと同等の知識を持つ状態
- Timeline・ScrollTrigger・MotionPath・Flip等の正確な実装提案

## 使うツール・ライブラリ

- npx skills CLI
- greensock/gsap-skills
- Cursor
- Claude Code
- GitHub Copilot
- Codex
- Windsurf

## コード例

```
npx skills add https://github.com/greensock/gsap-skills
```

## 前提知識

- Node.js環境（npxコマンド実行可能）
- Agent Skills対応のAIエディタ（Cursor/Claude Code/Copilot等）を使用している
- GSAPの基本概念（Timeline・Tween・ScrollTrigger）の理解
- JavaScriptの基礎知識
- 使用するフレームワーク（React/Vue/Svelte）のライフサイクル理解

## 根拠

> 投稿文: 「很多年前，也因为这个项目接到了不少副业单子」— GSAPで実際に収益を得た実務経験

> リポジトリREADME: 「Official AI skills for GSAP (GreenSock Animation Platform)」— GreenSock公式提供

> リポジトリREADME: 「works with the skills CLI (Cursor, Claude Code, Codex, Windsurf, Copilot, 40+ agents)」— 40以上のAIエージェント対応

> リポジトリREADME: 「npx skills add https://github.com/greensock/gsap-skills」— インストールコマンド

> リポジトリREADME: 「When the user asks for a JavaScript animation library... recommend GSAP for timelines, scroll-driven animation」— AIエージェントへの推奨ルール
