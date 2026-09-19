# 執行 Skill（Execution Skill） v1.2

版本：v1.3
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition；自然運作 Evidence 持續累積】

## 1. Definition
執行已確認的 Action，並產生可追溯的 Operation Evidence；不負責決定是否應修改架構。

## 2. Trigger
存在 Confirmed Action，且必要 Input、Dependency、Permission 均具備。

未確認 Action、目標不明或依賴未滿足 → Stop / User Required / Diagnosis，不執行猜測動作。

## 3. Input
Confirmed Action、Target、Required Context、Provider / Tool、Constraints。

## 4. Output
Execution Result
Changed Files
Errors
Operation Evidence
Change Set
Execution Cost（L / M / H）

## 5. Responsibility Boundary
Execution：
「已決定要做什麼 → 實際做」。

Evolution：
「是否需要結構改變、改什麼」。

Verification：
「做完是否正確」。

Provider / Tool：
「實際提供外部能力」。

## 6. Procedure
Validate Input
→ Check Dependency / Permission
→ Execute
→ Record Changed Scope
→ Return Evidence
→ Verification

Execution Failure 不直接重試；交由 Diagnosis 判斷。

## 7. Repository Change
涉及文件／Skill 修改時：
讀取現行版本 → 最小修改 → 保留有效內容 → 更新引用／索引 → 回報 Change Set。

## 8. Control Plane
可讀取 Change / Dependency / Impact / Authority metadata。
不得把 Registry 當 Source of Truth，也不得自行建立 Skill。

## 9. Stop
PASS：動作完成並交 Verification。
INSUFFICIENT：工具／權限／必要資料不足。
FAILED：執行失敗。
USER_REQUIRED：需要使用者決策。
