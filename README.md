# Ai-knowledge

這是一套以 Markdown + GitHub 為核心的個人 AI 工程知識庫。

## AI／工具接手入口

一般工作依現行入口鏈恢復必要 Context；若使用者要求「交接／開始交接／進行交接／交給下一個 AI」等交接意圖，優先進入 Handoff Skill。

目前唯一工程 CURRENT：
`2-方案/完善/CURRENT Baseline-v1.0.md`

交接任務入口：
1. `README.md`
2. `2-方案/完善/CURRENT Baseline-v1.0.md`
3. `規則.md`
4. `待辦清單.md`
5. `1-系統/交接 Skill.md`
6. 依任務需要讀取 Handoff Skill 產生的最小交接資訊；不再保留固定交接資料檔。
7. 依任務載入相關 Skill / System / Evidence。

舊交接文件、舊快照與舊施工總控只作歷史／背景參考，不得覆蓋 CURRENT。
若只提供 GitHub 首頁，AI 必須先讀 README，再讀 CURRENT Baseline；不得依舊文件猜測目前狀態。

## Agent 啟動規則

本 repository 採用「Agent as Top-Level Skill」運作方式。

任何 AI／工具第一次接手時，必須先恢復必要工作狀態並讀取：
`1-系統/Agent Skill.md`

讀取後立即啟動 Agent Skill，不等待使用者另外輸入「啟動」。
除非使用者明確要求停止，否則保持 `AGENT_STATE = ACTIVE`。

後續任務必須先經：
`Task Understanding → Context → Skill Selection → Execute → Verify → Replan if needed`

## 目前工程運作基準

目前唯一工程游標：
`2-方案/完善/CURRENT Baseline-v1.0.md`

目前：
- G1 FIELD：22 cases
- G1-P01～P12：CLOSED / Re-test PASS
- Handoff Skill：FIELD PASS；Memoryless Homepage-only PASS
- 暫行品質監控：已接入「啟動監控／停止監控」；FIELD 成本收益尚未完成
- Phase 1 CURRENT Baseline：Gate PASS
- Large Mode：暫緩

## 檔案變更紀錄

任何新建、實質修改、移動或刪除都必須同步更新根目錄 `檔案索引.md`。

新建／實質更動：
- 完整目前路徑
- 用途／本次主要內容
- 預計隔日檢索日期
- 狀態先標記 `待檢索`

隔日重新檢索後，找到且確認正常可見才移除近期紀錄；找不到則保留並標記待處理。

## 文件責任

`README.md` = 入口導航
`CURRENT Baseline-v1.0.md` = 唯一目前工程游標
`規則.md` = 操作規則 Authority
`待辦清單.md` = 唯一 Workpool
`目前狀態.md` = 高階架構總覽
`1-系統/交接 Skill.md` = Handoff 生成與生命週期規則；交接資料採按需建立、完成後退出，不維持固定交接檔。
`藍圖/AI單人工作室整體工程最新藍圖-v2.0.md` = 最新施工藍圖
`檔案索引.md` = 近期變更檢索驗證

歷史文件保存證據，但不得因存在而成為 CURRENT。

## 重要界線

不預載整個 repository。
不把 Simulation 當 FIELD。
不把 Provider、Tool、Mode 自動新增為 Skill。
不因單次問題建立新 Skill。
不建立第二 CURRENT。
不建立第二 Workpool。

## AI Control Plane

後台管理入口：
- `1-系統/AI Control Plane.md`
- `1-系統/Control Plane Registry 規格.md`
- `1-系統/Control Plane Query 規格.md`

用途：管理平常不需載入、但不能遺失且需要追蹤時必須可查的 Entity、State、Dependency、Impact、Change、Evidence、Provenance、Authority、Lifecycle、Capability、Trace。

原則：Source of Truth 優先；Registry 不取代原始文件；Graph / Index / Cache 可重建；Context 按需載入；高風險 Repository 修改需 USER CONFIRM。
