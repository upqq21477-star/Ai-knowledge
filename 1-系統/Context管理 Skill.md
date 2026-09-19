# Context 管理 Skill（Context Management Skill） v1.2

版本：v1.3
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition；自然運作 Evidence 持續累積】

## 1. Definition
決定本次任務需要載入哪些 Context，控制上下文邊界、來源權威與成本；不負責保存 Knowledge，也不負責一般任務路由。

## 2. Trigger
- 新任務開始。
- 任務跨文件／跨 Skill。
- 現有 Context 不足或過大。
- Context 重置。
- 來源衝突。
- 需要從 Control Plane 取得最小必要 metadata。

## 3. Input
Task Definition、CURRENT、Repository 入口、文件索引、可用 metadata、已載入 Context。

## 4. Output
Required Context
Context Boundary
Loaded Sources
Missing Context
Conflict Flags
Context Cost（L / M / H）

## 5. Procedure
L0：現有 Context
→ L1：必要 metadata
→ L2：直接關係
→ L3：Evidence / Provenance
→ L4：Canonical Source
→ L5：History

取得足以完成目前任務的資訊後立即停止，不預載整個 Repository。

## 6. Responsibility Boundary
Context：現在需要載入什麼。
Knowledge：資料如何保存與管理。
Handoff：如何把目前工作狀態交給下一個 AI。
Agent：拿到 Context 後如何分流。

## 7. Source Rule
來源衝突時優先現行入口與 Canonical Source。
無法確認 Canonical Source → UNKNOWN，不用舊文件猜測。

## 8. Control Plane
Control Plane 提供 Entity / State / Dependency / Impact / Evidence / Provenance / Authority metadata。
Context 只決定載入範圍，不複製 Registry。

## 9. Stop
Context 足以讓下一個 Skill 工作即停止。
若仍缺資料 → Research / Knowledge。
若只是 Context 過大 → 縮減，不自動重建架構。
