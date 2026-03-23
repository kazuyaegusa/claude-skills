# Progressive Disclosure Architectureによる効率的なSkill読み込み

> Skillsを段階的に読み込むことで、コンテキストウィンドウを圧迫せずに多数のSkillsを利用可能にする

- 出典: https://github.com/travisvn/awesome-claude-skills
- 投稿者: travisvn
- カテゴリ: claude-code-workflow

## なぜ使うのか

全Skillsを常時ロードするとトークンを大量消費するが、メタデータのみ事前スキャンし、関連性が高いものだけフルロードすることで、複数Skillsの並行利用が現実的になる

## いつ使うのか

複数のSkillsを同時に利用可能にしたいが、コンテキストウィンドウの制約がある場合

## やり方

1. Claudeは全Skillsのメタデータ（name, description）を約100トークンでスキャン
2. タスクとの関連性を評価し、該当Skillsのフル命令（<5kトークン）をロード
3. 必要に応じてバンドルされたスクリプトやリソースを追加ロード

### 入力

- Skillsディレクトリ内のYAMLフロントマター付きSKILL.mdファイル

### 出力

- タスクに応じて動的にロードされた専門知識と実行可能スクリプト

## 前提知識

- Claude Pro/Max/Team/Enterpriseアカウント（Free tierはSkills非対応）
- Claude Code CLIまたはClaude.ai、Claude APIへのアクセス
- YAMLとMarkdownの基本知識
- gitによるバージョン管理の基礎（チーム配布する場合）
- Skillsが実行するスクリプト言語（Python、JavaScript等）の基礎知識（カスタムSkills作成時）

## 根拠

> Skills employ a progressive disclosure architecture for efficiency: 1. Metadata loading (~100 tokens): Claude scans available Skills to identify relevant matches 2. Full instructions (<5k tokens): Load when Claude determines the Skill applies 3. Bundled resources: Files and executable code load only as needed
