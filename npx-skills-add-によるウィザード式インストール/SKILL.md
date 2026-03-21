# npx skills add によるウィザード式インストール

> `npx skills add microsoft/skills` を実行すると、対話式ウィザードで必要なSkillだけを選択してインストールできる

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

132スキル全てをコピーすると context rot(注意散漫、トークン浪費、パターン混同)が起きる。プロジェクトに必要なものだけ選ぶことで、Agentの精度を保つ

## いつ使うのか

新規プロジェクトでSkillを導入する時、既存プロジェクトに必要なSkillだけ追加したい時

## やり方

1. `npx skills add microsoft/skills` を実行 2. ウィザードが起動し、言語・カテゴリ・個別Skillを選択 3. 選択したSkillが `.github/skills/` (または指定ディレクトリ)へコピー/symlinkされる 4. 既存のAGENTS.mdやcopilot-instructions.mdへ自動登録(オプション) 5. インストール後、`git add .github/skills/` でバージョン管理

### 入力

- microsoft/skills リポジトリ
- インストール先ディレクトリ(デフォルト `.github/skills/`)

### 出力

- 選択されたSkillのコピー/symlink
- AGENTS.md/copilot-instructions.md更新(オプション)

## 使うツール・ライブラリ

- npx
- skills CLI(推測)

## コード例

```
npx skills add microsoft/skills
# Interactive wizard:
# ? Select language: Python
# ? Select category: Foundry & AI
# ? Select skills: [x] azure-ai-projects-py [ ] azure-search-documents-py
# ✓ Installed to .github/skills/azure-ai-projects-py
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "Skills, custom agents, AGENTS.md templates, and MCP configurations for AI coding agents working with Azure SDKs and Microsoft AI Foundry."

> "132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery"

> "Use skills selectively. Loading all skills causes context rot: diluted attention, wasted tokens, conflated patterns."

> "Sensei-style Scoring — Skills are evaluated on frontmatter compliance: Low(Basic description only) / Medium(Description > 150 chars, has trigger keywords) / Medium-High(Has triggers AND anti-triggers) / High(Triggers + anti-triggers + compatibility field)"

> "128 skills with 1158 test scenarios — all skills have acceptance criteria and test scenarios."
