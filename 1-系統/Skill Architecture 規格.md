# Skill Architecture 規格 v1.1

版本：v1.1
日期：2026-09-19
狀態：【Control Plane 基線；已套用至現有核心 Skill】
定位：Skill Control Plane 的 Skill Architecture 正式規格。
來源：A 交接「Skill Architecture」施工成果。
Authority：本文件定義 Skill Architecture；Skill Definition 個別內容仍由各 Skill 自身 Source of Truth 保存。

## 1. 目的

建立固定、可重複的 Skill 判定模型：

新能力／既有能力變更
→ Responsibility 判定
→ Skill Boundary 判定
→ Family / Skill / Mode 分層
→ Definition Contract
→ Verification
→ Lifecycle / Version
→ Evolution

本文件只處理 Skill Architecture。
不取代：
- Agent orchestration
- Skill Routing
- Workflow execution
- Registry Query
- Semantic Router Runtime
- Verification Runtime

## 2. 核心定義

Agent：任務級推理、協調與重新分流。
Workflow：多個 Skill 的責任組合與順序。
Skill：可獨立路由、具有明確責任、明確 I/O、可獨立驗證、可重用的工作單位。
Mode：同一 Skill Responsibility 下的不同運作方式。
Skill Family：具有共同責任邊界與治理語義的 Skill 集合。

判斷核心：

「Skill 是責任單位，不是功能清單、工具名稱、Provider 名稱、文件名稱或模型能力名稱。」

## 3. Skill Definition Contract

每個正式 Skill 至少必須能回答：

### Identity
- Skill ID
- Name
- Family
- Source Path

### Responsibility
- Purpose
- Responsibility
- Boundary
- Non-responsibility

### Activation
- Trigger
- Trigger Conditions
- Required Capability

### Interface
- Input
- Output
- Input Preconditions
- Output Conditions

### Capability
- Capability Summary
- Supported Operations
- Mode

### Dependency
- Required Context
- Skill / System / Knowledge / Plan dependencies
- Provider / Tool dependency（若存在）

### Execution
- Execution procedure pointer
- Expected execution behavior

### Failure
- Known Failure Pattern
- Failure Classification
- Failure fallback / reroute pointer

### Verification
- Verification method pointer
- Acceptance condition

### Governance
- State / Availability
- Acceptance Stage（【未】／【驗】／【代】／【已建立】）
- Lifecycle
- Version
- Source
- Authority
- Change / Evolution pointer

### Cost
- Context Cost
- Execution Cost
- Maintenance Cost
- Cost evidence（若已有）

缺少資料時：
- 已知但尚未定義 → PENDING
- 無法由現有資料證明 → UNKNOWN
- 不得自行補值。

## 4. Source / Derived / Runtime / Governance 四類資料

### Source of Truth
直接定義 Skill 行為與責任的正式文件。

例如：
Skill Definition、正式 Skill 指令、正式版本內容。

### Derived Metadata
由 Source 推導出的查詢資料。

例如：
Family、Trigger Summary、Capability Summary、I/O Summary、Path、Updated。

Derived Metadata 可重建，不得反向覆寫 Source。

### Runtime Data
實際運作產生的資料。

例如：
Task、Selected Skill、Mode、Execution Result、Failure、Cost、Trace。

Runtime Data 不得直接改寫 Skill Definition。

### Governance Data
管理 Skill 生命週期與變更的資料。

例如：
Change、Impact、Verification Status、Lifecycle、Version Decision、Migration Decision。

治理決策不得冒充 Runtime Evidence。

## 5. Skill Boundary Gate

候選能力必須依下列順序判定，不使用名稱或關鍵字直接建立 Skill。

### Gate A：獨立 Responsibility
問題：

「它是否有一個可以單獨描述、單獨交付的工作責任？」

否 → 不建立 Skill。

### Gate B：獨立 Trigger
問題：

「是否存在可辨識的觸發條件，使系統能知道何時需要這個責任？」

否 → 優先檢查是否其實是 Mode、Workflow 或內部步驟。

### Gate C：明確 I/O
問題：

「Input 與 Output 是否可以明確描述，且可由其他工作單位使用？」

否 → 不建立正式 Skill。

### Gate D：獨立 Verification
問題：

「是否可以單獨判定這個責任是否完成？」

否 → 優先檢查是否只是 Workflow 內部步驟。

### Gate E：可重用
問題：

「責任是否可跨至少一個以上合理情境重複使用？」

若只能服務單一一次性情境 → 優先歸入 Workflow / Application / Plan。

### Gate F：獨立 Failure Pattern
問題：

「失敗是否有自身可辨識的錯誤模式與處理邊界？」

若失敗完全依附另一責任 → 優先保持在同一 Skill 或 Workflow。

### Gate G：分離收益
確認拆分後是否至少改善其中一項：
- Context 載入
- Routing 清晰度
- Verification
- Reuse
- Failure isolation

同時不得造成不合理的：
- Dependency
- Token / Context
- Execution
- Maintenance
成本增加。

拆分不是因「功能多」而成立。

## 6. Skill / Agent Boundary

### Agent
負責：
- 任務理解
- 多 Skill 協調
- Context 選擇
- 失敗後重新分流
- 任務級決策

### Skill
負責：
- 一個可獨立路由的工作責任
- 該責任的執行規則
- 該責任的輸入輸出
- 該責任的驗證邊界

判定規則：

若核心問題是「這次任務整體要怎麼安排多個責任」→ Agent。

若核心問題是「完成某一明確、可重用責任」→ Skill。

不得因 Skill 較複雜就升格 Agent。

## 7. Skill / Workflow Boundary

Workflow 是責任組合，不是單一責任。

判定：

A Skill 可獨立完成核心責任
→ 保持 Skill。

需要：
Skill A → Output → Skill B → Output → Verification
且兩者責任不同
→ Workflow / Composition。

若只是同一責任中的多步驟
→ 保持在同一 Skill。

不得把固定步驟數量當成 Skill 拆分條件。

## 8. Skill / Mode Boundary

Mode 必須滿足：

Responsibility 不變
+
Input / Output 契約基本不變
+
只是運作方式、深度、成本或策略不同。

例如：
同一 Research Responsibility 下的 Standard / Deep 模式可保持同一 Skill。

若某 Mode 長期形成：
- 獨立 Responsibility
- 獨立 Trigger
- 獨立 I/O
- 獨立 Verification
- 獨立 Failure Pattern

則重新進入 Skill Boundary Gate。

不得因 Mode 名稱不同直接建立新 Skill。

## 9. Skill Family Boundary

預設分層：

Skill Family
→ Skill
→ Mode

Family 不是第二個執行單位。

建立 Family 的條件：
- 多個 Skill 具有穩定共同責任領域。
- Family 能降低治理與查找成本。
- Skill 之間仍保持清楚責任邊界。

若只有一個 Skill：
不必為了形式完整建立 Family 結構。

Domain 暫作預留概念，不建立獨立 Domain Registry，除非 FIELD / Evaluation 證明需要。

## 10. Provider / Tool / Knowledge / System Boundary

Provider：
提供能力來源。

Tool：
提供外部操作介面。

Knowledge / Reference：
提供可引用內容。

System：
提供可重複的方法結構。

Skill：
提供可獨立路由的工作責任。

因此：
- Provider 不自動成為 Skill。
- Tool 不自動成為 Skill。
- Knowledge 不自動成為 Skill。
- System 不自動成為 Skill。
- Model 不自動成為 Skill。

只有當它形成獨立 Responsibility，且通過 Boundary Gate，才進入 Skill Classification。

## 11. Skill Creation Decision

新能力出現時：

Candidate
→ 既有 Responsibility 檢查
→ Context / Routing / Provider / Tool 問題排除
→ Boundary Gate
→ Classification

可能結果：

KEEP
既有 Skill 已足夠，不修改。

MERGE
責任可由既有 Skill + Mode / Workflow 合理承接。

UPDATE
既有責任正確，但 Definition / 規則需要修改。

REPLACE
已有充分證據證明新 Skill 可完整承接舊責任，並完成替代驗證。

REFERENCE
不是工作責任，只需作 Rule / Knowledge / Reference。

DEFER
證據不足，不做永久結構變更。

ARCHIVE
退出現行工作結構，但保留歷史證據。

NEW
只有在 Boundary Gate 全部滿足，且無合理既有承接方式時才建立。

## 12. Split / Merge / Replace

### Split

觸發條件：
既有 Skill 同時承擔兩個以上長期獨立 Responsibility，且分離後能改善 Context、Routing、Verification 或維護。

流程：
Evidence
→ Problem
→ Boundary Analysis
→ Proposal
→ Verification
→ Split
→ New Versions
→ Re-test
→ Activate

### Merge

觸發條件：
兩個 Skill 長期具有相同或高度重疊 Responsibility，且分開維護造成實際成本。

不得只因文件相似就 Merge。

### Replace

必要條件：
- 新 Skill 覆蓋舊 Responsibility。
- Interface 相容或已完成 Migration。
- 有 Verification Evidence。
- 舊 Skill 的依賴與使用關係已處理。
- 回退方式已明確。

沒有替代證據 → DEFER，不 Replace。

### Archive

退出現行候選，但保留：
- Source
- Version
- Change history
- Reason
- Replacement / successor（若存在）

Archive 不等於 Delete。

## 13. Evolution Contract

正式演化流程固定：

Evidence
→ Problem
→ Proposal
→ Verification
→ Change
→ New Version
→ Verification
→ Activate

禁止：

一次失敗
→ 直接改 Skill 邊界。

一次命名衝突
→ 直接 Merge。

新 Provider
→ 直接建立 Skill。

新 Model
→ 直接建立 Skill。

功能數量增加
→ 直接 Split。

所有結構變更都需要可追溯 Evidence；證據不足時 DEFER。

## 14. Version / Lifecycle

Version：
表示 Definition 的可辨識版本。

Lifecycle：
描述 Skill 在工作結構中的生命週期。

採用既有系統已使用的生命週期語義：
Created → Tested → FIELD → Active → Updated / Superseded → Historical / Retired

具體 State 以正式 Control Plane / Registry 規格為準；Acceptance Stage 以《工程資產狀態與驗收控制規格》為準；Lifecycle 以正式 Lifecycle 規格為準。

Version Change 至少在以下情況發生：
- Responsibility 改變。
- Trigger 改變。
- I/O 契約改變。
- Boundary 改變。
- Verification 契約改變。
- Dependency 改變且影響行為。
- Execution 規則重大改變。

純 Derived Metadata 更新不得偽裝成 Skill Definition Version Change。

## 15. Dependency 最小規則

Dependency 表示：

「A 的正常工作需要 B。」

只記錄可證明的直接依賴。

未知：
→ UNKNOWN。

不得從名稱相似推導 Dependency。

不得把：
DEPENDS_ON
直接等同
AFFECTS。

Impact 必須由 Change Set、明確關係或 Evidence 支持。

Dependency 深度與 Impact 查詢由 Control Plane Query 規格管理，本文件不建立 Query Runtime。

## 16. Verification / Evidence Boundary

Verification：
「使用什麼方法判定結果是否符合要求？」

Evidence：
「這一次實際驗證產生了什麼證據？」

例：

Verification：
「重新執行 8 個邊界案例並檢查分類結果。」

Evidence：
「Case A1～A8 的實際結果、日期、輸出與 PASS / FAIL。」

規則：
- Verification ≠ Evidence。
- Simulation ≠ FIELD。
- Research ≠ FIELD。
- Summary ≠ Evidence。
- Registry metadata ≠ Verification result。

## 17. A 工作包邊界

本 Architecture 不建立：
- Registry Query Runtime
- Semantic Router Runtime
- Ranking Engine
- Embedding Search
- Vector Database
- Graph Database
- Large Capability Registry
- Skill Execution Runtime

需要這些能力時，只提出 Interface Requirement。

## 18. 給 B 的 Interface Requirements

B Registry / Query 至少需要：

- Skill ID
- Name
- Family
- Responsibility / Capability Summary
- Trigger Summary
- Input Summary
- Output Summary
- Boundary Summary
- State
- Lifecycle
- Version
- Dependency Summary
- Verification Summary
- Path
- Updated
- Authority
- Provenance

B 不得把 Registry View 當 Skill Source of Truth。

## 19. 給 C 的 Interface Requirements

C Router / Runtime 至少需要能取得：

- Candidate Skill ID
- Skill Responsibility
- Trigger
- Boundary
- Input / Output compatibility
- Required Context pointer
- Mode
- Lifecycle / Availability
- Minimal Verification target
- Source pointer

C 不需要知道 Registry 儲存方式。

C 不得因 Candidate 不存在直接建立 Skill。

## 20. 8 個邊界案例

### A1：新 Provider 提供既有 Research 能力
結果：不建立新 Skill。
理由：Provider 是能力來源，不是 Responsibility。

### A2：同一 Research Skill 增加 Deep Research 模式
結果：預設保持同一 Skill + Mode。
理由：Responsibility 不變。
若後續形成獨立 Responsibility，再重新進 Boundary Gate。

### A3：一個 Skill 同時負責 Research 與 Repository 修改
結果：進 Split 評估。
理由：兩者 Responsibility、Execution、Verification 可獨立。

### A4：兩個 Skill 只有名稱不同，但 Responsibility / I/O / Verification 相同
結果：進 Merge 評估。
理由：名稱差異不足以形成獨立 Skill。

### A5：Workflow 固定先 Research 再 Verify
結果：不因此建立第三個 Skill。
理由：這是多 Skill Composition。

### A6：某 Skill 一次路由失敗
結果：不立即改 Definition。
理由：一次 Routing Failure 不足以證明 Boundary 錯誤。

### A7：新能力找不到現有 Skill
結果：先排除 Task / Context / Capability / Candidate / Routing / Provider 問題，再進 Classification。
理由：「路由不到」不等於「需要新 Skill」。

### A8：新 Skill 已可替代舊 Skill，但尚未完成依賴與驗證遷移
結果：DEFER REPLACE。
理由：替代證據與 Migration 尚未完成。

## 21. A 完成驗收

A 必須全部 PASS：

- Skill Definition Contract
- Skill Boundary Gate
- Skill Family
- Skill / Agent Boundary
- Skill / Workflow Boundary
- Skill / Mode Boundary
- Provider / Tool Boundary
- Split
- Merge
- Replace
- Archive / Defer
- Version / Lifecycle
- Dependency
- Verification / Evidence
- Evolution
- B Interface
- C Interface
- 8 Boundary Cases

完成條件：

「任何新能力都可以依固定規則判斷：是否為 Skill、是否需要拆分、屬於哪個 Family、是否應 Merge / Replace / Archive / Defer，以及如何形成 Definition。」

達成後停止 Architecture 擴張；新增想法只能進 Future Work / Change Request。

## 22. 已知 UNKNOWN / 待驗證

1. FIELD 中不同 Skill 數量增加後，Family 是否仍足以降低管理成本：UNKNOWN。
2. Boundary Gate 在自然工作中是否能穩定降低錯誤分類：PENDING。
3. Skill Definition 的最小欄位是否仍可進一步壓縮：PENDING。
4. Version / Lifecycle 的實際操作成本：PENDING。
5. B Registry 與本 Contract 的實際 Derived View 同步：依 Source 重建，不另建第二 Source of Truth。
6. C Router / Runtime 與本 Contract 的實際自然運作證據：後續工作，不作本輪阻塞條件。

不得在證據不足時自行補完以上項目。

## 23. 參考與採用界線

外部 Agent Skills 實踐共同支持：
- Skill 作為可重用、可組合的工作能力。
- Metadata 先行、完整指令按需載入。
- Progressive Disclosure 降低 Context 成本。
- Skill 可包含 instructions、resources、scripts。

本架構採用的是上述可驗證設計原理，不直接複製任何單一平台的實作。

參考：
- Anthropic Agent Skills：Skill metadata → full instructions → additional resources 的 progressive disclosure。
- OpenAI Academy：Skill 作為可重用 workflow。
- Microsoft Agent Skills：Skill 的 name / description / instructions、可攜性、progressive disclosure 與 Skill / Tool / Knowledge 邊界。

外部實踐只作設計證據；本 Repository 的 CURRENT / Authority / Evidence / FIELD 規則優先。
