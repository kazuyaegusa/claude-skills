# スキルインデックス

合計: 22 スキル

| slug | 名前 | カテゴリ | 説明 | 出典 |
|------|------|----------|------|------|
| タスクキューとしてlinearを活用する | タスクキューとしてLinearを活用する | agent-orchestration | LinearのIssueをAIエージェントへのジョブ投入口として使い、ステータス（not human / human / | 遠藤巧巳 - AIネイティブな会社の作り |
| cronで10分ポーリングループを構築する | cronで10分ポーリングループを構築する | agent-orchestration | cronジョブまたはsystemdタイマーでポーリングスクリプトを定期実行し、常駐プロセスなしにエージェントループを維持 | 遠藤巧巳 - AIネイティブな会社の作り |
| claude-pでタスクをノンインタラクティブ実行する | claude -pでタスクをノンインタラクティブ実行する | claude-code-workflow | `claude -p`（print mode）を使い、タスク内容を標準入力またはプロンプト引数として渡してClaudeC | 遠藤巧巳 - AIネイティブな会社の作り |
| タスク種別でエージェント処理を分岐する | タスク種別でエージェント処理を分岐する | agent-orchestration | タスクに『not human（AIが自律実行）』と『human（AIがリサーチのみ実行）』の2種別を設け、種別に応じて実 | 遠藤巧巳 - AIネイティブな会社の作り |
| 自宅常駐pcをエージェント基盤として活用する | 自宅常駐PCをエージェント基盤として活用する | claude-code-workflow | クラウドサーバーを使わず、自宅の常時起動LinuxPCをエージェントの実行基盤として使うアーキテクチャを採用する。 | 遠藤巧巳 - AIネイティブな会社の作り |
| homerowで画面全体をキーボード操作する | Homerowで画面全体をキーボード操作する | ui-ux | macOS上の全ネイティブアプリのボタン・リンク・UI要素に一時的なキーボードラベルを表示し、ラベルのキーを押すだけでク | Oikon |
| commandagentskillオーケストレーション | Command→Agent→Skillオーケストレーション | claude-code-workflow | Claude Codeの3つの拡張機能（Commands・Subagents・Skills）を役割分担して組み合わせ、複 | Kyohei - OSS, 外資IT |
| claudemd最適化分割管理 | CLAUDE.md最適化・分割管理 | claude-code-workflow | CLAUDE.mdを200行以下に保ち、大きくなった場合は`.claude/rules/`ディレクトリに分割して管理する | Kyohei - OSS, 外資IT |
| コンテキスト50compactルール | コンテキスト50%compactルール | claude-code-workflow | コンテキスト使用率が50%に達したタイミングで手動で`/compact`を実行し、新しいタスクに切り替える際は`/cle | Kyohei - OSS, 外資IT |
| プランモードaskuserquestion設計フロー | プランモード+AskUserQuestion設計フロー | claude-code-workflow | 作業開始時は必ずプランモードで開始し、要件が曖昧な場合はClaudeにAskUserQuestionツールを使ったインタ | Kyohei - OSS, 外資IT |
| git-worktrees並列エージェント開発 | Git Worktrees並列エージェント開発 | claude-code-workflow | git worktreesを使って複数のエージェントが同一リポジトリの異なるブランチで同時並列に作業できる環境を構築する | Kyohei - OSS, 外資IT |
| ベストプラクティスナレッジリポジトリ構築 | ベストプラクティスナレッジリポジトリ構築 | claude-code-workflow | プログラムコードではなく、ツール活用ナレッジ・ベストプラクティス・Tips・ワークフローをマークダウンで構造化・集約した | Kyohei - OSS, 外資IT |
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
