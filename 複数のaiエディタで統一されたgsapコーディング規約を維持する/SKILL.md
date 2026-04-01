# 複数のAIエディタで統一されたGSAPコーディング規約を維持する

> Agent Skills形式を採用することで、Cursor・Claude Code・Codex・Windsurf・Copilot等40以上のAIエージェントに同一のGSAPスキルを適用し、チーム全体で一貫したコード品質を保つ

- 出典: https://x.com/zeroz_jq/status/2035307813065597293
- 投稿者: 关木
- カテゴリ: claude-code-workflow

## なぜ使うのか

開発者ごとに異なるAIエディタを使っていても、GSAPの書き方が統一されていればコードレビューコストが下がり、保守性が向上するため

## いつ使うのか

複数人チームでWebアニメーションプロジェクトを開発する際に、AIエージェント支援下でもコーディング規約を統一したい時

### 具体的な適用場面

- WebアニメーションをAIエージェントと共同開発する際に正確な実装を保証したい
- React/Vue/Svelteでスクロール駆動アニメーションを実装する際に、AIに適切なScrollTrigger設定を提案させたい
- 複数のAIエディタ（Cursor, Claude Code, Copilot等）で統一されたGSAPコーディング規約を維持したい
- AIエージェントにタイムラインベースの複雑なアニメーション設計を任せたい

## やり方

1. プロジェクトルートまたはグローバル設定で `npx skills add https://github.com/greensock/gsap-skills` を実行 2. Agent Skills仕様により、各AIエディタが自動的にスキルを認識する（Cursor→.cursorrules, Claude Code→.claude/skills/, Copilot→設定ファイル） 3. チームメンバー全員が同じコマンドでスキルを導入 4. 全員のAIエージェントが同じGSAPベストプラクティスを参照するようになる

### 入力

- チームメンバーが使用する各種AIエディタ
- プロジェクトの共有リポジトリ

### 出力

- 全AIエディタで統一されたGSAP実装パターン
- コードレビュー時の指摘減少

## 使うツール・ライブラリ

- Agent Skills CLI
- Cursor
- Claude Code
- Codex
- Windsurf
- GitHub Copilot
- その他40以上のエージェント

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
