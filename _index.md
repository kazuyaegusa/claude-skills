# スキルインデックス

合計: 363 スキル

| slug | 名前 | カテゴリ | 説明 | 出典 |
|------|------|----------|------|------|
| managed-settings経由でotel設定を強制配布 | Managed Settings経由でOTel設定を強制配布 | claude-code-workflow | Claude CodeのManaged Settings JSONファイルをMDMツール（Intune等）で全社員の端末 | ホリエ |
| otel-collectorでresource-attributeをlog-attributeにコピー | OTel CollectorでResource AttributeをLog Attributeにコピー | claude-code-workflow | OTel CollectorのTransform Processorを使い、Resource Attributeの情報を | ホリエ |
| cloud-loggingにlinked-datasetを作成してbigqueryから直接クエリ | Cloud LoggingにLinked Datasetを作成してBigQueryから直接クエリ | claude-code-workflow | Cloud LoggingのログバケットにLinked Datasetを作成し、BigQueryから直接SQL クエリで | ホリエ |
| api-requestイベントのcost-usdを集計して最適プランを自動判定 | api_requestイベントのcost_usdを集計して最適プランを自動判定 | claude-code-workflow | OTelで収集したapi_requestイベントのcost_usdフィールドをユーザー別・日別に集計し、固定料金プランと | ホリエ |
| タスクキューとしてlinearを活用する | タスクキューとしてLinearを活用する | agent-orchestration | LinearのIssueをAIエージェントへのジョブ投入口として使い、ステータス（not human / human / | 遠藤巧巳 - AIネイティブな会社の作り |
| cronで10分ポーリングループを構築する | cronで10分ポーリングループを構築する | agent-orchestration | cronジョブまたはsystemdタイマーでポーリングスクリプトを定期実行し、常駐プロセスなしにエージェントループを維持 | 遠藤巧巳 - AIネイティブな会社の作り |
| claude-pでタスクをノンインタラクティブ実行する | claude -pでタスクをノンインタラクティブ実行する | claude-code-workflow | `claude -p`（print mode）を使い、タスク内容を標準入力またはプロンプト引数として渡してClaudeC | 遠藤巧巳 - AIネイティブな会社の作り |
| タスク種別でエージェント処理を分岐する | タスク種別でエージェント処理を分岐する | agent-orchestration | タスクに『not human（AIが自律実行）』と『human（AIがリサーチのみ実行）』の2種別を設け、種別に応じて実 | 遠藤巧巳 - AIネイティブな会社の作り |
| 自宅常駐pcをエージェント基盤として活用する | 自宅常駐PCをエージェント基盤として活用する | claude-code-workflow | クラウドサーバーを使わず、自宅の常時起動LinuxPCをエージェントの実行基盤として使うアーキテクチャを採用する。 | 遠藤巧巳 - AIネイティブな会社の作り |
| homerowで画面全体をキーボード操作する | Homerowで画面全体をキーボード操作する | ui-ux | macOS上の全ネイティブアプリのボタン・リンク・UI要素に一時的なキーボードラベルを表示し、ラベルのキーを押すだけでク | Oikon |
| commandagentskillオーケストレーションパターンを使う | Command→Agent→Skillオーケストレーションパターンを使う | claude-code-workflow | スラッシュコマンド（/xxx）でワークフローを起動し、Agentが隔離コンテキストで実行し、Skillが再利用可能な知識 | Kyohei - OSS, 外資IT |
| claudemdを200行以内に管理する | CLAUDE.mdを200行以内に管理する | claude-code-workflow | プロジェクトルートのCLAUDE.mdは200行以下に保ち、大きくなったら `.claude/rules/` 配下のファ | Kyohei - OSS, 外資IT |
| コンテキスト50でmanual-compactを実行する | コンテキスト50%でmanual /compactを実行する | claude-code-workflow | コンテキスト使用率が50%に達したタイミングで手動で `/compact` を実行し、新タスクに切り替える時は `/cl | Kyohei - OSS, 外資IT |
| agent-teams-git-worktreesで並列開発する | Agent Teams + Git Worktreesで並列開発する | claude-code-workflow | 複数のClaude Codeエージェントをtmuxで並列起動し、各エージェントにgit worktreeで独立したブラン | Kyohei - OSS, 外資IT |
| プランモードを常に最初に使う | プランモードを常に最初に使う | claude-code-workflow | 実装に入る前に必ずPlan Mode（`Shift+Tab` またはメニューから）でClaudeに計画を立てさせ、承認し | Kyohei - OSS, 外資IT |
| loopで定期監視タスクをスケジュールする | /loopで定期監視タスクをスケジュールする | claude-code-workflow | Claude Codeの `/loop` コマンドで最大3日間、定期的なプロンプト実行をスケジュールし、デプロイ監視・P | Kyohei - OSS, 外資IT |
| パーミッションをワイルドカード構文で細かく制御する | パーミッションをワイルドカード構文で細かく制御する | claude-code-workflow | `dangerously-skip-permissions` の代わりに `/permissions` でワイルドカード | Kyohei - OSS, 外資IT |
| エレガントな解法プロンプトで品質を強制する | 「エレガントな解法」プロンプトで品質を強制する | claude-code-workflow | 平凡な修正が出た後に「knowing everything you know now, scrap this and i | Kyohei - OSS, 外資IT |
| askuserquestionツールでインタビュー形式の仕様収集をする | AskUserQuestionツールでインタビュー形式の仕様収集をする | claude-code-workflow | Claude Codeに `AskUserQuestion` ツールを使ったインタビュー形式で仕様を引き出させ、その後新 | Kyohei - OSS, 外資IT |
| esc-escrewindで脱線を即座にアンドゥする | Esc Esc（/rewind）で脱線を即座にアンドゥする | claude-code-workflow | Claudeが間違った方向に進んだ時、同じコンテキストで修正しようとせず `Esc Esc` または `/rewind` | Kyohei - OSS, 外資IT |
| claude-worktreeで並列エージェント起動 | claude --worktreeで並列エージェント起動 | claude-code-workflow | `claude --worktree`フラグを使い、各Claude Codeエージェントを独立したgit worktre | Boris Cherny |
| git-worktreeで独立作業環境を作成 | git worktreeで独立作業環境を作成 | claude-code-workflow | `git worktree add`でリポジトリに紐づいた複数の作業ディレクトリを作成し、それぞれで異なるブランチを同時 | Boris Cherny |
| 0xbreadguy--megaeth-ai-developer-skills | --- |  |  |  |
| abracadabra50--claude-code-voice-skill | --- |  |  |  |
| adeze--raindrop-mcp | Raindrop.io MCP Server |  |  |  |
| adityasugandhi--skillsync-mcp | SkillSync MCP — Security-Gated Skill Manager |  |  |  |
| agent-cards--skill | --- |  |  |  |
| airbnb--airflow | --- |  |  |  |
| albedo-tabai--lets-go-rss | --- |  |  |  |
| alexknowshtml--drawbridge | --- |  |  |  |
| anomalyco--opencode | --- |  |  |  |
| antonbabenko--terraform-skill | --- |  |  |  |
| apache--airflow | --- |  |  |  |
| apache--incubator-airflow | --- |  |  |  |
| aplaceforallmystuff--the-antislop | --- |  |  |  |
| appleboy--codegpt | --- |  |  |  |
| art9mid--arc-skill | --- |  |  |  |
| art9mid--react-native-arc | --- |  |  |  |
| arunjrk--audit-flow | --- |  |  |  |
| ashad001--remotion-transitions | --- |  |  |  |
| ashutos1997--claude-design-auditor-skill | --- |  |  |  |
| assafelovic--gpt-researcher | --- |  |  |  |
| autogluon--autogluon | --- |  |  |  |
| avdlee--swiftui-agent-skill | --- |  |  |  |
| axiaoge2--apple-hig-designer | --- |  |  |  |
| axtonliu--smart-illustrator | --- |  |  |  |
| better-auth--better-icons | --- |  |  |  |
| bitbond--token-tool-mcp | --- |  |  |  |
| blader--claude-code-continuous-learning-skill | --- |  |  |  |
| blader--claudeception | --- |  |  |  |
| blader--humanizer | --- |  |  |  |
| blader--razor | --- |  |  |  |
| blader--schematic | --- |  |  |  |
| blader--theorist | --- |  |  |  |
| bowenliang123--md_exporter | --- |  |  |  |
| browserwing--browserwing | --- |  |  |  |
| bytebase--dbhub | --- |  |  |  |
| cassmtnr--claude-code-starter | --- |  |  |  |
| checkra1neth--xbird-skill | --- |  |  |  |
| chromedevtools--chrome-devtools-mcp | --- |  |  |  |
| cli-argparse-subcommands | --- |  |  |  |
| cli-demo-runner | --- |  |  |  |
| codexstar69--bug-hunter | --- |  |  |  |
| coleam00--context-engineering-intro | --- |  |  |  |
| commonpaper--claude-skill | --- |  |  |  |
| conorbronsdon--avoid-ai-writing | --- |  |  |  |
| copilotkit--copilotkit | --- |  |  |  |
| cosmoblk--email-marketing-bible | --- |  |  |  |
| cyrus-cai--claude-cobrain | --- |  |  |  |
| d-kimuson--claude-code-viewer | --- |  |  |  |
| daaain--claude-code-log | --- |  |  |  |
| dammyjay93--claude-design-engineer | --- |  |  |  |
| dammyjay93--interface-design | --- |  |  |  |
| danielcanton--webxr-dev-skill | --- |  |  |  |
| danpeg--bug-hunt | --- |  |  |  |
| dataclass-models | --- |  |  |  |
| datadog-labs--agent-skills | --- |  |  |  |
| davidgeorgehope--elasticsearch-skill | --- |  |  |  |
| devswha--oh-my-humanizer | --- |  |  |  |
| dgallitelli--aws-hyperpod-skill | --- |  |  |  |
| digidai--product-manager-skills | --- |  |  |  |
| discord-context-search | --- |  |  |  |
| dotnet--core | --- |  |  |  |
| everyinc--charlie-cfo-skill | --- |  |  |  |
| everything-claude-code-ja | --- |  |  |  |
| expo--expo | --- |  |  |  |
| folder-digest | --- |  |  |  |
| forayconsulting--gemini_cli_skill | --- |  |  |  |
| frdel--agent-zero | --- |  |  |  |
| gabberflast--academic-pptx-skill | --- |  |  |  |
| game-asset-generator | --- |  |  |  |
| genielabsopensource--spine-animation-ai | --- |  |  |  |
| github-pr-automation | --- |  |  |  |
| gradio-app--gradio | --- |  |  |  |
| happycastle114--oh-my-openclaw | --- |  |  |  |
| hashgraph-online--registry-broker-skills | --- |  |  |  |
| homenshum--nodebench-ai | Skill: Flywheel UI Dogfood |  |  |  |
| html-arch-visualizer | --- |  |  |  |
| html-slide-generator | --- |  |  |  |
| htmlstreamofficial--preline | --- |  |  |  |
| huggingface--trl | --- |  |  |  |
| hugoduncan--criterium | --- |  |  |  |
| jax-transformer-ranker | --- |  |  |  |
| jcfischer--supertag-cli | Supertag CLI Skill |  |  |  |
| jftuga--transcript-critic | --- |  |  |  |
| jnemargut--better-plan-mode | --- |  |  |  |
| kadenzipfel--scv-scan | --- |  |  |  |
| kework-content-writer | --- |  |  |  |
| kework-customer-support | --- |  |  |  |
| kework-event-planning | --- |  |  |  |
| kework-message-draft | --- |  |  |  |
| kework-web-research | --- |  |  |  |
| kilo-org--kilocode | --- |  |  |  |
| kingkongshot--pensieve | --- |  |  |  |
| komal-skynet--claude-skill-homeassistant | --- |  |  |  |
| kridaydave--file-organizer-mcp | --- |  |  |  |
| lackeyjb--playwright-skill | --- |  |  |  |
| linear-api-client | --- |  |  |  |
| ludo-technologies--pyscn | --- |  |  |  |
| lukasniessen--terrashark | --- |  |  |  |
| marmelab--react-admin | --- |  |  |  |
| mixedbread-ai--mgrep | --- |  |  |  |
| modelcontextprotocol--typescript-sdk | --- |  |  |  |
| mrexodia--ida-pro-mcp | --- |  |  |  |
| multi-agent-patterns | --- |  |  |  |
| multi-agent-systems | --- |  |  |  |
| muratcankoylan--agent-skills-for-context-engineering | --- |  |  |  |
| mvanhorn--last30days-skill | --- |  |  |  |
| n1byn1kt--apitap | ApiTap — The MCP Server That Turns Any Website Into an API |  |  |  |
| ndpvt-web--latex-document-skill | --- |  |  |  |
| nextlevelbuilder--ui-ux-pro-max-skill | --- |  |  |  |
| nia-agent-cyber--openai-voice-skill | OpenAI Voice Skill |  |  |  |
| numman-ali--openskills | --- |  |  |  |
| numpy-ann-search | --- |  |  |  |
| op7418--humanizer-zh | --- |  |  |  |
| op7418--nanobanana-ppt-skills | PPT Generator Pro - Claude Code Skill |  |  |  |
| op7418--youtube-clipper-skill | --- |  |  |  |
| openai--openai-cookbook | --- |  |  |  |
| openhands--openhands | --- |  |  |  |
| pdf-logo-remover | --- |  |  |  |
| pdf-slide-editor | --- |  |  |  |
| phase-report | フェーズ完了レポート自動生成 |  |  |  |
| piebald-ai--tweakcc | --- |  |  |  |
| pingcap--tidb | --- |  |  |  |
| pixelml--agenticflow-skill | --- |  |  |  |
| pleaseprompto--google-ai-mode-skill | --- |  |  |  |
| pleaseprompto--notebooklm-skill | --- |  |  |  |
| polaroteam--moltdj-skill | --- |  |  |  |
| prefecthq--prefect | --- |  |  |  |
| project-review | --- |  |  |  |
| projectopensea--opensea-skill | --- |  |  |  |
| pubkey--rxdb | --- |  |  |  |
| quality-harness | --- |  |  |  |
| qwenlm--qwen-code | --- |  |  |  |
| rafsilva85--credit-optimizer-v5 | --- |  |  |  |
| ramsbaby--openclaw-self-healing | --- |  |  |  |
| realtime-feature-engine | --- |  |  |  |
| rebelytics--one-skill-to-rule-them-all | --- |  |  |  |
| reflectt--reflectt-node | SKILL.md — reflectt-node operator playbook |  |  |  |
| refly-ai--refly | --- |  |  |  |
| remotion-dev--skills | --- |  |  |  |
| repo-phuocdt--prompt-engineer-skill | --- |  |  |  |
| repo-security-clone | --- |  |  |  |
| repo-tracker | --- |  |  |  |
| risingwavelabs--risingwave | --- |  |  |  |
| rivradev--recite-agent-skill | name: recite |  |  |  |
| rohunvora--x-research-skill | --- |  |  |  |
| sammorrowdrums--remarkable-mcp | --- |  |  |  |
| sawyerhood--dev-browser | --- |  |  |  |
| scottcjn--grazer-skill | Grazer |  |  |  |
| severity1--claude-code-prompt-improver | --- |  |  |  |
| shadcn-ui--ui | --- |  |  |  |
| shap--shap | --- |  |  |  |
| significant-gravitas--autogpt | --- |  |  |  |
| silverov--yandex-direct-skill | --- |  |  |  |
| sinzin91--search-sessions | --- |  |  |  |
| slundberg--shap | --- |  |  |  |
| smithery-ai--cli | --- |  |  |  |
| sqlite-storage-pattern | --- |  |  |  |
| sstklen--claude-api-cost-optimization | --- |  |  |  |
| supabase--agent-skills | --- |  |  |  |
| synthetic-lab--octofriend | --- |  |  |  |
| terminal-ui-generator | --- |  |  |  |
| textgrad-optimizer | --- |  |  |  |
| ticket-to-pr-pipeline | --- |  |  |  |
| tobi--qmd | --- |  |  |  |
| topologyhealth--claudefhirskill | --- |  |  |  |
| tripleyak--skillforge | --- |  |  |  |
| trycua--cua | --- |  |  |  |
| ui-automation-agent | --- |  |  |  |
| ui-automation-agent-2 | --- |  |  |  |
| update-dashboards | --- |  |  |  |
| uriva--find-scene-skill | --- |  |  |  |
| vercel-labs--add-skill | --- |  |  |  |
| vercel-labs--skills | --- |  |  |  |
| voidborne-d--claude-code-pro | --- |  |  |  |
| volcengine--openviking | --- |  |  |  |
| voltagent--voltagent | --- |  |  |  |
| webzler--agentmemory | --- |  |  |  |
| wrsmith108--linear-claude-skill | --- |  |  |  |
| yoniassia--memclawz | --- |  |  |  |
| yusufkaraaslan--skill_seekers | Bootstrap Skill - Self-Hosting (v2.7.0) |  |  |  |
| zarazhangrui--frontend-slides | --- |  |  |  |
| zeframlou--call-me | Phone Call Input Skill |  |  |  |
| zooeyii--ship-page-skill | --- |  |  |  |
| npxで即時起動する | npxで即時起動する | automation-pipeline | Node.jsがあれば`npx n8n`一発でローカルにn8nエディタを起動する | n8n-io |
| dockerでデータ永続化デプロイする | Dockerでデータ永続化デプロイする | automation-pipeline | Dockerボリュームを作成してn8nコンテナを起動し、ワークフロー設定を永続化する | n8n-io |
| langchainでaiエージェントワークフローを構築する | LangChainでAIエージェントワークフローを構築する | agent-orchestration | n8nのAI-Nativeノードを使い、LangChainベースのAIエージェントを視覚的に組み込んだワークフローを作成 | n8n-io |
| カテゴリ別server検索 | カテゴリ別Server検索 | automation-pipeline | 機能ドメイン（ファイルシステム、データベース、コミュニケーション等）ごとに分類されたMCP Serverリストから目的の | punkpeye |
| 言語プラットフォーム絞り込み | 言語・プラットフォーム絞り込み | dev-tool | アイコン（🐍 Python, 📇 TypeScript, 🏎️ Go, 🦀 Rust等）とプラットフォーム表示（☁️ C | punkpeye |
| 公式評価済みserver優先 | 公式・評価済みServer優先 | other | 🎖️（公式実装）やGlamaスコアバッジで品質を判断し、信頼性の高いServerを選ぶ | punkpeye |
| 既存実装からの学習 | 既存実装からの学習 | other | 類似機能を持つMCP Serverのコードを参照し、実装パターンや設定方法を学ぶ | punkpeye |
| 役割特化エージェントによる並列オーケストレーション | 役割特化エージェントによる並列オーケストレーション | agent-orchestration | Sisyphus（メインエージェント、Opus 4.5 High）を中心に、Oracle（GPT 5.2 Medium： | code-yeongyu |
| lspast統合によるリファクタリングの信頼性向上 | LSP/AST統合によるリファクタリングの信頼性向上 | agent-orchestration | Language Server Protocol（LSP）とAST-Grepを使い、決定論的で安全なコード変更を実現 | code-yeongyu |
| todo-enforcer-による継続強制パターン | Todo Enforcer による継続強制パターン | agent-orchestration | LLMエージェントがタスクを途中で止めた場合、自動的に再開させて完了まで強制継続する仕組み | code-yeongyu |
| ultraworkキーワードによる全機能自動起動 | `ultrawork`キーワードによる全機能自動起動 | agent-orchestration | プロンプトに`ultrawork`（または短縮形`ulw`）を含めるだけで、全ての並列エージェント・探索・継続強制が自動 | code-yeongyu |
| コンテキスト分散戦略background-agents | コンテキスト分散戦略（Background Agents） | agent-orchestration | メインエージェントのコンテキストを軽く保つため、重い探索・検索タスクをバックグラウンドの専門エージェントに並列委譲する | code-yeongyu |
| comment-checkerによるコード品質保証 | Comment Checkerによるコード品質保証 | agent-orchestration | LLMが過剰なコメントを追加しようとすると警告し、人間が書いたコードと区別がつかないレベルに保つ | code-yeongyu |
| agent-skillsでドメイン専門知識を注入 | Agent Skillsでドメイン専門知識を注入 | claude-code-workflow | Claude Codeに特定分野（DevOps、科学計算、セキュリティ監査等）の専門的な知識と実行能力を付与する | hesreallyhim |
| hooksで開発プロセスをガードレール化 | Hooksで開発プロセスをガードレール化 | claude-code-workflow | Claude Codeのライフサイクルイベント（ファイル書き込み前、Bash実行前等）に自動チェック・承認ロジックを挿入 | hesreallyhim |
| slash-commandsでタスク固有プロンプトをテンプレート化 | Slash Commandsでタスク固有プロンプトをテンプレート化 | claude-code-workflow | 頻繁に使う複雑なプロンプト（PR作成、GitHub Issue修正、TDD実装等）を再利用可能なコマンドとして定義 | hesreallyhim |
| orchestratorsで複数エージェントを並列実行 | Orchestratorsで複数エージェントを並列実行 | claude-code-workflow | 複数のClaude Codeインスタンスを並列・階層的に管理し、大規模タスクを分散処理 | hesreallyhim |
| usage-monitorsでトークン消費を可視化分析 | Usage Monitorsでトークン消費を可視化・分析 | claude-code-workflow | Claude Codeのトークン使用量、コスト、バーンレート、セッション履歴を詳細に追跡・可視化 | hesreallyhim |
| claudemdでプロジェクト固有ルールを定義 | CLAUDE.mdでプロジェクト固有ルールを定義 | claude-code-workflow | リポジトリのルート、またはグローバル設定に配置するMarkdownファイルで、Claude Codeにプロジェクト固有の | hesreallyhim |
| ide-integrationsでエディタ内でclaude-codeを操作 | IDE Integrationsでエディタ内でClaude Codeを操作 | claude-code-workflow | VS Code、Neovim、Emacs等のエディタ内でClaude Codeとインタラクティブに対話 | hesreallyhim |
| mcpサーバー経由でlspベースのシンボル解析を提供する | MCPサーバー経由でLSPベースのシンボル解析を提供する | claude-code-workflow | Language Server Protocol実装をMCPサーバーでラップし、`find_symbol`/`inser | oraios |
| jetbrainsプラグインでより強力なコード解析を利用する | JetBrainsプラグインでより強力なコード解析を利用する | agent-orchestration | IntelliJ/PyCharm等のJetBrains IDE解析エンジンを使ってSerenaツールを提供し、LSPより | oraios |
| mcpoでmcp非対応llmchatgpt等にserenaを接続する | mcpoでMCP非対応LLM（ChatGPT等）にSerenaを接続する | agent-orchestration | mcpo（MCP to OpenAPI変換ツール）を使ってSerena MCPサーバーをOpenAPIエンドポイント化し | oraios |
| カスタムエージェントフレームワークにserenaツールを組み込む | カスタムエージェントフレームワークにSerenaツールを組み込む | agent-orchestration | Serenaのツール実装（`serena.agent.Tool`サブクラス）を独自エージェントフレームワークに移植し、フ | oraios |
| 3ファイルパターンによる永続化 | 3ファイルパターンによる永続化 | claude-code-workflow | 全ての複雑タスクで task_plan.md（フェーズと進捗）、findings.md（調査結果）、progress.m | OthmanAdi |
| hookによる注意操作attention-manipulation | Hookによる注意操作（Attention Manipulation） | claude-code-workflow | PreToolUse hookでツール実行前に task_plan.md を読み直し、PostToolUse hookで | OthmanAdi |
| セッションリカバリー機能 | セッションリカバリー機能 | claude-code-workflow | コンテキストが埋まり /clear を実行した際、~/.claude/projects/ から前回セッションデータを自動 | OthmanAdi |
| 2-actionルールによる発見保存 | 2-Actionルールによる発見保存 | context-management | view や browser 操作を2回実行するごとに、発見した情報を findings.md に保存する。 | OthmanAdi |
| エラーの永続化とアプローチ変更 | エラーの永続化とアプローチ変更 | agent-orchestration | 失敗したアクションとその理由を progress.md に記録し、同じ方法を5回繰り返さず、試行回数とアプローチ変更を追 | OthmanAdi |
| マルチプラットフォーム対応スキル配布 | マルチプラットフォーム対応スキル配布 | claude-code-workflow | Agent Skills仕様（agentskills.io）に準拠したSKILL.mdと、各IDE固有のフォーマット（h | OthmanAdi |
| waspテンプレートで即座にsaas基盤を構築する | Waspテンプレートで即座にSaaS基盤を構築する | claude-code-workflow | Wasp CLIの`wasp new -t saas`コマンドで、認証・決済・メール・ジョブ・UI・AI統合が事前設定さ | wasp-lang |
| waspの宣言的設定で認証を数行で実装する | Waspの宣言的設定で認証を数行で実装する | ui-ux | Waspの設定ファイルに認証プロバイダーを宣言するだけで、フルスタック認証（Email確認・ソーシャルログイン）を自動生 | wasp-lang |
| waspのバックグラウンドジョブでcronキュー処理を設定する | Waspのバックグラウンドジョブでcron/キュー処理を設定する | automation-pipeline | Waspの設定ファイルでジョブ関数を宣言し、cron式またはキューとして自動実行する仕組みを構築する | wasp-lang |
| 型安全なエンドツーエンド通信を自動生成する | 型安全なエンドツーエンド通信を自動生成する | dev-tool | バックエンドの関数型を定義すると、Waspがフロントエンドで型推論されたRPC関数を自動生成する | wasp-lang |
| ワンコマンドでrailwayflyioへデプロイする | ワンコマンドでRailway/Fly.ioへデプロイする | infrastructure | Wasp CLIの`wasp deploy`コマンドで、DB・サーバー・クライアントを一括でホスティングサービスにデプロ | wasp-lang |
| ai開発ツール向けのagentsmdスキルを活用する | AI開発ツール向けのAGENTS.md/スキルを活用する | claude-code-workflow | プロジェクトに同梱されたAGENTS.md、Cursorルール、llms-full.txtをAIコーディングツール（Cl | wasp-lang |
| awesome-listでスキルを分野別に整理して公開する | Awesome Listでスキルを分野別に整理して公開する | ui-ux | GitHubでClaude Skillsを11カテゴリ（Document, Development, Data, Sci | BehiSecc |
| セキュリティスキルを開発ワークフローに組み込む | セキュリティスキルを開発ワークフローに組み込む | claude-code-workflow | VibeSec-Skill（OWASP Top 10対応）やTrail of Bits Skills（CodeQL/Se | BehiSecc |
| スキル発見導入検証のワークフローを確立する | スキル発見→導入→検証のワークフローを確立する | claude-code-workflow | Awesome Listからスキルを検索し、ローカルにクローンして試用、プロジェクトに適合するか検証してから正式採用する | BehiSecc |
| mcp-serverとskillを併用して機能を拡張する | MCP ServerとSkillを併用して機能を拡張する | claude-code-workflow | MCP（Model Context Protocol）サーバーとClaude Skillsを組み合わせ、外部API（Li | BehiSecc |
| git-worktreeによるエージェント隔離 | git worktreeによるエージェント隔離 | claude-code-workflow | 各タスクを独立したgit worktree（ブランチ＋作業ディレクトリ）に割り当て、複数エージェントが同一リポジトリで干 | superset-sh |
| workspace-preset自動化 | workspace preset自動化 | agent-orchestration | workspace作成時に環境変数コピー、依存インストール、初期セットアップスクリプトを自動実行し、エージェントが即座に | superset-sh |
| 統合エージェントモニタリング | 統合エージェントモニタリング | agent-orchestration | 複数稼働中のエージェントのステータスを一元UIで監視し、変更準備完了時に通知を受け取る | superset-sh |
| キーボードショートカットによる高速切り替え | キーボードショートカットによる高速切り替え | agent-orchestration | ⌘1-9でworkspace直接切り替え、⌘Nで新規作成等のショートカットでタスク間を瞬時に移動する | superset-sh |
| ビルド済みバイナリによる即座導入 | ビルド済みバイナリによる即座導入 | agent-orchestration | GitHubリリースページから.dmg/.appをダウンロードし、ビルド不要で即座にSupersetを利用開始する | superset-sh |
| skillmd形式でエージェント用知識を構造化 | SKILL.md形式でエージェント用知識を構造化 | claude-code-workflow | フロントマター + 指示・ワークフロー・意思決定フレームワークをMarkdownで定義し、AIエージェントが解釈可能な形 | alirezarezvani |
| マルチツール変換スクリプトによる11ツール対応 | マルチツール変換スクリプトによる11ツール対応 | claude-code-workflow | ./scripts/convert.sh を実行して、全スキルを Cursor (.mdc), Aider (CONVE | alirezarezvani |
| スキルセキュリティ監査による安全性担保 | スキルセキュリティ監査による安全性担保 | claude-code-workflow | skill-security-auditor を使って、インストール前にスキルのコード・指示内容をスキャンし、コマンドイ | alirezarezvani |
| スキルエージェントペルソナの3層オーケストレーション | スキル・エージェント・ペルソナの3層オーケストレーション | claude-code-workflow | スキル（How）、エージェント（What）、ペルソナ（Who）を組み合わせて、ドメイン横断的な複雑タスクをフェーズ分けし | alirezarezvani |
| stdlib依存のみの254-pythonツール提供 | stdlib依存のみの254 Pythonツール提供 | claude-code-workflow | pip install不要、Python標準ライブラリのみで動作する254個のCLIツールを各スキルに同梱 | alirezarezvani |
| x-scout | X Scout - X投稿からの技術発見・スキル化 | sennin-scout | X投稿URLを受け取り、技術情報の抽出・スキル化・再現キット生成・検証レポート作成を自動実行するスキル | sennin_scout |
| serenaをmcpサーバーとして起動してllmクライアントに接続 | SerenaをMCPサーバーとして起動してLLMクライアントに接続 | claude-code-workflow | Serenaを各種LLMクライアント（Claude Code/Desktop、VSCode、Cursor、Cline等） | oraios |
| lspバックエンドで30以上の言語にシンボル解析を適用 | LSPバックエンドで30以上の言語にシンボル解析を適用 | agent-orchestration | Language Server Protocol実装をSerena経由で利用し、多言語プロジェクト（Python、JS/ | oraios |
| jetbrainsプラグインバックエンドで最強の解析精度を実現 | JetBrainsプラグインバックエンドで最強の解析精度を実現 | agent-orchestration | Serena JetBrainsプラグインをインストールし、IntelliJ/PyCharm/WebStorm等のIDE | oraios |
| mcpo経由でchatgpt等の非mcp対応クライアントに統合 | mcpo経由でChatGPT等の非MCP対応クライアントに統合 | agent-orchestration | mcpo（MCP to OpenAPI変換ツール）を使い、MCPをサポートしないクライアント（ChatGPT等）でもSe | oraios |
| カスタムエージェントフレームワークへのserenaツール組み込み | カスタムエージェントフレームワークへのSerenaツール組み込み | agent-orchestration | Serenaのツール実装（serena.agent.Tool）をサブクラス化し、独自のエージェントフレームワークに統合す | oraios |
| typescript-pieces-frameworkによるmcp自動公開 | TypeScript pieces frameworkによるMCP自動公開 | automation-pipeline | TypeScriptでワークフロー統合（pieces）を作成すると、それが自動的にMCPサーバーとしてClaude De | activepieces |
| セルフホスト可能なノーコードプロコードハイブリッドアーキテクチャ | セルフホスト可能なノーコード×プロコードハイブリッドアーキテクチャ | automation-pipeline | ノーコードビルダーでワークフローを構築しつつ、TypeScriptによるカスタム拡張を可能にし、全体をセルフホストできる | activepieces |
| human-in-the-loopパターンの標準pieces化 | Human-in-the-loopパターンの標準pieces化 | automation-pipeline | 承認待ち、遅延実行、人間入力（チャット、フォーム）をpiecesとして標準実装し、AIワークフローに組み込めるようにする | activepieces |
| オープンエコシステムによる280統合の集約 | オープンエコシステムによる280+統合の集約 | automation-pipeline | npmjs.comを統合パッケージのリポジトリとして使い、コミュニティが作成した統合（60%がコミュニティ貢献）を集約・ | activepieces |
| waspテンプレートからプロジェクト初期化 | Waspテンプレートからプロジェクト初期化 | automation-pipeline | Wasp CLIの公式SaaSテンプレートを使い、認証・決済・ジョブ・UI・デプロイ設定を含むプロジェクトを生成する | wasp-lang |
| waspの宣言的設定でフルスタック認証を実装 | Waspの宣言的設定でフルスタック認証を実装 | dev-tool | Waspの設定ファイル（wasp.config）に認証方式（email/Google/GitHub/Slack等）を記述 | wasp-lang |
| waspのジョブ定義でcronとキューを実装 | Waspのジョブ定義でcronとキューを実装 | automation-pipeline | 設定ファイルにジョブ（cron/キュー）を宣言し、TypeScript関数を実装するだけでバックグラウンド処理を実行する | wasp-lang |
| end-to-end型安全性でフロントバック連携 | End-to-End型安全性でフロント・バック連携 | dev-tool | バックエンドのクエリ/アクション関数にTypeScript型を付けると、フロントエンドで自動的に型推論されたAPIが利用 | wasp-lang |
| ai開発ツール向けメタデータ同梱 | AI開発ツール向けメタデータ同梱 | claude-code-workflow | Claude Code・Cursor等のAIエージェントが読み取る専用ドキュメント（AGENTS.md、llms-ful | wasp-lang |
| ワンコマンドデプロイでdbサーバークライアントを一括公開 | ワンコマンドデプロイでDB・サーバー・クライアントを一括公開 | infrastructure | Wasp CLIの `wasp deploy` コマンドでRailway/Fly.ioへDB・バックエンド・フロントエン | wasp-lang |
| cuabotで既存エージェントをサンドボックス化 | CuaBotで既存エージェントをサンドボックス化 | claude-code-workflow | Claude CodeやOpenClaw等の任意のコーディングエージェントを、分離された仮想デスクトップ環境で動かす | trycua |
| cua-agentでcomputer-use-agentを実装 | Cua AgentでComputer-Use Agentを実装 | agent-orchestration | Python SDKを使い、スクリーン認識・UI操作・タスク実行を行うLLMエージェントを数行で構築する | trycua |
| cua-benchで既存ベンチマーク実行 | Cua-Benchで既存ベンチマーク実行 | agent-orchestration | OSWorld、ScreenSpot、Windows Arena等の公開データセットで自作エージェントを評価する | trycua |
| lumeでmacos仮想環境を高速起動 | LumeでmacOS仮想環境を高速起動 | agent-orchestration | Apple Silicon Mac上でmacOS VMを数秒で起動し、エージェント開発・テストに使う | trycua |
| cuabotの画面操作コマンドで軽量ワークフロー実行 | CuaBotの画面操作コマンドで軽量ワークフロー実行 | agent-orchestration | LLMエージェントを使わず、cuabotコマンド単体でスクリーンショット・クリック・タイプ操作を実行する | trycua |
| 段階的開示アーキテクチャでskillsを設計する | 段階的開示アーキテクチャでSkillsを設計する | claude-code-workflow | Claude Skillsを、メタデータスキャン（~100トークン）→フル命令ロード（<5kトークン）→リソースロード（ | travisvn |
| skill-creatorで対話的にskillを生成する | skill-creatorで対話的にSkillを生成する | claude-code-workflow | Anthropic公式のskill-creator Skillを使い、Q&A形式で新しいSkillを作成する | travisvn |
| claude-code-cliでskillをインストール管理する | Claude Code CLIでSkillをインストール・管理する | claude-code-workflow | マーケットプレイスまたはローカルディレクトリから、/pluginコマンドでSkillをインストールする | travisvn |
| web-uiでskillsトグルを有効化管理する | Web UIでSkillsトグルを有効化・管理する | ui-ux | Claude.ai Web インターフェースの Settings > Capabilities でSkillsを有効化し | travisvn |
| skills-vs-promptsprojectssubagentsmcpを使い分ける | Skills vs Prompts/Projects/Subagents/MCPを使い分ける | agent-orchestration | タスクの性質に応じて、Skills、システムプロンプト、Projects、Subagents、MCPを適切に選択する | travisvn |
| 公式skillsでoffice形式pdf操作を自動化する | 公式SkillsでOffice形式・PDF操作を自動化する | automation-pipeline | docx/pdf/pptx/xlsx公式Skillsを使い、Word/PowerPoint/Excel/PDFの作成・編 | travisvn |
| frontend-design-skillでaiっぽいデザインを回避する | frontend-design Skillで「AIっぽいデザイン」を回避する | ui-ux | frontend-design Skillを使い、Claude生成のReact+Tailwindコードで平凡な美学を避け | travisvn |
| obrasuperpowersで20バトルテスト済みskillsを一括導入する | obra/superpowersで20+バトルテスト済みSkillsを一括導入する | claude-code-workflow | Jesse Vincentによるコミュニティライブラリ obra/superpowers をマーケットプレイス経由でイン | travisvn |
| セキュリティベストプラクティスでskillsを安全運用する | セキュリティベストプラクティスでSkillsを安全運用する | claude-code-workflow | Skillsインストール前にSKILL.mdと全スクリプトをレビューし、信頼できるソースからのみ導入、バージョン管理とコ | travisvn |
| claude-skillsをカテゴリ別に分類して発見可能にする | Claude Skillsをカテゴリ別に分類して発見可能にする | ui-ux | 400以上のスキルを12のカテゴリ（Document、Development、Data、Scientific、Writi | BehiSecc |
| vibesec-skillで脆弱性を防ぐ | VibeSec-Skillで脆弱性を防ぐ | claude-code-workflow | Claude Codeでセキュアなコードを書くための専用スキル（VibeSec-Skill）を導入し、一般的な脆弱性を予 | BehiSecc |
| skill-creatorで新規スキルを開発する | skill-creatorで新規スキルを開発する | claude-code-workflow | Anthropics公式のskill-creatorテンプレートを使って、標準的な構造を持つClaude Skillを作 | BehiSecc |
| mcp-serverでスキルを動的に拡張する | MCP Serverでスキルを動的に拡張する | claude-code-workflow | Model Context Protocol（MCP）Serverを実装して、Claude Codeの機能を動的にAPI | BehiSecc |
| agentskillsio仕様でスキルを標準化する | agentskills.io仕様でスキルを標準化する | claude-code-workflow | agentskills.io（またはagentskill.sh）のスキル仕様に従って、Claude Code以外のAIツ | BehiSecc |
| git-worktreeでエージェントタスクを分離する | git worktreeでエージェントタスクを分離する | claude-code-workflow | 各エージェントタスクに専用のgit worktree（独立した作業ディレクトリ+ブランチ）を割り当て、タスク間の干渉を物 | superset-sh |
| workspace-presetsでエージェント環境を自動セットアップする | Workspace Presetsでエージェント環境を自動セットアップする | agent-orchestration | .superset/config.json にsetup/teardownスクリプトを定義し、ワークスペース作成時の環境 | superset-sh |
| エージェント監視とクイックコンテキストスイッチング | エージェント監視とクイックコンテキストスイッチング | agent-orchestration | Supersetのモニタリング機能で全エージェントの状態を1画面で追跡し、変更準備完了の通知を受け取る。⌘1-9で瞬時に | superset-sh |
| 任意のcliエージェントをsupersetで実行する | 任意のCLIエージェントをSupersetで実行する | claude-code-workflow | Claude Code, Cursor Agent, Copilot, Gemini CLI等、あらゆるCLIベースのコ | superset-sh |
| mcpクライアントサーバーアーキテクチャでllmコンテキスト提供を標準化する | MCPクライアント・サーバーアーキテクチャでLLMコンテキスト提供を標準化する | prompt-engineering | Model Context Protocol (MCP)を使い、LLMアプリケーション（MCPホスト）とデータソース・ツ | microsoft |
| monorepoで複数mcpサーバーを統一管理し共通toolingで品質リリースを効率化する | monorepoで複数MCPサーバーを統一管理し、共通toolingで品質・リリースを効率化する | automation-pipeline | microsoft/mcpリポジトリで、Azure MCP, Fabric MCP等のサーバー実装をまとめて管理し、co | microsoft |
| local型とremote型mcpサーバーを用途別に使い分ける | Local型とRemote型MCPサーバーを用途別に使い分ける | infrastructure | Local型（stdio, コマンド実行）は開発者環境で直接実行、Remote型（HTTP, HTTPS URL）はクラ | microsoft |
| ide拡張とmcpサーバーを1クリックインストール可能にする | IDE拡張とMCPサーバーを1クリックインストール可能にする | prompt-engineering | VS Code/Visual Studio/IntelliJ用のインストールリンク（vscode:mcp/install | microsoft |
| mcpサーバーをカテゴリ別に分類し用途別検索可能なカタログで提供する | MCPサーバーをカテゴリ別に分類し、用途別検索可能なカタログで提供する | infrastructure | CLOUD AND INFRASTRUCTURE, DEVELOPER TOOLS, PRODUCTIVITY, DAT | microsoft |
| azure-developer-cli-azd-テンプレートとmcpサーバーを連携させインフラ付きでデプロイ可能にする | Azure Developer CLI (azd) テンプレートとMCPサーバーを連携させ、インフラ付きでデプロイ可能にする | context-management | azd templates（Bicep/Terraform等のIaC含む）にMCP統合を組み込み、`azd up`一発で | microsoft |
| github-copilot-cliプラグインとしてmcpサーバーを配布する | GitHub Copilot CLIプラグインとしてMCPサーバーを配布する | automation-pipeline | Copilot CLI (/plugin install形式) でMCPサーバーの機能を提供し、ターミナルからAzure | microsoft |
| agentgatewayを介したmcpa2a通信の透過プロキシ化 | agentgatewayを介したMCP/A2A通信の透過プロキシ化 | agent-orchestration | AIエージェントとMCPサーバー（またはAgent）間の通信をagentgatewayに中継させ、認証・監視・ポリシー適 | agentgateway |
| openapiをmcpリソースに変換してエージェントに公開 | OpenAPIをMCPリソースに変換してエージェントに公開 | agent-orchestration | 既存のREST APIのOpenAPI定義をagentgatewayに読み込ませ、エージェントがMCPプロトコル経由で呼 | agentgateway |
| kubernetes-gateway-apiでエージェント通信を動的管理 | Kubernetes Gateway APIでエージェント通信を動的管理 | agent-orchestration | Kubernetes上のエージェントをGateway APIのHTTPRoute/TLSRoute等で宣言的にルーティン | agentgateway |
| mcpa2a特化rbacでエージェント権限を制御 | MCP/A2A特化RBACでエージェント権限を制御 | agent-orchestration | agentgatewayのRBACシステムを使い、どのエージェントがどのMCPリソース（ツール・プロンプト・サンプリング | agentgateway |
| oauth認証で無料gemini-3モデルを即座に利用する | OAuth認証で無料Gemini 3モデルを即座に利用する | context-management | Google OAuthログイン経由で、APIキー不要・日1000リクエスト枠のGemini 3モデル（1Mトークン）に | google-gemini |
| 非対話モードでjson出力を取得してcicdに統合する | 非対話モードでJSON出力を取得してCI/CDに統合する | agent-orchestration | Gemini CLIを`-p`フラグ付きで実行し、`--output-format json`または`stream-js | google-gemini |
| mcp-serverで外部ツールを拡張しエージェントワークフローを構築する | MCP Serverで外部ツールを拡張しエージェントワークフローを構築する | agent-orchestration | ~/.gemini/settings.jsonにMCP（Model Context Protocol）サーバー定義を追加 | google-gemini |
| geminimdでプロジェクト固有のコンテキストを永続化する | GEMINI.mdでプロジェクト固有のコンテキストを永続化する | claude-code-workflow | リポジトリルートまたはホームディレクトリに`GEMINI.md`を配置し、プロジェクトのアーキテクチャ・コーディング規約 | google-gemini |
| チェックポイント機能で長時間セッションを保存再開する | チェックポイント機能で長時間セッションを保存・再開する | context-management | Gemini CLIのチェックポイント機能で、対話履歴とコンテキストをスナップショットとして保存し、後日同じ状態から作業 | google-gemini |
| google-search-groundingでリアルタイム情報を統合する | Google Search groundingでリアルタイム情報を統合する | prompt-engineering | Gemini CLIの組み込みGoogle Search grounding機能を使い、LLMの応答に最新のWeb情報を | google-gemini |
| 制限環境でanaconda経由でインストールする | 制限環境でAnaconda経由でインストールする | dev-tool | 企業ネットワークやエアギャップ環境でnpm直接インストールが困難な場合、Anacondaでnode.js環境を作成してか | google-gemini |
| claude-codeの公式推奨インストール | Claude Codeの公式推奨インストール | claude-code-workflow | npmではなく公式インストールスクリプトまたはパッケージマネージャーを使ってClaude Codeをインストールする | anthropics |
| プロジェクトディレクトリでclaude-codeを起動する | プロジェクトディレクトリでClaude Codeを起動する | claude-code-workflow | コードベースのルートディレクトリに移動してから `claude` コマンドを実行し、対話セッションを開始する | anthropics |
| bugコマンドでバグレポートを送信する | /bugコマンドでバグレポートを送信する | claude-code-workflow | Claude Codeセッション内で `/bug` コマンドを実行し、問題を直接AnthropicのGitHub Iss | anthropics |
| プラグインでclaude-codeを拡張する | プラグインでClaude Codeを拡張する | claude-code-workflow | 公式リポジトリのpluginsディレクトリにあるプラグインを導入し、カスタムコマンドやエージェント機能を追加する | anthropics |
| agent-skills-でドメイン知識を注入する | Agent Skills でドメイン知識を注入する | claude-code-workflow | Claude Code に専門分野の知識・ワークフローを教え込み、特定タスクを自律実行させる仕組み。Skills は「モ | hesreallyhim |
| hooks-でライフサイクルに介入する | Hooks でライフサイクルに介入する | claude-code-workflow | Claude Code の動作ライフサイクル（ツール呼び出し前後、ファイル書き込み前後など）に独自スクリプトを挿入し、品 | hesreallyhim |
| slash-commands-で定型プロンプトを再利用する | Slash-Commands で定型プロンプトを再利用する | claude-code-workflow | 頻繁に使うプロンプトを `/commit`, `/tdd`, `/analyze-issue` などのコマンドとして登録 | hesreallyhim |
| workflows-で複数ステージのプロセスを構造化する | Workflows で複数ステージのプロセスを構造化する | claude-code-workflow | 開発プロセス全体（Research → Plan → Execute → Review など）を明示的なステージに分割し | hesreallyhim |
| マルチエージェント並列実行でタスク分散 | マルチエージェント並列実行でタスク分散 | claude-code-workflow | 複数の Claude Code インスタンスを並列に起動し、それぞれ独立したタスクを実行させることで、開発速度を向上させ | hesreallyhim |
| 使用量監視でコストトークン消費を可視化 | 使用量監視でコスト・トークン消費を可視化 | claude-code-workflow | Claude Code のローカルログ（`.jsonl` ファイル）を解析し、トークン消費量・コスト・セッション履歴をダ | hesreallyhim |
| claudemd-でプロジェクト文脈を注入 | CLAUDE.md でプロジェクト文脈を注入 | claude-code-workflow | プロジェクトルートまたは `~/.claude/` に配置する Markdown ファイルで、プロジェクト固有のルール・ | hesreallyhim |
| プラグインのインストールと利用 | プラグインのインストールと利用 | agent-orchestration | Awesome Copilotマーケットプレイスから公開されているプラグイン（agents/skills/instruc | github |
| instructionsによるファイルパターン別コーディング規約の自動適用 | Instructionsによるファイルパターン別コーディング規約の自動適用 | prompt-engineering | 特定のファイルパターン（例: *.ts, *.py）に対して自動適用されるコーディング規約やスタイルガイドをInstru | github |
| skillsによる自己完結型機能バンドルの利用 | Skillsによる自己完結型機能バンドルの利用 | infrastructure | Instructions、サンプルコード、設定ファイルなどをフォルダ単位でバンドルしたSkillを導入し、特定の技術領域 | github |
| agentsによる専門的なaiアシスタントの導入 | Agentsによる専門的なAIアシスタントの導入 | agent-orchestration | MCP server（Model Context Protocol）と連携し、外部API、データベース、開発ツールにアク | github |
| hooksによるセッション自動化 | Hooksによるセッション自動化 | agent-orchestration | Copilot agentセッション中に特定イベント（例: ファイル保存、コミット前）で自動実行されるシェルコマンドやス | github |
| agentic-workflowsによるgithub-actions統合 | Agentic WorkflowsによるGitHub Actions統合 | agent-orchestration | Markdown形式で記述されたAI駆動のGitHub Actionsワークフローを導入し、PR自動レビュー、ドキュメン | github |
| langfuse自動トレーシング実装 | Langfuse自動トレーシング実装 | agent-orchestration | LLMアプリケーションの全実行フローを自動でトレースし、各LLM呼び出し・retrieval・embedding・age | langfuse |
| langfuseセルフホスト構築 | Langfuseセルフホスト構築 | infrastructure | Langfuseをローカル/VM/Kubernetesで自前インフラ上に5分～30分でデプロイし、外部SaaS依存なしで | langfuse |
| prompt-management統合 | Prompt Management統合 | prompt-engineering | プロンプトをコードから分離してLangfuse UIで一元管理し、バージョン管理・A/Bテスト・リアルタイム更新を可能に | langfuse |
| evaluation-dataset-run実装 | Evaluation & Dataset Run実装 | prompt-engineering | テストセット（Dataset）を作成し、LLM-as-a-judge/ユーザーフィードバック/カスタム評価スクリプトで継 | langfuse |
| マルチllmプロバイダー統合 | マルチLLMプロバイダー統合 | infrastructure | OpenAI、Anthropic、Ollama（ローカル）、AWS Bedrock、Azure等のLLMを統一インターフ | langfuse |
| 階層的スウォームトポロジーによるマルチエージェント協調 | 階層的スウォームトポロジーによるマルチエージェント協調 | agent-orchestration | クイーンエージェントが戦略を決定し、ワーカーエージェント（researcher, coder, tester等）に作業を | ruvnet |
| reasoningbankによるパターン学習と再利用 | ReasoningBankによるパターン学習と再利用 | agent-orchestration | 成功したタスク実行の軌跡（trajectory）をHNSW索引付きベクトルストアに保存し、類似タスクで過去のパターンを0 | ruvnet |
| agent-boosterによるllmスキップ高速編集 | Agent BoosterによるLLMスキップ高速編集 | agent-orchestration | 単純なコード変換（var→const、型注釈追加等）をRust/WASM実装で<1ms処理し、LLM APIを呼ばずに3 | ruvnet |
| 3層モデルルーティングによるコスト最適化 | 3層モデルルーティングによるコスト最適化 | agent-orchestration | タスク複雑度を自動判定し、Tier 1（Agent Booster、$0）→Tier 2（Haiku、$0.0002）→ | ruvnet |
| hnsw索引による超高速ベクトル検索 | HNSW索引による超高速ベクトル検索 | agent-orchestration | Hierarchical Navigable Small World（HNSW）アルゴリズムで384次元ベクトルを<1m | ruvnet |
| ewcによる忘却防止と継続学習 | EWC++による忘却防止と継続学習 | agent-orchestration | Elastic Weight Consolidation++で重要な重みを固定し、新しいパターン学習時に過去の知識を忘れ | ruvnet |
| aidefenceによるプロンプトインジェクション防御 | AIDefenceによるプロンプトインジェクション防御 | agent-orchestration | 50+パターンで「命令上書き」「ジェイルブレイク」「PII漏洩」を0.04ms（250倍高速）で検出し、脅威入力をブロッ | ruvnet |
| context-autopilotによる無限コンテキスト | Context Autopilotによる無限コンテキスト | claude-code-workflow | Claude Codeの20万トークン上限を回避し、ターン単位でSQLiteにアーカイブ+復元することで、事実上無限のコ | ruvnet |
| typescriptでpieceを実装しmcpサーバー化 | TypeScriptでpieceを実装しMCPサーバー化 | automation-pipeline | Activepiecesのpiece frameworkでTypeScriptのnpmパッケージとして統合を実装すると、 | activepieces |
| hot-reloadでローカルpiece開発 | hot reloadでローカルpiece開発 | automation-pipeline | Activepiecesはローカルマシンでpieceを開発中、変更を保存すると即座にビルダーに反映されるhot relo | activepieces |
| human-in-the-loopパターンの実装 | Human-in-the-Loopパターンの実装 | automation-pipeline | ワークフロー実行中に承認待ちや遅延を挿入し、人間の判断を介入させるpieceを実装 | activepieces |
| ai-first統合とask-ai-in-code-piece | AI-First統合とASK AI in Code Piece | automation-pipeline | ビルダーのCodeピース内で「ASK AI」機能を使い、非技術者がコード不要でデータクリーニング等を実行 | activepieces |
| オープンエコシステムでのpiece共有 | オープンエコシステムでのpiece共有 | automation-pipeline | 開発したpieceをnpmjs.comに公開し、コミュニティと共有する。60%の統合がコミュニティ貢献 | activepieces |
| セルフホストネットワークギャップ運用 | セルフホスト&ネットワークギャップ運用 | automation-pipeline | Activepiecesをオンプレミスまたはプライベートクラウドにセルフホストし、外部ネットワークと隔離した環境で運用 | activepieces |
| wasp-cliで2コマンドsaas初期化 | Wasp CLIで2コマンドSaaS初期化 | claude-code-workflow | Waspフレームワークの公式CLIを使い、フル機能SaaSテンプレートを即座にクローンして起動する | wasp-lang |
| wasp宣言的設定で型安全apiを自動生成 | Wasp宣言的設定で型安全APIを自動生成 | dev-tool | main.wasp ファイルにクエリ・アクション（CRUD操作）を宣言すると、バックエンド関数の型がフロントエンドに自動 | wasp-lang |
| ai開発ツール向けagentsmdとスキルを同梱 | AI開発ツール向けAGENTS.mdとスキルを同梱 | claude-code-workflow | Claude Code/Cursor等のAIエージェントが参照する AGENTS.md（コードベース全体の構造・ルール） | wasp-lang |
| ワンコマンドデプロイrailwayflyio | ワンコマンドデプロイ（Railway/Fly.io） | infrastructure | Wasp CLIの `wasp deploy` コマンドで、DB・サーバー・クライアントを一括で本番環境にデプロイする | wasp-lang |
| toolsyamlによるデータベースツールの宣言的定義 | tools.yamlによるデータベースツールの宣言的定義 | agent-orchestration | データベース接続情報（sources）、実行するSQL/操作（tools）、ツールのグループ化（toolsets）をYA | googleapis |
| mcpサーバーによるツールの中央管理と動的リロード | MCPサーバーによるツールの中央管理と動的リロード | agent-orchestration | tools.yamlの変更を検知し、サーバー再起動なしでツール定義を自動更新する | googleapis |
| ide統合によるaiアシスタントへのデータベース操作委譲 | IDE統合によるAIアシスタントへのデータベース操作委譲 | claude-code-workflow | Claude Code、Cursor、Windsurf等のIDE内AIアシスタントをMCP Toolbox経由でデータベ | googleapis |
| フレームワーク横断でのツール統一インターフェース | フレームワーク横断でのツール統一インターフェース | agent-orchestration | Python（LangChain/LlamaIndex）、JS/TS（LangChain/Genkit/ADK）、Go（ | googleapis |
| gemini-cli-extensionsによるコマンドライン直接操作 | Gemini CLI Extensionsによるコマンドライン直接操作 | automation-pipeline | Gemini CLIの拡張機能として事前定義済みツール（AlloyDB/BigQuery/Cloud SQL等）またはカ | googleapis |
| カテゴリ別リソース検索でclaude-code拡張を発見する | カテゴリ別リソース検索でClaude Code拡張を発見する | claude-code-workflow | awesome-claude-codeリポジトリの目次から、Agent Skills、Hooks、Slash Comma | hesreallyhim |
| agent-skillsでclaude-codeに専門知識を付与する | Agent SkillsでClaude Codeに専門知識を付与する | claude-code-workflow | Agent Skillsカテゴリのリソース（例: Claude Scientific Skills、Trail of B | hesreallyhim |
| hooksでclaude-codeの動作をリアルタイム制御する | HooksでClaude Codeの動作をリアルタイム制御する | claude-code-workflow | Hooksカテゴリのリソース（例: TDD Guard、parry、Dippy）をインストールし、Claude Code | hesreallyhim |
| slash-commandsでclaude-codeにプロジェクト固有ワークフローを実行させる | Slash CommandsでClaude Codeにプロジェクト固有ワークフローを実行させる | claude-code-workflow | Slash Commandsカテゴリのリソース（例: /commit、/create-pr、/tdd-implement | hesreallyhim |
| toolingでclaude-codeの可観測性管理性を向上させる | ToolingでClaude Codeの可観測性・管理性を向上させる | claude-code-workflow | Toolingカテゴリのリソース（例: ccflare使用量ダッシュボード、claude-tmux、Claudex会話履 | hesreallyhim |
| orchestratorでclaude-code複数インスタンスを並列実行する | OrchestratorでClaude Code複数インスタンスを並列実行する | claude-code-workflow | Orchestratorsカテゴリのリソース（例: sudocode、Claude Squad、Happy Coder） | hesreallyhim |
