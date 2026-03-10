---
title: CLI Demo Runner Pattern
description: CLIツールの機能を順番に実行してデモンストレーションするパターン
tags: [cli, demo, testing, python]
---

# CLI Demo Runner Pattern

CLIツールの機能を順番に実行してデモンストレーションする汎用パターン。

## 基本実装

```python
#!/usr/bin/env python3
"""
CLI Demo Runner
CLIツールの機能を順次実行してデモンストレーション
"""
import sys
import subprocess
import time
from pathlib import Path
from typing import List, Tuple, Optional

class DemoRunner:
    def __init__(self, cli_module: str = "cli", delay: float = 0.5):
        """
        Args:
            cli_module: 実行するCLIモジュール名
            delay: コマンド間の遅延時間（秒）
        """
        self.cli_module = cli_module
        self.delay = delay
        self.results = []
    
    def run_command(self, cmd: List[str], display: bool = True) -> Tuple[str, str, int]:
        """コマンド実行"""
        full_cmd = [sys.executable, "-m", self.cli_module] + cmd
        
        if display:
            print(f"$ {' '.join([self.cli_module] + cmd)}")
        
        result = subprocess.run(
            full_cmd,
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent
        )
        
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        
        if display and stdout:
            for line in stdout.split('\n'):
                print(f"  {line}")
        
        if display and stderr:
            for line in stderr.split('\n'):
                print(f"  [ERROR] {line}")
        
        self.results.append({
            "command": " ".join(cmd),
            "stdout": stdout,
            "stderr": stderr,
            "returncode": result.returncode
        })
        
        return stdout, stderr, result.returncode
    
    def section(self, title: str, emoji: str = "📌"):
        """セクション表示"""
        print(f"\n{emoji} {title}")
        print("-" * 40)
        time.sleep(self.delay)
    
    def assert_output_contains(self, output: str, expected: str):
        """出力検証"""
        if expected not in output:
            print(f"❌ Expected '{expected}' not found in output")
            return False
        return True
    
    def summary(self):
        """実行サマリー表示"""
        print("\n" + "=" * 50)
        print("📊 Demo Summary")
        print("=" * 50)
        
        total = len(self.results)
        success = sum(1 for r in self.results if r["returncode"] == 0)
        
        print(f"Total commands: {total}")
        print(f"Successful: {success}")
        print(f"Failed: {total - success}")
        
        if total == success:
            print("\n✅ All demos completed successfully!")
        else:
            print("\n⚠️ Some commands failed. Check the output above.")

def main():
    """メインデモ実行"""
    demo = DemoRunner("mycli", delay=0.3)
    
    print("=" * 50)
    print("🚀 CLI Tool Demo")
    print("=" * 50)
    
    # デモシナリオ
    demo.section("1. Initialize")
    stdout, _, _ = demo.run_command(["init", "--name", "demo_project"])
    demo.assert_output_contains(stdout, "Initialized")
    
    demo.section("2. Create Items")
    demo.run_command(["create", "item1", "--type", "basic"])
    demo.run_command(["create", "item2", "--type", "advanced"])
    
    demo.section("3. List Items")
    stdout, _, _ = demo.run_command(["list"])
    demo.assert_output_contains(stdout, "item1")
    demo.assert_output_contains(stdout, "item2")
    
    demo.section("4. Process Items")
    demo.run_command(["process", "item1"])
    
    demo.section("5. Status Check")
    demo.run_command(["status"])
    
    # サマリー表示
    demo.summary()

if __name__ == "__main__":
    main()
```

## 使用例

```python
# 基本的な使用
demo = DemoRunner("myapp")
demo.run_command(["--version"])
demo.run_command(["--help"])

# カスタムシナリオ
class MyAppDemo(DemoRunner):
    def run_scenario(self):
        self.section("Setup")
        self.run_command(["setup", "--config", "demo.conf"])
        
        self.section("Main Operations")
        for i in range(3):
            stdout, _, _ = self.run_command(["process", f"file{i}.txt"])
            if "success" in stdout.lower():
                print("  ✅ Processing successful")
        
        self.summary()

demo = MyAppDemo("myapp")
demo.run_scenario()
```

## 特徴

- コマンド実行結果の自動キャプチャ
- 視覚的なセクション分割
- 出力検証機能
- 実行サマリーの自動生成
- エラーハンドリング付き