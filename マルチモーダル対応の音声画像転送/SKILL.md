# マルチモーダル対応の音声・画像転送

> チャットアプリから送信された音声メッセージや画像を、AIエージェントが処理できる形式（テキスト化、画像データ）に変換して転送する

- 出典: https://github.com/chenhg5/cc-connect
- 投稿者: chenhg5
- カテゴリ: agent-orchestration

## なぜ使うのか

音声での指示やスクリーンショットでのバグ報告が可能になり、テキスト入力の手間が省ける

## いつ使うのか

スマホから音声やスクリーンショットでAIエージェントに指示したい場合

## やり方

1. プラットフォームAPIから音声ファイルまたは画像URLを取得
2. 音声の場合、STT（Speech-to-Text）APIでテキスト化
3. 画像の場合、base64エンコードまたはURLをエージェントに渡す
4. エージェントがマルチモーダルモデル（Claude 3等）の場合、直接画像を解析
5. 応答をTTS（Text-to-Speech）で音声化してチャットに返すことも可能

### 入力

- 音声メッセージファイル（.ogg等）
- 画像ファイル（.png、.jpg等）

### 出力

- テキスト化された音声内容
- 画像解析結果

## 使うツール・ライブラリ

- STT API（OpenAI Whisper、Google STT等）
- TTS API
- 画像処理ライブラリ

## コード例

```
if msg.Type == "voice" {
  text := sttAPI.Transcribe(msg.VoiceURL)
  response := agent.Process(text)
  sendToPlatform(response)
} else if msg.Type == "image" {
  img := downloadImage(msg.ImageURL)
  response := agent.ProcessImage(img)
  sendToPlatform(response)
}
```

## 前提知識

- 各チャットプラットフォームのBot API基礎知識（認証、メッセージ送受信）
- WebSocketまたはLong Pollingの概念
- AIエージェント（Claude Code、Gemini CLI等）の基本的な使い方
- Go言語の基礎（ソースビルドする場合）
- TOML設定ファイルの記法
