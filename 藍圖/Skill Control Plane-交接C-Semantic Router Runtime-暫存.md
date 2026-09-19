# Skill Control Plane｜交接 C：Semantic Router / Skill Runtime

狀態：【TEMP HANDOFF｜完成後刪除】
日期：2026-09-19
工作包：C — Router / Runtime
工作方式：與 A、B **並行施工**；不得把 A/B 完成作為 C 的開工前置條件。
最終整合：A + B + C End-to-End

## 1. 工作目的

把以下資料流真正接成可驗證的運作鏈：

Task
→ Agent
→ Semantic Router
→ Control Plane Query
→ Skill Registry
→ Candidate
→ Skill Definition
→ Runtime
→ Verification
→ Evidence / Trace

核心問題：

「找到 Skill 後，如何正確選擇、載入、執行、驗證，並在失敗時停止或重新路由？」

## 2. 並行施工規則

A / B / C 是三個**可同時開始的獨立工作包**，不是 A→B→C 流水線。

C 不得因 A/B 尚未完成而停止。

若 A 的 Definition Contract 尚未完成：
- 依目前 Authority 建立最小 Skill Interface 假設。
- 將未確定部分記為 UNKNOWN / Interface Dependency。
- 先完成 Router / Runtime 可獨立完成的研究、邊界與設計。
- A 完成後再做 Definition 對齊。

若 B 的 Query / Registry 尚未完成：
- 依已知 Query Interface 建立 Router 邊界。
- 將實際接口差異記為 Interface Dependency。
- 不自行重建 Registry。
- B 完成後進行整合驗證。

若發現 A/B 與 C 衝突：
- 不猜測。
- 記錄 Conflict / Change Request。
- 不擅自改寫 A/B 核心規格。
- 繼續完成 C 可獨立完成的部分。

## 3. 啟動前強制流程

第一次讀到本文件，不得直接施工。

必須：
1. 讀取 README.md。
2. 讀取 CURRENT Baseline。
3. 讀取目前施工交接包。
4. 檢查現有 Agent / Semantic Router / Skill Routing / Runtime 實際狀態。
5. 讀取 A/B 的**目前可用成果（若已存在）**，但不得把 A/B 完成視為 C 的開工條件。
6. 做完整資料流與責任邊界分析。
7. 深度研究 Semantic Routing、Skill discovery、agent-tool routing、failure recovery、verification 等外部實踐。
8. 找漏洞、權責重疊、錯誤路由、無 Skill、候選衝突、Failure Loop。
9. 依影響與嚴重程度排序。
10. 確認施工方案與完成終點。
11. 才開始修改。

## 4. Router 職責

Semantic Router = 「誰應該做？」

可以分析：
- Intent
- Task Type
- Required Capability
- Input / Output Requirements
- Constraints
- Context

不得：
- 執行 Skill
- 保存 Skill Definition
- 建立 Registry
- 修改 Skill Definition
- 取代 Workflow / Agent Orchestration

## 5. Control Plane 職責

Router 向 Control Plane Query：

「找符合條件、目前可用的 Skill。」

Control Plane 回傳候選與最小必要 metadata。

Router 不直接掃描完整 Skill Definition。

## 6. Candidate Handling

必須處理：
0 Candidate
1 Candidate
Multiple Candidates
Invalid Candidate
Conflicting Candidates

不能只測理想的「找到一個」。

Multiple Candidate：
Router / Agent 依任務條件決定，不由 Registry 偽裝成唯一真相。

## 7. Runtime

Skill 確定後：

Load Definition
→ Validate Input
→ Check Dependency
→ Execute
→ Stop Condition
→ Output

Runtime 不得直接修改 Skill Definition。

## 8. Verification

Output
→ Skill Verification Rule
→ Verification Result
→ Evidence
→ Trace

Verification Rule = 如何驗證。
Evidence = 本次實際證據。
Trace = 本次運作紀錄。

不得混為同一資料。

## 9. Failure / Re-route

至少處理：
- Missing Input
- Invalid Input
- Dependency Failure
- Execution Failure
- Verification Failure
- No Candidate
- Ambiguous Candidate

基本流程：

Failure
→ 判斷是否可 Re-route
→ 可：重新 Query / Router
→ 不可：明確停止並記錄原因

禁止因 Skill 失敗而讓 Agent 任意發明新 Skill。

## 10. Workflow Boundary

多 Skill：

Skill A
→ Skill B
→ Skill C

屬 Workflow / Agent Coordination。

C 必須驗證單 Skill、多 Skill、Workflow、Re-route，但不得把 Workflow 邏輯偷偷塞入單一 Skill。

## 11. 不得越權

不得自行：
- 重新定義 Skill Contract
- 重新定義 Registry Schema
- 重新定義 Query Contract
- 建立大型 Ranking
- 建立 Embedding
- 建立 Graph DB
- 自動修改 Skill Definition

發現 A/B 缺口時，記錄 Interface Change，不直接另立規格。

## 12. 完成驗收

以下全部 PASS：
- Router Input
- Intent Extraction
- Control Plane Query
- Candidate Selection
- No Candidate
- Multiple Candidate
- Invalid Candidate
- Skill Loading
- Input Validation
- Dependency Check
- Execution
- Verification
- Evidence
- Trace
- Failure Handling
- Re-route
- Workflow Handling

至少 10 個 End-to-End 案例。

## 13. 最終整合驗收

A + B + C 必須共同通過：

Task
→ Agent
→ Semantic Router
→ Control Plane Query
→ Skill Registry
→ Candidate
→ Skill Definition
→ Runtime
→ Verification
→ Evidence / Trace

並另外測：
1. Skill Update → Registry Update → Router 可取得正確版本
2. Skill Disable → 正常 Query 不再選出
3. Registry Rebuild → Source 可恢復 Query
4. Dependency Failure → 不產生錯誤成功結果
5. Verification Failure → 正確停止或 Re-route

## 14. 第一階段總完成終點

只有以下全部 PASS 才宣布：

SKILL CONTROL PLANE PHASE 1 = DONE

條件：

A PASS
+ B PASS
+ C PASS
+ End-to-End PASS
+ Change PASS
+ Disable PASS
+ Rebuild PASS

三個工作包在施工期間可以並行；「A/B/C PASS」指各自完成驗收，不代表施工順序。

達成後停止第一階段擴張。
Ranking / Embedding / Graph / Autonomous Evolution 等不得因「未來可能需要」加入本階段。

## 15. 清理規則

本文件是一次性施工交接，不是永久架構文件。

Phase 1 最終整合驗收完成後，才執行一次性清理：

1. 確認 A PASS。
2. 確認 B PASS。
3. 確認 C PASS。
4. 確認 End-to-End / Change / Disable / Rebuild PASS。
5. 確認正式成果已寫入正式 System / Registry / Query / Evidence / Change / CURRENT 文件。
6. 刪除 A、B、C 三個 TEMP HANDOFF。
7. 從檔案索引移除三個 TEMP 項目。
8. 重新讀取 Repository，確認三個檔案與索引引用均已消失。
9. 確認 Repository 只留下正式成果。

在上述清理驗證完成前，不得宣稱 Phase 1 已完成。

最終目標：

「交接檔完成使命後消失，正式系統留下成果，Repository 保持乾淨。」
