# React/Vue/Svelteでのフレームワーク統合知識をAIに持たせる

> GSAP AI Skillsに含まれるReact/Vue/Svelteでの正しいGSAP統合パターン（useGSAP・onMountでの初期化・クリーンアップ等）をAIに学習させる

- 出典: https://x.com/zeroz_jq/status/2035307813065597293
- 投稿者: 关木
- カテゴリ: skill-management

## なぜ使うのか

フレームワークのライフサイクルとGSAPのTimeline管理を適切に統合しないとメモリリークや再レンダリング時の不具合が発生するため

## いつ使うのか

React/Vue/SvelteでGSAPアニメーションを実装する際に、AIエージェントにフレームワーク最適化されたコードを生成させたい時

### 具体的な適用場面

- WebアニメーションをAIエージェントと共同開発する際に正確な実装を保証したい
- React/Vue/Svelteでスクロール駆動アニメーションを実装する際に、AIに適切なScrollTrigger設定を提案させたい
- 複数のAIエディタ（Cursor, Claude Code, Copilot等）で統一されたGSAPコーディング規約を維持したい
- AIエージェントにタイムラインベースの複雑なアニメーション設計を任せたい

## やり方

1. `npx skills add https://github.com/greensock/gsap-skills` でスキルをインストール 2. スキルに含まれるフレームワーク別のベストプラクティスがAIに読み込まれる 3. Reactではuseeffect・useGSAPフック、Vueではonmounted・onUnmounted、SvelteではonMount・onDestroyでのTimeline管理パターンがAI提案に反映される 4. AIがコンポーネントのクリーンアップも含めた完全な実装を提案するようになる

### 入力

- 使用フレームワーク（React/Vue/Svelte）
- アニメーション要件

### 出力

- フレームワークのライフサイクルに適合したGSAPコード
- 適切なクリーンアップ処理を含む実装

## 使うツール・ライブラリ

- GSAP
- React
- Vue
- Svelte
- useGSAP（Reactフック）

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
