# Skill Control Plane｜交接 A：Skill Architecture

狀態：【A WORK PACKAGE：STATIC PASS；等待 B/C 整合與 FIELD 驗證】
日期：2026-09-19
工作包：A — Skill Architecture
工作方式：與 B、C **並行施工**；不得把 B/C 完成作為 A 的開工前置條件。
下游：B Registry / Query、C Router / Runtime

## 1. 工作目的

建立 Skill 的正式控制模型。

本工作只回答：

「什麼東西應該成為 Skill，以及 Skill 如何被定義、拆分、分層、驗證、演化？」

不負責正式 Registry Query、Semantic Router Runtime。

## 2. 並行施工規則

A / B / C 是三個**可同時開始的獨立工作包**，不是 A→B→C 流水線。

本工作可以在 B/C 尚未完成時直接開始。

若施工中發現 B/C 尚未提供的接口或成果：
- 不得因此停止 A。
- 將需求記為 Interface Requirement / UNKNOWN / Change Request。
- 先完成 A 可獨立完成的工作。
- 最終整合時再驗證跨工作包接口。

若發現 B/C 與 A 的規格衝突：
- 不自行猜測。
- 保留衝突。
- 依 CURRENT / Authority 規則判定。
- 必要時建立 Interface Change Request。
- 不擅自改寫其他工作包核心規格。

## 3. 啟動前強制流程

第一次讀到本文件，不得直接施工。

必須：
1. 讀取 README.md。
2. 讀取 CURRENT Baseline。
3. 讀取目前施工交接包。
4. 檢查現有 Skill / Agent / Routing / Control Plane 文件與實際狀態。
5. 盤點本工作已完成、未完成、衝突、UNKNOWN。
6. 做整體架構分析。
7. 深度研究 Skill definition、boundary、hierarchy、agent/workflow boundary、progressive disclosure、version/lifecycle/evolution 等外部實踐。
8. 找漏洞、反例、重複與過度工程化風險。
9. 依影響與嚴重程度排序。
10. 確認施工方案與完成終點。
11. 才開始修改。

若發現上游資料與本文件衝突，以 CURRENT / Authority 規則為準；未知不得猜測。

## 4. 已確立的架構基線

Agent = 任務級推理與協調。
Workflow = 多 Skill 的流程組合。
Skill = 可獨立呼叫、具有明確責任、I/O、可驗證的工作單位。
Mode = 同一 Skill 的不同工作方式。
Skill Family = 共同責任與管理邊界。
Skill Definition = Skill Source of Truth。
Skill Registry = Control Plane 的 Skill 專用 View / Query 層，不是第二資料庫。

Control Plane：需要什麼 Context。
Semantic Router：誰應該做。
Skill：執行。
Verification：如何判定結果。
Evidence：本次實際驗證證據。
Trace：實際運作紀錄。

## 5. 本工作範圍

### A1 Skill Definition Contract
至少處理：
Identity、Responsibility、Purpose、Boundary、Trigger、Input、Output、Capability、Mode、Dependency、Routing、Execution、Failure、Verification、Cost、Lifecycle、Version、Source。

必須區分：
- Source of Truth
- Derived Metadata
- Runtime Data
- Governance Data

### A2 Skill Boundary
建立可重複判斷：
- 獨立責任
- 獨立 Trigger
- 明確 Input / Output
- 可獨立驗證
- 可重用
- 獨立 Failure Pattern
- Context 是否下降
- Routing 是否簡化
- Dependency / Token / 管理成本是否上升

### A3 Skill 分層
預設：
Skill Family → Skill → Mode

Domain 暫作預留層；除非研究與實測證明需要，不建立獨立 Domain Registry。

### A4 邊界
正式判定：
- Skill / Agent
- Skill / Workflow
- Skill / Mode
- Skill / Family

### A5 Evolution
流程：
Evidence → Problem → Proposal → Verification → Change → New Version → Test → Activate

需定義 Split / Merge / Replace / Deprecate / Retire。

### A6 Dependency / Verification
建立最小可用規則。
Verification = 驗證方法。
Evidence = 實際驗證證據。
不得混合。

## 6. 不得越權

不得在本工作自行建立：
- Registry Query
- Semantic Router
- Runtime
- Ranking Engine
- Embedding Search
- Graph Database
- 大型 Capability Registry

若需要修改下游介面，只提出 Interface Requirement。

## 7. 完成驗收

以下全部 PASS 才算 A 完成：
- Skill Definition Contract
- Skill Boundary Test
- Skill Family 規則
- Skill / Agent Boundary
- Skill / Workflow Boundary
- Skill / Mode Boundary
- Split / Merge / Replace
- Version / Lifecycle
- Dependency 基本規則
- Verification / Evidence 邊界
- Evolution 流程

至少用 8 個邊界案例驗證。

## 8. 明確完成終點

A 結束的必要條件：

「任何新能力都可以依固定規則判斷：是否為 Skill、是否需要拆分、屬於哪個 Family、是否應 Merge / Replace / Archive / Defer，以及如何形成 Definition。」

達成後立即停止 A 的架構擴張。
新增想法只能記為 Future Work / Change，不得讓本工作無限延伸。

## 9. 給 B/C 的輸出

完成後交付：
- Skill Definition Contract
- Boundary Test
- Classification Rules
- Evolution Rules
- 已知漏洞
- 未解決 UNKNOWN
- Registry 所需欄位與 Interface Requirements
- Router / Runtime 所需 Skill Interface Requirements

B/C 不必等待 A 完成才能施工；整合階段再共同驗證接口。

## 10. 清理規則

本文件是一次性施工交接，不是永久架構文件。

A 完成、成果被正式系統吸收，且 Phase 1 最終整合驗收完成後，與 B/C 暫存交接檔**一次性統一刪除**。

不要把本文件升格為 CURRENT、System 或正式 Skill Definition。


## 本次接續狀態

A 正式成果已寫入：
- `1-系統/Skill Architecture 規格.md`
- `1-系統/Skill Control Plane A Skill Architecture 靜態驗收紀錄-v1.0.md`

A 已完成 Definition Contract、Boundary Gate、Family / Skill / Mode、Agent / Workflow 邊界、Provider / Tool 邊界、Split / Merge / Replace / Archive / Defer、Version / Lifecycle、Dependency、Verification / Evidence、Evolution，以及 B/C Interface。

8 個 Boundary Cases 已完成 STATIC PASS。

目前不得把 A 標記為最終 DONE。剩餘驗收：
1. B/C Interface Alignment。
2. Natural FIELD Boundary Evidence。
3. Context / Routing / Maintenance 實際成本 Evidence。
4. A/B/C End-to-End Final Acceptance。

後續原則：A 不再擴張 Architecture；若整合或 FIELD 發現缺口，走 Evidence → Problem → Change Request。


## 本次獨立施工進度（2026-09-19）

A 不等待 B/C 的實際驗證結果，先完成自己的 FIELD 驗證準備。

已新增：
- `1-系統/Skill Control Plane A FIELD Boundary 驗證規格-v1.0.md`

已確認：
- A Architecture Static：PASS
- A Boundary Static：PASS
- Natural FIELD Protocol：READY
- Natural FIELD Evidence：PENDING

FIELD 僅接受自然工作證據，不以 Simulation / 推演代替。

下一步仍只屬 A：不再擴張 Architecture。等待自然工作事件產生 FIELD Evidence；若發現結構性缺口，走 Evidence → Problem → Proposal → Verification → Change Request。若沒有結構性缺口，保持 v1.0。

A 不因 B/C 尚未驗證而停止，也不把其他工作包的結果提前寫成 A 的 FIELD 結論。最終跨包結果由 D 統一驗收。


## A-only 獨立一致性審計（2026-09-19）

新增：
- 1-系統/A-Skill Architecture 獨立一致性審計紀錄-v1.0.md

結果：
- 50/50 一致性案例 PASS
- 結構性規則衝突：0
- 決策死路：0
- 主要 Classification → Change → Version/Lifecycle → Verification 閉環：PASS
- B/C：未使用

本輪沒有證據支持修改 Architecture，因此保持 v1.0。

目前 A-only 可完成工作已做到：
Static → 30-case Stress → 50-case Consistency Audit → FIELD Protocol Ready → Handoff State Synchronized。

FIELD Protocol 已建立，但 Natural FIELD Evidence 尚未發生，不能自行填 PASS。
