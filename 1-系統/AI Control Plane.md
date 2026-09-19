# AI Control Plane

版本：v1.3
日期：2026-09-19
狀態：【正式架構規格；Control Plane 已接入現有 Skill；FIELD 持續累積】

## 定位
AI Control Plane 是後台管理／控制層。
它不取代資產層、Agent、CURRENT Authority 或 Problem Registry。

核心目的：
「讓 AI 在不載入全庫的情況下，知道目前需要查什麼、去哪裡查、查到何種深度即可停止，以及修改後如何驗證與恢復。」

## 核心閉環
Task
→ Task Understanding
→ Semantic Router（條件式）
→ Control Plane Registry / Query
→ 最小 Context
→ Skill Execute
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

## Semantic Router 與 Control Plane 邊界

Agent Skill Semantic Router 是獨立的輕量分流系統。

Router：
Task → Observation / Task Features → Capability / Skill

Control Plane：
Capability / Skill → 必要 Context Query

因此正式邊界為：

「Router 決定誰來做；Control Plane 決定做它需要知道什麼。」

Router 不得為了分流而載入完整 Skill / System / Knowledge。
Router 只使用最小 Skill Metadata。
無匹配或不明確時回退 Agent，不強行推測。

詳細規格：
1-系統/Agent Skill語意路由系統.md

## Routing 與 Context 邊界

Routing：
Task → Capability / Skill

Control Plane：
Task / Capability → 必要 Context Query

因此上層先分流，後台再按需分發必要查詢。
目的不是增加一層完整推理，而是避免為了選 Skill 提前載入大量 Context。

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
Agent Skill Semantic Router：低成本能力分流。
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
- 不讓 Semantic Router 變成第二個 Agent。
- 不為 Router 預載完整 Skill / System / Knowledge。

## 設計完成 Gate
已完成：
- Entity / State / Dependency / Impact / Change / Evidence / Authority / Trace 邊界。
- Query 深度與停止規則。
- Observer / Trigger 邊界。
- Change Set / Reconciliation。
- Context 最小化。
- Source 可重建原則。
- 與 Agent / Skill / Problem / Handoff / Monitoring / Evolution 邊界。
- Semantic Router 與 Control Plane 的責任邊界。

後續自然運作觀察：
- Context 成本。
- Query Stop 深度。
- Registry / Derived data 重建。
- Drift / Impact / Change Set。
- Semantic Router 路由結果與額外成本。
- 實際工作成本與恢復效果。

因此目前架構已正式接入既有 Skill；實際成本與效果由後續自然運作 Evidence 持續更新，不以額外測試阻塞架構使用。
