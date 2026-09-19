# Skill Control Plane｜交接 B：Skill Registry / Control Plane Query

狀態：【TEMP HANDOFF｜完成後刪除】
日期：2026-09-19
工作包：B — Registry View / Query
上游：A Skill Architecture
下游：C Semantic Router / Runtime

## 1. 工作目的

建立 Skill 在 Control Plane 中的專用 Registry View 與 Query 層。

核心問題：

「Skill 已被定義後，Control Plane 如何以最少 Context 找到正確、有效、可用的候選 Skill？」

Registry 不是 Source of Truth，不建立第二套 Skill 資料庫。

## 2. 啟動前強制流程

第一次讀到本文件，不得直接施工。

必須：

1. 讀取 README.md。
2. 讀取 CURRENT Baseline。
3. 讀取目前施工交接包。
4. 讀取 A 的最新成果並確認 A 是否完成。
5. 檢查既有 Control Plane Registry / Query / Semantic Router 實際狀態。
6. 做整體資料流與 Authority 分析。
7. 深度研究 Registry、Skill discovery、progressive disclosure、version/lifecycle、rebuildable index 等外部實踐。
8. 找漏洞、重複 Registry、Authority 衝突、Query 過載與 Context 浪費。
9. 依影響與嚴重程度排序。
10. 確認施工方案與完成終點。
11. 才開始修改。

## 3. 正式資料流

Skill Definition
→ Control Plane Entity / Relation
→ Skill Registry View
→ Control Plane Query
→ Candidate Skill

Registry 必須可由 Source 重建。

Registry 損壞 ≠ Skill 遺失。

## 4. Registry View 第一版

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

## 5. Query Contract

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

## 6. Candidate Filtering

正常 Runtime Query 預設排除：
- Disabled
- Retired / Decommissioned
- Invalid Definition
- Invalid Dependency
- 明確驗證失效者

Deprecated 是否可作候選必須有正式規則，不由 Router 臨時決定。

Multiple Candidate 不由 Registry 自己宣判最佳者。
Registry 提供候選與必要 metadata。

## 7. Query Stop

基本原則：

Metadata Query
→ Candidate
→ 必要時擴展
→ Definition
→ 停止

不得每次把完整 Skill 庫載入 Context。

## 8. Rebuild

必須驗證：

Definition
→ derive
→ Registry View

並測試：
Registry 遺失
→ Source
→ Rebuild
→ 功能恢復

## 9. Change / Impact

Skill Definition 修改：

Definition
→ Change
→ Affected Relations
→ Registry Invalidate / Rebuild
→ Verification

B 負責 View / Query，不負責修改 Skill Definition 本身。

## 10. 不得越權

不得在本工作自行：
- 重新定義 Skill Contract
- 決定 Skill / Agent / Workflow 邊界
- 建立大型 Ranking
- 建立 Embedding / Vector Search
- 建立 Graph DB
- 建立大型 Capability Registry
- 實作 Skill Runtime

需要修改 A 的規則時，記錄為上游 Change Request。

## 11. 完成驗收

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

## 12. 明確完成終點

B 結束的必要條件：

「給定查詢條件，可以從 Registry 找到正確、有效、可用的候選 Skill；查詢深度與 Context 有明確停止規則；Registry 可以由 Source 重建；Definition 變更可以正確反映。」

達成後立即停止 Registry 擴張。

Embedding、Graph、Large Ranking、Autonomous Discovery 等全部進 Future Work，不得偷偷加入本階段。

## 13. 給 C 的輸出

完成後交付：
- Registry View Contract
- Query Contract
- Filtering Rules
- Query Stop Rules
- Fallback Rules
- Rebuild Rules
- Change / Impact Interface

## 14. 清理規則

本文件是一次性施工交接，不是永久架構文件。

B 完成並被整合測試吸收後，刪除此檔。

不要把本文件升格為 CURRENT、Registry Source of Truth 或永久藍圖。
