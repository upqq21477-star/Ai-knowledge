# 交接 Skill（Handoff Skill） v1.2

版本：v1.2
日期：2026-09-19
狀態：【FIELD 驗收 PASS；Control Plane 接入；正式 Definition】

## 1. Definition
將目前工作狀態壓縮成下一個無既有對話記憶的 AI 可以恢復與繼續工作的最小充分 Handoff Package。

## 2. Trigger
- Context 即將重置。
- 更換 AI / Model。
- 工作跨對話延續。
- 使用者要求交接。
- 任務形成可暫停施工的穩定節點。
- 長 Context 已不足以可靠繼續。

## 3. Input
Repository 入口、CURRENT Baseline / State、施工總控、Problem Registry、相關 Skill / System、FIELD / Real Work Evidence、未完成工作與施工游標。

## 4. Output
Purpose
CURRENT State
Completed
Incomplete
Closed Problems
OPEN / DEFER / ACCEPTED RISK
Current Cursor
Next Action
Required Reading
Prohibitions
Unknown
Verification / Recovery Conditions

## 5. Procedure
CURRENT Inventory
→ Current / Historical / Deferred / Unknown
→ Problem State
→ Freeze Cursor
→ Build Handoff
→ Minimize Context
→ Memoryless Recovery Check
→ HANDOFF-READY / STALE

交接只驗證恢復資訊是否足夠，不重新執行整個工作。

## 6. Boundary
Context：決定接手時需要載入哪些 Context。
Handoff：把工作狀態轉成恢復包。
Agent：拿到恢復包後重新分流。
Handoff 不取代 Task Understanding。

## 7. Lifecycle
HANDOFF-DRAFT：整理中。
HANDOFF-READY：可交接但尚未完成恢復驗證。
HANDOFF-VALIDATED：恢復條件已確認。
HANDOFF-STALE：Repository 狀態變更後未同步。

## 8. Control Plane
按需查詢 CURRENT、Authority、State、Relevant Entity、Evidence、Recovery Data。
不要求完整 Registry；Source 文件仍為權威。

## 9. Stop
交接包足以恢復 → HANDOFF-READY。
若狀態已變更 → HANDOFF-STALE。
缺必要資訊 → UNKNOWN / 回到 Context 或 Knowledge。

## 10. Boundary Rule
Memoryless 驗收 PASS 不代表所有後續任務 PASS；它只證明交接包具備恢復所需資訊。
