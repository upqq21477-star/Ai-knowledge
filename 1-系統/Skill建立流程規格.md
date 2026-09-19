# Skill 建立流程規格 v1.0

版本：v1.1
日期：2026-09-19
狀態：【正式規格；Control Plane 接入】
定位：Skill 建立的流程規格；本文件不是 Skill。

## 1. 目的

防止「發現功能 → 直接建立 Skill」造成 Skill 膨脹、責任重疊與路由成本增加。

## 2. 建立觸發

出現以下任一候選時進入本流程：
- 新能力可能需要獨立工作責任。
- 既有 Skill 可能無法承接新的工作責任。
- 既有 Skill 出現長期責任膨脹、重疊或路由衝突。
- 新功能可能需要獨立 Trigger、Input / Output 或驗證。

## 3. 預設研究深度

新 Skill 建立候選預設為 D3 深度／結構研究。

只有研究證明候選只是既有 Skill 的內部功能、Mode、Workflow、Shared Capability、Provider / Tool 或 Reference，才停止新 Skill 建立流程。

## 4. D3 研究內容

1. 定義問題與建立原因。
2. 拆解候選責任。
3. 建立研究問題地圖。
4. 盤點現有 Skill。
5. 盤點可重用 Capability。
6. 分析 Responsibility Boundary。
7. 比較 Trigger、Input、Output、Dependency、Failure、Verification。
8. 比較 Context、Execution、Maintenance 成本。
9. 搜尋同領域案例。
10. 必要時進行跨領域類比。
11. 找反例與可能失敗模式。
12. 形成分類候選。

## 5. 分類

交由 Skill 分類判斷：

NEW / KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE

## 6. NEW 必要條件

至少具備：
- 獨立 Responsibility。
- 可辨識 Trigger 或獨立路由需求。
- 明確 Input / Output。
- 可定義 Verification。
- 既有 Skill 無法合理以 Mode / Workflow / Capability 承接。
- 建立後的 Context / Routing / Maintenance 成本合理。

資料不足 → DEFER，不猜測。

## 7. 建立後流程

分類確認 NEW
→ Evolution Management
→ Execution
→ Simulation Verification
→ 寫入 Skill Definition
→ Derived Registry Reconcile
→ 更新檔案索引
→ 正式運行（未實際驗證者標註「（代）」）
→ 建立 Usage / Failure 回饋

若建立過程發現問題：
- 立即建立 Problem Record。
- Structural Blocking：立即修正後再繼續建立。
- Non-Blocking：允許完成本 Skill 建立，再於 Verification / 回修階段處理。
- 不因非阻塞問題中斷整個建立流程。

## 8. 不建立的情況

Provider 不同：不建立。
Tool 不同：不建立。
Model 不同：不建立。
名稱不同：不建立。
同責任不同深度：優先 Mode。
單一工作流程步驟：優先 Workflow。
共享操作能力：優先 Capability。
證據不足：DEFER。

## 9. Small / Large 相容

Small Mode：由 Agent / Semantic Router 依 Responsibility、Trigger 與 Control Plane 最小 metadata 選擇。

Large Mode：未來可透過 Registry / Retrieval / Ranking 找到本 Skill；不得要求重新定義 Skill Responsibility。

## 10. 驗證

建立文件 ≠ Skill 驗收。

前置驗收一律先採模擬驗收：
- Trigger 可觸發。
- Input 足夠。
- Output 可交付。
- 與既有 Skill 路由不衝突。
- 可完成責任。
- Verification 可執行。
- Failure 可分類。
- 正常與主要失敗情境均通過模擬。

模擬 PASS → 正式 Skill → 立即進入運行。
尚未取得實際運行證據 → 標註「（代）」並進入追蹤。
實際運行不再是准入門檻，而是解除「（代）」的成熟度驗證。

## 11. 建立階段問題處理 Gate

單一 Skill 建立以「完成建立 → 模擬驗收 → 正式運行（代）→ 實際運行追蹤 → 必要回修」為預設。

只有會影響後續結構的問題才立即阻塞建立，包括：
- Responsibility Boundary 錯誤
- Data Contract 錯誤
- Routing 基礎錯誤
- 關鍵 Dependency / 上下游契約錯誤
- 會使後續 Skill 建立建立在錯誤前提上的問題

建立族群若包含多個相互依賴 Skill，先完成整體族群，再統一進行 Verification 與非阻塞問題回修。

建立階段結束前，該批次 Problem 必須完成或正式 DEFER / ACCEPTED RISK；不得把未處理 OPEN 問題直接帶入下一依賴階段。
