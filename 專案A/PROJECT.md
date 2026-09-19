# 專案 A

狀態：【遊戲開發工作區；開發期完整能力模式】

## 專案定位

本資料夾是中央 Ai-knowledge Repository 內的 Project A 工作區。

目前方案 A 專門承載遊戲開發所需的資料、Game Model、遊戲專用 Skill、系統規劃、Transformation、Code、Test、Evidence 與後續實際遊戲專案資料。

開發期間不把遊戲能力再拆成獨立副系統執行。方案 A 直接使用中央系統的完整通用能力，以開發效率為優先；遊戲開發完成後，才依真實使用 Evidence 進行精簡、抽取、封裝與回收。

## Agent Mode

遊戲模式：
- 讀取方案 A 作為遊戲專用工作資料
- 中央系統提供完整共用 Agent / Skill / Context / Routing / Verification / Governance 能力
- 方案 A 可讀寫
- 其他專案不載入
- 中央系統治理規則不得由方案 A 直接改寫

遊戲模式不是第二套 Agent 或 Control Plane，而是「中央完整能力 + 方案 A 遊戲資料」的工作模式。

## 方案 A 分層

依主程式資料分層概念整理，但開發期間不做過度隔離：

- 0-知識/：遊戲領域知識；有實際需求才建立
- 1-系統/：遊戲專用 System / Skill / Game Model 規格
- 2-方案/：遊戲開發方案、Transformation、實作規劃
- 3-軟體/：實際遊戲工具或程式；有實際需求才建立
- 應用/：實際遊戲專案資料；有實際需求才建立
- 參考資料/：外部／補充參考資料

目前不預先建立大量空目錄。

## 中央系統

中央系統仍是唯一的共用治理與執行核心，包括 Agent、Control Plane、Runtime Closure、Skill Governance、State / Acceptance、Evidence / Verification、Evolution、Change 等。

方案 A 使用中央系統，不複製第二套治理核心。

## 遊戲資產原則

方案 A 內的遊戲 Skill、資料、Game Model、Transformation、Code、Test 與 Evidence 預設只屬方案 A。

只有經既有 Evidence、Research / Evaluation、Evolution / Verification 判定後，才可能提出跨專案重用或中央升格。

## 開發完成後

完成遊戲開發後，再執行：

使用紀錄 → Dependency Audit → 影響分析 → Evidence 整理 → KEEP / MERGE / COMPRESS / ARCHIVE / DELETE → 可重用能力抽取 → 最終精簡

開發期間不為了最終精簡而增加額外的跨層路由與資料隔離成本。

## 參考資料

本專案的外部／補充參考資料放在「參考資料」資料夾。


## 共用框架與專案專屬資料分層

方案 A 的遊戲資料分為兩種：

### A. 可跨遊戲重用的「遊戲開發框架層」

這是針對「如何使用本系統開發遊戲」的共通方法，例如：
- Game Model 最小契約
- Core Loop 設計方法
- Game System / Rule / State / Flow 的建模方式
- L1 / L2 / L3 驗證分層
- System Integration Validation
- Game Rule → Game Model → Skill → Transformation → Code → Verification 的追蹤
- Runtime → Evidence → Code → Transformation → Skill → Rule / Game Model 的反向除錯
- 遊戲開發相關的共通 Skill 治理與最小記錄格式

這些內容不應因 Project A 結束而重新建立一次。經 Project A 實際使用、驗證並確認具有跨遊戲價值後，整理成中央「遊戲開發共用框架封存」。

中央封存的狀態是：
【ARCHIVE-REUSABLE；不啟用；可供新遊戲專案套用】

它不是中央 Agent / Control Plane 的第二套執行系統，也不是第二個 CURRENT。

### B. Project A 專屬遊戲設計層

實際屬於本遊戲的內容，例如：
- 戰鬥設計
- 敵人
- 武器
- 數值
- 地圖
- 關卡
- 經濟
- 技能效果
- 特殊規則
- 劇情
- 美術／音效規格
- 實際 Game Data
- 本遊戲專屬測試與 Playtest 結果

預設留在方案 A，不因其存在而升格為中央共用框架。

判定原則：
「如何開發遊戲」偏向共用框架；
「這個遊戲是什麼」偏向專案專屬。

無法確認跨遊戲價值時，先留在 Project A，不提前抽取。

## 跨遊戲重用流程

Project A 開發取得的共通能力：

Project A 實際使用
→ Evidence / Verification
→ 判定是否具有跨遊戲重用價值
→ 蒸餾共通部分
→ 更新中央遊戲開發共用框架封存
→ 新 Project B 建立時直接套用
→ Project B 再以實際 Evidence 回饋框架

Project B 不需要重新建立 Project A 已驗證的共通框架。

但是 Project B 不直接讀取 Project A 的專屬遊戲資料。

## 框架版本同步原則

中央封存的「遊戲開發共用框架」視為共通框架的可重用版本庫。

當共通框架本身發生修正：
- 先修改共通框架的正式內容
- 同步更新中央封存版本
- 新專案套用最新版本
- 已在開發中的專案是否升級，依相容性與影響分析決定，不強制覆蓋專案現況

因此：
「共通框架要跟著改」；
但「專案專屬遊戲設計不跟著共通框架同步」。

這避免中央備份與各遊戲專案形成無限雙向同步。

