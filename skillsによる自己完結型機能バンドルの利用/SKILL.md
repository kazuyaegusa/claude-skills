# Skillsによる自己完結型機能バンドルの利用

> Instructions、サンプルコード、設定ファイルなどをフォルダ単位でバンドルしたSkillを導入し、特定の技術領域（例: React Testing Library, Docker, OpenAPI）の開発を加速する

- 出典: https://github.com/github/awesome-copilot
- 投稿者: github
- カテゴリ: infrastructure

## なぜ使うのか

単なるテキスト指示だけでなく、実行可能なサンプルや設定ファイルもセットで提供されるため、学習コストを削減し即座に実務適用できる

## いつ使うのか

特定フレームワーク、テスト手法、DevOps toolingなど複合的な知識が必要な開発タスクに取り組む時

## やり方

1. https://awesome-copilot.github.com/skills でSkillを検索
2. Skillフォルダをローカル環境またはプロジェクトに配置
3. Copilotが自動的にSkillフォルダ内のInstructionとアセットを読み込み
4. チャットやコード補完時にSkillの知識が適用される

### 入力

- Skillフォルダ（instructions.md、サンプルコード、設定ファイルを含む）
- 配置先パス（プロジェクトまたはグローバル設定）

### 出力

- 特定技術領域に特化したCopilot支援
- 即座に利用可能なサンプルコードとベストプラクティス

## 使うツール・ライブラリ

- GitHub Copilot
- VS Code
- Awesome Copilot Skills collection

## 前提知識

- GitHub Copilot（個人またはOrganizationサブスクリプション）
- VS CodeまたはCopilot CLI
- 基本的なGit操作知識
- 対象技術スタック（導入するagents/skills/instructionsが対象とする言語・フレームワーク）の基礎知識
