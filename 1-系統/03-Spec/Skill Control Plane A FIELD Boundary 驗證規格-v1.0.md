# Skill Control Plane A｜FIELD Boundary 驗證規格 v1.0

日期：2026-09-19
工作包：A — Skill Architecture
狀態：【FIELD PROTOCOL READY；NATURAL EVIDENCE PENDING】

## 1. 目的

本文件只驗證 A 的 Skill Architecture 是否能在自然工作中正確判斷：

- 是否應建立 Skill
- 是否應保持同一 Skill
- 是否應使用 Mode
- 是否應 Split / Merge / Replace
- 是否應保持 Workflow / Agent 邊界
- 是否應 Defer / Archive
- Definition 變更是否有足夠理由

本文件不是 Simulation 結果，也不替 A 製造通過證據。

## 2. FIELD 原則

只有真實工作流程中自然發生的事件，才能形成 FIELD Evidence。

不得：
- 為了驗收故意製造錯誤
- 用人工題目直接宣稱實戰通過
- 把 Simulation / 推演 / 文件閱讀寫成 FIELD
- 沒有觀測資料時填寫 PASS
- 由單一事件直接推導永久架構變更

每筆 Evidence 必須保留：
Task / Context / 原始需求 / 當時候選分類 / 實際處理 / 結果 / 問題 / Evidence / 是否需要 Change Request。

## 3. 觀測單位

每次自然工作遇到「新增能力、能力變形、重複能力、路由失敗、替代能力、流程組合」時，建立一筆 Case。

Case ID：
日期：
Task：
Context：
涉及 Skill：
原始分類：
實際處理：
結果：
Verification：
Evidence：
Architecture 是否需要修改：
Change Request（若有）：

## 4. FIELD Case 類型

### F-A1 新 Provider / Tool

自然事件：同一責任由新的 Provider / Tool 提供。

驗證目標：
確認 Provider / Tool 不會被誤分類為新 Skill。

通過條件：
Responsibility 未形成新的獨立工作單位，且原 Skill 可承接。

### F-A2 新 Mode

自然事件：同一 Skill 出現速度、深度、輸出形式或工作方式差異。

驗證目標：
確認 Responsibility 不變時可使用 Mode，而不是無理由拆 Skill。

### F-A3 Split

自然事件：既有 Skill 長期出現兩個可獨立呼叫、獨立驗證且責任不同的工作。

驗證目標：
Boundary Gate 能指出 Split，而不是只因文件變長就拆分。

### F-A4 Merge

自然事件：兩個既有 Skill 長期出現責任、I/O、Verification 高度重疊。

驗證目標：
確認 Merge 有實際證據，不因名稱相似就合併。

### F-A5 Workflow / Agent Boundary

自然事件：任務需要多個 Skill 串接或由 Agent 協調。

驗證目標：
確認多 Skill Composition 不被誤建立成單一 Skill。

### F-A6 Routing Failure

自然事件：既有 Skill 路由或分類失敗。

驗證目標：
確認單次 Failure 不直接改 Definition；先 Diagnosis。

### F-A7 No Candidate

自然事件：任務找不到現有 Skill。

驗證目標：
確認先排除 Task / Context / Capability / Candidate / Routing / Provider 問題，再判斷是否需要新 Skill。

### F-A8 Replacement / Defer

自然事件：新能力可能替代舊 Skill，但 Migration、Dependency 或 Verification 尚未完成。

驗證目標：
確認在證據不足時 Defer，而不是直接 Replace。

## 5. FIELD 判定

單一 Case 不足以宣稱架構整體 FIELD PASS。

A FIELD 需要累積自然 Evidence，並至少觀察：
1. Boundary 誤分類
2. 不必要 Split
3. 不必要 Merge
4. Mode / Skill 誤判
5. Workflow / Skill 混淆
6. Failure 導致過早改 Definition
7. No Candidate 導致任意建立 Skill
8. Replace / Defer 判斷錯誤

若發現問題：
Evidence → Problem → Proposal → Verification → Change Request。

沒有結構性問題：
保持目前 Architecture，不為了產生變更而變更。

## 6. 與 B/C 的隔離

本文件只驗證 A。

B Registry、C Router 的實際成本、Query Depth、Candidate Accuracy、Runtime Recovery 等，不在此文件判定。

跨包結果留待最終 D 驗收。

## 7. 目前結果

Architecture Static：PASS
Boundary Static：PASS
FIELD Protocol：READY
Natural FIELD Evidence：PENDING
A Final FIELD：PENDING

不得因为 Protocol Ready 而宣稱 A FIELD PASS。

## 8. 完成終點

當自然工作累積足夠 Evidence，且沒有未解決的結構性 Boundary 缺口時：

A FIELD → PASS

若發現結構性缺口：

A FIELD → CHANGE REQUEST

修改後重新驗證，不直接覆寫舊 Evidence。
