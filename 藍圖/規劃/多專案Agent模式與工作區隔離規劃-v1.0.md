# 多專案 Agent 模式與工作區隔離規劃 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃中；先建立最小實體，後續以實際運作驗證】

## 1. 目的

建立「中央系統 + 多個獨立專案」的工作模型。

中央系統提供共用的：
- 規格
- 方法
- Skill
- Agent 運作方式
- 研究方法
- 驗證方法
- 治理與管理方法

各專案只保存自己的專案資料與專案專用能力。

核心原則：

> 共用治理方法，不共用專案資料。
> 中央系統可被專案讀取，但專案模式不得直接改寫中央系統。
> 專案可以使用中央系統的方法建立自己的 System / Skill / Research / Evidence，但成果只屬於該專案。

## 2. Agent 工作模式

### SYSTEM MODE

資料權限：
- 中央系統：R/W
- Project A：R
- Project B：R

用途：
- 修改中央規格
- 修改中央 System / Skill / Governance
- 研究中央能力
- 處理跨專案共用能力
- 管理 Framework 版本與 Migration

### PROJECT-A MODE

資料權限：
- 中央系統：R
- Project A：R/W
- 其他 Project：不載入／不可用

用途：
- 開發 Project A
- 使用中央 Skill / System / 方法
- 建立 Project A 專用 System / Skill / Research
- 保存 Project A 的 Evidence、問題、測試與決策

### PROJECT-B MODE

與 Project A 相同，但可寫入範圍只限 Project B。

## 3. Context 邊界

Mode 不只是「寫入權限」。

進入專案模式時，Context 應優先載入：
1. 中央 Framework 必要部分
2. 目前專案資料
3. 目前任務所需 Context

其他專案資料不得因方便而混入 Context。

因此：
- Project A 不應讀取 Project B 的專案內容。
- Project A 的專用 System / Skill 不應自動成為中央 System / Skill。
- 中央系統不因讀取專案資料而把專案資料自動升格為共用 Knowledge。

## 4. 中央系統與專案的互通

中央 → 專案：
- Framework
- Skill
- 規格
- 方法
- 治理
- 驗證方法
- 研究方法

專案 → 中央：
- Capability Gap
- Framework 使用 Evidence
- Failure / Problem
- 改進建議
- Migration Request
- 可被考慮提升為中央能力的候選成果

專案提出回饋不等於中央系統立即修改。

若要修改中央系統：
Project → Proposal / Evidence → SYSTEM MODE → Research / Evaluation → Change → Verification。

## 5. 專案資料最小化

專案端不重複複製中央系統的大型治理文件。

專案只保留：
- Project Manifest
- 專案內容
- 專案專用 System / Skill
- 專案測試與 Evidence
- 專案問題與決策
- 必要的參考資料
- Framework / Governance 版本基線與接口資訊

中央複雜能力維持在主系統。

## 6. 版本與更新

專案不需要因中央系統一般能力更新而複製／重建整套系統。

專案記錄所依賴的 Framework Baseline。

中央更新後：
- 相容的能力可直接由專案模式使用。
- 若接口、資料格式或契約發生破壞性變更，才進入 Migration 判定。
- Migration 必須有 Evidence，不因版本號變更而自動施工。

因此避免「每個專案各自維護一份中央系統」造成 Framework Drift。

## 7. 專案生命週期

新專案：
中央 Repository 根目錄建立最小 Project Workspace。

進入實際開發：
Project Mode + 中央 Framework。

成熟：
可移出成獨立 GitHub Repository。

移出後：
保留 Project Contract / Framework Baseline，使獨立 Repository 仍知道使用哪一套中央治理。

完成／廢棄：
依專案生命週期保存、封存或刪除，不影響中央系統。

## 8. 第一個實體：Project A

本輪先建立最小 Project A：

Project A/
├─ PROJECT.md
└─ 參考資料/
   └─ README.md

「參考資料」只作 Project A 的參考資料邊界，不等於中央 Knowledge。

後續實際開發時，再依需求建立專案專用資料夾；不預先建立大型結構。

## 9. 目前不提前建立

暫不建立：
- Project Registry
- Capability Graph
- 自動化 Orchestrator
- 大型 Project Permission System
- 複製整套中央 System 到每個 Project
- Project-specific Skill 的統一大型管理平台

理由：
目前需求可以由 Mode + Context Boundary + Project Contract + 現有 Control Plane / Runtime Closure 承擔；是否需要更大型基礎設施，交由 Natural FIELD Evidence 決定。

## 10. 驗證方向

後續以模擬驗收先驗證：

1. SYSTEM MODE 可讀寫中央系統。
2. PROJECT-A MODE 可讀中央、可寫 Project A。
3. PROJECT-A MODE 不可寫中央。
4. PROJECT-A MODE 不載入 Project B。
5. Project A 可使用中央 Research / Skill / Verification。
6. Project A 建立的新 System / Skill 預設只屬 Project A。
7. Project A 發現中央缺口時能產生 Proposal / Evidence，而不是直接修改中央。
8. Runtime Receipt 能記錄 Mode、Workspace、Context Source、Write Target。
9. 中央更新不要求每個專案複製中央資料。
10. 發生破壞性契約變更時，能進入 Migration 判定。

目前以上屬規劃與後續驗證項目；不得把 Simulation PASS 當成 Natural FIELD PASS。

## 11. 與現有架構的關係

本規劃不修改既有：

Rules → Knowledge → System → Plan → Software / Tool → Application

也不取代：

Agent → Task Understanding → Context → Skill Selection → Execute → Verify → Replan

它增加的是「專案隔離」這個正交維度：

Central Framework
→ SYSTEM MODE / PROJECT MODE
→ 各自 Workspace

因此不建立第二套資料層。

## 12. 下一步

1. 建立 Project A 最小 Workspace。
2. 建立參考資料邊界。
3. 以 Project A 進行 Agent Mode / Context / Permission 的模擬運行。
4. 根據實際工作再決定是否需要 Project Contract、Migration 機制的進一步實體化。
5. Natural FIELD 後再進行整體健檢。

最高原則：

> 先隔離資料，再共享方法；先建立最小接口，再由實際運作決定是否擴張。


## 2026-09-19｜附加 Skill 分層

新增「遊戲開發附加 Skill 統御」層，與中央 Core System 分開管理。

分層：
L0 中央治理 → L1 附加 Skill 統御 → L2 領域附加 Skills → L3 專案 Skills → L4 Game Model / Transformation / Code / Runtime。

附加 Skill 按需載入，不進行全庫預載；專案 Skill 不自動升格中央；升格必須經 Evidence / Evaluation / Evolution。

統御 Skill 不建立第二個 Agent、Control Plane、CURRENT、Workpool 或 Registry Authority。
