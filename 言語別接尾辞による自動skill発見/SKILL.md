# 言語別接尾辞による自動Skill発見

> Skillファイル名に `-py`, `-dotnet`, `-ts`, `-java`, `-rust` 等の接尾辞を付けることで、Agent側が言語を自動判定して読み込む

- 出典: https://github.com/microsoft/skills
- 投稿者: microsoft
- カテゴリ: claude-code-workflow

## なぜ使うのか

従来はディレクトリ階層で言語を分けていたが、フラット構造+接尾辞の方が検索性が高く、複数言語対応のプロジェクトでも混乱しない。AI Agentが「このファイルはPython向け」と即座に判断できる

## いつ使うのか

複数言語のSDKスキルを同一リポジトリで管理し、Agentに自動選択させたい時。特にAzure SDKのようにPython/C#/TS/Java全対応のライブラリ群を扱う時

## やり方

1. `.github/skills/` 配下にスキルを作成する際、ファイル名を `<service>-<language>` 形式にする(例: `azure-cosmos-db-py`, `azure-search-documents-ts`) 2. YAMLフロントマターに `name: azure-cosmos-db-py` を記載 3. 従来の言語別ディレクトリ(`skills/python/`, `skills/dotnet/`)へはsymlinkを張る(後方互換性維持) 4. AI Agentは接尾辞でフィルタリングして必要なスキルだけ読み込む

### 入力

- スキル対象のSDK名とドキュメントURL
- 対象言語(python/dotnet/typescript/java/rust)

### 出力

- `.github/skills/<skill-name>-<lang>/SKILL.md` ファイル
- `skills/<lang>/<category>/` へのsymlink
- Agentが自動発見可能な状態

## 使うツール・ライブラリ

- ln (シンボリックリンク)
- YAMLフロントマター

## コード例

```
# 例: Python Cosmos DB skillを作成
mkdir -p .github/skills/azure-cosmos-db-py
echo '---\nname: azure-cosmos-db-py\ndescription: Cosmos DB patterns — FastAPI service layer, dual auth, partition strategies, TDD.\n---' > .github/skills/azure-cosmos-db-py/SKILL.md

# 後方互換用symlink
cd skills/python/data
ln -s ../../../.github/skills/azure-cosmos-db-py cosmos-db
```

## 前提知識

- AI Coding Agent(GitHub Copilot/Claude/Gemini等)の基本操作
- Git/シンボリックリンクの理解
- YAMLフロントマターの読み書き
- Azure SDK/Foundry SDK(対象ドメイン)の基礎知識
- CI/CD(GitHub Actions等)でのテスト自動化経験(テストハーネス活用時)

## 根拠

> "132 skills in `.github/skills/` — flat structure with language suffixes for automatic discovery"
