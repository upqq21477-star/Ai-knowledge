# CURRENT Baseline v1.0

日期：2026-09-19
狀態：【CURRENT；Phase 1 Gate PASS；進入 Phase 2】
前一工程游標：`2-方案/完善/目前工程狀態快照-006.md`
定位：目前工程狀態、下一施工游標與最小恢復資訊的唯一 CURRENT Authority。

> 本文件承接快照-006 的工程游標責任。快照-006 自本文件建立後降為 HISTORICAL，不再作為目前工程入口。

## 1. 最小恢復

新 AI 只需依序讀取：

1. `README.md`
2. `2-方案/完善/CURRENT Baseline-v1.0.md`
3. `規則.md`
4. `待辦清單.md`

需要跨 AI 接手資訊時：
由 `1-系統/交接 Skill.md` 依 CURRENT／Workpool／Evidence 按需產生最小交接資訊；不再維持固定交接檔。

需要工程藍圖再讀：
`藍圖/AI單人工作室整體工程最新藍圖-v2.0.md`

## 2. CURRENT 工程位置

Phase 0：架構與入口收束【完成第一輪；持續觀察】
Phase 1：CURRENT Baseline【Gate PASS】
Phase 2：G1/G2 小批次 FIELD【持續】
Phase 3：Real Work Observation【未開始正式批次】
Phase 4：Dependency Audit【待證據】
Phase 5：Minimum Evaluation【待施工】
Phase 6：Capability Evolution【條件式】
Phase 7：Migration / Refactoring【條件式】
Phase 8：Large Mode Decision【暫緩】
Phase 9：Final Closure【未開始】

## 3. 已確認能力

- Agent as Top-Level Skill：現行運作模型。
- Task Understanding / Context / Skill Selection / Execute / Verify / Replan：固定運作鏈。
- Handoff Skill：FIELD PASS；Memoryless Homepage-only PASS。
- G1 FIELD：22 cases。
- G1-P01～P12：CLOSED / Re-test PASS。
- Problem Registry：正式使用。
- Atomic Synchronization / Completion Gate：已建立，正在用自然工作驗證 recurrence。
- 暫行品質監控：已接入「啟動監控／停止監控」；尚無完整 FIELD 成本收益證據。
- Large Mode：僅保留規格與切換條件，暫不施工。
- 四正式方案：已完成既有模擬／回歸；不建立第五方案。

## 4. CURRENT 架構語義

### 資產層

Rules
→ Knowledge / Memory
→ System
→ Plan
→ Software / Tool
→ Application

### AI 運作層

Agent
→ Task Understanding
→ Context
→ Skill Selection
→ Execute
→ Verify
→ Replan

兩者不是競爭架構：
資產層描述資料／工程資產如何組織；
運作層描述 AI 如何使用這些資產完成工作。

## 5. CURRENT 文件權威

| 文件 | 權責 |
|---|---|
| README.md | 入口導航 |
| CURRENT Baseline v1.0 | 唯一目前工程游標 |
| 規則.md | 操作規則 Authority |
| 待辦清單.md | 唯一 Workpool |
| 目前狀態.md | 高階專案／架構總覽 |
| Handoff Skill | 跨 AI 接手資訊的生成與退出規則 |
| 最新藍圖 v2.0 | 施工順序與決策框架 |
| Problem Registry | 問題生命週期 |
| 檔案索引.md | 近期變更檢索驗證 |
| 舊快照／舊交接／舊方案 | Historical Evidence |

不得由其他文件另行宣告新的工程 CURRENT。

## 6. Phase 1 任務

### A. 已完成

- 確認目前架構兩維語義。
- 建立本 CURRENT Baseline。
- 建立唯一待辦 Workpool。
- 將快照-006降為歷史候選。
- 固定 Handoff / Problem / Blueprint 的角色邊界。

### B. Gate 結果

- README / 規則 / CURRENT / Handoff Skill：已同步。
- Authority Matrix：已切換至 CURRENT Baseline v1.0。
- Memoryless Takeover Test：PASS（只提供 README → CURRENT → 規則 → Workpool，可恢復目前工程、禁止事項與下一游標）。
- CURRENT / Historical 掃描：PASS；搜尋仍可找到歷史文件，但其角色已明確標示為 Historical，不得覆蓋 CURRENT。
- Dependency Map v0：已建立；未知依賴維持 UNKNOWN，不猜測。
- Phase 1 Gate：PASS。

### C. 下一階段

Phase 2：G1/G2 小批次 Natural FIELD。

## 7. Dependency Map v0

目前只記錄已確認的直接依賴，不猜測未知關係。

| Current Asset | 主要依賴／關聯 | 狀態 |
|---|---|---|
| Agent Skill | Task / Context / Skill Routing / Execute / Verify | 已確認 |
| Handoff Skill | CURRENT / Handoff Package / Agent | 已確認 |
| Problem Registry | FIELD / Verification / Fix / Re-test | 已確認 |
| Skill Classification | Skill / Routing / Failure Evidence | 已確認 |
| Research Skill | Research / Evidence / External comparison | 已確認 |
| Knowledge Management | Knowledge / Context / Evidence | 已確認 |
| Execution Skill | Skill selection / Execution / Verification | 已確認 |
| Evolution Management | Change Signal / Evaluation / Migration | 已確認 |
| Distillation Skill | Dependency / overlap / restructuring | 已確認 |
| 四正式方案 | 已完成方案層責任整合 | 已確認 |
| Large Mode | Skill scale / Routing / Dependency | 條件式；未啟動 |

未知依賴：
【UNKNOWN；不得猜測】

## 8. Current Problem State

G1-P01～P12 均 CLOSED。

共同結構模式：
`Atomic Synchronization / Completion Gate`

目前不是重新設計，而是觀察後續自然工作是否再次發生。

若 recurrence：
→ 進入 Failure Pattern / Evaluation。

Phase 2 Natural FIELD 已再次發現同步失配：G1-F19 / G1-P09、G1-F20 / G1-P10、G1-F21 / G1-P11、G1-F22 / G1-P12；目前仍屬同一 Atomic Synchronization / Completion Gate 模式，不建立新 Skill。

若不再 recurrence：
→ 保持現規則。

## 9. 下一施工游標

**目前唯一下一步：Phase 2 G1/G2 小批次 Natural FIELD；Runtime Closure Natural E2E 為其中的觀察主線。**

目前 Natural FIELD 累計：G1=22 cases；P01～P12 全部 CLOSED / Re-test PASS。

Phase 1 Gate 已通過：
CURRENT 引用同步
→ Handoff 同步
→ Authority Matrix 更新
→ Memoryless Takeover Test PASS
→ CURRENT / Historical 掃描 PASS
→ Gate PASS

下一步：
G1/G2 Natural FIELD
→ Runtime Closure Natural E2E Observation
→ Real Work Observation
→ Dependency Audit。

## 系統分層搬遷施工支線

目前施工支線：既有 System 文件責任分層與實體路徑整理。

已完成：
- 00～05 邏輯分層入口建立。
- 04-Evidence 第一批低風險實體搬遷。
- 05-Research 第一階段 10 份外部比對材料搬遷。
- Research / System 機制邊界確認。
- 搬遷風險與批次紀錄同步更新。

目前：
- Research 第一階段搬遷完成。
- 完整引用／Authority 回歸仍待施工。
- 01-Skill / 03-Spec 核心 Runtime 文件尚未實體搬遷。

下一游標：
Research 回歸 → 功能工作包依賴盤點 → Control Plane A/B/C package-level 回歸 → 下一工作包搬遷。

原則：
「邊搬、邊記錄、邊驗證」；不得全部搬完後才補工程紀錄。

## Runtime Closure 狀態

已建立《1-系統/03-Spec/Agent Runtime Closure 最小契約.md》與 12/12 Simulation Acceptance。

狀態：契約 PASS；Simulation PASS；Natural FIELD PENDING。

自然工作觀察項：Trigger / Route / Invocation / Context / Execution / Verification / Failure Recovery / Receipt / Stop Reason / Multi-Skill。

不得因自然觀察前的規格或 Simulation 結果宣告 Runtime Reliability PASS。

## 10. 禁止

- 不把快照-006當 CURRENT。
- 不建立第二 CURRENT。
- 不建立第二 Workpool。
- 不猜 UNKNOWN dependency。
- 不因本次 Baseline 建立而刪除歷史文件。
- 不把 Simulation 當 FIELD。
- 不提前施工 Large Mode。
- 不因單次問題新增 Skill。

## AI Control Plane 建置狀態

2026-09-19 已建立 Control Plane 核心規格與 Registry / Query 文件，並接入 Agent、Context、Evidence、Evolution、Problem、Handoff、Monitoring、README。

狀態：正式接入現有核心 Skill；自然工作 Evidence 持續累積。

Control Plane 不取代 CURRENT Authority；所有衍生 Registry / Index / Graph / Cache 均須可由 Source 重建。

Skill Control Plane：正式接入現有核心 Skill；A/B/C 工作包施工階段已結束。自然工作 Evidence 持續累積，不另設人工測試門檻。
