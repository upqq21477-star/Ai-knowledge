# 多專案 Agent 模式與工作區隔離規劃 v1.1

版本：v1.1
日期：2026-09-19
狀態：【方案 A 遊戲開發模式已確立；實際模式運作待 FIELD】

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

各專案保存自己的專案資料與專案專用能力。

## 2. Agent 工作模式

### SYSTEM MODE

- 中央系統：R/W
- Project A：R
- 其他 Project：R 或依實際模式定義

用途：修改中央規格、中央 System / Skill / Governance、跨專案共用能力與 Framework。

### GAME / PROJECT-A MODE

方案 A 目前作為遊戲開發工作區。

- 中央系統：提供完整共用能力；治理規格不由方案 A 直接改寫
- 方案 A：R/W
- 其他專案：不載入

用途：遊戲開發。

重要：GAME / PROJECT-A MODE 不是第二套 Agent、Control Plane 或 Runtime。它是「中央完整能力 + 方案 A 遊戲資料」的工作模式。

## 3. Context 邊界

遊戲模式啟動時，優先取得：
1. 中央系統執行目前任務所需的完整能力與規則。
2. 方案 A 的遊戲資料、Skill、Game Model、Evidence 與目前工作內容。
3. 目前任務所需的最小 Context。

其他專案不得因方便而混入 Context。

「最小 Context」是執行成本控制，不代表開發期間要把遊戲能力隔離成另一套 Domain Runtime。

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

專案回饋不等於中央系統立即修改。

## 5. 方案 A 的遊戲資料與分層

開發期間，所有已確認屬於遊戲開發領域的 Skill 與資料集中於方案 A，作為遊戲專用工作資料。

方案 A 比照主程式的資料分層概念：
- 0-知識/：遊戲領域知識
- 1-系統/：遊戲專用 System / Skill / Game Model
- 2-方案/：遊戲開發方案、Transformation、實作規劃
- 3-軟體/：實際遊戲工具或程式
- 應用/：實際遊戲專案
- 參考資料/：外部／補充資料

目前只建立已有需求的層級與資產，不預先建立大型空架構。

## 6. 開發期原則

方案 A 是開發工作區，不是最終發布結構。

開發期間：
- 允許使用中央全部必要能力。
- 允許遊戲 Skill 與遊戲資料集中存在方案 A。
- 不為最終精簡提前建立跨層路由成本。
- 保留實際使用 Evidence。

因此目前優先順序是：
開發效率 > 最終結構精簡。

## 7. 版本與更新

方案 A 不複製整套中央系統。

中央一般能力更新時，方案 A 使用中央最新相容能力；只有破壞性契約或資料格式變更才進入 Migration 判定。

## 8. 開發完成後的精簡

遊戲開發完成後才進行：

使用紀錄
→ Dependency Audit
→ 影響分析
→ Evidence 整理
→ KEEP / MERGE / COMPRESS / ARCHIVE / DELETE
→ 可重用能力抽取
→ 最終精簡／封裝

此階段才判斷哪些遊戲 Skill 應保留於專案、哪些可成為共用能力、哪些應壓縮或移除。

## 9. 專案生命週期

新專案：建立最小工作區。

開發：Project Mode + 中央完整 Framework。

成熟：可移出成獨立 GitHub Repository。

移出後：保留 Project Contract / Framework Baseline。

完成／廢棄：依生命週期保存、封存或刪除。

## 10. 目前不提前建立

暫不建立：
- Project Registry
- Capability Graph
- 自動化 Orchestrator
- 大型 Project Permission System
- 第二套中央治理核心
- 為遊戲模式複製整套 Agent / Control Plane / Runtime

是否需要更大型基礎設施，由實際運作 Evidence 決定。

## 11. 驗證方向

先以模擬驗收驗證：
1. 遊戲模式可讀取方案 A。
2. 遊戲模式可寫入方案 A。
3. 中央治理規格不被方案 A 直接改寫。
4. 其他專案不載入。
5. 方案 A 可直接使用中央完整必要能力。
6. 遊戲 Skill 與資料可在方案 A 內累積。
7. 方案 A 的成果不自動升格中央。
8. Runtime Receipt 能記錄 Mode、Workspace、Context Source、Write Target。
9. 開發期間不因分層而增加不必要路由成本。
10. 完成後可依 Evidence 進行精簡與抽取。

以上先作 Simulation；Natural FIELD 證據後再調整。

## 12. 目前決策

方案 A 現階段正式定位為「遊戲開發完整能力工作區」。

啟動遊戲模式的核心動作是：

GAME MODE
→ 讀取方案 A
→ 使用中央系統完整必要能力
→ 執行遊戲開發

而不是：

GAME MODE
→ 啟動另一套遊戲 Domain Runtime。

最高原則：

> 開發期間完整使用能力、集中保存遊戲專用資料；完成後再以 Evidence 進行精簡。
