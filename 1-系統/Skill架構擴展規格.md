# Skill 架構擴展規格 v1.0

版本：v1.0
日期：2026-09-19
狀態：【預備規格；Small Mode 使用中】

## 1. 定位
本文件是 Skill 架構的實作規格，不是新的 Skill。
目的：讓目前小規模 Skill 系統直接具備未來擴展至大型 Skill Library 所需的資料契約與切換介面。

## 2. 固定資料契約
每個正式 Skill 原則上保留：
- Skill ID
- Name
- Responsibility
- Purpose
- Trigger
- Input
- Output
- Mode
- Dependencies
- Routing Conditions
- Failure Patterns
- Verification
- Cost
- Lifecycle
- Provider / Tool references

缺少資料不得補猜，標記 UNKNOWN。

## 3. 概念邊界
Capability：可完成的能力。
Responsibility：對一項工作結果負責的範圍。
Skill：可重複、可獨立路由的工作責任。
Mode：同一 Skill 責任下的不同運作方式。
Workflow：多個能力／Skill 的任務流程。
Provider：提供能力的來源。
Tool：進行外部操作的工具。
Reference / Rule / Knowledge：提供依據的資料。

## 4. 小規模實作
目前 Skill 數量少，由 Agent 根據 Responsibility、Trigger、Context 直接選擇 Skill。

不建立：
- 獨立 Skill Registry
- 自動 Ranking
- Embedding
- Vector Database
- 動態 Composition Runtime

檔案索引仍是近期檔案檢索工具，不升級成大型 Registry。

## 5. 大規模介面
未來可在不修改 Skill 定義的情況下增加：
Registry → Capability Retrieval → Candidate Skill Retrieval → Ranking → Composition → Dependency Resolution

這些屬於 Provider / Infrastructure 層，不自動成為 Skill。

## 6. 切換判斷
當實際紀錄反覆證明以下現象開始超過 Small Mode 可合理管理範圍時，才進入 Large Mode 評估：
- Skill Selection 錯誤
- Skill Overlap
- Context 膨脹
- Candidate 搜尋成本
- 多 Skill Composition 成本
- Dependency 管理成本

不以 Skill 數量單一門檻決定。

## 7. 相容性要求
Large Mode 必須能讀取現有 Skill Definition。
不得要求重新建立全部 Skill。
不得改變既有 Responsibility 語義而未經 Skill Classification → Evolution → Verification。

## 8. 擴展順序
1. Skill Registry
2. Capability Registry
3. Candidate Retrieval
4. Ranking
5. Composition
6. Dependency Resolution
7. Routing Telemetry
8. 自動化

每階段必須由實際瓶頸觸發。

## 9. 驗證
任何大型化升級都必須比較：
- Context Cost
- Routing Cost
- Execution Cost
- Verification Cost
- Maintenance Cost
- Failure Rate

如果大型化後沒有降低主要瓶頸，允許停止或退回 Small Mode。

## 10. 與現有 Skill 系統的關係
Problem Triage：目前由 Research Skill 內部負責研究深度判斷。
Skill Boundary Analysis：目前由 Skill Classification Skill 負責。
Skill Routing：目前由 Agent 直接負責。

大型化後，這些責任不必重新定義；只增加檢索、排序、組合等基礎設施。

## 11. 禁止事項
- 不因大型化預期而提前建立大型 Runtime。
- 不因新 Provider 建立 Skill。
- 不因新 Tool 建立 Skill。
- 不因 Mode 增加建立 Skill。
- 不因功能數量增加直接拆 Skill。
- 不以單次失敗改變架構。
- 不把 Simulation PASS 當成 Field PASS。
