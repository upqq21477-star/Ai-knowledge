# AI Control Plane

版本：v1.0
日期：2026-09-19
狀態：正式建立

## 目的
統一管理 AI 工作室中「平常不必載入、但不能遺失、需要追蹤時必須可查」的後台資料。

核心原則：
- Source of Truth 優先於 Registry。
- Registry 優先於 Cache / Graph。
- 所有衍生資料可重建。
- Context 按需載入，不全庫預載。
- AI 可觀察、分析、提出方案；高風險修改仍經 USER CONFIRM。
- 不另建常駐 Server、Graph DB、Vector DB。

## 管理範圍
Entity、State、Dependency、Impact、Change、Evidence、Provenance、Authority、Lifecycle、Capability、Runtime Trace、Drift、Reconciliation、Snapshot、Recovery。

## 架構
Source of Truth
→ Registry
→ Query
→ 最小 Context
→ AI 分析
→ Proposal
→ USER CONFIRM
→ Change
→ Verification
→ Evidence / Registry 更新

## Source of Truth
最高權威依序由當前正式文件、FIELD Evidence、Problem Registry、Git History 等提供。
Registry 不取代原始文件。

## Registry
- Entity：資產身份與基本 metadata。
- State：目前狀態。
- Dependency：明確關係。
- Impact：變更可能影響的範圍。
- Change：跨文件變更集合。
- Evidence：驗證與事件證據索引。
- Provenance：資料來源與形成鏈。
- Authority：文件權威層級。
- Lifecycle：建立、驗證、使用、替代、歷史。
- Capability：能力來源與可用功能。
- Trace：實際工作執行摘要。

## Observer
Observer 只負責：
Observe → Detect → Compare → Diagnose → Propose。
不得繞過 USER CONFIRM 直接執行高風險 Repository 修改。

## Reconciliation
Desired State
→ Observed State
→ Diff
→ Impact
→ Proposal
→ Approval
→ Change
→ Verification
→ Close。

## Retrieval
Level 0：目前 Context。
Level 1：Entity metadata。
Level 2：直接 Dependency / Impact。
Level 3：Evidence / Provenance。
Level 4：原始文件。
Level 5：History。

前一層足夠即停止。

## 資料遺失防護
Graph、Index、Cache 遺失時，可由 Registry / Source 重建。
Registry 遺失時，可由 Source 重建。
不得讓衍生圖成為唯一真相。

## 與既有系統關係
Agent：使用 Control Plane。
Task Understanding：決定需要查什麼。
Context：接收 Query 結果。
Problem：觸發 Impact Query。
Evidence：提供驗證依據。
Evolution：使用 Change / Impact / Dependency。
Handoff：使用 State / Authority / Recovery。
Monitoring：提供事件與 Drift 訊號。

## 禁止
- 不建立第二個 CURRENT。
- 不建立第二個 Workpool。
- 不把全部 Chat 歷史寫入 Registry。
- 不把所有資料建立 Dependency。
- 不把 AI 推測直接視為真值。
- 不因 Control Plane 建立而重新引入已暫緩的複雜 State。
- 不建立獨立 Graph Database 作為必要基礎設施。

## 完成判定
能查目前狀態、關係、影響、來源、變更、證據；能在不載入全庫的情況下支援工作；衍生資料遺失可重建；高風險修改有 USER CONFIRM；無記憶 AI 可依 Repository 恢復運作。
