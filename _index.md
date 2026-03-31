# スキルインデックス

合計: 685 スキル

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
| typescript型安全pieceフレームワークでの統合開発 | TypeScript型安全pieceフレームワークでの統合開発 | automation-pipeline | 自動化ワークフローの統合コンポーネント（piece）をTypeScriptのnpmパッケージとして開発し、型安全性とホッ | activepieces |
| mcpサーバーへの自動変換による統合 | MCPサーバーへの自動変換による統合 | claude-code-workflow | Activepiecesで開発された280以上のpieceを自動的にMCP（Model Context Protocol | activepieces |
| オープンエコシステムによるコミュニティ駆動の拡張 | オープンエコシステムによるコミュニティ駆動の拡張 | automation-pipeline | 全てのpieceをオープンソース（MIT）として公開し、npmjs.comでバージョン管理することで、コミュニティからの | activepieces |
| ai-first設計とhuman-in-the-loop統合 | AI-First設計とHuman-in-the-Loop統合 | agent-orchestration | AIネイティブなpiece（AIプロバイダー統合、AI SDK）を提供し、かつ承認待ち・遅延実行といったHuman-in | activepieces |
| エンタープライズ向けセルフホストカスタマイズ | エンタープライズ向けセルフホスト＋カスタマイズ | automation-pipeline | Activepiecesをセルフホスト（ネットワークギャップ環境含む）で運用し、ブランディングからアクセス制御まで完全に | activepieces |
| waspテンプレートから新規saasプロジェクトを生成 | Waspテンプレートから新規SaaSプロジェクトを生成 | infrastructure | Wasp CLIを使ってOpen SaaSテンプレートをクローンし、認証・決済・UI・デプロイ設定が全て揃ったプロジェク | wasp-lang |
| waspの宣言的設定で認証ジョブデプロイを実装 | Waspの宣言的設定で認証・ジョブ・デプロイを実装 | automation-pipeline | Waspの設定ファイル（.waspファイル）に認証プロバイダー、バックグラウンドジョブ、デプロイターゲットを宣言的に記述 | wasp-lang |
| aiコーディング支援環境を標準装備 | AIコーディング支援環境を標準装備 | claude-code-workflow | Open SaaSテンプレートに同梱されたAGENTS.md、Cursorルール、llms-full.txtを使い、Cl | wasp-lang |
| エンドツーエンド型安全性でフロントバック連携 | エンドツーエンド型安全性でフロント・バック連携 | dev-tool | バックエンド関数の型定義をフロントエンドで自動推論させることで、サードパーティライブラリなしに完全な型安全性を実現する | wasp-lang |
| tmux-cliワーカーによるマルチai並列実行 | tmux CLIワーカーによるマルチAI並列実行 | claude-code-workflow | tmux上で複数のAI CLI（claude/codex/gemini）を独立ペインとしてオンデマンド起動し、同一タスク | Yeachan-Heo |
| ステージドパイプラインによる協調実行 | ステージドパイプラインによる協調実行 | claude-code-workflow | Team mode実行時、team-plan（計画）→ team-prd（要件定義）→ team-exec（実装）→ t | Yeachan-Heo |
| プロバイダーアドバイザーパターンomc-ask | プロバイダーアドバイザーパターン（omc ask） | claude-code-workflow | 単一タスクを複数AIプロバイダー（claude/codex/gemini）に同時問い合わせし、各回答をMarkdownア | Yeachan-Heo |
| レート制限自動待機再開 | レート制限自動待機・再開 | claude-code-workflow | Claude Code APIのレート制限到達時、tmuxセッション検出でリセット時刻まで自動待機し、制限解除後にセッシ | Yeachan-Heo |
| openclawイベントブリッジ | OpenClawイベントブリッジ | claude-code-workflow | Claude Codeのセッション開始・終了・ツール実行前後などのイベントを、設定したOpenClawゲートウェイにHT | Yeachan-Heo |
| マジックキーワードによる実行モード切替 | マジックキーワードによる実行モード切替 | claude-code-workflow | 自然言語プロンプト内に特定キーワード（autopilot, ralph, ulw, ralplan等）を含めることで、異 | Yeachan-Heo |
| progressive-disclosure-でスキルを軽量化する | Progressive Disclosure でスキルを軽量化する | claude-code-workflow | スキルのメタデータ（name, description）を先にスキャンし、関連性が高い場合のみ本文とリソースをロードする | travisvn |
| skill-creator-で対話的にスキルを生成する | skill-creator で対話的にスキルを生成する | claude-code-workflow | 公式の skill-creator スキルを有効化し、Claudeとの対話形式で新しいスキルの構造を自動生成する | travisvn |
| git-リポジトリでスキルをチーム配布する | git リポジトリでスキルをチーム配布する | claude-code-workflow | スキルフォルダをgitリポジトリに格納し、チームメンバーが `/plugin add` や git clone で共有・ | travisvn |
| skills-と-mcp-を使い分ける | Skills と MCP を使い分ける | claude-code-workflow | 再利用可能なタスク手順は Skills、外部データ・API統合は MCP として実装し、必要に応じて組み合わせる | travisvn |
| セキュリティ監査を実施してからスキルをインストールする | セキュリティ監査を実施してからスキルをインストールする | claude-code-workflow | スキルの SKILL.md と全スクリプトを精査し、任意コード実行のリスクがないか確認してから有効化する | travisvn |
| クローズドループ学習によるスキル自動生成改善 | クローズドループ学習によるスキル自動生成・改善 | agent-orchestration | 複雑なタスク完了後にエージェントが自律的にスキル（手続き的記憶）を生成し、使用中に改善し、定期的なナッジで知識を永続化す | NousResearch |
| サーバーレス永続化ターミナルバックエンドの利用 | サーバーレス永続化ターミナルバックエンドの利用 | agent-orchestration | エージェントの実行環境をDaytona/Modalといったサーバーレスバックエンドで動かし、アイドル時に休止・オンデマン | NousResearch |
| マルチllmプロバイダー切り替えアーキテクチャ | マルチLLMプロバイダー切り替えアーキテクチャ | agent-orchestration | `hermes model`コマンドで、コード変更なしに200+モデル（OpenRouter、z.ai/GLM、Kimi | NousResearch |
| ワンライナーインストールスクリプトによる全依存解決 | ワンライナーインストールスクリプトによる全依存解決 | agent-orchestration | Linux/macOS/WSL2でPython・Node.js・全依存関係・`hermes`コマンドまでを1コマンドで自 | NousResearch |
| 統合メッセージングゲートウェイによるクロスプラットフォーム会話継続 | 統合メッセージングゲートウェイによるクロスプラットフォーム会話継続 | agent-orchestration | 単一のゲートウェイプロセスでTelegram、Discord、Slack、WhatsApp、Signal、CLIから同一 | NousResearch |
| cron自然言語スケジューリングとプラットフォーム配信 | cron自然言語スケジューリングとプラットフォーム配信 | agent-orchestration | 自然言語でスケジュールタスク（日次レポート、夜間バックアップ、週次監査等）を定義し、任意のメッセージングプラットフォーム | NousResearch |
| openclawからの自動マイグレーション | OpenClawからの自動マイグレーション | claude-code-workflow | OpenClawの設定・メモリ・スキル・APIキーをHermes Agentへ自動インポートする | NousResearch |
| カテゴリ別スキル分類を活用して目的のスキルを発見する | カテゴリ別スキル分類を活用して目的のスキルを発見する | claude-code-workflow | 12の機能別カテゴリ（Document Skills、Development & Code Tools、Data & A | BehiSecc |
| スキルコレクションを一括導入してclaude-codeの能力を拡張する | スキルコレクションを一括導入してClaude Codeの能力を拡張する | claude-code-workflow | Collections カテゴリに掲載された複数スキルのバンドル（例: OpenPaw 38スキル、agentskill | BehiSecc |
| セキュリティスキルvibesec-owasp-trail-of-bitsを導入して脆弱性を予防する | セキュリティスキル（VibeSec, OWASP, Trail of Bits）を導入して脆弱性を予防する | claude-code-workflow | Security & Web Testing カテゴリのスキル（VibeSec-Skill, owasp-securit | BehiSecc |
| tddスキルを適用してテスト駆動開発を自動化する | TDDスキルを適用してテスト駆動開発を自動化する | claude-code-workflow | test-driven-development スキルをClaude Codeに導入し、機能実装前に必ずテストを書かせる | BehiSecc |
| mcpmodel-context-protocol対応スキルでツール統合を実現する | MCP（Model Context Protocol）対応スキルでツール統合を実現する | claude-code-workflow | Linear, NotebookLM, Google Workspace, VideoDB など、MCP対応スキルを導入 | BehiSecc |
| プロジェクト管理スキルpm-skills-product-manager-skillsで製品開発を体系化する | プロジェクト管理スキル（pm-skills, Product-Manager-Skills）で製品開発を体系化する | claude-code-workflow | Collaboration & Project Management カテゴリのスキル（pm-skills 24スキル、 | BehiSecc |
| git-worktreeでagentタスクを物理分離する | git worktreeでagentタスクを物理分離する | claude-code-workflow | 1つのgitリポジトリから複数のworking directoryを作り、それぞれ独立したブランチで作業させる | superset-sh |
| 複数agentの状態をダッシュボードで監視する | 複数agentの状態をダッシュボードで監視する | claude-code-workflow | Supersetの単一画面で全workspace（agent）のステータス・出力・差分を一覧表示する | superset-sh |
| workspace-presetで環境構築を自動化する | workspace presetで環境構築を自動化する | agent-orchestration | 新しいworkspaceを作った瞬間に、環境変数コピー・依存インストール・初期設定を自動実行する | superset-sh |
| 任意のcli-agentをsupersetで実行する | 任意のCLI agentをSupersetで実行する | claude-code-workflow | Claude Code, Codex, Cursor Agent, Gemini CLI, Copilotなど、ターミナ | superset-sh |
| mcpサーバーのカタログ化と分類 | MCPサーバーのカタログ化と分類 | infrastructure | 20以上のMCPサーバーをREADME・ソースコード・CHANGELOG・ドキュメント・トラブルシューティング・サポート | microsoft |
| local型とremote型mcpサーバーの使い分け | Local型とRemote型MCPサーバーの使い分け | agent-orchestration | MCPサーバーをLocal型(ローカルプロセスとして起動、stdio通信)とRemote型(HTTPSエンドポイント経由 | microsoft |
| ideワンクリックインストールurlの生成 | IDEワンクリックインストールURLの生成 | prompt-engineering | VS Code/Visual Studio等のIDEが直接解釈できるMCPインストールプロトコルURLを生成し、バッジボ | microsoft |
| モノレポでの複数mcpサーバー統合管理 | モノレポでの複数MCPサーバー統合管理 | automation-pipeline | 単一リポジトリ(microsoft/mcp)内に、コアライブラリ・テストフレームワーク・エンジニアリングシステム・パイプ | microsoft |
| microsoft-graph-api統合mcpサーバーのパターン | Microsoft Graph API統合MCPサーバーのパターン | agent-orchestration | Microsoft 365の各サービス(Calendar, Mail, Teams, Word等)をMicrosoft  | microsoft |
| ローカルaiエージェントのwebsocketブリッジ構築 | ローカルAIエージェントのWebSocketブリッジ構築 | claude-code-workflow | ローカルマシン上のCLI型AIエージェント（Claude Code, Cursor Agent等）をメッセンジャープラッ | chenhg5 |
| 複数aiエージェントのグループチャット内連携 | 複数AIエージェントのグループチャット内連携 | agent-orchestration | 1つのグループチャットに複数のAIボット（Claude, Gemini等）を参加させ、相互に対話・情報共有させる。 | chenhg5 |
| aiエージェントへのファイル送信機能の実装 | AIエージェントへのファイル送信機能の実装 | agent-orchestration | AIエージェントがローカルで生成したスクリーンショット・グラフ・PDF等を、チャットアプリに自動送信させる。 | chenhg5 |
| 自然言語でのcronジョブ設定 | 自然言語でのcronジョブ設定 | agent-orchestration | チャットから自然言語でスケジュールタスクを登録し、定時実行させる。 | chenhg5 |
| 公開ipなしでのメッセンジャーボット運用 | 公開IPなしでのメッセンジャーボット運用 | agent-orchestration | Webhook不要のWebSocket/Long Polling接続を使い、ローカル環境から直接メッセンジャーボットを動 | chenhg5 |
| 機能別カテゴリによるリソース選定 | 機能別カテゴリによるリソース選定 | claude-code-workflow | 70以上のClaude Code拡張リソースを8カテゴリ（Agent Skills/Workflows/Tooling/ | hesreallyhim |
| hooksによる品質ゲート自動化 | Hooksによる品質ゲート自動化 | claude-code-workflow | Claude Codeのライフサイクルイベント（ファイル書き込み前後、Bashコマンド実行前等）にスクリプトを挿入し、T | hesreallyhim |
| agent-skillsによる専門知識の注入 | Agent Skillsによる専門知識の注入 | claude-code-workflow | Claude Codeに特定ドメイン（科学研究・セキュリティ監査・DevOps IaC・フルスタック開発等）の専門知識・ | hesreallyhim |
| usage-monitorsによるコスト可視化 | Usage Monitorsによるコスト可視化 | claude-code-workflow | Claude Codeのトークン消費・API呼び出し・コストをリアルタイムまたは事後に可視化し、予算超過・非効率利用を検 | hesreallyhim |
| orchestratorsによるマルチエージェント協調 | Orchestratorsによるマルチエージェント協調 | claude-code-workflow | 複数のClaude Codeインスタンスまたは異なるAIエージェントを並列・逐次実行し、大規模タスクを分割・統合する | hesreallyhim |
| claudemdによるプロジェクト固有ルールの標準化 | CLAUDE.mdによるプロジェクト固有ルールの標準化 | claude-code-workflow | プロジェクトルート（または`.claude/`）に`CLAUDE.md`を配置し、コーディング規約・ビルドコマンド・アー | hesreallyhim |
| activepiecesのtypescript-pieceフレームワークで統合コンポーネントを作成 | ActivepiecesのTypeScript pieceフレームワークで統合コンポーネントを作成 | automation-pipeline | TypeScriptでtype-safeな統合コンポーネント(piece)を作成し、npmパッケージとして公開すると、自 | activepieces |
| activepiecesを280のmcpサーバーツールキットとして利用 | Activepiecesを280+のMCPサーバーツールキットとして利用 | agent-orchestration | Activepiecesに既に存在する280以上のpiece（Google Sheets, OpenAI, Discor | activepieces |
| activepiecesのホットリロード機能でローカル開発効率化 | Activepiecesのホットリロード機能でローカル開発効率化 | automation-pipeline | Activepiecesのpiece開発時に、コード変更が即座にノーコードビルダーに反映されるホットリロード機能を活用す | activepieces |
| human-in-the-loop機能でワークフローに承認フローを組み込む | Human-in-the-Loop機能でワークフローに承認フローを組み込む | automation-pipeline | Activepiecesの「遅延実行」「承認待ち」「チャットインターフェース」「フォームインターフェース」pieceを使 | activepieces |
| 3ファイルパターンでタスク状態を永続化する | 3ファイルパターンでタスク状態を永続化する | claude-code-workflow | 全ての複雑タスクをtask_plan.md（フェーズとチェックボックス）、findings.md（調査結果・発見）、pr | OthmanAdi |
| フックで判断前にプランを再読込させる | フックで判断前にプランを再読込させる | context-management | PreToolUse（ツール実行直前）フックでAIにtask_plan.mdを再読込させ、現在のフェーズと目標を思い出さ | OthmanAdi |
| 2アクション後に発見をfindingsmdへ保存する | 2アクション後に発見をfindings.mdへ保存する | context-management | ブラウザ操作やファイル閲覧を2回実行したら、その発見を必ずfindings.mdに書き出す（The 2-Action R | OthmanAdi |
| 全てのエラーをtask-planmdに記録し反復を防ぐ | 全てのエラーをtask_plan.mdに記録し反復を防ぐ | automation-pipeline | テスト失敗、ビルドエラー、API呼び出し失敗等を全てtask_plan.mdの「## Errors」セクションに記録し、 | OthmanAdi |
| stopフックで完了検証を強制する | Stopフックで完了検証を強制する | automation-pipeline | セッション終了時（/stop, /exit）にStopフックがtask_plan.mdの全チェックボックスを確認し、未完 | OthmanAdi |
| セッションリカバリーでclear後も作業を継続する | セッションリカバリーで/clear後も作業を継続する | claude-code-workflow | /clearでコンテキストをリセットした後、前回の.planning/ファイルと~/.claude/projects/セ | OthmanAdi |
| 専門化サブエージェントの定義と配置 | 専門化サブエージェントの定義と配置 | claude-code-workflow | 特定タスク（例: TypeScript開発、AWS構築、セキュリティ監査）に特化したサブエージェント定義（YAML fr | VoltAgent |
| プラグインベースの一括インストール | プラグインベースの一括インストール | claude-code-workflow | カテゴリ単位で複数のサブエージェントをClaude Codeプラグインとして一括インストールする | VoltAgent |
| モデル自動ルーティングの活用 | モデル自動ルーティングの活用 | claude-code-workflow | サブエージェント定義のYAML `model` フィールドで、タスクの複雑度に応じてOpus/Sonnet/Haikuを | VoltAgent |
| ツール権限の最小化原則 | ツール権限の最小化原則 | claude-code-workflow | サブエージェントごとに必要最小限のClaude Codeツール（Read, Write, Edit, Bash等）のみを | VoltAgent |
| 対話式インストーラーによる選択的導入 | 対話式インストーラーによる選択的導入 | claude-code-workflow | 提供されているシェルスクリプト `install-agents.sh` を使い、カテゴリとエージェントを選択的にインスト | VoltAgent |
| agent-installerサブエージェントによるメタ管理 | Agent Installerサブエージェントによるメタ管理 | claude-code-workflow | Claude Code内から `agent-installer` サブエージェント自身を使い、他のエージェントを検索・イ | VoltAgent |
| yamlベースの宣言的ツール定義 | YAMLベースの宣言的ツール定義 | agent-orchestration | データベースツールをYAML形式で定義し、複数フレームワーク・言語で再利用可能な形式で管理する | googleapis |
| マルチsdkによる統一インターフェース | マルチSDKによる統一インターフェース | agent-orchestration | Python、JavaScript/TypeScript、Go向けの公式SDKを使い、同一のツール定義を各フレームワーク | googleapis |
| 動的リロード機能によるゼロダウンタイムツール更新 | 動的リロード機能によるゼロダウンタイムツール更新 | other | Toolboxサーバーの起動中に`tools.yaml`を編集すると、サーバー再起動なしで新しいツール定義が反映される | googleapis |
| mcpプロトコルによるide統合 | MCPプロトコルによるIDE統合 | claude-code-workflow | Model Context Protocol (MCP)を介してClaude Code、Cursor、Gemini CL | googleapis |
| コントロールプレーンによるツールのライフサイクル管理 | コントロールプレーンによるツールのライフサイクル管理 | agent-orchestration | Toolboxサーバーを中央コントロールプレーンとして、複数のアプリケーション・エージェントが同一のツールを参照し、ツー | googleapis |
| progressive-disclosure-architectureでスキルを設計する | Progressive Disclosure Architectureでスキルを設計する | claude-code-workflow | スキルのメタデータ（name/description）を軽量に保ち、詳細な指示とリソースは必要時のみ読み込む3段階構造で | travisvn |
| skill-creatorで対話的にスキルを生成する | skill-creatorで対話的にスキルを生成する | claude-code-workflow | 公式のskill-creatorスキルを使い、Q&A形式でスキルを自動生成させる | travisvn |
| skillsmcppromptsprojectssubagentsを用途で使い分ける | Skills/MCP/Prompts/Projects/Subagentsを用途で使い分ける | agent-orchestration | 5つのアプローチ（Skills/MCP/Prompts/Projects/Subagents）の使い分け基準を理解し、適 | travisvn |
| claude-code-cliでスキルをマーケットプレイスからインストールする | Claude Code CLIでスキルをマーケットプレイスからインストールする | claude-code-workflow | Claude Code CLIの/pluginコマンドを使い、マーケットプレイスまたはローカルディレクトリからスキルをイ | travisvn |
| frontend-designスキルでai臭のないui設計をさせる | frontend-designスキルでAI臭のないUI設計をさせる | ui-ux | 公式frontend-designスキルを使い、汎用的・AI特有の美学を避け、大胆なデザイン判断をClaudeに促す | travisvn |
| obrasuperpowersで20の実践スキルライブラリを一括導入する | obra/superpowersで20+の実践スキルライブラリを一括導入する | claude-code-workflow | obra/superpowersコミュニティスキルパックをインストールし、TDD/デバッグ/コラボレーションパターン等2 | travisvn |
| セキュリティスキャンでスキルの安全性を検証する | セキュリティスキャンでスキルの安全性を検証する | claude-code-workflow | スキルをインストール前にSKILL.mdと全スクリプトをレビューし、悪意あるコード・プロンプトインジェクション・データ流 | travisvn |
| awesome-list形式でスキルをキュレーション | awesome-list形式でスキルをキュレーション | other | GitHub上でClaude Skillsを機能カテゴリ（Document、Development、Data、Secur | BehiSecc |
| スキルに1行機能説明を付与 | スキルに1行機能説明を付与 | claude-code-workflow | 各スキルのリンクの後に、そのスキルが何をするのかを簡潔に記述する（例: "Create, edit, analyze W | BehiSecc |
| セキュリティスキルを明示的に推奨 | セキュリティスキルを明示的に推奨 | ui-ux | READMEの冒頭にTipセクションを配置し、Web開発者向けにセキュリティスキル（VibeSec-Skill）の利用を | BehiSecc |
| スキルをドメイン別に階層化 | スキルをドメイン別に階層化 | other | スキルを「Document Skills」「Development & Code Tools」「Data & Analy | BehiSecc |
| スキルコレクションをメタスキルとして扱う | スキルコレクションをメタスキルとして扱う | claude-code-workflow | 個別スキルだけでなく、複数スキルをバンドルした「コレクション」（例: OpenPaw、claude-starter）も1 | BehiSecc |
| スキルマーケットプレイスへのリンク提供 | スキルマーケットプレイスへのリンク提供 | claude-code-workflow | Collectionsセクションに、スキル検索・インストールを支援する外部サービス（agentskill.sh等）へのリ | BehiSecc |
| git-worktreeによるエージェント隔離実行 | Git worktreeによるエージェント隔離実行 | agent-orchestration | 各AIエージェントタスクに独立したgit worktree（ブランチ+作業ディレクトリ）を割り当て、並列実行時の干渉を完 | superset-sh |
| エージェント監視と通知による待機時間削減 | エージェント監視と通知による待機時間削減 | agent-orchestration | 複数エージェントの実行状態を統合ダッシュボードで監視し、レビュー準備完了時に通知を受け取ることで、人間の待機時間をゼロに | superset-sh |
| workspace-presetsによる環境構築自動化 | Workspace Presetsによる環境構築自動化 | agent-orchestration | 各worktree作成時に実行されるsetup/teardownスクリプトをプリセット化し、依存関係インストール・環境変 | superset-sh |
| ユニバーサルcliエージェント対応アーキテクチャ | ユニバーサルCLIエージェント対応アーキテクチャ | claude-code-workflow | 特定のエージェントに依存せず、任意のCLIベースエージェント（Claude Code、Codex、Cursor、Gemi | superset-sh |
| hosted-mcp-serverをhttp経由で接続 | hosted MCP serverをHTTP経由で接続 | other | Exa MCPサーバー（https://mcp.exa.ai/mcp）にHTTPトランスポートで接続し、AI assis | exa-labs |
| カテゴリ別フィルタ制限を考慮したクエリ設計 | カテゴリ別フィルタ制限を考慮したクエリ設計 | data-processing | Exa検索のcategoryパラメータに応じて、利用可能/不可能なフィルタを使い分ける | exa-labs |
| claude-skillでmcpツールの使用パターンを定型化 | Claude SkillでMCPツールの使用パターンを定型化 | claude-code-workflow | Exa MCP用のClaude Skillを作成し、カテゴリ別の最適な検索パターン・フィルタ制限・トークン管理を文書化 | exa-labs |
| task-agentでトークン消費を分離 | Task agentでトークン消費を分離 | claude-code-workflow | Exa検索を常にTask agent（fork context）で実行し、メインコンテキストに検索結果全体を流さない | exa-labs |
| クエリバリエーションで検索カバレッジ向上 | クエリバリエーションで検索カバレッジ向上 | other | 同一検索意図に対して複数のクエリ表現を生成し、並列実行後にマージ・重複排除 | exa-labs |
| vs-code拡張機能としてmcpサーバーをワンクリックインストールする | VS Code拡張機能としてMCPサーバーをワンクリックインストールする | claude-code-workflow | 公式READMEのINSTALLバッジリンク（vscode:extension/...）をクリックし、MCPサーバーをV | microsoft |
| remoteタイプのmcpサーバーをhttpエンドポイント経由で接続する | REMOTEタイプのMCPサーバーをHTTPエンドポイント経由で接続する | claude-code-workflow | サーバーレス実行されるMCPサーバー（例: Microsoft Foundry `https://mcp.ai.azur | microsoft |
| 複数のmicrosoft公式mcpサーバーを組み合わせて企業ワークフローを構築する | 複数のMicrosoft公式MCPサーバーを組み合わせて企業ワークフローを構築する | claude-code-workflow | Azure MCP + Microsoft 365 Mail MCP + GitHub MCP等、複数の公式サーバーを同 | microsoft |
| microsoftmcpリポジトリから最新のmcpサーバーリリースを追跡する | microsoft/mcpリポジトリから最新のMCPサーバーリリースを追跡する | infrastructure | microsoft/mcpリポジトリのReleasesページで、Azure MCP・Fabric MCP等の最新バージョ | microsoft |
| azure-mcpサーバーをローカルで実行しazure-cliの資格情報を再利用する | Azure MCPサーバーをローカルで実行しAzure CLIの資格情報を再利用する | claude-code-workflow | Azure MCPサーバーをnpx/uvx経由でローカル起動し、既存のAzure CLI認証（`az login`）を使 | microsoft |
| mcp経由でシンボルレベルコード操作を提供する | MCP経由でシンボルレベルコード操作を提供する | claude-code-workflow | LSPまたはJetBrainsプラグインを使い、ファイルではなくシンボル（関数・クラス・変数等）単位でコードを検索・編集 | oraios |
| lsp抽象化レイヤーで30言語以上に対応する | LSP抽象化レイヤーで30言語以上に対応する | agent-orchestration | Language Server Protocol（LSP）を抽象化し、30言語以上の言語サーバーを統一インターフェースで | oraios |
| jetbrainsプラグインで最強のコード解析を提供する | JetBrainsプラグインで最強のコード解析を提供する | agent-orchestration | JetBrains IDE（IntelliJ、PyCharm等）のコード解析エンジンをプラグイン経由でSerenaに統合 | oraios |
| mcpoでchatgpt等の非mcp対応クライアントに接続する | mcpoでChatGPT等の非MCP対応クライアントに接続する | agent-orchestration | MCPサーバーをOpenAPI経由で公開するmcpoツールを使い、MCP非対応だがツール呼び出し（Function Ca | oraios |
| カテゴリ別サブエージェントプラグインのインストール | カテゴリ別サブエージェントプラグインのインストール | claude-code-workflow | 127以上のサブエージェントを9つのカテゴリ（Core Development、Language Specialists | VoltAgent |
| サブエージェント定義のyamlフロントマター構造化 | サブエージェント定義のYAMLフロントマター構造化 | claude-code-workflow | 各サブエージェントをYAMLフロントマター（name, description, tools, model）+ 詳細プロ | VoltAgent |
| ツールベースの最小権限原則least-privilege | ツールベースの最小権限原則（Least Privilege） | claude-code-workflow | 各サブエージェントに必要最小限のツール権限のみを付与し、読み取り専用エージェント（レビュー、監査）とコード変更エージェン | VoltAgent |
| モデルルーティングによるコスト最適化 | モデルルーティングによるコスト最適化 | claude-code-workflow | タスクの複雑度に応じて、opus（高度推論）、sonnet（日常コーディング）、haiku（軽量タスク）を自動選択する | VoltAgent |
| 4種類のインストール手法の使い分け | 4種類のインストール手法の使い分け | claude-code-workflow | プラグイン、手動コピー、対話式インストーラ、AI経由インストールの4つの方法を用途に応じて選択する | VoltAgent |
| プロジェクトグローバルの優先順位設計 | プロジェクト/グローバルの優先順位設計 | claude-code-workflow | プロジェクト固有のサブエージェント（`.claude/agents/`）とグローバルエージェント（`~/.claude/ | VoltAgent |
| メタオーケストレーションエージェントの活用 | メタオーケストレーションエージェントの活用 | claude-code-workflow | multi-agent-coordinator等のメタエージェントを使い、複数の専門エージェントを動的に起動・調整して複 | VoltAgent |
| mcp-toolboxサーバーを起動してツールを提供する | MCP Toolboxサーバーを起動してツールを提供する | agent-orchestration | tools.yamlでツール定義を記述し、toolboxバイナリまたはnpxでMCPサーバーを起動する | googleapis |
| sdkでツールをaiフレームワークに読み込む | SDKでツールをAIフレームワークに読み込む | agent-orchestration | Toolbox SDKを使い、起動したToolboxサーバーからツール定義を取得し、LangChain/LlamaInd | googleapis |
| ideからmcp経由でtoolboxに接続する | IDEからMCP経由でToolboxに接続する | claude-code-workflow | Claude CodeやCursor等のMCP対応IDEにToolboxサーバーを接続し、AI assistantに自然 | googleapis |
| toolsetsで複数エージェント用にツールをグループ化する | toolsetsで複数エージェント用にツールをグループ化する | agent-orchestration | tools.yamlのtoolsetsセクションで、ツールを名前付きグループに分け、エージェントやアプリケーションごとに | googleapis |
| 段階的開示アーキテクチャでskillを設計する | 段階的開示アーキテクチャでSkillを設計する | claude-code-workflow | Skillをメタデータ・命令・リソースの3層に分け、関連性に応じて段階的にロードすることでトークン効率を最大化する | travisvn |
| skills-vs-mcp-vs-プロンプトの使い分け判断 | Skills vs MCP vs プロンプトの使い分け判断 | agent-orchestration | タスクの性質に応じて、Skill・MCP・システムプロンプト・サブエージェントのどれを使うべきか判断する | travisvn |
| gitリポジトリでチーム向けskillを配布する | Gitリポジトリでチーム向けSkillを配布する | other | カスタムSkillをGitリポジトリで管理し、バージョン管理とコードレビューを経てチームに配布する | travisvn |
| skillのセキュリティレビューを実施する | Skillのセキュリティレビューを実施する | claude-code-workflow | Skillをインストールする前に、SKILL.mdと全スクリプトをレビューし、悪意あるコードや脆弱性がないか確認する | travisvn |
| claude-skillsカタログから適切なスキルを発見導入する | Claude Skillsカタログから適切なスキルを発見・導入する | claude-code-workflow | awesome-claude-skillsリポジトリから目的に合ったスキルを検索し、自分のClaude Code環境にイ | BehiSecc |
| カテゴリ別分類でスキルを効率的に検索する | カテゴリ別分類でスキルを効率的に検索する | other | 10の標準カテゴリ（Document Skills, Development & Code Tools, Data &  | BehiSecc |
| セキュリティスキルvibesec等でコード生成時の脆弱性を防止する | セキュリティスキル（VibeSec等）でコード生成時の脆弱性を防止する | claude-code-workflow | VibeSec-SkillなどのセキュリティスキルをClaude Codeに統合し、生成されるコードが一般的な脆弱性（O | BehiSecc |
| tddスキルで実装前にテストを自動生成する | TDDスキルで実装前にテストを自動生成する | claude-code-workflow | test-driven-developmentスキルを使い、機能実装の前に必ずテストケースを先に書くワークフローを強制す | BehiSecc |
| コレクションスキルopenpaw等で複数スキルを一括導入する | コレクションスキル（OpenPaw等）で複数スキルを一括導入する | claude-code-workflow | OpenPaw、agentskill.sh等のコレクションから、関連する複数スキルをまとめて導入し、包括的な能力を獲得す | BehiSecc |
| skill-creatorテンプレートで新規スキルを標準化して作成する | skill-creatorテンプレートで新規スキルを標準化して作成する | claude-code-workflow | Anthropic公式のskill-creatorテンプレートを使い、SKILL.md標準に準拠した新しいスキルを作成・ | BehiSecc |
| ワークスペースプリセットによる環境自動セットアップ | ワークスペースプリセットによる環境自動セットアップ | agent-orchestration | .superset/config.jsonでsetup/teardownスクリプトを定義し、workspace作成時に環 | superset-sh |
| マルチエージェント並列実行とモニタリング | マルチエージェント並列実行とモニタリング | claude-code-workflow | 複数のCLIエージェント（Claude Code、Codex等）を同時起動し、各エージェントの状態を一元監視する | superset-sh |
| npxで即座にmcpjam-inspectorを起動する | npxで即座にMCPJam Inspectorを起動する | ui-ux | インストール不要でMCPJam Inspectorをローカルで起動し、MCP開発環境を立ち上げる | MCPJam |
| apps-builderでウィジェットをローカルエミュレートする | Apps Builderでウィジェットをローカルエミュレートする | dev-tool | ChatGPT appsやMCP appsのウィジェットをローカル環境で表示・操作テストする | MCPJam |
| oauth実装を段階的にデバッグする | OAuth実装を段階的にデバッグする | dev-tool | MCPサーバーのOAuth認証フローを各ステップごとに可視化・検証する | MCPJam |
| llm-playgroundで複数モデルに対してテストする | LLM Playgroundで複数モデルに対してテストする | prompt-engineering | 開発中のMCPサーバーを複数のLLMモデル（GPT-5, Claude Sonnet, Gemini 2.5等）で動作検 | MCPJam |
| json-rpcメッセージを詳細監視する | JSON-RPCメッセージを詳細監視する | prompt-engineering | MCPサーバーとクライアント間のすべてのJSON-RPC通信を記録・検査する | MCPJam |
| 言語別接尾辞による自動skill発見 | 言語別接尾辞による自動Skill発見 | claude-code-workflow | Skillファイル名に `-py`, `-dotnet`, `-ts`, `-java`, `-rust` 等の接尾辞を | microsoft |
| acceptance-criteria-test-harness-による品質保証 | Acceptance Criteria + Test Harness による品質保証 | agent-orchestration | 各SkillにAcceptance Criteria(正しい/誤ったコードパターン)を定義し、Copilot SDKベー | microsoft |
| ralph-loop-による反復改善 | Ralph Loop による反復改善 | agent-orchestration | 生成→評価→フィードバック→再生成を繰り返し、品質閾値(例: 85点)に達するまでコードを改善し続ける | microsoft |
| sensei-style-frontmatter-scoring | Sensei-style Frontmatter Scoring | claude-code-workflow | SkillのYAMLフロントマターに `triggers` (使うべき場面), `anti_triggers` (使って | microsoft |
| symlink-による-multi-agent-共有 | symlink による Multi-Agent 共有 | claude-code-workflow | `.github/skills/` を正とし、`.claude/skills`, `.opencode/skills`  | microsoft |
| npx-skills-add-によるウィザード式インストール | npx skills add によるウィザード式インストール | claude-code-workflow | `npx skills add microsoft/skills` を実行すると、対話式ウィザードで必要なSkillだけ | microsoft |
| mcp-server-skill-の連携 | MCP server + Skill の連携 | claude-code-workflow | Model Context Protocol(MCP) serverでドキュメント検索・GitHub操作等のツールを提供 | microsoft |
| context-driven-development-アーキテクチャ | Context-Driven Development アーキテクチャ | claude-code-workflow | Skills(知識) + MCP servers(ツール) + Custom Agents(役割) + AGENTS.m | microsoft |
| hooksによるライフサイクル介入 | Hooksによるライフサイクル介入 | claude-code-workflow | Claude Codeの特定のライフサイクルイベント（ファイル書き込み前後、コマンド実行前後など）で任意のスクリプトを実 | hesreallyhim |
| slash-commandsによる専門タスクの定型化 | Slash Commandsによる専門タスクの定型化 | claude-code-workflow | 複雑なプロンプトや手順を単一のコマンド（例：`/commit`、`/tdd`、`/create-pr`）にカプセル化し、 | hesreallyhim |
| claudemdによるプロジェクト文脈の注入 | CLAUDE.mdによるプロジェクト文脈の注入 | claude-code-workflow | プロジェクトルートまたは`.claude/`ディレクトリに`CLAUDE.md`ファイルを配置し、コーディング規約・アー | hesreallyhim |
| skillsによる専門知識の外部化 | Skillsによる専門知識の外部化 | claude-code-workflow | 特定ドメイン（セキュリティ監査、科学計算、DevOps等）の専門知識を独立したモジュール（Skill）として定義し、Cl | hesreallyhim |
| orchestratorsによる並列マルチエージェント実行 | Orchestratorsによる並列マルチエージェント実行 | claude-code-workflow | 複数のClaude Codeインスタンスを並列実行し、タスクを分散処理してから結果を統合する | hesreallyhim |
| usage-monitorsによるコスト管理 | Usage Monitorsによるコスト管理 | claude-code-workflow | Claude Codeのトークン消費量・コスト・セッション履歴を可視化し、使用状況を監視・分析する | hesreallyhim |
| デコレータでmcpツールを宣言 | デコレータでMCPツールを宣言 | other | Python関数に`@mcp.tool`デコレータを付けるだけでMCPツールとして公開する | PrefectHQ |
| fastmcpで3層アーキテクチャ構築 | FastMCPで3層アーキテクチャ構築 | prompt-engineering | Servers（ツール公開）・Apps（UI統合）・Clients（サーバー接続）の3つのコンポーネントを組み合わせてM | PrefectHQ |
| uvでfastmcpをインストール | uvでFastMCPをインストール | other | Astral社のuvパッケージマネージャでfastmcpをインストールする | PrefectHQ |
| 既存sdkからfastmcpへ移行 | 既存SDKからFastMCPへ移行 | dev-tool | FastMCP v2、MCP Python SDK、または低レベルSDKからFastMCP v3以降へアップグレードする | PrefectHQ |
| llmstxt形式でドキュメント提供 | llms.txt形式でドキュメント提供 | context-management | FastMCPのドキュメントをllms.txt標準に従ってLLM可読形式で公開する | PrefectHQ |
| beadsをプロジェクトに導入してエージェントに永続メモリを与える | Beadsをプロジェクトに導入してエージェントに永続メモリを与える | claude-code-workflow | BeadsというCLIツールをインストールし、プロジェクトルートで初期化することで、Doltベースのタスク管理DBを作成 | steveyegge |
| git不要モードでbeadsを使う | Git不要モードでBeadsを使う | agent-orchestration | 環境変数 `BEADS_DIR` を設定し `bd init --quiet --stealth` で初期化することで、 | steveyegge |
| 階層idでエピックタスクサブタスクを管理する | 階層IDでエピック・タスク・サブタスクを管理する | agent-orchestration | Beadsはハッシュベースの階層ID（`bd-a3f8`, `bd-a3f8.1`, `bd-a3f8.1.1`）を使い | steveyegge |
| コントリビューターモードで個人計画を分離する | コントリビューターモードで個人計画を分離する | agent-orchestration | `bd init --contributor` でBeadsを初期化すると、計画用タスクを別リポジトリ（例: `~/.b | steveyegge |
| stealthモードでローカル専用タスク管理 | Stealthモードでローカル専用タスク管理 | agent-orchestration | `bd init --stealth` で初期化すると、Beadsの `.beads/` ディレクトリやGitフックをコ | steveyegge |
| oh-my-claudecodeのプラグインセットアップ | oh-my-claudecodeのプラグインセットアップ | claude-code-workflow | Claude Codeにマルチエージェントオーケストレーション機能を追加する初期設定 | Yeachan-Heo |
| teamモードでのステージ型パイプライン実行 | Teamモードでのステージ型パイプライン実行 | claude-code-workflow | 複数Claude エージェントを plan→PRD→exec→verify→fix の段階的パイプラインで協調動作させる | Yeachan-Heo |
| tmux-cli-workersでcodexgeminiを並列起動 | tmux CLI workersでCodex/Geminiを並列起動 | claude-code-workflow | tmuxペイン内に実際のcodex/gemini CLIプロセスをオンデマンド起動し、タスク完了時に自動終了させる | Yeachan-Heo |
| skillシステムで過去の知見を自動再利用 | Skillシステムで過去の知見を自動再利用 | claude-code-workflow | プロジェクト固有（.omc/skills/）またはユーザー全体（~/.omc/skills/）のデバッグ知識をYAML形 | Yeachan-Heo |
| magic-keywordsで即座にモード切替 | Magic keywordsで即座にモード切替 | claude-code-workflow | autopilot/ralph/ulw/ralplan等の予約語をプロンプトに含めるだけで、対応する実行モードを起動する | Yeachan-Heo |
| deep-interviewで要件を事前明確化 | Deep Interviewで要件を事前明確化 | claude-code-workflow | 曖昧な要求に対してソクラテス式質問で段階的に要件を掘り下げ、実装前に明確性を測定する | Yeachan-Heo |
| 閉じた学習ループによる自律的スキル改善 | 閉じた学習ループによる自律的スキル改善 | agent-orchestration | エージェントが複雑なタスク完了後に自動でスキルを生成し、使用中に改善し、定期的に記憶を永続化する仕組み | NousResearch |
| マルチバックエンドサーバーレス対応ターミナル | マルチバックエンド・サーバーレス対応ターミナル | agent-orchestration | local/Docker/SSH/Daytona/Singularity/Modalの6種類のターミナルバックエンドを切 | NousResearch |
| 統一メッセージングゲートウェイ | 統一メッセージングゲートウェイ | agent-orchestration | Telegram/Discord/Slack/WhatsApp/Signal/CLI/Emailを単一ゲートウェイプロセ | NousResearch |
| llmプロバイダ非依存設計 | LLMプロバイダ非依存設計 | agent-orchestration | Nous Portal/OpenRouter/z.ai/Kimi/MiniMax/OpenAI等のプロバイダを herm | NousResearch |
| cron自然言語スケジューリング | cron自然言語スケジューリング | agent-orchestration | 自然言語でタスクをスケジュール登録し、cron的に定期実行→結果を任意プラットフォームに配信 | NousResearch |
| サブエージェント並列実行 | サブエージェント並列実行 | agent-orchestration | 親エージェントから独立したサブエージェントを並列起動し、Pythonスクリプト経由でツールRPC呼び出し | NousResearch |
| ワンライナーインストールマイグレーション | ワンライナーインストール+マイグレーション | agent-orchestration | curl \| bash で全依存（Python/Node.js/hermes CLI）を自動インストールし、OpenCl | NousResearch |
| progressive-disclosure設計でskillを構造化する | Progressive Disclosure設計でSkillを構造化する | claude-code-workflow | Claude Skillsを「メタデータ（~100トークン）→本体指示（<5kトークン）→リソースファイル（必要時のみ） | travisvn |
| skills-vs-mcp-vs-promptsの判断基準を適用する | Skills vs MCP vs Promptsの判断基準を適用する | agent-orchestration | 「同じ指示を複数会話で繰り返す→Skill」「外部データ統合→MCP」「1回限りの指示→Prompt」「独立タスク実行→ | travisvn |
| 公式skillライブラリから用途別skillを選択する | 公式Skillライブラリから用途別Skillを選択する | claude-code-workflow | Anthropic公式の20+Skillsから、ドキュメント操作（docx/pdf/pptx/xlsx）、デザイン（ca | travisvn |
| obrasuperpowersコレクションでtddデバッグコラボパターンを適用する | obra/superpowersコレクションでTDD/デバッグ/コラボパターンを適用する | claude-code-workflow | obra氏のsuperpowersライブラリ（20+の実戦検証済みSkill）を導入し、`/brainstorm`、`/ | travisvn |
| skillのセキュリティ監査を実施してから有効化する | Skillのセキュリティ監査を実施してから有効化する | claude-code-workflow | コミュニティSkillや自作Skillを有効化する前に、SKILL.md・scripts/の全コードをレビューし、データ | travisvn |
| npx経由でmcpサーバーを即座に検証する | npx経由でMCPサーバーを即座に検証する | prompt-engineering | 開発中のMCPサーバーをクローン不要・設定不要でInspector UIに接続し、tools/resources/pro | modelcontextprotocol |
| cliモードでmcpサーバーをスクリプト可能にテストする | CLIモードでMCPサーバーをスクリプト可能にテストする | prompt-engineering | MCP Inspectorをコマンドラインから実行し、tools/resources/promptsの操作を標準出力に出 | modelcontextprotocol |
| ui-exportボタンでmcpjson設定を自動生成する | UI Exportボタンでmcp.json設定を自動生成する | claude-code-workflow | Inspector UIで動作確認したサーバー設定を「Server Entry」「Servers File」ボタンでクリ | modelcontextprotocol |
| 設定ファイル-configで複数サーバーを管理する | 設定ファイル（--config）で複数サーバーを管理する | other | mcp.json形式の設定ファイルを用意し、`--config`と`--server`オプションで特定サーバーをInsp | modelcontextprotocol |
| 認証トークンでinspector-proxyを保護する | 認証トークンでInspector Proxyを保護する | ui-ux | Inspector起動時に自動生成されるセッショントークンをブラウザに入力またはURL経由で渡し、プロキシサーバーへの不 | modelcontextprotocol |
| 分野別スキルカタログから必要なスキルを発見してインストールする | 分野別スキルカタログから必要なスキルを発見してインストールする | claude-code-workflow | awesome-claude-skillsのような分野別整理されたカタログから、プロジェクトのニーズに合致するスキルを検 | BehiSecc |
| skillmd-標準形式で独自スキルを作成共有する | SKILL.md 標準形式で独自スキルを作成・共有する | claude-code-workflow | skill-creator テンプレートを使い、name/description/使用タイミング/具体的手順を記述した  | BehiSecc |
| 複数スキルを組み合わせてワークフロー全体を最適化する | 複数スキルを組み合わせてワークフロー全体を最適化する | claude-code-workflow | TDD（test-driven-development） + セキュリティ（VibeSec） + デバッグ（system | BehiSecc |
| ドメイン特化型スキルコレクションを一括導入する | ドメイン特化型スキルコレクションを一括導入する | agent-orchestration | claude-starter（40スキル）、Agent Almanac（317スキル）、agentskills.sh（6 | BehiSecc |
| mcpmodel-context-protocol対応スキルでツール連携を拡張する | MCP（Model Context Protocol）対応スキルでツール連携を拡張する | claude-code-workflow | Linear、Google Workspace、PostgreSQL、NotebookLM等の外部サービスと連携するMC | BehiSecc |
| git-worktreeベースのエージェント分離実行 | git worktreeベースのエージェント分離実行 | claude-code-workflow | 各タスクを独立したgit worktree（別ディレクトリ＋ブランチ）に配置し、複数のCLIエージェントを同時並行で動か | superset-sh |
| workspace-setupteardownスクリプトによる環境自動化 | workspace setup/teardownスクリプトによる環境自動化 | agent-orchestration | workspaceごとに.envコピー、依存インストール、DB初期化等を自動実行する | superset-sh |
| ワンクリックエディタターミナル遷移による高速レビュー | ワンクリックエディタ/ターミナル遷移による高速レビュー | agent-orchestration | diff viewerで変更確認後、⌘Oでエディタまたはターミナルを開いて即座に編集できる | superset-sh |
| プリセットベースのターミナル分割レイアウト | プリセットベースのターミナル分割レイアウト | agent-orchestration | よく使うコマンド組み合わせ（dev server + log watch等）をプリセット保存し、Ctrl+1-9で即起動 | superset-sh |
| トークン最適化設定による-60-70-コスト削減 | トークン最適化設定による 60-70% コスト削減 | claude-code-workflow | model, MAX_THINKING_TOKENS, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE  | affaan-m |
| フック駆動の自動品質ゲート | フック駆動の自動品質ゲート | claude-code-workflow | ツール実行の前後で自動的にチェック（console.log 検出、シークレット検出、フォーマット実行）を挟み込む | affaan-m |
| 継続学習-v2instinct-ベース | 継続学習 v2（Instinct ベース） | claude-code-workflow | セッションから自動的にパターンを抽出し、信頼度スコア付きで蓄積。関連するパターンをクラスタリングして再利用可能なスキルに | affaan-m |
| 検証ループeval-harness | 検証ループ（Eval Harness） | claude-code-workflow | ビルド・テスト・リント・型チェック・セキュリティスキャンを自動実行し、結果を評価。pass@k メトリクスで品質を定量化 | affaan-m |
| クロスプラットフォームインストール | クロスプラットフォームインストール | claude-code-workflow | 単一のインストーラーで、Claude Code/Cursor/Codex/OpenCode に対応した設定を自動配置 | affaan-m |
| agentshield-セキュリティスキャン | AgentShield セキュリティスキャン | claude-code-workflow | CLAUDE.md, settings.json, MCP configs, hooks, agents, skills | affaan-m |
| マニフェスト駆動の選択的インストール | マニフェスト駆動の選択的インストール | agent-orchestration | ユーザーが必要なコンポーネント（agents/commands/skills/rules）だけをインタラクティブに選択し | affaan-m |
| カテゴリ別リソース分類によるエコシステム整理 | カテゴリ別リソース分類によるエコシステム整理 | claude-code-workflow | Claude Code の拡張機能を「Agent Skills」「Workflows」「Tooling」「Status  | hesreallyhim |
| フックhooksを活用した-claude-code-のライフサイクル制御 | フック（Hooks）を活用した Claude Code のライフサイクル制御 | claude-code-workflow | Claude Code の動作ライフサイクルの特定ポイント（ファイル書き込み前、コマンド実行前など）でスクリプトを自動実 | hesreallyhim |
| スラッシュコマンドによるカスタムプロンプトのテンプレート化 | スラッシュコマンドによるカスタムプロンプトのテンプレート化 | claude-code-workflow | 頻繁に使う複雑なプロンプトを `/commit`、`/tdd`、`/create-pr` などのスラッシュコマンドとして | hesreallyhim |
| claudemd-によるプロジェクト固有ルールの注入 | CLAUDE.md によるプロジェクト固有ルールの注入 | claude-code-workflow | プロジェクトルートに `CLAUDE.md` ファイルを配置し、コーディング規約・アーキテクチャ・禁止事項などを Cla | hesreallyhim |
| agent-skills-による専門知識のモジュール化 | Agent Skills による専門知識のモジュール化 | claude-code-workflow | 特定ドメイン（セキュリティ監査、科学計算、デザインレビューなど）の専門知識をスキルファイルとしてパッケージ化し、Clau | hesreallyhim |
| 使用状況監視ツールによるトークン消費の可視化 | 使用状況監視ツールによるトークン消費の可視化 | claude-code-workflow | Claude Code のログファイルを解析し、トークン消費量・コスト・セッション履歴などをダッシュボードで可視化する | hesreallyhim |
| オーケストレーターによる複数-claude-code-セッションの並列制御 | オーケストレーターによる複数 Claude Code セッションの並列制御 | claude-code-workflow | 複数の Claude Code インスタンスを並列起動し、異なるタスク（フロントエンド開発、バックエンド開発、テストなど | hesreallyhim |
| デコレータベースのツール定義でmcpスキーマ自動生成 | デコレータベースのツール定義でMCPスキーマ自動生成 | other | Python関数に`@mcp.tool`デコレータを付けるだけで、MCP準拠のツールスキーマ・バリデーション・ドキュメン | PrefectHQ |
| fastmcpの3本柱アーキテクチャで役割分離 | FastMCPの3本柱アーキテクチャで役割分離 | prompt-engineering | Servers（ツール公開）、Apps（UI提供）、Clients（サーバー接続）の3コンポーネントを使い分けてMCPア | PrefectHQ |
| url接続でトランスポート層を抽象化 | URL接続でトランスポート層を抽象化 | dev-tool | Clientsを使う際、MCPサーバーへの接続をURLで指定するだけで、トランスポート（stdio/SSE/WebSoc | PrefectHQ |
| uv経由でのインストールで依存解決を高速化 | uv経由でのインストールで依存解決を高速化 | automation-pipeline | FastMCPのインストールを`uv pip install fastmcp`で行い、従来のpipより高速な依存解決を利 | PrefectHQ |
| prefect-horizon無料ホスティングで本番デプロイ | Prefect Horizon無料ホスティングで本番デプロイ | automation-pipeline | 開発したFastMCPサーバーをPrefect Horizonにデプロイし、無料で本番環境として公開する | PrefectHQ |
| カテゴリ別サブエージェントのプラグインインストール | カテゴリ別サブエージェントのプラグインインストール | claude-code-workflow | 10カテゴリ（Core Development、Language Specialists、Infrastructure、 | VoltAgent |
| サブエージェントのマニュアルインストールとカスタマイズ | サブエージェントのマニュアルインストールとカスタマイズ | claude-code-workflow | GitHubリポジトリから特定のサブエージェントファイル（Markdown形式）をダウンロードし、`~/.claude/ | VoltAgent |
| モデル選択による品質とコスト最適化 | モデル選択による品質とコスト最適化 | claude-code-workflow | 各サブエージェントのYAMLフロントマターに記載された`model`フィールド（opus, sonnet, haiku） | VoltAgent |
| ツール権限の最小化によるセキュリティ確保 | ツール権限の最小化によるセキュリティ確保 | claude-code-workflow | 各サブエージェントの`tools`フィールドに、そのエージェントが実行可能なClaude Code組み込みツール（Rea | VoltAgent |
| グローバルとプロジェクト固有のエージェント使い分け | グローバルとプロジェクト固有のエージェント使い分け | claude-code-workflow | `~/.claude/agents/`（グローバル）にチーム共通のエージェントを配置し、`.claude/agents/ | VoltAgent |
| 独立コンテキストウィンドウによるタスク分離 | 独立コンテキストウィンドウによるタスク分離 | claude-code-workflow | 各サブエージェントは独立したコンテキストウィンドウ内で動作するため、メインの会話履歴と混ざらず、タスク固有の詳細情報が隔 | VoltAgent |
| メタオーケストレーションエージェントによる複雑ワークフローの自動化 | メタオーケストレーションエージェントによる複雑ワークフローの自動化 | claude-code-workflow | Meta & Orchestrationカテゴリのエージェント（multi-agent-coordinator, wor | VoltAgent |
| progressive-disclosure-architectureによる効率的なskill読み込み | Progressive Disclosure Architectureによる効率的なSkill読み込み | claude-code-workflow | Skillsを段階的に読み込むことで、コンテキストウィンドウを圧迫せずに多数のSkillsを利用可能にする | travisvn |
| skill-vs-他手法の使い分け判断マトリクス適用 | Skill vs 他手法の使い分け判断マトリクス適用 | agent-orchestration | Skills、Prompts、Projects、Subagents、MCPそれぞれの特性を理解し、タスクに最適な手法を選 | travisvn |
| yamlフロントマター-skillmd構造でのskill作成 | YAMLフロントマター + SKILL.md構造でのSkill作成 | claude-code-workflow | 再利用可能なSkillを標準フォーマットで作成し、バージョン管理・共有可能にする | travisvn |
| skill-creatorによる対話的skill生成 | skill-creatorによる対話的Skill生成 | claude-code-workflow | 公式のskill-creatorスキルを使い、Q&A形式で新しいSkillを自動生成する | travisvn |
| セキュリティ監査ベストプラクティスの適用 | セキュリティ監査ベストプラクティスの適用 | claude-code-workflow | Skillsが任意コード実行可能であることを踏まえ、信頼できるソースのみから導入し、コードレビューを徹底する | travisvn |
| claude-code-cliでのskillインストール | Claude Code CLIでのSkillインストール | claude-code-workflow | Claude Code CLI環境でマーケットプレイスまたはローカルディレクトリからSkillsをインストールする | travisvn |
| 公式コミュニティskillsカタログからの選択と活用 | 公式・コミュニティSkillsカタログからの選択と活用 | automation-pipeline | ドキュメント処理、デザイン、開発、コミュニケーション等の分野別に整理された既存Skillsから、タスクに適したものを選ん | travisvn |
| awesome-listsパターンでスキルをカタログ化する | Awesome Listsパターンでスキルをカタログ化する | other | GitHub上でClaude Skillsを分野別（Document、Development、Security等）に分類 | BehiSecc |
| skillmdフォーマットでスキルを定義する | SKILL.mdフォーマットでスキルを定義する | claude-code-workflow | Claude Codeが読み込める標準フォーマット（SKILL.md）でスキルの動作・トリガー条件・ツール呼び出しを記述 | BehiSecc |
| mcpサーバーとスキルを組み合わせる | MCPサーバーとスキルを組み合わせる | claude-code-workflow | Model Context Protocol (MCP)サーバーが提供するツールをSKILL.mdから呼び出し、複雑な外 | BehiSecc |
| スキルをコレクション形式で配布する | スキルをコレクション形式で配布する | claude-code-workflow | 複数のスキルを1つのリポジトリにまとめ、`npx`やインストールスクリプト経由で一括導入できるようにする | BehiSecc |
| セキュリティスキルで脆弱性を自動検出する | セキュリティスキルで脆弱性を自動検出する | claude-code-workflow | OWASP Top 10、ASVS、Agentic AI Securityの知識をSKILL.mdに埋め込み、Claud | BehiSecc |
| git-worktreeでエージェント隔離実行 | git worktreeでエージェント隔離実行 | claude-code-workflow | 1つのリポジトリから複数のworktree（独立した作業ディレクトリ）を作成し、それぞれに異なるブランチを割り当てること | superset-sh |
| 統合監視uiでエージェント状態を一元管理 | 統合監視UIでエージェント状態を一元管理 | agent-orchestration | Electron製デスクトップアプリ（Superset）で複数worktree/エージェントのステータス、変更内容、通知 | superset-sh |
| workspace-presetで環境セットアップ自動化 | Workspace Presetで環境セットアップ自動化 | agent-orchestration | .superset/config.json にセットアップ・ティアダウンスクリプトを定義し、worktree作成時に自動 | superset-sh |
| キーボードショートカットで高速切り替え | キーボードショートカットで高速切り替え | agent-orchestration | Superset UIに組み込まれたカスタマイズ可能なショートカット（⌘1-9でワークスペース切替、⌘Tで新規タブ、⌘D | superset-sh |
| oauth-debuggerで認証フロー全体を可視化する | OAuth Debuggerで認証フロー全体を可視化する | dev-tool | MCPサーバーのOAuth実装を各ステップごとに詳細表示し、ネットワークメッセージを検査する | MCPJam |
| llm-playgroundで複数モデルに対してサーバーをテストする | LLM Playgroundで複数モデルに対してサーバーをテストする | prompt-engineering | GPT-5、Claude Sonnet、Gemini 2.5等のフロンティアモデルを使い、MCPサーバーの応答を無料でテ | MCPJam |
| dockerでポータブルなテスト環境を構築する | Dockerでポータブルなテスト環境を構築する | automation-pipeline | MCPJam InspectorをDockerコンテナで起動し、チーム全体で統一されたテスト環境を提供する | MCPJam |
| 手動ツール実行でウィジェットを即座にプレビューする | 手動ツール実行でウィジェットを即座にプレビューする | prompt-engineering | LLMを介さず、MCPツールを直接実行してウィジェット/リソース/プロンプトの表示を確認する | MCPJam |
| 段階的文脈注入progressive-disclosureでエージェントを専門化する | 段階的文脈注入（Progressive Disclosure）でエージェントを専門化する | claude-code-workflow | CLAUDE.mdをエントリポイントとし、関連性に応じてTier1（思考フレームワーク）、Tier2（エキスパートペルソ | gadievron |
| litellm統合でマルチllmプロバイダをオーケストレーションする | LiteLLM統合でマルチLLMプロバイダをオーケストレーションする | claude-code-workflow | LiteLLMを使ってAnthropic、OpenAI、Gemini、Ollama等を統一インターフェースで扱い、自動フ | gadievron |
| セキュリティツールチェーンをllmで自律オーケストレーションする | セキュリティツールチェーンをLLMで自律オーケストレーションする | claude-code-workflow | Semgrep（静的解析）→CodeQL（データフロー検証）→AFL（ファジング）→LLM分析→PoC生成→パッチ提案を | gadievron |
| secopsagentkitでオフェンシブセキュリティタスクを専門サブエージェントに委譲する | SecOpsAgentKitでオフェンシブセキュリティタスクを専門サブエージェントに委譲する | claude-code-workflow | .claude/agents/offsec-specialist.mdで定義された自律的なペネトレーションテスト専門エー | gadievron |
| oss-forensicsで削除されたgithub履歴をbigquerywayback-machineで復元する | OSS Forensicsで削除されたGitHub履歴をBigQuery+Wayback Machineで復元する | claude-code-workflow | /oss-forensicsコマンドでGitHub Archive（BigQuery）、Wayback Machine、 | gadievron |
| npxで即座にgemini-cliを起動 | npxで即座にGemini CLIを起動 | prompt-engineering | インストール不要で、npxコマンドを使ってGemini CLIをその場で実行する | google-gemini |
| google-oauth認証で無料枠を利用 | Google OAuth認証で無料枠を利用 | context-management | API Keyを使わず、個人のGoogleアカウントでOAuthログインし、無料枠（60req/min, 1000req | google-gemini |
| 非対話モードheadlessでスクリプト実行 | 非対話モード（headless）でスクリプト実行 | prompt-engineering | 対話セッションを開かず、`-p`フラグで直接プロンプトを渡して結果を取得する | google-gemini |
| geminimdでプロジェクト固有コンテキストを永続化 | GEMINI.mdでプロジェクト固有コンテキストを永続化 | context-management | プロジェクトルートに`GEMINI.md`を配置し、Gemini CLIにコーディング規約・アーキテクチャ情報を常に読み | google-gemini |
| mcpサーバー統合でツール拡張 | MCPサーバー統合でツール拡張 | dev-tool | `~/.gemini/settings.json`でMCPサーバーを設定し、Slack、DB、メディア生成などの外部ツー | google-gemini |
| github-action統合でpr自動レビュー | GitHub Action統合でPR自動レビュー | prompt-engineering | Gemini CLI GitHub Actionを使い、PRが作成されたときに自動でコードレビューコメントを投稿する | google-gemini |
| リリースタグで安定版previewnightlyを使い分け | リリースタグで安定版・preview・nightlyを使い分け | dev-tool | npmインストール時に`@latest`、`@preview`、`@nightly`タグを指定し、安定版・週次プレビュー | google-gemini |
| google-search-groundingでリアルタイム情報取得 | Google Search groundingでリアルタイム情報取得 | prompt-engineering | Gemini CLIの標準機能でGoogle Searchをgrounding sourceとして使い、最新情報を含む回 | google-gemini |
| promptfooによるプロンプト自動評価の実行 | promptfooによるプロンプト自動評価の実行 | prompt-engineering | YAML設定ファイルに評価対象のプロンプト、テストケース、使用モデル、評価基準（アサーション）を記述し、promptfo | promptfoo |
| promptfooによるレッドチーム脆弱性スキャン実施 | promptfooによるレッドチーム（脆弱性スキャン）実施 | prompt-engineering | promptfoo red teamコマンドで、プロンプトインジェクション、PII漏洩、有害コンテンツ生成など、LLMア | promptfoo |
| cicdパイプラインへのpromptfoo評価統合 | CI/CDパイプラインへのpromptfoo評価統合 | prompt-engineering | promptfoo evalをCI/CDスクリプトに組み込み、プロンプト変更が品質基準を満たさない場合にビルドを失敗させ | promptfoo |
| promptfoo-code-scanによるpull-requestセキュリティレビュー | promptfoo code scanによるPull Requestセキュリティレビュー | prompt-engineering | Pull Request差分内のLLM関連コード（プロンプト、パラメータ変更等）を静的解析し、セキュリティ・コンプライア | promptfoo |
| promptfooでの複数モデル並列比較 | promptfooでの複数モデル並列比較 | prompt-engineering | 同一プロンプトを複数のLLMプロバイダー（OpenAI、Anthropic、Gemini、Ollama等）に並列送信し、 | promptfoo |
| カテゴリ別サブエージェント分類 | カテゴリ別サブエージェント分類 | claude-code-workflow | 127個のサブエージェントを10カテゴリ(Core Development、Language Specialists、I | VoltAgent |
| 4段階インストール手段の提供 | 4段階インストール手段の提供 | claude-code-workflow | プラグイン方式、手動コピー、対話型スクリプト、スタンドアロンインストーラの4種類を用意し、ユーザーの環境と好みに応じて選 | VoltAgent |
| モデル自動ルーティング設定 | モデル自動ルーティング設定 | claude-code-workflow | 各サブエージェントのfrontmatterに `model: opus/sonnet/haiku` を記述し、タスクの複 | VoltAgent |
| ツール権限の最小化設定 | ツール権限の最小化設定 | claude-code-workflow | 各サブエージェントの役割に応じて、アクセスできるClaude Code組み込みツール(Read, Write, Edit | VoltAgent |
| グローバルプロジェクト固有の配置戦略 | グローバル/プロジェクト固有の配置戦略 | claude-code-workflow | `~/.claude/agents/` に配置したエージェントは全プロジェクトで利用可能(グローバル)、`.claude | VoltAgent |
| サブエージェント構造の標準化 | サブエージェント構造の標準化 | claude-code-workflow | 全エージェント定義ファイルを `name, description, tools, model` のYAML front | VoltAgent |
| yamlベースのツール定義でmcpサーバー化 | YAMLベースのツール定義でMCPサーバー化 | agent-orchestration | データベース接続情報とSQL操作をtools.yamlに宣言的に定義し、toolboxコマンドでMCPサーバーとして起動 | googleapis |
| npxでの即座起動によるプロトタイピング | NPXでの即座起動によるプロトタイピング | dev-tool | バイナリのダウンロード・インストールなしに、npxコマンド1行でMCP Toolboxサーバーを起動する | googleapis |
| toolsetによるツールのグループ化 | Toolsetによるツールのグループ化 | agent-orchestration | 複数のツールをtoolsetとして名前付きグループ化し、エージェントごとに必要なツールセットだけをロードする | googleapis |
| ideとの統合によるdb自然言語操作 | IDEとの統合によるDB自然言語操作 | claude-code-workflow | Claude Code/Cursor等のAI IDEにMCP ToolboxをMCPサーバーとして接続し、コーディング中 | googleapis |
| マルチフレームワーク対応sdkによる統一ロード | マルチフレームワーク対応SDKによる統一ロード | agent-orchestration | Python/JS/Go各言語で、LangChain/LlamaIndex/Genkit/ADK等のフレームワーク別SD | googleapis |
| 動的リロードによるノーダウンタイム更新 | 動的リロードによるノーダウンタイム更新 | agent-orchestration | toolboxサーバー起動時にデフォルトで有効化される設定変更の自動検出・リロード機能 | googleapis |
| oh-my-claudecodeプラグインインストールでteam機能有効化 | oh-my-claudecodeプラグインインストールでTeam機能有効化 | claude-code-workflow | Claude Codeに/plugin marketplace経由でoh-my-claudecodeをインストールし、T | Yeachan-Heo |
| team-modeで複数claudeエージェントをステージドパイプライン実行 | Team Modeで複数Claudeエージェントをステージドパイプライン実行 | claude-code-workflow | 1つのタスクを plan → prd → exec → verify → fix の5段階に分割し、各段階で専門化された | Yeachan-Heo |
| tmux-cliワーカーでcodexgeminiclaudeを並列実行 | tmux CLIワーカーでCodex/Gemini/Claudeを並列実行 | claude-code-workflow | `omc team N:codex\|gemini\|claude "タスク"` で tmux pane内に実際のCLIプロ | Yeachan-Heo |
| スキル学習システムで問題解決パターンを自動抽出再利用 | スキル学習システムで問題解決パターンを自動抽出・再利用 | claude-code-workflow | セッション中の対話から「再利用可能な問題解決パターン」を自動抽出してYAML形式のスキルファイル化し、次回以降同じtri | Yeachan-Heo |
| deep-interview-でsocratic質問により要件を深掘り | /deep-interview でSocratic質問により要件を深掘り | claude-code-workflow | 曖昧なアイデアをSocratic法（問答法）で段階的に掘り下げ、隠れた前提・制約・ゴールを言語化してから実装に入る | Yeachan-Heo |
| openclaw統合でセッションイベントを外部ゲートウェイに転送 | OpenClaw統合でセッションイベントを外部ゲートウェイに転送 | claude-code-workflow | Claude Codeセッションの開始・停止・ツール実行などのイベントを、OpenClawゲートウェイ（Discord/ | Yeachan-Heo |
| ccg-で-codex-gemini-claude-三者統合アドバイザリー | /ccg で Codex + Gemini + Claude 三者統合アドバイザリー | claude-code-workflow | 1つのタスクに対し、`/ask codex` と `/ask gemini` を並列実行し、両者の回答をClaudeが統 | Yeachan-Heo |
| skills-vs-mcp-vs-prompts-vs-subagentsの使い分けルールを適用する | Skills vs MCP vs Prompts vs Subagentsの使い分けルールを適用する | agent-orchestration | タスクの性質に応じて、Skills（再利用可能な手順）、MCP（外部データ統合）、Prompts（即時指示）、Subag | travisvn |
| 公式コミュニティスキルをマーケットプレイスから導入する | 公式/コミュニティスキルをマーケットプレイスから導入する | claude-code-workflow | Anthropic公式スキル（docx, pdf, pptx, xlsx, frontend-design, mcp-b | travisvn |
| スキルのセキュリティ監査とベッティングを実施する | スキルのセキュリティ監査とベッティングを実施する | claude-code-workflow | スキルは任意コード実行可能なため、導入前にSKILL.mdと全スクリプトをレビューし、信頼できるソース・バージョン管理・ | travisvn |
| gitリポジトリでスキルをバージョン管理チーム配布する | Gitリポジトリでスキルをバージョン管理・チーム配布する | claude-code-workflow | カスタムスキルをGitリポジトリで管理し、バージョンタグ付け・ドキュメント化・チーム配布を行う | travisvn |
| awesome-list形式でai-agentスキルをキュレーションする | Awesome List形式でAI agentスキルをキュレーションする | claude-code-workflow | GitHubのAwesome List形式（カテゴリ分類+1行説明+リンク）でClaude Skillsを整理したリポジ | BehiSecc |
| claude-skillをgithubリポジトリとして公開する | Claude SkillをGitHubリポジトリとして公開する | claude-code-workflow | SKILL.mdファイルを含むGitHubリポジトリを作成し、特定のタスク（例: PDFからテキスト抽出、テスト駆動開発 | BehiSecc |
| カテゴリ別にスキルを分類し発見性を高める | カテゴリ別にスキルを分類し発見性を高める | dev-tool | スキルを機能別カテゴリ（Document Skills, Development & Code Tools, Data  | BehiSecc |
| 特定ドメインセキュリティ開発等のスキルをtipとして強調する | 特定ドメイン（セキュリティ、開発等）のスキルをTipとして強調する | agent-orchestration | README冒頭にTipセクションを設け、特に重要なスキル（例: セキュリティ対策）を強調表示し、ユーザーの注意を引く | BehiSecc |
| contributionガイドとcontactセクションでコミュニティ参加を促進する | ContributionガイドとContactセクションでコミュニティ参加を促進する | other | README末尾にContributionガイドとContactセクションを設け、ユーザーがスキルを追加・修正したり、問 | BehiSecc |
| claude-code-marketplaceからスキルプラグインをインストール | Claude Code Marketplaceからスキルプラグインをインストール | claude-code-workflow | Trail of BitsのセキュリティスキルリポジトリをClaude Codeのプラグインマーケットプレイスとして追加 | trailofbits |
| codex環境向けにスキルをローカルインストール | Codex環境向けにスキルをローカルインストール | claude-code-workflow | Codex（Google製CLI AI環境）でTrail of Bitsスキルを利用できるようにする | trailofbits |
| variant-analysisスキルで類似脆弱性を横断検索 | variant-analysisスキルで類似脆弱性を横断検索 | claude-code-workflow | 1つの脆弱性パターンを見つけたら、コードベース全体から同様のパターンを検出する | trailofbits |
| semgrep-rule-creatorで脆弱性検出ルールを作成 | semgrep-rule-creatorで脆弱性検出ルールを作成 | claude-code-workflow | 特定の脆弱性パターンを検出するSemgrepルールをAI支援で作成・改善する | trailofbits |
| fp-checkスキルで偽陽性を体系的に検証 | fp-checkスキルで偽陽性を体系的に検証 | claude-code-workflow | 静的解析ツールが報告したセキュリティ問題が本物の脆弱性か偽陽性かを段階的にレビューする | trailofbits |
| constant-time-analysisでタイミングサイドチャネルを検出 | constant-time-analysisでタイミングサイドチャネルを検出 | claude-code-workflow | 暗号化コードがコンパイラ最適化によって定数時間性を失っていないか検証する | trailofbits |
| ローカル開発環境でマーケットプレイスをテスト | ローカル開発環境でマーケットプレイスをテスト | claude-code-workflow | 自作スキルをマーケットプレイスに公開する前にローカルで動作確認する | trailofbits |
| claude-codeをインストールして起動する | Claude Codeをインストールして起動する | claude-code-workflow | ターミナルからClaude Codeをインストールし、プロジェクトディレクトリで起動する | anthropics |
| 自然言語コマンドでコードベース操作を実行する | 自然言語コマンドでコードベース操作を実行する | claude-code-workflow | Claude Codeセッション内で自然言語の指示を与え、コード理解・編集・Git操作などを実行させる | anthropics |
| プラグインで機能を拡張する | プラグインで機能を拡張する | claude-code-workflow | Claude Code公式リポジトリのpluginsディレクトリを参照し、カスタムコマンドやエージェントを追加する | anthropics |
| bugコマンドでフィードバックを送る | /bugコマンドでフィードバックを送る | claude-code-workflow | Claude Code内で `/bug` コマンドを実行し、問題報告を直接送信する | anthropics |
| slash-commandsによる再利用可能プロンプト | Slash-Commandsによる再利用可能プロンプト | claude-code-workflow | 頻繁に使う複雑なプロンプトを `/commit`, `/tdd` 等の短縮コマンドとして登録し、即座に呼び出す | hesreallyhim |
| claudemdによるプロジェクト固有知識注入 | CLAUDE.mdによるプロジェクト固有知識注入 | claude-code-workflow | リポジトリルートまたは `.claude/` に `CLAUDE.md` を配置し、ビルドコマンド、コーディング規約、ア | hesreallyhim |
| オーケストレータによるマルチエージェント協調 | オーケストレータによるマルチエージェント協調 | claude-code-workflow | 複数のClaude Codeインスタンスを並列起動し、タスクを分散実行・結果を統合する | hesreallyhim |
| セッション履歴の検索復元 | セッション履歴の検索・復元 | claude-code-workflow | 過去のClaude Codeセッションログ（.jsonl）を全文検索し、関連する会話・コード変更を復元する | hesreallyhim |
| 使用量コスト可視化ダッシュボード | 使用量・コスト可視化ダッシュボード | claude-code-workflow | Claude Codeのトークン消費量、APIコスト、モデル使用率をリアルタイム集計・グラフ表示する | hesreallyhim |
| cliskillsによるトークン効率化 | CLI+SKILLSによるトークン効率化 | agent-orchestration | MCPサーバーの代わりにPlaywright CLIとSKILLSを使ってブラウザ自動化を実行し、コンテキストウィンドウ | microsoft |
| mcpによる永続的ブラウザコンテキスト管理 | MCPによる永続的ブラウザコンテキスト管理 | claude-code-workflow | Model Context Protocol (MCP)サーバーを使ってブラウザ自動化を行い、永続的な状態と豊富なイント | microsoft |
| アクセシビリティツリーベースの自動化 | アクセシビリティツリーベースの自動化 | agent-orchestration | スクリーンショットやビジョンモデルの代わりに、Playwrightのアクセシビリティツリーを使ってブラウザ操作を行う | microsoft |
| mcpサーバーのマルチクライアント対応設定 | MCPサーバーのマルチクライアント対応設定 | claude-code-workflow | Playwright MCPサーバーを複数のMCPクライアント（VS Code, Claude Desktop, Cur | microsoft |
| コンテナ単位でのagent分離実行 | コンテナ単位でのAgent分離実行 | claude-code-workflow | 各グループのAI AgentをLinuxコンテナ（macOSならApple Container、Linux/Window | qwibitai |
| スキルベースの機能拡張アーキテクチャ | スキルベースの機能拡張アーキテクチャ | claude-code-workflow | 新機能をコアコードベースにマージせず、Claude Codeスキル（`/add-whatsapp`等のコマンド）として配 | qwibitai |
| 設定ファイルなしのコード直接カスタマイズ | 設定ファイルなしのコード直接カスタマイズ | claude-code-workflow | 設定ファイルを用意せず、ユーザーがコードを直接変更することでカスタマイズする | qwibitai |
| ai-nativeなセットアップデバッグ | AI-nativeなセットアップ・デバッグ | claude-code-workflow | インストールウィザードやダッシュボードの代わりに、Claude Code CLIがセットアップ・監視・デバッグを対話的に | qwibitai |
| onecli-agent-vaultによるクレデンシャル保護 | OneCLI Agent Vaultによるクレデンシャル保護 | agent-orchestration | API keyをコンテナに渡さず、外向きリクエスト時にプロキシ層（OneCLI Agent Vault）がクレデンシャル | qwibitai |
| mcpサーバーでlsp機能をllmに公開する | MCPサーバーでLSP機能をLLMに公開する | claude-code-workflow | LSP（Language Server Protocol）やJetBrains IDE解析をMCPサーバーとしてラップし | oraios |
| シンボルレベルツールでコードを検索編集する | シンボルレベルツールでコードを検索・編集する | other | find_symbol でシンボル名から定義箇所を特定し、find_referencing_symbols で使用箇所を | oraios |
| lspとjetbrains-pluginから選択する | LSPとJetBrains Pluginから選択する | other | バックエンドとしてLSP（無償・オープンソース、40+言語対応）またはJetBrains Plugin（IDE解析、最強 | oraios |
| activepiecesのpieceをtypescriptで開発してmcpサーバー化する | ActivepiecesのpieceをTypeScriptで開発してMCPサーバー化する | agent-orchestration | TypeScriptでActivepieces用のpiece（統合コンポーネント）を作成し、npmに公開することで、自動 | activepieces |
| activepiecesをセルフホストしてエンタープライズ環境で運用する | Activepiecesをセルフホストしてエンタープライズ環境で運用する | automation-pipeline | Activepiecesをオンプレミスまたはプライベートクラウドにデプロイし、ネットワークギャップ環境でも安全にワークフ | activepieces |
| activepiecesのビルダーでノーコードワークフローを構築する | Activepiecesのビルダーでノーコードワークフローを構築する | automation-pipeline | Activepiecesのビルダー（ノーコードUI）を使い、Loops、Branches、Auto Retries、HT | activepieces |
| 宣言的なevals設定でプロンプトを自動評価する | 宣言的なevals設定でプロンプトを自動評価する | prompt-engineering | YAML設定ファイルにプロンプト・モデル・テストケース・評価基準を記述し、promptfoo CLIで一括評価を実行する | promptfoo |
| レッドチーム攻撃で脆弱性を自動検出する | レッドチーム攻撃で脆弱性を自動検出する | prompt-engineering | promptfooのred teamingモードで、prompt injection・jailbreak・PII漏洩・バ | promptfoo |
| 複数モデルを横断比較して最適な選択をする | 複数モデルを横断比較して最適な選択をする | prompt-engineering | promptfooconfig.yamlのproviders配列に複数のLLMプロバイダーを列挙し、同一テストケースで性 | promptfoo |
| cicdパイプラインにevalsred-teamingを組み込む | CI/CDパイプラインにevals/red teamingを組み込む | prompt-engineering | promptfoo CLIをCI/CDスクリプトに統合し、Pull Request時やデプロイ前に自動評価を実行、品質ゲ | promptfoo |
| ローカル実行でプライバシーを保護する | ローカル実行でプライバシーを保護する | prompt-engineering | promptfooはすべての評価処理をローカル環境で実行し、プロンプトや評価データを外部サーバーに送信しない | promptfoo |
| agent-skills標準でドメイン特化スキルを定義 | Agent Skills標準でドメイン特化スキルを定義 | claude-code-workflow | 科学計算ライブラリ・データベース・ツールをAgent Skills仕様のSKILL.mdファイルとして構造化し、AIエー | K-Dense-AI |
| 100データベースを統一database-lookupスキルで検索 | 100+データベースを統一database-lookupスキルで検索 | agent-orchestration | PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov等78データベー | K-Dense-AI |
| 複雑な科学ワークフローを1プロンプトで実行 | 複雑な科学ワークフローを1プロンプトで実行 | agent-orchestration | 「データ取得→前処理→解析→可視化→レポート生成」といった多段階ワークフローを、複数スキルを組み合わせて1プロンプトで完 | K-Dense-AI |
| uvパッケージマネージャでスキル依存関係管理 | uvパッケージマネージャでスキル依存関係管理 | claude-code-workflow | 各スキルのPython依存関係をuvで高速インストール・管理し、環境構築を自動化する | K-Dense-AI |
| セキュリティスキャンで悪意あるスキルを検出 | セキュリティスキャンで悪意あるスキルを検出 | claude-code-workflow | Cisco AI Defense Skill Scannerを使い、スキルがプロンプトインジェクション・データ流出・悪意 | K-Dense-AI |
