# Skill 分流運作規格 v1.0

版本：v1.1
日期：2026-09-19
狀態：【正式規格；Control Plane Query 接入；Small Mode 啟用】
定位：Skill Routing / Skill 分流運作規格；本文件不是 Skill。

## 1. 創建模式分類結果

本項依《Skill 建立流程規格》重新執行創建判斷。

候選問題：
「系統如何依任務判斷應使用哪個 Skill、Mode，失敗後如何重新分流？」

分類結果：

- 類型：System Architecture / Routing Specification
- 不是：新 Skill
- 不是：Provider
- 不是：Tool
- 不是：單一 Capability
- 不是：固定 Workflow
- 不是：Skill Classification Skill 的替代品

原因：
Skill Classification 負責判斷「Skill 結構是否應建立、融合、更新、取代、延後或封存」。
Skill Routing 負責判斷「目前這個任務現在應該使用哪個既有 Skill / Mode」。

兩者輸入、決策目的與輸出不同，但目前 Skill Routing 尚未證明需要獨立工作責任，因此先作為 Agent 的運作規格，不建立新的 Skill。

## 2. 核心邊界

### Skill Classification

回答：

「這個能力／責任是否應成為、修改或退出一個 Skill？」

輸出：
NEW / KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE

觸發：
新 Skill 候選、責任重疊、責任漂移、結構變更、長期失效等。

### Skill Routing

回答：

「這個任務現在應該走哪個既有 Skill？」

輸出：
Selected Skill / Selected Mode / Required Context / Routing Reason / Verification Target

觸發：
每次任務需要選擇工作責任時。

### Skill Execution

回答：

「已確認使用哪個 Skill 後，如何完成該責任？」

### Verification

回答：

「執行結果是否符合要求？」

### Failure Re-routing

回答：

「如果目前 Skill 沒有成功，問題屬於哪一層，以及下一次應如何重新選擇？」

## 3. Small Mode 目前正式分流流程

Task
→ Task Understanding
→ Problem Triage
→ Required Capability
→ Control Plane Query
→ Candidate Skill
→ Skill Routing
→ Mode Selection
→ Context Selection
→ Execution
→ Verification

若失敗：

Failure
→ Failure Classification
→ Diagnosis
→ 判斷是否為 Routing Failure
→ 必要時重新 Skill Routing
→ Execution
→ Verification

不是每次都完整執行全部節點。

能直接判斷時，允許跳過不必要步驟。

## 4. 第一層：Task Understanding

先確認：

- Goal
- Required Output
- Constraints
- Known Facts
- Unknowns
- Verification Target

如果任務本身尚未定義清楚，不直接進 Skill Routing。

路由：

Goal 不清
→ Task Understanding

資料不足但目標清楚
→ Research / Context 等後續 Skill

## 5. 第二層：Required Capability

不直接用「關鍵字 → Skill」方式路由。

先問：

「目前任務需要完成什麼能力？」

例如：

需要研究問題
→ Research Capability

需要管理 Context
→ Context Management Capability

需要驗證結果
→ Evidence / Verification / Diagnosis Capability

需要修改已確認文件
→ Execution Capability

需要改變系統結構
→ Evolution / Skill Classification Governance

Capability 是中間判斷層，不代表必須建立 Capability Runtime。

## 6. 第三層：Candidate Skill

依 Capability、Task、Trigger、Responsibility、Context 與現有 Skill Definition 找候選。

Small Mode 已可使用 Control Plane Registry 的 Derived View / Query；不啟用大型 Ranking Runtime。

Agent 透過 Control Plane Query 取得最小候選 metadata；只有需要時才展開 Skill Definition。

候選不足時：

先確認是否 Context 不足。

若 Context 不足：
→ Context Management

若問題本身未知：
→ Research

若現有 Skill 定義真的不足：
→ Skill Classification

不得因找不到立即建立新 Skill。

## 7. 第四層：Skill Routing

至少比較：

- Responsibility
- Purpose
- Trigger
- Input
- Output
- Mode
- Routing Conditions
- Dependencies
- Context Cost
- Execution Cost
- Verification
- Failure Pattern

選擇原則：

1. Responsibility 必須覆蓋任務核心工作。
2. Trigger 必須成立。
3. Input 必須足夠。
4. Output 必須能交付。
5. Verification 必須存在。
6. 不應為了次要需求選擇責任不符的 Skill。
7. 能由單一 Skill 完成時，不強制串接多個 Skill。
8. 若任務本身跨多責任，才形成 Skill Chain / Workflow。

不得只依：
- 名稱
- 文件位置
- 關鍵字
- Provider
- Tool
- 模型名稱
- Skill 數量

決定路由。

## 8. Mode Selection

Skill 已選定後，再選擇該 Skill 的 Mode。

原則：

Skill 責任不變，只改變運作方式。

例如 Research：

Research
├─ Search
├─ Standard Research
└─ Deep / Structural Research

Mode 不得被誤當成新 Skill。

若 Mode 長期形成獨立 Responsibility，才重新進入 Skill Classification。

## 9. Context Selection

Skill 選擇與 Context 選擇互相影響，但不混為同一責任。

基本順序：

Task
→ 判斷需要什麼責任
→ 找候選 Skill
→ 確認該 Skill 所需 Context
→ Context Management
→ 載入最小充分 Context
→ 執行

若 Context 不足導致無法判斷 Skill：

Skill Routing
→ Context Management
→ 再次 Routing

不得為了避免路由錯誤而預載整個 Repository。

## 10. 多 Skill 任務

Small Mode 優先：

單一 Skill
→ 完成
→ Verify

只有在一個 Skill 無法合理完成全部責任時：

Skill A
→ Output
→ Skill B
→ Output
→ Verification

串接前必須確認：

- 每個 Skill 的 Responsibility 不重複。
- 前一 Skill 的 Output 是下一 Skill 可接受的 Input。
- 串接有實際必要。
- 串接成本沒有超過直接處理成本。
- Failure 時知道應回哪一層。

不要因「功能很多」而建立 Skill Chain。

## 11. Failure Classification 與重新分流

失敗後不得直接重跑相同路由。

先分類：

Data
Context
Research
Routing
Skill
Provider
Execution
Verification

### Routing Failure

例如：

- 選錯 Skill。
- 正確 Skill 存在但未被選到。
- 多個 Skill 邊界無法區分。
- Skill Trigger 判斷錯誤。
- Mode 選擇錯誤。

處理：

Failure
→ Diagnosis
→ 修正 Routing Input / Context / Candidate
→ Re-route
→ Execute
→ Verify

### Skill Failure

如果路由正確，但 Skill 本身責任、規則或能力不足：

不要單純重新路由。

應：

Failure
→ Diagnosis
→ 判斷是否 Skill Definition 問題
→ Skill Classification / Evolution
→ 驗證

### Provider / Tool Failure

若只是 Provider / Tool 無法提供能力：

不得自動建立新 Skill。

應：

Capability 保留
→ 更換 Provider / Tool
→ 重新執行

## 12. Skill Classification 與 Routing 的互動

正常工作：

Task
→ Routing
→ Existing Skill
→ Execute

發現「現有 Skill 不足」：

Task
→ Routing
→ Failure / Gap
→ Research D3
→ Skill Classification
→ NEW / MERGE / UPDATE / REPLACE / DEFER
→ Evolution
→ Execution
→ Verification
→ 回到 Routing

因此：

「路由不到」不等於「建立新 Skill」。

必須先區分：

1. Context 不足
2. Task Understanding 錯誤
3. Capability 判斷錯誤
4. Candidate 檢索不足
5. Routing 判斷錯誤
6. Skill 本身不足
7. Provider / Tool 不可用
8. Verification 誤判

## 13. Routing 與 Skill Classification 的分流判斷

### 情況 A：Skill 已存在，只是不知道選哪個

→ Routing

### 情況 B：Skill 已存在，但 Trigger / Responsibility 定義不清

→ Skill Classification

### 情況 C：兩個 Skill 責任重疊

→ Skill Classification

### 情況 D：新 Provider 可以提供相同能力

→ Routing / Provider Selection

不建立新 Skill。

### 情況 E：新 Mode 可以完成相同責任

→ Mode Selection

不建立新 Skill。

### 情況 F：現有 Skill 無法承接新責任

→ Research D3
→ Skill Classification

### 情況 G：單一任務需要多個既有 Skill

→ Workflow / Skill Composition

不是自動建立新 Skill。

## 14. Small Mode 的路由成本控制

目前不追求形式化 Ranking。

使用最小充分比較：

1. Responsibility
2. Trigger
3. Input / Output
4. Context
5. Verification

只有候選相近或有衝突時，才增加：

6. Failure Pattern
7. Dependency
8. Cost
9. Actual Usage

因此：

簡單任務 → 輕量 Routing
複雜任務 → 增加比較
高不確定性 → Research
結構性疑問 → D3 + Classification

## 15. Large Mode 相容介面

未來 Large Mode：

Task
→ Task Understanding
→ Problem Triage
→ Problem Decomposition
→ Capability Retrieval
→ Candidate Skill Retrieval
→ Ranking
→ Composition
→ Dependency Resolution
→ Context Retrieval
→ Skill Routing
→ Execution
→ Verification
→ Telemetry
→ Replan

Large Mode 可以自動化：

- Candidate Retrieval
- Ranking
- Composition
- Dependency Resolution

但最終仍必須輸出與 Small Mode 相容的：

- Selected Skill / Skills
- Selected Mode
- Required Context
- Execution Result
- Verification Result
- Failure Classification
- Replan Requirement

不得因 Large Mode 改變 Skill Responsibility。

## 16. 路由資料紀錄

目前使用既有 Skill Usage / Failure Feedback。

至少記錄：

Task
Selected Skill
Selected Mode
Routing Reason
Context Used
Execution Result
Verification Result
Failure Type
Re-route
Final Result
Cost

這些資料未來可用於：

- Routing Error Analysis
- Skill Overlap Detection
- Large Mode 切換評估
- Skill Classification
- Distillation

## 17. Routing Error 的結構性判斷

單次路由錯誤：

→ 修正任務處理
→ 不立即改架構。

重複同類錯誤：

→ 分析 Failure Pattern。

若發現：

- Skill 邊界問題
- Trigger 衝突
- Responsibility 重疊
- Context 無法支持判斷
- Candidate 檢索成本過高

才進一步進入：

Research
→ Classification / Evolution
或
Large Mode 評估

## 18. 禁止事項

- 不用關鍵字直接決定 Skill。
- 不因路由失敗直接建立 Skill。
- 不因 Provider 不同建立 Skill。
- 不因 Tool 不同建立 Skill。
- 不因 Mode 不同建立 Skill。
- 不因一次 Routing Failure 改變架構。
- 不預載全部 Context。
- 不為了「完整」強制串接全部 Skill。
- 不把 Skill Classification 當成一般 Routing。
- 不把 Routing 當成 Skill Classification。
- 不把 Simulation PASS 當成 Field PASS。
- 不提前建立 Large Mode Runtime。

## 19. 驗收方法

文件層：

- Routing Boundary：PASS
- Classification Boundary：PASS
- Small Mode Flow：PASS
- Failure Re-routing：PASS
- Large Mode Interface：PASS

實際運作：

PENDING

後續使用真實任務記錄：

- Routing Accuracy
- Re-routing Rate
- Wrong Skill Rate
- Unnecessary Skill Chain Rate
- Context Cost
- Verification Failure Rate

目前不設定硬性數值門檻。

先取得實際資料，再決定是否需要修改 Routing 規格或建立新的獨立責任。

## 20. 最終模型

目前：

Task
→ Understand
→ Triage
→ Capability
→ Candidate
→ Route
→ Mode
→ Context
→ Execute
→ Verify

失敗：

Failure
→ Classify
→ Diagnose
→ Re-route / Fix Skill / Fix Provider
→ Execute
→ Verify

結構變更：

Gap
→ Research D3
→ Skill Classification
→ Evolution
→ Execution
→ Verification
→ 回到 Routing

核心原則：

「Routing 決定現在走哪裡；Classification 決定系統本身是否應該改變。」

