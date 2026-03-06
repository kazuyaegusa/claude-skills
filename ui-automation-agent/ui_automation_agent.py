import json
import re
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum


class ActionType(Enum):
    CLICK = "click"
    TYPE = "type"
    SCROLL = "scroll"
    WAIT = "wait"


@dataclass
class UIElement:
    element_type: str
    text: str
    position: Tuple[int, int]
    size: Tuple[int, int]
    clickable: bool
    input_field: bool


@dataclass
class Action:
    action_type: ActionType
    target: Optional[UIElement]
    value: Optional[str] = None


class VisionAnalyzer:
    """画面UIを解析してインタラクション可能な要素を検出"""
    
    def analyze_screen(self, screen_html: str) -> List[UIElement]:
        elements = []
        
        # ボタン検出
        button_pattern = r'<button[^>]*>(.*?)</button>'
        for match in re.finditer(button_pattern, screen_html, re.DOTALL):
            text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
            elements.append(UIElement(
                element_type="button",
                text=text,
                position=(100, 100),
                size=(120, 40),
                clickable=True,
                input_field=False
            ))
        
        # 入力フィールド検出
        input_pattern = r'<input[^>]*name=["\']([^"\' ]+)["\'][^>]*>'
        for match in re.finditer(input_pattern, screen_html):
            name = match.group(1)
            elements.append(UIElement(
                element_type="input",
                text=name,
                position=(100, 200),
                size=(300, 30),
                clickable=False,
                input_field=True
            ))
        
        # リンク検出
        link_pattern = r'<a[^>]*>(.*?)</a>'
        for match in re.finditer(link_pattern, screen_html, re.DOTALL):
            text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
            elements.append(UIElement(
                element_type="link",
                text=text,
                position=(150, 300),
                size=(100, 20),
                clickable=True,
                input_field=False
            ))
        
        return elements


class TaskPlanner:
    """タスク目標から実行アクション列を生成"""
    
    def __init__(self, vision: VisionAnalyzer):
        self.vision = vision
    
    def plan_actions(self, task: str, screen_html: str) -> List[Action]:
        elements = self.vision.analyze_screen(screen_html)
        actions = []
        
        task_lower = task.lower()
        
        # フォーム入力タスク
        if "fill" in task_lower or "入力" in task_lower:
            form_data = self._extract_form_data(task)
            
            for field_name, value in form_data.items():
                target = next((e for e in elements if e.input_field and field_name in e.text.lower()), None)
                if target:
                    actions.append(Action(ActionType.CLICK, target))
                    actions.append(Action(ActionType.TYPE, target, value))
        
        # クリックタスク
        if "click" in task_lower or "クリック" in task_lower:
            button_keywords = ["submit", "送信", "確認", "book", "予約"]
            for keyword in button_keywords:
                if keyword in task_lower:
                    target = next((e for e in elements if e.clickable and keyword in e.text.lower()), None)
                    if target:
                        actions.append(Action(ActionType.CLICK, target))
        
        return actions
    
    def _extract_form_data(self, task: str) -> dict:
        data = {}
        
        name_match = re.search(r'名前[:：]\s*([^\s,，]+)', task)
        if name_match:
            data["name"] = name_match.group(1)
        
        email_match = re.search(r'メール[:：]\s*([^\s,，]+@[^\s,，]+)', task)
        if email_match:
            data["email"] = email_match.group(1)
        
        date_match = re.search(r'日付[:：]\s*([0-9/\-]+)', task)
        if date_match:
            data["date"] = date_match.group(1)
        
        rooms_match = re.search(r'部屋[:：]\s*(\d+)', task)
        if rooms_match:
            data["rooms"] = rooms_match.group(1)
        
        return data


class BrowserExecutor:
    """アクション列を実際のブラウザ操作に変換"""
    
    def __init__(self):
        self.execution_log = []
    
    def execute(self, actions: List[Action]) -> bool:
        print("\n[BrowserExecutor] アクション実行開始")
        
        for i, action in enumerate(actions, 1):
            log_entry = self._execute_single(action, i)
            self.execution_log.append(log_entry)
            print(f"  {log_entry}")
        
        print("[BrowserExecutor] 実行完了")
        return True
    
    def _execute_single(self, action: Action, step: int) -> str:
        if action.action_type == ActionType.CLICK:
            return f"Step {step}: CLICK on '{action.target.text}' at {action.target.position}"
        elif action.action_type == ActionType.TYPE:
            return f"Step {step}: TYPE '{action.value}' into '{action.target.text}'"
        elif action.action_type == ActionType.SCROLL:
            return f"Step {step}: SCROLL to {action.value}"
        elif action.action_type == ActionType.WAIT:
            return f"Step {step}: WAIT {action.value}s"
        return f"Step {step}: UNKNOWN action"


class CUAgent:
    """Computer Using Agent メインクラス"""
    
    def __init__(self):
        self.vision = VisionAnalyzer()
        self.planner = TaskPlanner(self.vision)
        self.executor = BrowserExecutor()
    
    def execute_task(self, task: str, screen_html: str) -> dict:
        print(f"\n{'='*60}")
        print(f"TASK: {task}")
        print(f"{'='*60}")
        
        print("\n[1] 画面UI解析中...")
        elements = self.vision.analyze_screen(screen_html)
        print(f"  検出要素: {len(elements)}個")
        for elem in elements:
            print(f"    - {elem.element_type}: '{elem.text}' (clickable={elem.clickable}, input={elem.input_field})")
        
        print("\n[2] アクション計画生成中...")
        actions = self.planner.plan_actions(task, screen_html)
        print(f"  計画アクション数: {len(actions)}個")
        
        print("\n[3] ブラウザ操作実行中...")
        success = self.executor.execute(actions)
        
        return {
            "success": success,
            "elements_detected": len(elements),
            "actions_planned": len(actions),
            "execution_log": self.executor.execution_log
        }


if __name__ == "__main__":
    sample_screen = """
    <html>
        <body>
            <h1>ホテル予約フォーム</h1>
            <form>
                <input type="text" name="name" placeholder="お名前">
                <input type="email" name="email" placeholder="メールアドレス">
                <button type="submit">予約を確定</button>
            </form>
        </body>
    </html>
    """
    
    task = "名前: 山田太郎 メール: yamada@example.com を入力して送信"
    
    agent = CUAgent()
    result = agent.execute_task(task, sample_screen)
    
    print("\n" + "="*60)
    print("実行結果")
    print("="*60)
    print(f"成功: {result['success']}")
    print(f"検出UI要素: {result['elements_detected']}")
    print(f"実行アクション: {result['actions_planned']}")
