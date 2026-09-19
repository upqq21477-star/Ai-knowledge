# Agent Skill v1.3

版本：v1.3
日期：2026-09-19
狀態：【建立；Small Mode 分流規格已接入；暫行監控指令已接入；待 FIELD】
定位：最上層 Orchestration Skill（Agent as Top-Level Skill）

## 1. 目的
在 AI 對話、Markdown、GitHub 與可用工具環境中，提供最小 Agent 編排：
任務理解 → 問題分流 → Context → Skill 選擇 → 執行 → 驗證 → 失敗診斷 → 重新分流 → 完成。
Agent 不依賴常駐程序、API、本地資料庫或背景服務。

## 2. 核心定位
Agent = 決策與編排。
Skill = 可重複工作責任。
Knowledge = 可引用資料。
Provider / Tool = 能力來源與外部操作。
Application = 實際工作場景。

## 3. 啟動
第一次接手 repository：
1. 依 README 現行入口鏈讀取必要文件。
2. 讀取本 Agent Skill。
3. 立即 ACTIVE，不等待「啟動」。
4. 後續任務維持 ACTIVE，除非使用者要求停止。
5. Context 重置時重新讀取並恢復。

## 4. 標準循環
Understand → Triage → Capability → Candidate Skill → Route → Mode → Context → Execute → Verify

FAIL → Failure Classification → Diagnosis → Re-route / Fix Skill / Fix Provider → Execute → Verify

完成後停止本次任務，但 Agent 保持 ACTIVE。

## 5. Skill 分流
完整分流規則由：
1-系統/Skill分流運作規格.md
定義。

目前 Small Mode 採：
Task → Task Understanding → Problem Triage → Required Capability → Candidate Skill → Skill Routing → Mode Selection → Context Selection → Execution → Verification

不以關鍵字直接選 Skill。

優先比較：
Responsibility → Trigger → Input / Output → Context → Verification

候選接近或有衝突時，再比較：
Failure Pattern → Dependency → Cost → Actual Usage

## 6. Skill 治理路由
出現新 Skill、新能力、Provider / Tool / Mode 變更、Skill 重疊、責任漂移或失效：
→ Skill 分類判斷 Skill
→ 若需修改：Evolution Management
→ Execution
→ Verification

重要邊界：
Skill Routing：「目前任務走哪個既有 Skill？」
Skill Classification：「系統是否應該建立、融合、更新、取代、延後或封存 Skill？」

路由不到不等於應建立新 Skill。

## 7. 工作路由
任務目標不清 → 任務理解
需要外部或歷史資料 → 研究
需要決定載入哪些資料 → Context 管理
需要跨對話／跨 AI 保存目前工作狀態 → 交接
需要判斷證據／正確性／失敗原因 → 證據／驗證／診斷
需要保存或管理長期資料 → 知識管理
需要執行已確認動作 → 執行
需要修改系統／Skill／結構 → 演化管理
出現長期重複、責任漂移、結構性成本 → 蒸餾

## 7.5 交接路由

需要把目前工作狀態交給下一個 AI / Context → 交接 Skill。
交接完成後，由 Context 管理決定接手時的必要載入範圍，再由 Agent 恢復正常分流。

交接 Skill 不負責一般任務路由，也不取代 Context 管理。

## 7.6 暫行品質監控指令

暫行方案：
`2-方案/暫行-上下文品質閾值監測方案-v1.0.md`

控制指令：
- 使用者輸入「啟動監控」→ 啟用暫行品質監控。
- 使用者輸入「停止監控」→ 停用暫行品質監控。
- 「刪除品質監測方案」→ 進入方案停用／刪除流程，不直接刪除正式 Skill。

監控啟用後：
1. 前 5 輪不做品質審計。
2. 第 6 輪起依 Context 風險與提前觸發事件決定檢查層級。
3. 正常情況只做對應級別的輕量檢查。
4. 發現 SUSPECT / FAIL 才進入深度 Diagnosis。
5. 單輪只記錄 PASS / SUSPECT / FAIL；累積樣本後才計算錯誤率。
6. 若本輪實際執行監控，在回答最底部追加極簡「監控額外消耗」行；未執行則不顯示。
7. 成本只能使用工作量代理估算，不得虛構 GPU／FLOPs／計費數據。
6. 監控本身不新增 Skill，也不改變正式 Skill 邊界。

執行限制：
目前環境沒有獨立、可信的 Context 百分比計量器，因此 25% / 40% / 60% / 75% 不得被宣稱為實測值。實際 FIELD 階段只能使用可觀測的 Context／任務複雜度代理指標，或在取得可靠量測後再套用百分比閾值。

監控是方案層暫行機制，不取代 Agent 的正常分流、Execution 或 Verification。

## 8. Failure Re-routing
Failure 不直接重跑相同路由。

先分類：
Data / Context / Research / Routing / Skill / Provider / Execution / Verification

若為 Routing Failure：
Failure → Diagnosis → 修正 Routing Input / Context / Candidate → Re-route → Execute → Verify

若為 Skill Failure：
Failure → Diagnosis → 判斷 Skill Definition 是否不足 → 必要時 Skill Classification / Evolution

若為 Provider / Tool Failure：
Capability 保留 → 更換 Provider / Tool → 重新執行

## 9. 最小化原則
不預載整個 repository。
不因存在 Skill 就強制使用。
不因 Provider、Tool、Mode 或名稱變化建立新 Skill。
能單一 Skill 完成就不串接。
只有必要時才進入 Impact / Migration / Distillation。
不因單次 Routing Failure 改變架構。

## 10. 成本
至少觀察：
Context Cost
Routing Cost
Execution Cost
Migration Cost
Maintenance Cost

第一版以 L / M / H 相對量級記錄，不假裝具有精密數值。

## 11. 失敗閉環
Failure 發生後，不直接重試同一流程。
先分類 → 診斷 → 修正 → 重新分流 → 驗證。
若同一 Failure Pattern 重複出現，送交 Skill 分類判斷或 Distillation 評估。

## 12. 停止條件
PASS：完成且必要驗證通過。
INSUFFICIENT：缺必要資料／權限／工具。
FAILED：合理修正後仍失敗。
USER_REQUIRED：必須由使用者提供資料或決策。
LIMIT：達到合理循環／成本限制。

## 13. 權限
Agent 可選擇與串接 Skill、要求驗證、重新規劃。
Agent 不可無證據永久新增／刪除／取代 Skill。
結構變更進入：
Research D3 → Skill 分類判斷 → Evolution → Execution → Verification

## 14. 文件修改
修改前讀取現行版本。
最小必要修改。
保留有效內容。
修改後檢查引用。
新增／實質修改／移動／刪除檔案時更新檔案索引。
文件建立不等於功能驗收。

## 15. Small / Large
目前使用 Small Mode。

Small：
Agent 直接依 Responsibility、Trigger、Context 與 Routing Conditions 選擇。

Large：
未來可增加 Registry / Retrieval / Ranking / Composition / Dependency Resolution。

兩者共用 Skill Definition。
Large Mode 不重新定義 Skill，也不因大型化提前建立新 Skill。

## 16. 暫行監控驗收

文件接入：PASS
「啟動監控」指令路由：已接入
「停止監控」指令路由：已接入
自動 Context 百分比量測：NOT AVAILABLE
實際 FIELD 監控：PENDING；成本帳本已接入

## 17. 驗收
文件建立：PASS
規則定義：PASS
Skill 治理路由：PASS（文件層）
Skill 分流規格：PASS（文件層）
實際運作：PENDING
零記憶接手：PENDING
50 次實際任務：PENDING

## 18. AI Control Plane

涉及目前狀態、Entity、Dependency、Impact、Evidence、Authority、Change 或 Provenance 時，使用：
- `1-系統/AI Control Plane.md`
- `1-系統/Control Plane Registry 規格.md`
- `1-系統/Control Plane Query 規格.md`

Control Plane 是 metadata / relationship / state 管理層，不取代 Source of Truth。
一般任務不強制查詢；跨文件修改、狀態衝突、影響分析、交接、重大演化時按需查詢。
修改 Repository 前仍須列出 Change Set 並等待 USER CONFIRM。
