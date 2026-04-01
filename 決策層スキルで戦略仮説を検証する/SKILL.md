# 決策層スキルで戦略仮説を検証する

> 実装前に /plan-ceo-review や /office-hours 等のスキルを実行し、CEO視角・YC式プロダクト思考で方針の妥当性と見落としを洗い出す

- 出典: https://x.com/xxx111god/status/2035013351734997499
- 投稿者: Jason Zuo
- カテゴリ: skill-management

## なぜ使うのか

AIで実装コストがゼロになると、間違った方向に全速力で進むリスクが高まる。数千社を見てきたYCの判断基準を事前適用することで、致命的な前提の見落としや方向性の誤りを早期発見できる

## いつ使うのか

「方向性は決まった、あとは実装するだけ」と思った瞬間。複数の選択肢がありどれを選ぶべきか迷ったとき。過去に方向性の誤りで工数を無駄にした経験がある場合

### 具体的な適用場面

- 複数プロジェクトを並行推進中で、どれに集中すべきか迷っている場合
- 機能実装の方向性は決めたが、見落としている前提条件や代替案がないか確認したい場合
- AI支援で開発速度は上がったが、プロダクトの方向性に不安がある場合
- YC式の戦略レビューを受けたいが、実際にYCに参加できない環境にいる場合

## やり方

1. gstack リポジトリをクローン: `git clone https://github.com/garrytan/gstack`
2. gstack/skills/ ディレクトリを ~/.claude/skills/ にコピーまたはシンボリックリンク
3. Claude Code で実装計画を書いた後、コードを書く前に `/plan-ceo-review` を実行
4. 出力された指摘（見落とした仮説、代替案、リスク）を計画に反映してから実装開始
5. 必要に応じて `/office-hours` (YC式プロダクト思考)、`/plan-eng-review` (アーキテクチャ評審) も併用

### 入力

- 実装しようとしている機能・プロジェクトの計画書（マークダウン等）
- 現在の前提条件・制約・目的の記述
- gstack の決策層スキル（/plan-ceo-review, /office-hours, /plan-eng-review）

### 出力

- 見落としていた前提条件のリスト
- 代替アプローチの提案
- 実装前に検証すべき仮説
- 優先順位の再評価結果

## 使うツール・ライブラリ

- gstack (https://github.com/garrytan/gstack)
- Claude Code
- /plan-ceo-review スキル
- /office-hours スキル
- /plan-eng-review スキル

## 前提知識

- Claude Code または同等の AI コーディング環境の基本的な使い方
- スキル（skill）の概念と、~/.claude/skills/ へのインストール方法
- マークダウン形式のプロンプト・スキルファイルの構造理解
- プロダクト開発における「実装」と「戦略判断」の区別

## 根拠

> gstack 里 15 个角色本质上分两类：执行层 — /review、/qa、/ship 帮你做得更快；决策层 — /office-hours、/plan-ceo-review、/plan-eng-review 帮你想得更对

> 真正的瓶颈暴露了：不是能不能做 是该不该做

> Garry 看过几千个创业公司 什么时候推进 什么时候砍掉 什么时候转向 这种判断力是他几十年积累的 现在打包成 skill 开源了

> 刚用 /plan-ceo-review 重新审了一遍我的预测市场trader的auto research 本来觉得方向挺清楚的 跑完之后发现自己漏掉了两三个关键假设

> gstack README: 'I am doing 10,000 to 20,000 usable lines of code per day... My last /retro: 140,751 lines added, 362 commits, ~115k net LOC'
