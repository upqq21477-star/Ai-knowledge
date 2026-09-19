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
