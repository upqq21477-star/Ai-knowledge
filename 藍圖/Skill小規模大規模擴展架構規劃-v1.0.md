# Skill 小規模／大規模擴展架構規劃 v1.0

版本：v1.0
日期：2026-09-19
狀態：【預備架構；Small Mode 啟用；Large Mode 預留】

## 1. 目的

建立一套可由小規模直接成長至大規模的 Skill 架構。

核心要求：

- 現在以低成本、小量 Skill 運作。
- 不提前建置大型 Router、向量資料庫或複雜 Runtime。
- 但現在就固定未來擴展所需的責任、資料欄位、路由介面與切換條件。
- Skill 數量增加後，改用 Large Mode，不重新設計核心責任。
- Small Mode 與 Large Mode 使用同一套 Skill 定義與責任模型。

## 2. 核心原則

### 2.1 小規模優先

目前 Skill 數量少時：

Task Understanding
→ Problem Triage
→ Context
→ Skill Selection
→ Execute
→ Verify

由 Agent 直接判斷即可。

不因未來可能變大而現在增加不必要系統。

### 2.2 大規模可切換

未來當 Skill 數量、重疊、Context 成本或 Routing 錯誤達到門檻時，才啟用：

Problem Decomposition
→ Capability Retrieval
→ Skill Candidate Retrieval
→ Skill Ranking
→ Skill Composition
→ Execution
→ Verification

### 2.3 不改核心資料契約

Small / Large Mode 必須共用：

- Skill ID
- Responsibility
- Purpose
- Trigger
- Input
- Output
- Mode
- Dependency
- Failure Pattern
- Verification
- Cost
- Routing Condition
- Lifecycle

## 3. 架構層

固定概念層：

1. Problem
2. Capability
3. Responsibility
4. Skill
5. Mode
6. Workflow
7. Provider
8. Tool
9. Reference / Rule / Knowledge

禁止把上述概念僅因名稱不同而重複建立。

## 4. Skill 邊界

候選功能必須依序檢查：

Candidate
→ Problem Triage
→ Problem Decomposition
→ Capability Identification
→ Responsibility Identification
→ Boundary Analysis
→ Existing Skill Match
→ Routing Value
→ Classification

Boundary Analysis 至少比較：

- Purpose
- Trigger
- Input
- Output
- Responsibility
- Decision Authority
- Mode
- Dependency
- Failure Pattern
- Verification
- Actual Usage
- Context Cost
- Execution Cost
- Maintenance Cost

## 5. 功能清單

### A. 問題層

A01 Task Understanding
A02 Problem Triage
A03 Problem Decomposition
A04 Research Depth Selection
A05 Dynamic Escalation / Downgrade

### B. Capability 層

B01 Capability Identification
B02 Capability Mapping
B03 Capability Reuse
B04 Capability / Provider Separation

### C. Skill 治理層

C01 Skill Classification
C02 Skill Boundary Analysis
C03 Skill Overlap Detection
C04 Skill Merge
C05 Skill Update
C06 Skill Replacement
C07 Skill Archive
C08 Skill Defer
C09 Skill Lifecycle Tracking

### D. Skill 運作層

D01 Skill Trigger
D02 Skill Selection
D03 Mode Selection
D04 Skill Execution
D05 Skill Verification
D06 Failure Routing
D07 Replanning

### E. Context 層

E01 Required Context Detection
E02 Context Loading
E03 Context Boundary
E04 Context Cost Tracking
E05 Large-Scale Context Retrieval（預留）

### F. Research 層

F01 Search
F02 Deep Research
F03 Same-Domain Research
F04 Cross-Domain Analogy
F05 Evidence Collection
F06 Solution Comparison
F07 Research Depth Adjustment

### G. 大規模擴展層

G01 Skill Registry
G02 Capability Registry
G03 Candidate Retrieval
G04 Skill Ranking
G05 Skill Composition
G06 Dependency Resolution
G07 Routing Telemetry
G08 Automated Candidate Filtering

G01–G08 現階段只保留規格，不提前實作。

## 6. Small Mode

目前啟用。

基本流程：

Task
→ Understand
→ Triage
→ Context
→ Skill Classification / Selection
→ Execute
→ Verify

特徵：

- 少量 Skill。
- Agent 直接選擇。
- 人工可檢查。
- 靜態文件即可。
- 不需要獨立 Registry。
- 不需要自動 Ranking。
- 不需要 Skill Embedding。
- 不需要動態 Composition Engine。

## 7. Large Mode

預留。

觸發後：

Task
→ Understand
→ Triage
→ Decompose
→ Capability Retrieval
→ Skill Candidate Retrieval
→ Ranking
→ Composition
→ Context Retrieval
→ Execute
→ Verify
→ Telemetry
→ Replan

Large Mode 仍使用相同 Skill 定義。

## 8. Large Mode 切換條件

以下任一類長期出現，即進入 Large Mode 評估：

### 規模

- Skill 數量顯著增加。
- Candidate Skill 無法由人工可靠搜尋。
- Skill Registry 成為必要成本。

### 路由

- Skill Selection 錯誤重複出現。
- Skill 之間重疊造成路由衝突。
- 多 Skill 組合頻率明顯增加。

### Context

- 手動載入 Context 成為主要成本。
- Skill 選擇需要大量文件才能判斷。

### 維護

- Skill Mapping 維護成本明顯增加。
- Dependency / Lifecycle 無法靠簡單索引管理。

### 工作流

- 單一任務經常需要多個 Skill 動態組合。
- 固定 Workflow 無法覆蓋主要任務。

切換必須以實際資料為依據，不以預測數字自動觸發。

## 9. 切換原則

Small → Large：

不是重建 Skill。

而是：

- 保留 Skill Definition。
- 保留 Responsibility。
- 保留 Trigger。
- 保留 Input / Output。
- 保留 Verification。
- 增加 Registry / Retrieval / Ranking / Composition 層。

Large → Small：

若實際證明大型機制成本過高，也允許退回 Small Mode。

## 10. Provider / Tool 邊界

Provider / Tool 不因能力增加而自動成為 Skill。

例如：

GPT、GitHub、Search Tool、Repository、人工判斷

都可能提供同一 Capability。

因此：

Capability = 做什麼
Provider = 誰提供
Tool = 如何操作
Skill = 如何組織可重複工作責任

## 11. Mode 邊界

同一 Responsibility 的不同成本、深度或方法，優先使用 Mode。

目前例：

Research
├── Search Mode
└── Deep Research Mode

未來例：

Research
├── Quick
├── Standard
├── Deep
└── Structural

只有當 Mode 已形成獨立 Trigger、Input / Output、責任、驗證與獨立路由價值時，才重新進行 Skill 分化判斷。

## 12. 驗證

每次新增／修改架構先檢查：

1. 是否新增真正責任？
2. 是否已有 Skill 可承擔？
3. 是否只是 Mode？
4. 是否只是 Capability？
5. 是否只是 Workflow？
6. 是否只是 Provider / Tool？
7. 是否增加不必要 Context？
8. 是否增加 Routing 成本？
9. 是否增加 Maintenance 成本？
10. 是否有實際 Failure Pattern 支持變更？

## 13. 創建模式

本規劃採「先規格、後實作」的創建模式。

### 現在建立

- 核心責任模型
- Skill 定義欄位
- 邊界判斷欄位
- Small Mode
- Large Mode 介面
- 切換條件
- 功能分類
- Lifecycle
- Feedback

### 現在不建立

- 大型 Skill Registry 實作
- Embedding
- Vector Database
- 自動 Skill Ranking Engine
- 自動 Skill Composition Runtime
- 常駐 Agent Runtime
- API 服務
- 複雜自動化 Pipeline

### 未來建立順序

1. Skill Registry
2. Capability Registry
3. Candidate Retrieval
4. Ranking
5. Composition
6. Dependency Resolution
7. Routing Telemetry
8. 自動化

每一層都必須由實際瓶頸觸發。

## 14. 與目前系統整合

目前：

Agent
→ Task Understanding
→ Research / Context / Verification / Execution / Evolution / Knowledge / Distillation
→ Skill Classification（需要 Skill 結構變更時）

新增的 Problem Triage / Depth Selection 屬於 Research 的研究前控制機制，目前不直接建立獨立 Skill。

Skill Boundary Analysis 目前屬於 Skill Classification 的判斷責任，不直接新增獨立 Skill。

未來若實際使用證明兩者具有獨立 Trigger、Input / Output、路由價值與維護必要性，再重新進行 Skill 分化判斷。

## 15. 狀態

整體架構規格：建立
Small Mode：啟用
Large Mode：預留
功能清單：建立
切換條件：建立
大型實作：未啟用
實際規模驗證：PENDING
