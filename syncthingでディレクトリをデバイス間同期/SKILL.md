# Syncthingでディレクトリをデバイス間同期

> 2台以上のコンピュータ間で任意のディレクトリをリアルタイムに双方向同期する。中央サーバー不要のP2P方式。

- 出典: https://x.com/nukonuko/status/2030503509838458910
- 投稿者: ぬこぬこ / NUKO
- カテゴリ: data-processing

## なぜ使うのか

データが自分のデバイスにのみ存在し第三者に渡らない。暗号化通信かつデバイス証明書で認証するため、クラウドストレージより高いプライバシーを確保できる。

## いつ使うのか

複数のMac/Linux/Windowsマシンで同一のローカルパスのディレクトリを使いたいとき。特にクラウドストレージを通したくないファイルや、常にローカルにある必要があるファイル（スキル・設定・再現キットなど）を同期するとき。

### 具体的な適用場面

- ~/.claude/skills/ や ~/.claude/projects/ などのAIエージェント設定ディレクトリを複数マシンで同期したい場面
- 機密性の高いコードや設定ファイルをクラウドサービスに預けずデバイス間で共有したい場面
- sennin_scoutのskills/x-mined/やreproductions/など、gitでも管理しているが別デバイスとリアルタイムで共有したいディレクトリがある場面

## やり方

1. syncthing.net からOSに合わせたバイナリをダウンロードしてインストール（macOS: `brew install syncthing`）
2. `syncthing` コマンドで起動後、ブラウザで `http://127.0.0.1:8384` を開く
3. 同期したい側のデバイスの「デバイスID」（長い英数字文字列）をコピー
4. もう一方のデバイスの管理UIで「リモートデバイスを追加」→ デバイスIDを貼り付けて承認
5. 管理UIで「フォルダを追加」→ 同期したいディレクトリのパスを指定（例: `/Users/yourname/.claude/skills`）
6. 追加したフォルダを相手デバイスと共有設定する
7. 両デバイスでlaunchdやsystemdに登録してバックグラウンド常駐させる（macOS: `brew services start syncthing`）

### 入力

- 同期元デバイスと同期先デバイス（2台以上）
- 同期したいディレクトリのパス（例: ~/.claude/skills/）
- 両デバイスがLANまたはインターネット経由で通信できる環境

### 出力

- 指定ディレクトリが全デバイスでリアルタイムに同一内容になる
- 片方のデバイスでファイルを追加・編集すると数秒以内に他デバイスへ反映

## 使うツール・ライブラリ

- Syncthing（https://syncthing.net/）
- brew（macOSの場合）: brew install syncthing / brew services start syncthing

## コード例

```
# macOSでのセットアップ
brew install syncthing
brew services start syncthing
# → http://127.0.0.1:8384 でWeb UIを開いてデバイス追加・フォルダ設定
```

## 前提知識

- 同期対象の2台以上のデバイスが存在すること
- 各デバイスにSyncthingをインストールできる権限があること
- デバイス間がネットワーク（LAN or インターネット）で到達可能であること

## 根拠

> 「ディレクトリは Syncthing で同期してる、おすすめ」

> 「None of your data is ever stored anywhere else other than on your computers. There is no central server」（syncthing.net）

> 「All communication is secured using TLS. The encryption used includes perfect forward secrecy」（syncthing.net）

> 「Every device is identified by a strong cryptographic certificate. Only devices you have explicitly allowed can connect」（syncthing.net）

> 「Works on macOS, Windows, Linux, FreeBSD, Solaris, OpenBSD, and many others」（syncthing.net）
