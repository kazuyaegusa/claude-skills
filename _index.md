# スキルインデックス

合計: 208 スキル

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
