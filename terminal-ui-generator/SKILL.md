---
tags: [html, css, javascript, terminal-ui]
dependencies: []
author: Assistant
version: 1.0.0
created: 2026-03-14
---

# Terminal UI Generator

ターミナル風の見た目を持つWeb UIを簡単に作成するためのHTML/CSS/JavaScriptテンプレート。

## 機能

- 黒背景・緑文字のターミナル風デザイン
- コマンド入力と結果表示
- 実行履歴の保持と表示
- キーボードショートカット対応

## 基本テンプレート

### HTML構造

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terminal UI</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="terminal-container">
        <div class="terminal-header">
            <span class="terminal-title">Terminal</span>
            <div class="terminal-controls">
                <span class="control minimize">_</span>
                <span class="control maximize">□</span>
                <span class="control close">×</span>
            </div>
        </div>
        <div class="terminal-body">
            <div id="output" class="terminal-output"></div>
            <div class="terminal-input-line">
                <span class="prompt">$</span>
                <input type="text" id="command-input" class="terminal-input" autofocus>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### CSSスタイル

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background: #1e1e1e;
    font-family: 'Courier New', monospace;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.terminal-container {
    width: 90%;
    max-width: 800px;
    background: #0c0c0c;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.1);
    overflow: hidden;
}

.terminal-header {
    background: #2d2d2d;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.terminal-title {
    color: #00ff00;
    font-size: 14px;
}

.terminal-controls {
    display: flex;
    gap: 8px;
}

.control {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    color: #000;
}

.minimize { background: #ffd700; }
.maximize { background: #00ff00; }
.close { background: #ff5555; }

.terminal-body {
    padding: 20px;
    min-height: 400px;
    max-height: 600px;
    overflow-y: auto;
}

.terminal-output {
    color: #00ff00;
    white-space: pre-wrap;
    margin-bottom: 10px;
    line-height: 1.4;
}

.terminal-input-line {
    display: flex;
    align-items: center;
}

.prompt {
    color: #00ff00;
    margin-right: 8px;
}

.terminal-input {
    flex: 1;
    background: transparent;
    border: none;
    color: #00ff00;
    font-family: inherit;
    font-size: 14px;
    outline: none;
}

/* カーソル点滅 */
.terminal-input {
    caret-color: #00ff00;
}

/* コマンド出力のスタイル */
.command-line {
    color: #00ff00;
    margin: 5px 0;
}

.output-line {
    color: #b0b0b0;
    margin-left: 20px;
}

.error-line {
    color: #ff5555;
}

.success-line {
    color: #50fa7b;
}

/* スクロールバーのカスタマイズ */
.terminal-body::-webkit-scrollbar {
    width: 8px;
}

.terminal-body::-webkit-scrollbar-track {
    background: #1a1a1a;
}

.terminal-body::-webkit-scrollbar-thumb {
    background: #00ff00;
    border-radius: 4px;
}
```

### JavaScriptロジック

```javascript
class Terminal {
    constructor() {
        this.output = document.getElementById('output');
        this.input = document.getElementById('command-input');
        this.history = [];
        this.historyIndex = -1;
        
        this.initEventListeners();
        this.printWelcome();
    }
    
    initEventListeners() {
        this.input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                this.executeCommand();
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                this.navigateHistory(-1);
            } else if (e.key === 'ArrowDown') {
                e.preventDefault();
                this.navigateHistory(1);
            } else if (e.ctrlKey && e.key === 'l') {
                e.preventDefault();
                this.clear();
            }
        });
    }
    
    printWelcome() {
        this.print('Terminal UI v1.0.0', 'success-line');
        this.print('Type "help" for available commands\n');
    }
    
    print(text, className = '') {
        const line = document.createElement('div');
        line.textContent = text;
        if (className) line.className = className;
        this.output.appendChild(line);
        this.scrollToBottom();
    }
    
    executeCommand() {
        const command = this.input.value.trim();
        if (!command) return;
        
        // コマンドを履歴に追加
        this.history.push(command);
        this.historyIndex = this.history.length;
        
        // コマンドを出力に表示
        this.print(`$ ${command}`, 'command-line');
        
        // コマンドを処理
        this.processCommand(command);
        
        // 入力をクリア
        this.input.value = '';
    }
    
    processCommand(command) {
        // ローカルコマンドの処理
        switch(command.toLowerCase()) {
            case 'help':
                this.showHelp();
                break;
            case 'clear':
                this.clear();
                break;
            case 'date':
                this.print(new Date().toString(), 'output-line');
                break;
            default:
                // サーバーにコマンドを送信
                this.sendToServer(command);
        }
    }
    
    async sendToServer(command) {
        try {
            const response = await fetch('/execute', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({command})
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.print(result.output, 'output-line');
            } else {
                this.print(result.output, 'error-line');
            }
        } catch (error) {
            this.print(`Error: ${error.message}`, 'error-line');
        }
    }
    
    showHelp() {
        const helpText = `
Available commands:
  help     - Show this help message
  clear    - Clear the terminal
  date     - Show current date and time
  
Keyboard shortcuts:
  Ctrl+L   - Clear screen
  ↑/↓      - Navigate command history
`;
        this.print(helpText, 'output-line');
    }
    
    clear() {
        this.output.innerHTML = '';
    }
    
    navigateHistory(direction) {
        if (this.history.length === 0) return;
        
        this.historyIndex += direction;
        
        if (this.historyIndex < 0) {
            this.historyIndex = 0;
        } else if (this.historyIndex >= this.history.length) {
            this.historyIndex = this.history.length;
            this.input.value = '';
            return;
        }
        
        this.input.value = this.history[this.historyIndex];
    }
    
    scrollToBottom() {
        this.output.scrollTop = this.output.scrollHeight;
    }
}

// Terminal初期化
document.addEventListener('DOMContentLoaded', () => {
    new Terminal();
});
```

## カスタマイズ例

### テーマカラーの変更

```css
/* Amber テーマ */
.terminal-amber {
    --primary-color: #ffb000;
    --background-color: #1a0e00;
}

/* Cyan テーマ */
.terminal-cyan {
    --primary-color: #00ffff;
    --background-color: #001a1a;
}

/* 使用例 */
.terminal-output,
.prompt,
.terminal-input {
    color: var(--primary-color);
}
```

### タイプライターエフェクト

```javascript
async function typeWriter(element, text, delay = 50) {
    element.textContent = '';
    for (let i = 0; i < text.length; i++) {
        element.textContent += text[i];
        await new Promise(resolve => setTimeout(resolve, delay));
    }
}

// 使用例
const outputLine = document.createElement('div');
output.appendChild(outputLine);
await typeWriter(outputLine, 'System initializing...', 30);
```

### ASCII アートの追加

```javascript
const asciiArt = `
 _____ _____ ____  __  __ ___ _   _    _    _     
|_   _| ____|  _ \\|  \\/  |_ _| \\ | |  / \\  | |    
  | | |  _| | |_) | |\\/| || ||  \\| | / _ \\ | |    
  | | | |___|  _ <| |  | || || |\\  |/ ___ \\| |___ 
  |_| |_____|_| \\_\\_|  |_|___|_| \\_/_/   \\_\\_____|`;

this.print(asciiArt, 'ascii-art');
```

## 高度な機能

### オートコンプリート

```javascript
const commands = ['help', 'clear', 'date', 'ls', 'pwd', 'echo'];

function autoComplete(input) {
    const value = input.value.toLowerCase();
    const matches = commands.filter(cmd => cmd.startsWith(value));
    
    if (matches.length === 1) {
        input.value = matches[0];
    } else if (matches.length > 1) {
        // 候補を表示
        console.log('Suggestions:', matches.join(', '));
    }
}

input.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
        e.preventDefault();
        autoComplete(input);
    }
});
```