# AI 單人工作室整體功能藍圖 v1.0

版本：v1.0
日期：2026-09-19
狀態：【CURRENT 藍圖地圖；不取代 CURRENT Baseline】
定位：把「目前已存在的功能／Skill／控制系統」與「未來藍圖規劃」放在同一張可導航地圖上，並明確區分已建立、可運行但待自然 Evidence、已規劃未建立、未知。

## 1. 本次掃描結論

本次以 Repository 實際檔案、CURRENT Baseline、AI Control Plane / Registry / Query、現有 Skill Definition、既有 Blueprint、功能導向 Mapping 與未來藍圖規劃交叉比對。

目前正式工程主線仍為：
Phase 2 → G1/G2 小批次 Natural FIELD。

目前不是缺少一個「總控制文件」，而是需要一張把現有資產與未來能力放在同一座標系的 Blueprint。

本圖不建立第二 CURRENT、第二 Workpool、第二 Registry。

## 2. 全局結構

### A. 資產層

Rules
→ Knowledge / Memory
→ System
→ Plan
→ Software / Tool
→ Application

### B. AI 運作層

Agent
→ Task Understanding
→ Context
→ Skill Selection / Routing
→ Execute
→ Verify
→ Replan

### C. Control / Governance 橫向層

Control Plane
├─ Registry / Query
├─ State / Authority / Lifecycle
├─ Dependency / Impact / Change
├─ Evidence / Provenance / Trace
└─ Drift / Recovery

治理能力：
Problem
Evidence
Handoff
Evolution
Distillation
Blueprint Governance
Meeting Record
Monitoring

這些橫向能力不構成新的資料層。

## 3. 目前已建立的核心 Skill

| Skill | 目前位置 | 狀態 | 主要責任 |
|---|---|---|---|
| Agent Skill | 1-系統 | ACTIVE | 任務級決策、編排、重新分流 |
| 任務理解 Skill | 1-系統 | ACTIVE | Goal / Output / Constraint / Unknown / Verification Target |
| Context 管理 Skill | 1-系統 | ACTIVE | 最小充分 Context、來源與邊界 |
| Skill 分類判斷 Skill | 1-系統 | ACTIVE | KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE |
| 交接 Skill | 1-系統 | ACTIVE；FIELD PASS | 最小充分 Handoff 與 Memoryless Recovery |
| 執行 Skill | 1-系統 | ACTIVE | 執行已確認 Action 並產生 Operation Evidence |
| 研究 Skill | 1-系統 | ACTIVE | 問題拆解、研究深度、搜尋、比較、證據候選 |
| 證據／驗證／診斷 Skill | 1-系統 | ACTIVE | Evidence、Verification、Diagnosis |
| 知識管理 Skill | 1-系統 | ACTIVE | 長期可重用資料、Source、Version、Lifecycle |
| 演化管理 Skill | 1-系統 | ACTIVE | Change Set、Impact、Migration |
| 蒸餾 Skill | 1-系統 | ACTIVE | 結構性重複、壓縮、重組 |
| Blueprint Governance Skill | 1-系統 | ACTIVE；【代】 | 維護 Blueprint 位置、主要關係與一致性 |
| 會議紀錄管理 Skill | 1-系統 | ACTIVE；【代】 | 會議成果保存、轉 Planning / Handoff / Update |

註：
Skill 的【代】表示已模擬驗收 PASS、可運行，但尚缺自然工作 Evidence；不是未完成，也不是新的 State。

## 4. 已建立但不是獨立 Skill 的核心功能

以下功能已存在，但目前沒有足夠依據把它們另立為 Skill：

- Skill Routing：由 Agent / Skill Routing 規格承擔。
- Semantic Router：獨立輕量系統，條件式啟動。
- AI Control Plane：後台查詢與控制層。
- Skill Registry / Query：Derived View / Query，不是 Source of Truth。
- Problem Registry：問題生命週期。
- 更新監控與觸發管理：Event / Signal / Trigger。
- 工程狀態與驗收控制：共同 State / Acceptance 語義。
- Skill 模擬驗收與【代】運行規則。
- Skill 建立流程。
- Skill 架構擴展 / Small Mode / Large Mode 介面。

判斷依據：
現有文件已明確把 Routing、Registry、Provider、Tool、Mode、Workflow 與 Skill 分開；不能因功能存在就自動建立 Skill。

## 5. 既有功能導向 Blueprint

既有 Mapping 已確認：
- A1–A12
- B1–B16
- C1–C18
- D1–D20
- K01–K06
- S01–S10

K07–K61、S11–S37 在既有 Mapping 中仍保持未知，不能補猜。

CAP Mapping 已形成 61 個 Capability ID 的現行 Mapping 視圖，其中：
- CAP-01～CAP-12：資料身份、Metadata、Provenance、Evidence、State、Version、Relationship、Lifecycle、History、Traceability、Impact、Shared Semantics。
- CAP-13～CAP-28：Intent、Decomposition、Search、Exploration、Research、Evidence Assessment、Applicability、Context Selection / Assembly、Memory / Current State、Execution、Verification、Uncertainty、Result Persistence、Feedback、Failure Diagnosis。
- CAP-29～CAP-41：Change Signal、Confirmation、Target、Goal、Capability Inventory、Evolution Necessity、Change Proposal、Version、Compatibility、Migration、Minimal Change Execution、Validation、Adoption Gate、Distillation Handoff。
- CAP-42～CAP-54：Distillation Case、Scope、Capability Inventory、Usage / Dependency Evidence、Validation Status、Capability Semantics、Overlap、Responsibility Boundary、Relationship、Cost / Risk、Disposition、Impact、Migration、Refactoring、Baseline、History、Distillation Record。
- CAP-56～CAP-61：Catalog、Routing、Ambiguity Handling、Canonical Source Boundary、Trigger Registry、Distillation Trigger。
- CAP-55 已不再承擔兩個不同責任的 Capability ID。

這些 CAP 是「能力比較與演化的 Mapping」，不是要求每一個都建立成 Skill。

## 6. 目前 Skill 對 Blueprint 的位置

### 運作入口

Task
→ Agent / Task Understanding
→ Semantic Router（條件式）
→ Control Plane Query
→ Candidate Skill / Skill Routing
→ Context
→ Execution
→ Verification
→ Evidence / Trace

### 結構演化

Natural Work / Failure / Change Signal
→ Research
→ Skill Classification
→ Evolution
→ Execution
→ Verification
→ Evidence
→ Distillation（只有長期結構成本成立時）

### 知識與交接

Verified Information
→ Knowledge Management

Context Reset / AI Switch
→ Handoff

Meeting / Decision / Design Preservation
→ Meeting Record
→ Planning / Handoff / Existing Update

### 地圖治理

主要功能／位置／關係變化
→ Blueprint Governance
→ Blueprint Map
→ Consistency Check
→ 必要時更新地圖

## 7. 未來藍圖：尚未建立的主要工程能力

以下來自既有未來藍圖與功能導向規劃，但「規劃存在」不代表已建立。

### F1｜Trigger / Recall 工作能力

規劃：
- Trigger
- Recall
- Capability Discovery
- Candidate Capability

目前：
已有 Skill Routing、Semantic Router、Control Plane Query、更新監控與 Trigger Registry 原理，但尚未形成獨立「Capability Trigger / Recall System」作為完整未來藍圖實體。

位置：
AI 運作層 → Routing / Discovery → Control Plane Query。

判定：
【規劃中／未實體化】

注意：
目前沒有證據要求建立新的 Trigger Skill 或 Recall Skill。

### F2｜Response Contract / 工作輸出契約

規劃：
P0-14 Response Contract。

目前：
Agent / Skill 已有 Input / Output、Verification Target、Stop，但尚未確認存在獨立完整 Response Contract 系統。

位置：
AI 運作層 → Execute → Verify 之間。

判定：
【規劃中／尚未形成獨立系統】

### F3｜主系統資料基線重建的後續資料治理工作

目前 CURRENT Baseline v1.0 已建立，Phase 1 Gate PASS，因此不能把舊藍圖的「建立 CURRENT」再列成未完成。

尚未完成的是後續：
- 舊資料完整 Dependency Audit。
- 大規模歷史／現行資產處置。
- 有證據的 KEEP / MERGE / COMPRESS / ARCHIVE / DEFER。
- 命名 Rename Migration 的實際施工。

位置：
Baseline → Dependency Audit → Migration / Refactoring。

判定：
【部分完成；後續待證據】

### F4｜Minimum Evaluation

規劃：
Scenario → Execution → Evidence → Evaluation → Decision。

目前：
已有 FIELD、Problem Registry、Skill Feedback、Simulation / Verification；但完整、可重複的 Minimum Evaluation 尚未成為目前正式工程主線的完成項。

位置：
Real Work Observation → Evaluation → Evolution。

判定：
【規劃中／待施工】

### F5｜Capability Evolution 的正式評估循環

規劃：
Capability Delta
→ Overlap Analysis
→ Provider Comparison
→ Partial / Full Replacement
→ Extension / Refactor
→ Migration。

目前：
已有 Skill Classification、Evolution、Distillation，以及 CAP Mapping；但尚未用足夠 Real Work + Evaluation 證據完成完整 Capability Evolution 循環。

位置：
Evaluation → Evolution → Migration。

判定：
【部分能力已建立；完整循環待證據】

### F6｜Capability Registry / Graph / Automation / Orchestration

規劃：
- Capability Registry
- Capability Graph
- Evaluation Engine
- Automation
- Orchestration

目前：
均未因藍圖存在而提前實體化。

位置：
Large / Future Infrastructure。

判定：
【後置／條件式】

啟動依據：
必須先出現實際瓶頸，不能以藍圖完整度作為建立理由。

## 8. 「尚未建立的 Skill」判定

本次比對沒有找到一個「未來藍圖明確要求、且已證明必須獨立成為 Skill」的新增 Skill。

目前尚未實體化的多數項目是：
- Capability
- System
- Registry / Infrastructure
- Evaluation
- Migration
- Automation

而不是 Skill。

因此目前不新增：
- Trigger Skill
- Recall Skill
- Evaluation Skill
- Capability Registry Skill
- Monitoring Skill
- Problem Solving Skill

除非未來實際工作證據證明它們具有獨立 Responsibility、Trigger、Input / Output 與路由價值，並經 Skill Classification → Evolution → Verification。

## 9. 未來藍圖施工順序

CURRENT 已進入 Phase 2，因此把舊未來藍圖重新投影到目前工程：

1. Phase 2：G1/G2 Natural FIELD
2. Real Work Observation
3. Dependency Audit
4. Minimum Evaluation
5. Capability Evolution
6. Migration / Refactoring
7. Large Mode Decision
8. Final Closure

其中：
- Blueprint Governance：現在運行，負責地圖維護。
- Meeting Record：現在運行，負責討論成果保存。
- Control Plane：現在運行，持續累積自然 Evidence。
- Large Mode：保持條件式，不提前施工。

## 10. Blueprint 與 TODO 的邊界

Blueprint：
回答「整體有什麼、在哪裡、彼此怎麼連」。

TODO：
回答「下一步現在做什麼」。

CURRENT：
回答「現在正式工程狀態是什麼」。

Registry：
回答「某個 Entity / Skill 詳細資料是什麼」。

Planning / Meeting Record：
回答「尚未實作的詳細設計與討論結果」。

因此本圖不取代待辦清單，也不把未來藍圖全部轉成 TODO。

只有已確認、可施工且目前應做的項目才進 Workpool。

## 11. 本輪掃描後的 TODO 投影

### P0｜立即

- 維護本整體功能藍圖與既有 Blueprint Map 的一致性。
- 確認 Blueprint Governance / Meeting Record 的【代】狀態在自然工作中持續追蹤。
- 持續執行 CURRENT 唯一游標下的 Phase 2 Natural FIELD。

### P1｜自然工作證據

- 累積 Natural Routing / Provider / Tool / Context / Verification / Composition evidence。
- 觀察 Control Plane Query / Registry Rebuild / Drift / Impact / Change Set。
- 觀察 Blueprint / Meeting Record 是否真的被正確觸發。

### P2｜Evaluation

- 建立 Minimum Evaluation 的最小 Scenario / Corpus。
- 定義 Evaluation → Decision 的最小閉環。
- 不人工製造 FIELD。

### P3｜Dependency / Evolution

- Skill → System → Knowledge → Plan 依賴核對。
- 以 KEEP / MERGE / COMPRESS / ARCHIVE / DEFER 判斷。
- 只有有證據才進 Capability Evolution / Migration。

### P4｜條件式未來

- Capability Registry / Graph / Automation / Orchestration 保持 DEFER。
- Large Mode 保持 DEFER。

## 12. 本圖的狀態語義

沿用《工程狀態與驗收最小規則》：
- 【未】：尚未正式開始建立。
- 【驗】：建立／整合／修正中。
- 【代】：模擬 PASS、可運行、尚缺自然 Evidence。
- 有足夠 Evidence：移除【代】。
- 發現問題：回【驗】。

不新增 Blueprint 自有狀態系統。

## 13. 核心原則

> 現有 Blueprint 是地圖入口。
>
> 本文件是「整體功能總圖」，不是第二套 CURRENT。
>
> 未來藍圖是方向，不是自動 TODO。
>
> CAP 是能力比較單位，不等於 Skill。
>
> Skill 是獨立可路由工作責任，不因能力存在就自動新增。
>
> Evidence 決定是否把規劃變成正式工程資產。
>
> 不確定就 UNKNOWN，不猜。
