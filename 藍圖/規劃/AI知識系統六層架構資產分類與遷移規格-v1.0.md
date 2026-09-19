# AI 知識系統六層架構資產分類與遷移規格 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃建立中】

## 1. 目的
把既有 repository 資產從「文件名稱」改以「實際責任」分類。判斷單位不是副檔名，而是內容責任。

## 2. 分類優先順序
1. 單一可重用事實／原理 → Knowledge
2. 單一可重用功能 → System
3. 只在某 Project 有效 → Project
4. 可被 Agent 路由並負責一段工作 → Skill
5. 負責總任務調度 → Agent Skill
6. 負責語意解析與確認 → 協助 Skill
7. 方案級組合與規則 → 方案 Skill
8. 目前狀態／驗證／歷史 → State / Evidence / History
9. 規範、藍圖、索引、交接、治理 → Governance / Blueprint / Handoff

不要因檔名含有「Skill」「System」「方案」就直接分類。

## 3. 遷移處理碼
KEEP = 原責任已符合新契約。
REFINE = 保留原位置，修正責任與內容邊界。
SPLIT = 一份文件包含多個責任，拆成多個資產。
MERGE = 多份文件實際承擔同一責任。
WRAP = 舊文件保留，建立新的 Skill / System 介面引用它。
ARCHIVE = 已不屬 CURRENT，但作為歷史證據保存。
DEFER = 證據不足，不現在處理。
UNKNOWN = 無法可靠判斷，不猜。

## 4. 特別規則
Knowledge：若文件包含「如何做一件完整事情」，通常不是純 Knowledge，需要 SPLIT。
System：若文件包含大量「何時啟動」「某個專案怎麼使用」，可能需要 SPLIT Project / Skill。
Skill：若沒有 Trigger / Input / Output / Boundary / Verification / Stop，先視為候選，不直接宣告正式 Skill。
Project：不得複製通用 Knowledge / System，只引用。
Agent：不保存大量領域知識，只管理任務與調度。

## 5. 現有架構第一輪投影
- 0-知識/：主要作為 Knowledge 候選區，但目前存在「分類、管理、系統、運作、證據」等混合責任，第一階段做分類，不直接假設全部都是純 Knowledge。
- 1-系統/：目前同時存在 System、Skill、Spec、Evidence、核心入口等不同責任；需要二次分類。
- 2-方案/：可作為方案 Skill 的主要候選區，但部分內容其實是工程治理、施工、研究或歷史，不應全部 Skill 化。
- 專案A/：已有 PROJECT.md、GAME-BLUEPRINT.md、1-系統/、2-方案/，可作為 Project Scope 第一個實驗樣本。
- 藍圖/：屬 Blueprint / Planning，不直接歸入 Runtime Skill。
- 規則.md：保持 Governance Authority，不降級成 Knowledge。
- 目前狀態.md：保持高階狀態總覽。
- 檔案索引.md：保持檔案檢索治理用途。

以上是第一輪結構投影，不是最終遷移結論。

## 6. 第一個實驗 Project
以 專案A 作為 Project Scope 實驗，不立即搬遷。
目標：證明同一套 Shared Knowledge / System / Skill 可以被 Project A 選擇性引用，而不把其他 Project 資料帶入。
至少測：Project 啟動、Skill 選擇、System 選擇、Knowledge 載入、Boundary 阻擋、Result 回傳、Verification。

## 7. 遷移順序
第一優先：Knowledge / System / Skill 責任切割。
第二優先：Project Scope。
第三優先：協助 Skill / Agent Skill 介面。
第四優先：Control Plane Mapping。
第五優先：舊文件實體搬遷。
最後才刪除或封存已完全替代的舊文件。

## 8. 不允許的捷徑
不得看到 MD 就判斷是 Knowledge；看到 Skill 字樣就判斷是 Skill；為了整齊直接大量搬檔；沒有引用掃描就刪除舊文件；把歷史規劃當 CURRENT；把模擬結果寫成 FIELD Evidence。

## 9. 最終遷移判定
只有同時滿足：
責任明確 + 引用完整 + 新介面可讀 + Context 邊界通過 + Simulation PASS + Real Work Evidence 足夠
才可以將舊資產標記為可封存／可移除。
