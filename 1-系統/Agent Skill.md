# Agent Skill v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】
定位：最上層 Orchestration Skill（Agent as Top-Level Skill）

## 1. 目的

在 AI 對話、Markdown、GitHub 與可用工具環境中，提供最小 Agent 編排：

任務理解 → Context → Skill 選擇 → 執行 → 驗證 → 失敗診斷 → 重新路由 → 完成。

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

Understand
→ Context
→ Select
→ Execute
→ Verify
→ PASS / FAIL

FAIL
→ Diagnosis
→ Failure Classification
→ 重新選擇必要 Skill
→ Execute
→ Verify

完成後停止本次任務，但 Agent 保持 ACTIVE。

## 5. Skill 路由

### 治理路由

出現新 Skill、新能力、Provider / Tool / Mode 變更、Skill 重疊、責任漂移或失效：
→ Skill 分類判斷 Skill
→ 若需修改：Evolution Management
→ Execution
→ Verification

### 工作路由

任務目標不清：
→ 任務理解

需要外部或歷史資料：
→ 研究

需要決定載入哪些資料：
→ Context 管理

需要判斷證據／正確性／失敗原因：
→ 證據／驗證／診斷

需要保存或管理長期資料：
→ 知識管理

需要執行已確認動作：
→ 執行

需要修改系統／Skill／結構：
→ 演化管理

出現長期重複、責任漂移、結構性成本：
→ 蒸餾

## 6. 最小化原則

不預載整個 repository。
不因存在 Skill 就強制使用。
不因 Provider、Tool、Mode 或名稱變化建立新 Skill。
能單一 Skill 完成就不串接。
只有必要時才進入 Impact / Migration / Distillation。

## 7. 成本

至少觀察：
Context Cost
Execution Cost
Migration Cost
Maintenance Cost

第一版以 L / M / H 相對量級記錄，不假裝具有精密數值。

## 8. 失敗閉環

Failure 發生後，不直接重試同一流程。

先分類：
Data / Context / Research / Routing / Skill / Provider / Execution / Verification

再選擇修正 Skill。

若同一 Failure Pattern 重複出現，送交 Skill 分類判斷或 Distillation 評估。

## 9. 停止條件

PASS：完成且必要驗證通過。
INSUFFICIENT：缺必要資料／權限／工具。
FAILED：合理修正後仍失敗。
USER_REQUIRED：必須由使用者提供資料或決策。
LIMIT：達到合理循環／成本限制。

## 10. 權限

Agent 可選擇與串接 Skill、要求驗證、重新規劃。
Agent 不可無證據永久新增／刪除／取代 Skill。
結構變更進入 Skill 分類判斷 → Evolution → Execution → Verification。

## 11. 文件修改

修改前讀取現行版本。
最小必要修改。
保留有效內容。
修改後檢查引用。
新增／實質修改／移動／刪除檔案時更新檔案索引。
文件建立不等於功能驗收。

## 12. 驗收

文件建立：PASS
規則定義：PASS
Skill 治理路由：PASS（文件層）
實際運作：PENDING
零記憶接手：PENDING
50 次實際任務：PENDING
