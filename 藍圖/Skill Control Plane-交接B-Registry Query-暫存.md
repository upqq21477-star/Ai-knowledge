# Skill Control Plane｜交接 B：Skill Registry / Control Plane Query

狀態：【TEMP HANDOFF｜完成後刪除】
日期：2026-09-19
工作包：B — Registry View / Query
工作方式：與 A、C **並行施工**；不得把 A/C 完成作為 B 的開工前置條件。
接口依賴：A 提供 Skill Definition Contract；若尚未完成，先以目前 Authority / UNKNOWN 建立暫時接口假設，並在整合階段驗證。
下游：C Registry / Query Consumer

## 1. 工作目的

建立 Skill 在 Control Plane 中的專用 Registry View 與 Query 層。

核心問題：

「Skill 已被定義後，Control Plane 如何以最少 Context 找到正確、有效、可用的候選 Skill？」

Registry 不是 Source of Truth，不建立第二套 Skill 資料庫。

## 2. 並行施工規則

A / B / C 是三個**可同時開始的獨立工作包**，不是流水線。

B 不得因 A 尚未完成而停止。

若 A 的正式 Definition Contract 尚未存在：
- 使用目前已確立的 Skill 基線建立最小接口假設。
- 將差異記為 Interface Dependency / UNKNOWN。
- 先完成 Registry / Query 可獨立完成的設計與研究。
- A 完成後進行 Contract 對齊與整合驗證。

若 C 尚未完成：
- 不等待 C。
- 只需明確交付 Query Interface 給 C。

若發現跨包衝突：
- 不猜測。
- 記錄 Conflict / Change Request。
- 不擅自重寫 A/C 的核心責任。

## 3. 啟動前強制流程

第一次讀到本文件，不得直接施工。

必須：
1. 讀取 README.md。
2. 讀取 CURRENT Baseline。
3. 讀取目前施工交接包。
4. 檢查現有 Control Plane Registry / Query / Semantic Router 實際狀態。
5. 讀取 A 的**目前可用成果（若已存在）**，但不得把 A 完成視為 B 的開工條件。
6. 做整體資料流與 Authority 分析。
7. 深度研究 Registry、Skill discovery、progressive disclosure、version/lifecycle、rebuildable index 等外部實踐。
8. 找漏洞、重複 Registry、Authority 衝突、Query 過載與 Context 浪費。
9. 依影響與嚴重程度排序。
10. 確認施工方案與完成終點。
11. 才開始修改。

## 4. 正式資料流

Skill Definition
→ Control Plane Entity / Relation
→ Skill Registry View
→ Control Plane Query
→ Candidate Skill

Registry 必須可由 Source 重建。
Registry 損壞 ≠ Skill 遺失。

## 5. Registry View 第一版

至少支援：
- ID
- Name
- Family
- Capability
- Trigger Summary
- Input Summary
- Output Summary
- State
- Version
- Lifecycle
- Dependency Summary
- Verification Summary
- Path
- Updated

一般 Router View 不預載：
- 完整 Execution
- 完整 Failure
- 完整 Verification Procedure
- Evidence
- Trace
- Change History

需要時再 Query。

## 6. Query Contract

至少處理：
Q0 Identity
Q1 Capability
Q2 Trigger
Q3 I/O
Q4 Constraint
Q5 Dependency
Q6 Verification
Q7 History
Q8 Impact

每一種 Query 必須明確：
- Input
- Output
- Scope
- Authority
- Stop Condition
- Filtering
- UNKNOWN 行為
- Fallback

## 7. Candidate Filtering

正常 Runtime Query 預設排除：
- Disabled
- Retired / Decommissioned
- Invalid Definition
- Invalid Dependency
- 明確驗證失效者

Deprecated 是否可作候選必須有正式規則，不由 Router 臨時決定。

Multiple Candidate 不由 Registry 自己宣判最佳者。
Registry 提供候選與必要 metadata。

## 8. Query Stop

基本原則：

Metadata Query
→ Candidate
→ 必要時擴展
→ Definition
→ 停止

不得每次把完整 Skill 庫載入 Context。

## 9. Rebuild

必須驗證：

Definition
→ derive
→ Registry View

並測試：
Registry 遺失
→ Source
→ Rebuild
→ 功能恢復

## 10. Change / Impact

Skill Definition 修改：

Definition
→ Change
→ Affected Relations
→ Registry Invalidate / Rebuild
→ Verification

B 負責 View / Query，不負責修改 Skill Definition 本身。

## 11. 不得越權

不得在本工作自行：
- 重新定義 Skill Contract
- 決定 Skill / Agent / Workflow 邊界
- 建立大型 Ranking
- 建立 Embedding / Vector Search
- 建立 Graph DB
- 建立大型 Capability Registry
- 實作 Skill Runtime

需要修改 A 的規則時，記錄為上游 Change Request；不得阻塞 B 的獨立工作。

## 12. 完成驗收

以下全部 PASS：
- Registry View Contract
- Query Contract
- Candidate Filtering
- Query Stop
- No Candidate Fallback
- Multiple Candidate Handling
- Invalid Skill Handling
- Dependency Query
- Registry Rebuild
- Definition Change → Registry Update
- Impact Query

至少 10 個 Query / Registry 案例。

## 13. 明確完成終點

B 結束的必要條件：

「給定查詢條件，可以從 Registry 找到正確、有效、可用的候選 Skill；查詢深度與 Context 有明確停止規則；Registry 可以由 Source 重建；Definition 變更可以正確反映。」

達成後立即停止 Registry 擴張。
Embedding、Graph、Large Ranking、Autonomous Discovery 等全部進 Future Work，不得偷偷加入本階段。

## 14. 給 C 的輸出

完成後交付：
- Registry View Contract
- Query Contract
- Filtering Rules
- Query Stop Rules
- Fallback Rules
- Rebuild Rules
- Change / Impact Interface

C 可在 B 未完成時先以 Interface Contract / UNKNOWN 建立 Router 工作；整合階段再驗證實際接口。

## 15. 清理規則

本文件是一次性施工交接，不是永久架構文件。

B 完成、成果被正式系統吸收，且 Phase 1 最終整合驗收完成後，與 A/C 暫存交接檔**一次性統一刪除**。

不要把本文件升格為 CURRENT、Registry Source of Truth 或永久藍圖。
