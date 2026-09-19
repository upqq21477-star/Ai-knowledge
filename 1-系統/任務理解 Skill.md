# 任務理解 Skill（Task Understanding Skill） v1.2

版本：v1.2
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition】

## 1. Definition
將使用者輸入轉成可路由、可執行、可驗證的 Task Definition；不執行主要工作。

## 2. Trigger
使用者提出新任務、修改需求、目標／完成條件不明，或既有任務邊界改變。

任務已有明確 Goal / Output / Constraint 時，不重複拆解。

## 3. Input
User Request、CURRENT 工作狀態、必要規則與已載入 Context。

## 4. Output
- Goal
- Required Output
- Constraints
- Known Facts
- Unknowns
- Verification Target
- Next Action
- Routing Conditions

## 5. Responsibility Boundary
負責「理解要做什麼」。
不負責：
- Research 的資料搜尋與比較
- Context Management 的資料載入決策
- Skill Routing 的既有 Skill 選擇
- Execution 的實際修改
- Verification / Diagnosis 的結果判定

## 6. Procedure
Request
→ Goal / Output / Constraint
→ Known / Unknown
→ Completion Condition
→ Required Capability
→ Route

若無法形成可靠 Task Definition：USER_REQUIRED / UNKNOWN，不自行補猜。

## 7. Control Plane
可讀取 Entity / State / Dependency / Authority metadata，但不修改 Skill Definition、Registry 或 Source。

## 8. Stop
Task Definition 足夠路由即停止，不繼續擴張問題範圍。
