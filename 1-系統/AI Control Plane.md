# AI Control Plane

版本：v1.1
日期：2026-09-19
狀態：【設計規劃完成；FIELD 驗證待進行】

## 定位
AI Control Plane 是後台管理／控制層。
它不取代資產層、Agent、CURRENT Authority 或 Problem Registry。

核心目的：
「讓 AI 在不載入全庫的情況下，知道目前需要查什麼、去哪裡查、查到何種深度即可停止，以及修改後如何驗證與恢復。」

## 核心閉環
Task
→ Task Understanding
→ Control Plane Query
→ 最小 Context
→ Skill Selection
→ Execute
→ Trace
→ Verify
→ Evidence
→ Impact / Problem（需要時）
→ Change Set（需要時）
→ Verification
→ Reconcile
→ Close

## 三個核心能力
1. Observe：觀察目前任務、變更、Verification、Problem、Drift。
2. Query：按需取得最小必要後台資訊。
3. Reconcile：把 Desired / Observed 差異轉成可驗證的變更閉環。

## 管理 Entity
Entity、State、Dependency、Impact、Change、Evidence、Provenance、Authority、Lifecycle、Capability、Trace、Drift、Recovery。

Registry 只保存 metadata / relationship / evidence pointer，不複製原始文件全文。

## Retrieval
L0：現有 Context
L1：Entity metadata / State / Authority
L2：直接 Dependency / Impact
L3：Evidence / Provenance / Problem
L4：原始文件
L5：History

停止規則：
目前層已足夠 → 停止。
不得為完整性而預載後續層。

## Routing 與 Context 邊界
Routing：
Task → Capability / Skill

Control Plane：
Task / Capability → 必要 Context Query

因此上層不負責決定載入整庫資料，只需識別任務與能力需求；後台查詢再按需分發。

## Observer
Observe → Detect → Compare → Diagnose → Propose

Observer 不等於常駐全庫掃描器。
自然工作、Change、Failure、Problem、Drift 才是主要觸發來源。

## Change / Reconciliation
Desired State
→ Observed State
→ Diff
→ Impact
→ Proposal
→ USER CONFIRM（高風險）
→ Change
→ Verification
→ Close

跨文件修改一律以 Change Set 為完成單位。

## Source / Authority
Source of Truth 高於 Registry。
Registry 高於 Cache / Graph。
Derived data 必須可由 Source 重建。

CURRENT Baseline 仍是唯一目前工程狀態 Authority。

## 與既有系統
Agent：執行與協調。
Skill：能力。
System：可重複工作方法。
Problem Registry：問題生命週期。
Evidence：驗證依據。
Handoff：跨 AI 最小恢復。
Monitoring：低成本觀察訊號。
Evolution：依 Evidence 決定結構演化。
Control Plane：後台狀態、查詢、關係、影響、變更與恢復。

## 不做
- 不建立第二 CURRENT。
- 不建立第二 Workpool。
- 不全庫預載。
- 不把全部 Chat 歷史寫入 Registry。
- 不把 AI 推測當真值。
- 不因 Control Plane 新增大量 State。
- 不提前建立 Graph DB / Vector DB / 常駐 Server。
- 不把 Registry 當 Source of Truth。

## 設計完成 Gate
已完成：
- Entity / State / Dependency / Impact / Change / Evidence / Authority / Trace 邊界。
- Query 深度與停止規則。
- Observer / Trigger 邊界。
- Change Set / Reconciliation。
- Context 最小化。
- Source 可重建原則。
- 與 Agent / Skill / Problem / Handoff / Monitoring / Evolution 邊界。

尚待：
- Natural FIELD 驗證 Context 成本。
- Natural FIELD 驗證 Query 是否可停止於最低必要深度。
- Natural FIELD 驗證 Registry / Derived data 重建。
- Natural FIELD 驗證 Drift / Impact / Change Set。
- 手機 + ChatGPT + GitHub 實際工作成本驗證。

因此目前狀態是「設計規劃完成」，不是「實戰驗收完成」。
