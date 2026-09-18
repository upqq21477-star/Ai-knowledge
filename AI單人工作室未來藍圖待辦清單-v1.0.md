# AI 單人工作室未來藍圖待辦清單 v1.0

> 文件定位：未來藍圖的第四份核心文件。  
> 文件性質：工程待辦（TODO）與建設順序規格，不是第五套正式方案。  
> 目前狀態：規劃中，尚未代表所有項目都應立即實作。  
> 核心原則：先凍結規格假設，再建立工作管理與能力啟動規則；先驗證實際工作循環，再決定哪些管理系統值得實體化。

---

## 一、文件目的

本文件用來回答未來藍圖最重要的工程問題：

1. 哪些規格必須最先確定？
2. 哪些項目會成為後續文件的共同依賴？
3. 哪些系統如果太早建立，未來很容易返工？
4. 如何避免「能力已建立，但 AI 不知道何時使用」？
5. 哪些項目應先以規格／人工流程存在，哪些項目等實際瓶頸出現後才實體化？
6. 未來藍圖應如何由「規格 → Mapping → 工作循環 → 驗證 → 演化」逐步落地？

本文件不負責重新定義四個正式方案，也不新增 A13、B17、C19、D21 等正式功能。

---

# 二、目前工程定位

目前正式系統已完成四個方案：

1. 方案一：整體資料治理
2. 方案二：AI 知識管理
3. 方案三：知識與資料迭代演化
4. 方案四：能力蒸餾與系統重構

A1–A12、B1–B16、C1–C18、D1–D20 已完成模擬／回歸驗收並進入正常工程運作。

因此，未來藍圖不是要取代四方案，而是建立更高一層的「能力導向（Capability-centric）」演化框架。

目前應避免：

- 把未來藍圖誤認為第五套正式方案。
- 因為藍圖列出某個系統，就立即實作該系統。
- 為了補滿 Mapping 而猜測未知的 K07–K61。
- 為了補滿 Scenario 而猜測未知的 S11–S37。
- 在沒有真實工作瓶頸前建立大型 Registry、Graph、Automation 或 Orchestration。
- 重新進行四方案整體驗收。
- 人為製造 FIELD 案例。

---

# 三、最高原則：先規格，後系統

未來藍圖的建設順序不能依照「文件章節順序」或「看起來最先進的功能」決定。

正確原則是：

> 先處理所有後續文件共同依賴的規格假設，再處理 AI 實際工作時的管理、觸發、召回與 Context，接著把既有資產 Mapping 進去，最後才根據真實工作證據決定哪些系統需要實體化。

核心順序：

    規格假設
        ↓
    工作管理規格
        ↓
    Trigger / Recall / Context
        ↓
    Provider / Capability / System 關係
        ↓
    Mapping
        ↓
    Scenario / Test Corpus
        ↓
    Evaluation
        ↓
    Real Work
        ↓
    Change Signal
        ↓
    Capability Evolution
        ↓
    必要時才實體化 Registry / Graph / Automation

---

# 四、P0：未來藍圖核心規格假設【最高優先】

## P0-01 核心物件模型

先凍結未來藍圖的基本物件：

- Knowledge
- Data
- Capability
- System
- Provider
- Scenario
- Plan
- Evidence
- Decision
- Change Signal

必須明確規定：

- Capability ≠ System
- Provider ≠ Capability
- Knowledge ≠ Capability
- System 可以提供 Capability
- GPT / Model 可以提供 Capability
- Tool 可以提供 Capability
- Human 可以提供 Capability
- 多個 Provider 可以共同提供同一 Capability

完成條件：

> 後續所有文件都可以引用同一套物件定義，而不需要重新解釋基本概念。

---

## P0-02 Namespace 規格

目前正式命名原則：

- Kxx = Knowledge
- CAP-xxx = Capability
- SYS-xxx = System
- PLN-xxx = Plan
- SCN-xxx = Scenario
- EVD-xxx = Evidence
- DEC-xxx = Decision

歷史 S01–S10 為已確認的 Scenario，未來正式名稱使用 SCN-01–SCN-10；歷史 S01–S10 保留作為來源識別。

Capability ID 已修復碰撞：

- K03 Trigger Registry → CAP-60 Trigger Registry
- D20 Distillation Trigger → CAP-61 Distillation Trigger

不得重新合併為 CAP-55。

完成條件：

> 未來新增物件不再自行發明不同 ID 格式。

---

## P0-03 Capability 標準規格

Capability 至少應具有：

- Capability ID
- Name
- Purpose
- Input
- Output
- Trigger
- Context
- Provider
- Dependency
- State
- Lifecycle
- Verification
- Evidence
- Scenario
- Cost
- Risk

核心定義：

> Capability 是在特定條件下，完成某種可驗證工作的能力。

完成條件：

> 未來所有 Capability Mapping 均能使用同一套欄位描述。

---

## P0-04 Provider 規格

Provider 至少區分：

- Human
- GPT / Model
- System
- Tool
- Hybrid

必須明確：

> Provider 是能力提供者，不等於 Capability 本身。

未來比較時必須比較「同一 Capability 的不同 Provider」，而不是只比較系統名稱。

---

## P0-05 State / Version / Git Commit 分離

三者不得混用：

- Version：版本識別
- State：生命週期狀態
- Git Commit：Repository 追蹤與證據

建議 State：

- CURRENT
- REVIEW
- DEPRECATED
- RETIRED
- HISTORICAL

完成條件：

> 任何文件都不能以 Git Commit 或版本號直接推論目前是否有效。

---

## P0-06 Lifecycle 規格

固定成熟度：

    DESIGNED
        ↓
    BUILT
        ↓
    SIMULATION-VALIDATED
        ↓
    REAL-WORK-VALIDATED
        ↓
    CURRENT

必須區分：

- 已定義
- 已文件化
- 已建立
- 可使用
- 已模擬驗證
- 已真實工作驗證
- 已成為 CURRENT

完成條件：

> 「檔案存在」不再被視為「能力已證明有效」。

---

## P0-07 Relationship 規格

至少區分：

- 使用
- 依賴
- 支撐
- 來源
- 支持
- 比較
- 衝突
- 分類
- 前身
- 取代
- 部分取代

基本原則：

- 使用 ≠ 依賴
- 支撐 ≠ 依賴
- 來源 ≠ 支持
- 比較 ≠ 衝突
- 分類 ≠ 關係

Relationship 應保留：

- Type
- Source
- Target
- Time
- Scope
- Condition
- State

完成條件：

> 後續 Mapping 不因語意含糊而產生錯誤依賴。

---

## P0-08 Change / Evolution 基本模型

固定：

    Change Signal
        ↓
    Impact
        ↓
    Change Proposal
        ↓
    Evaluation
        ↓
    Migration
        ↓
    Validation
        ↓
    Adoption

模型更新只是 Change Signal 的一種來源，不是唯一來源。

可能來源：

- Model Update
- Tool Update
- Workflow Change
- New Evidence
- Real-Work Bottleneck
- 新需求
- 驗證失敗
- 資料狀態變化

---

## P0-09 Failure Closure 規格

成功：

    Execution
        ↓
    Verification
        ↓
    PASS
        ↓
    Evidence / Observation

失敗：

    Execution
        ↓
    Verification
        ↓
    FAIL
        ↓
    Failure Classification
        ↓
    Diagnosis
        ↓
    Problem Confirmation
        ↓
    Solution Research
        ↓
    Fix Proposal
        ↓
    Implementation
        ↓
    Revalidation

Failure 類型至少包括：

- Data Insufficiency
- Evidence Insufficiency
- Data Conflict
- Insufficient Context
- Excessive Context
- Wrong Version / State
- System Capability Insufficiency
- Plan Composition Error
- Insufficient Verification

---

## P0-10 Disposition 規格

能力或系統的處置至少包括：

- Keep
- Extend
- Refactor
- Merge
- Split
- Replace
- Rebuild
- Retain
- Retire
- Archive

資料／知識演化至少包括：

- 補充
- 修正
- 部分取代
- 完全取代
- 融合
- 拆分
- 廢棄
- 前身／歷史

---

# 五、P0：AI 工作管理規格【與核心規格同等重要】

這一層是目前最需要提前建立的部分。

核心問題不是：

> 「我們有沒有建立 Capability？」

而是：

> 「AI 在實際工作時，能不能知道什麼時候應該使用哪個 Capability？」

因此必須先定義 AI 的最小工作循環：

    User Request
        ↓
    Intent
        ↓
    Task Classification
        ↓
    Decomposition
        ↓
    Capability Discovery
        ↓
    Trigger / Recall
        ↓
    Context Selection
        ↓
    Context Assembly
        ↓
    Provider Selection
        ↓
    Execution
        ↓
    Verification
        ↓
    Persistence
        ↓
    Feedback

注意：

> 這是一個工作模型，不代表每個任務都必須逐節執行全部步驟。

---

## P0-11 Trigger 規格

必須先定義什麼情況可能觸發 Capability。

候選 Trigger：

- Intent Trigger
- Task Type Trigger
- Keyword / Semantic Trigger
- Risk Trigger
- Change Trigger
- Failure Trigger
- Scenario Trigger
- Explicit User Trigger
- System State Trigger

但：

> Trigger ≠ Execute。

正確流程：

    Trigger
        ↓
    Candidate Capability
        ↓
    Applicability Check
        ↓
    適用？
       ├─ YES → Execute
       └─ NO  → Reject

避免為了提高「使用率」而強迫套用不適用的系統。

---

## P0-12 Recall 規格

必須定義：

- 如何找到相關 Capability
- 如何找到相關 System
- 如何找到 CURRENT 資料
- 如何排除 RETIRED / HISTORICAL
- 如何處理多個候選能力
- 如何處理能力重疊
- 如何處理搜尋不到能力的情況

核心原則：

> 有能力 ≠ 找得到能力 ≠ 知道應該使用能力。

---

## P0-13 Context Selection / Assembly 規格

必須先定義 Context 的：

- 來源
- 優先級
- 新鮮度
- 狀態
- 衝突處理
- 範圍
- 大小／預算
- 是否需要歷史
- 是否需要外部研究

最低原則：

    當前需求
        ↓
    CURRENT 規格
        ↓
    已驗證 Capability
        ↓
    相關歷史
        ↓
    外部參考

不得讓：

- 舊版本
- 草案
- 已廢棄規格
- 當前規格
- 外部參考

無差別混入 Context。

---

## P0-14 Response Contract

先定義每種工作要求 AI 產出的最低結果：

- 要回答什麼
- 要使用哪些資料
- 是否需要 Evidence
- 是否需要 Verification
- 是否需要保存
- 是否產生 Change Signal

目的：

> 讓工作邊界先固定，再決定需要哪些能力。

---

## P0-15 Verification 規格

Verification 不等於「每件事都做完整測試」。

應採 Risk-driven Verification。

基本模型：

    Goal
      ↓
    Minimum Sufficient Test
      ↓
    Result
      ↓
    Uncertainty
      ↓
    若仍影響決策 → Additional Test
      ↓
    否則 → Stop

目標：

> 用最小充分驗證取得足以支持決策的證據，而不是無限測試。

---

# 六、P1：既有資產 Mapping【高優先】

核心規格凍結後，才進行大量 Mapping。

目前：

- A1–A12：12/12 確認
- B1–B16：16/16 確認
- C1–C18：18/18 確認
- D1–D20：20/20 確認
- K01–K06：6/6 確認
- S01–S10：已確認為 Scenario

目前未知：

- K07–K61：缺乏權威現行定義
- S11–S37：缺乏權威現行定義

未知項目：

> 不得猜測補完。

Mapping 是 Derived View，不是 Canonical Source。

若 Mapping 與正式來源衝突：

    Mapping
       ↓
    回到 Canonical Source
       ↓
    修復來源
       ↓
    再更新 Mapping

---

# 七、P1：Scenario / Test Corpus / Evaluation

## P1-01 Scenario

Scenario 用來描述：

> 在什麼實際工作情境下測試某項 Capability。

目前已確認的歷史 Scenario：

- S01–S10
- 未來正式 Namespace：SCN-01–SCN-10

S11–S37 暫不猜測。

---

## P1-02 Test Corpus

每個重要 Capability 若要進行 Provider 比較，應逐步建立固定 Test Corpus。

基本結構：

    Scenario
        +
    Test Corpus
        +
    Provider
        ↓
    Execution
        ↓
    Result
        ↓
    Evidence
        ↓
    Evaluation

目的：

> 讓「新 Provider 是否更好」具有可重複比較的基準。

---

## P1-03 Evaluation

Evaluation 至少應比較：

- 是否完成目標
- 正確性
- 完整性
- 穩定性
- 成本
- 時間
- Context 要求
- 人工介入程度
- 風險
- 可追溯性

但不要預設所有項目都必須同時量化。

採：

> Goal → Minimum Sufficient Test → Result → Uncertainty → Stop

---

# 八、P2：Capability Evolution

當 Capability Mapping、Scenario、Test Corpus、Evaluation 開始具有實際證據後，才進入：

## P2-01 Capability Delta

比較：

    Current Provider
        vs
    Candidate Provider

產生：

- 新增能力
- 能力提升
- 能力下降
- 能力重疊
- 部分取代
- 完全取代
- 新的風險
- 新的成本
- 新的依賴

---

## P2-02 Overlap Analysis

比較 Capability 時，不得只看名稱。

至少比較：

- Purpose
- Input
- Output
- Trigger
- Responsibility
- State
- Data
- User / Role
- Dependency
- Verification

重要原則：

> Duplicate ≠ Redundant。

只有沒有合理責任區隔的重複能力，才可能構成真正的結構性冗餘。

---

## P2-03 Partial Replacement

取代不是二元事件。

可能出現：

    GPT
      ↓
    覆蓋 70%
    
    System
      ↓
    保留 30%

因此應支援：

- Full Replacement
- Partial Replacement
- Provider Combination
- Capability Extension

---

# 九、P2：Migration / Distillation / Refactoring

只有 Capability Delta 和 Evaluation 顯示有必要，才啟動。

大型變更流程：

    Proposal
        ↓
    Impact Analysis
        ↓
    Migration Design
        ↓
    Validation Plan
        ↓
    Approval
        ↓
    Implementation
        ↓
    Verification
        ↓
    Cutover
        ↓
    Observation
        ↓
    Regression / Recovery（必要時）
        ↓
    Final Adoption
        ↓
    Archive

Migration 期間可以暫時並行：

- CURRENT
- Candidate
- Validation Path
- Recovery Path

不得在未驗證前直接覆蓋 CURRENT。

---

# 十、P3：Registry / Graph / Automation【後置】

這些是實體化工具，不是前置規格。

## P3-01 Capability Registry

目前應先完成 Mapping。

只有當：

- Capability 數量增加
- 查找開始困難
- 人工管理產生重複成本
- Trigger / Recall 開始需要結構化支援

才考慮建立正式 Registry。

---

## P3-02 Capability Graph

只有當：

- Relationship 數量與複雜度真的增加
- 單純文件 Mapping 已無法有效理解關係
- 實際工作證明 Graph 能解決問題

才實體化。

---

## P3-03 Automation

Automation 的原則：

    人工流程
        ↓
    實際使用
        ↓
    重複工作
        ↓
    發現穩定模式
        ↓
    驗證值得自動化
        ↓
    Automation

不得：

> 因為藍圖寫了 Automation，就先建立 Automation。

---

## P3-04 Orchestration

Orchestration 是最後階段。

只有當：

- 多個 Capability 已穩定
- Trigger 已穩定
- Context 規則已穩定
- Provider Selection 已穩定
- Verification 已穩定
- 人工串接已反覆產生成本

才考慮自動編排。

---

# 十一、管理系統的核心問題：避免「系統存在但沒有被使用」

這是未來藍圖目前最重要的實際風險。

必須區分：

    Capability Exists
        ↓
    Capability Discoverable
        ↓
    Capability Applicable
        ↓
    Capability Triggered
        ↓
    Context Loaded
        ↓
    Provider Selected
        ↓
    Capability Executed
        ↓
    Result Verified

任何一層失敗，都可能造成：

> 系統已建立，但實際生成效果沒有改善。

因此未來驗證不能只問：

> 「系統有沒有建立？」

而必須問：

> 「實際工作時，系統是否在正確的情況下被正確召回、載入與使用？」

---

# 十二、Real Work 是最終驗證入口

未來藍圖不得自己製造大量 FIELD 案例。

正確流程：

    Real Work
        ↓
    Observation
        ↓
    Change Signal
        ↓
    Capability Delta
        ↓
    Impact
        ↓
    Evaluation
        ↓
    Evolution

FIELD 應由自然工作產生。

目前：

> FIELD 等待自然工作觸發，不應為了「完成藍圖」而人為製造。

---

# 十三、新 System 的建立條件

任何未來新增 System 都應經過：

    實際使用
        ↓
    Observation
        ↓
    重複瓶頸
        ↓
    結構性問題確認
        ↓
    驗證需要系統化
        ↓
    System Proposal
        ↓
    Implementation
        ↓
    Validation

因此：

> Mapping ≠ Registry  
> Registry ≠ Graph  
> Graph ≠ Orchestrator

也就是：

> 先理解 → 先 Mapping → 先比較 → 先測試 → 確認真的需要 → 才實體化。

---

# 十四、完整待辦順序

## Phase 0：規格凍結

- [ ] P0-01 核心物件模型
- [ ] P0-02 Namespace
- [ ] P0-03 Capability 標準
- [ ] P0-04 Provider
- [ ] P0-05 State / Version / Git Commit
- [ ] P0-06 Lifecycle
- [ ] P0-07 Relationship
- [ ] P0-08 Change / Evolution
- [ ] P0-09 Failure Closure
- [ ] P0-10 Disposition

完成後：

> 後續文件不得任意修改上述基礎語意；若發現重大問題，必須透過正式規格變更處理。

---

## Phase 1：AI 工作管理

- [ ] P0-11 Trigger
- [ ] P0-12 Recall
- [ ] P0-13 Context Selection / Assembly
- [ ] P0-14 Response Contract
- [ ] P0-15 Verification

完成後應能回答：

> 「使用者提出一個工作需求時，AI 如何知道需要哪些知識、Capability、System、Provider，以及什麼時候必須驗證？」

---

## Phase 2：既有資產翻譯

- [ ] A/B/C/D → Capability Mapping
- [ ] K01–K06 → Capability / Knowledge Mapping
- [ ] S01–S10 → Scenario Mapping
- [ ] 恢復 K07–K61 的權威定義
- [ ] 恢復 S11–S37 的權威定義
- [ ] 檢查 Mapping 與 Canonical Source 一致性

注意：

> K07–K61、S11–S37 未取得權威來源前保持未知，不猜測。

---

## Phase 3：Evaluation 基礎

- [ ] 建立第一批真實 Scenario
- [ ] 建立必要 Test Corpus
- [ ] 定義 Minimum Sufficient Test
- [ ] 執行第一批 Provider Comparison
- [ ] 建立 Evidence
- [ ] 記錄不確定性
- [ ] 驗證 Stop Condition

---

## Phase 4：Real Work

- [ ] 等待自然工作觸發
- [ ] 觀察 Trigger 是否成功
- [ ] 觀察 Recall 是否成功
- [ ] 觀察 Context 是否正確
- [ ] 觀察 Capability 是否真的被使用
- [ ] 觀察 Verification 是否足夠
- [ ] 記錄失敗閉環
- [ ] 產生 Change Signal

這一階段不能為了「完成待辦」而虛構案例。

---

## Phase 5：Capability Evolution

- [ ] Capability Delta
- [ ] Overlap Analysis
- [ ] Provider Comparison
- [ ] Partial Replacement
- [ ] Full Replacement
- [ ] Extension
- [ ] Refactor
- [ ] Merge / Split
- [ ] Migration

---

## Phase 6：必要時實體化管理系統

只有實際工作證明需要，才依序考慮：

- [ ] Capability Registry
- [ ] Trigger Registry
- [ ] Capability Graph
- [ ] Evaluation Engine
- [ ] Automation
- [ ] Orchestration

不要求全部建立。

---

# 十五、目前不應做的事情

以下事項目前不應因為「未來藍圖完整」而提前執行：

1. 不建立第五套正式方案。
2. 不新增 A13/B17/C19/D21。
3. 不重新驗收四方案。
4. 不猜測 K07–K61。
5. 不猜測 S11–S37。
6. 不因 Mapping 完成就建立 Registry。
7. 不因 Registry 概念存在就建立 Graph。
8. 不因 Graph 概念存在就建立 Orchestration。
9. 不人為製造 FIELD。
10. 不把模型更新視為唯一 Evolution Trigger。
11. 不把 Capability 名稱當作實際能力證明。
12. 不把文件存在當成 Real-Work Validation。
13. 不把 Provider Replacement 等同於 System Replacement。
14. 不把 Capability Evaluation 變成無限測試。
15. 不為了增加功能數量而增加系統。

---

# 十六、最重要的工程判斷

未來藍圖目前最大的風險，不是「系統太少」。

真正風險是：

> **規格尚未凍結，就開始大量建立後續系統。**

第二個風險是：

> **Capability 已建立，但 Trigger / Recall / Context 沒有建立，因此 AI 實際工作時根本沒有使用它。**

第三個風險是：

> **把藍圖上的概念直接實體化，導致管理成本超過實際工作收益。**

因此優先順序必須固定為：

    先理解
      ↓
    先凍結規格
      ↓
    先定義工作循環
      ↓
    先定義 Trigger / Recall / Context
      ↓
    先 Mapping
      ↓
    先實際使用
      ↓
    再 Evaluation
      ↓
    再觀察瓶頸
      ↓
    確認真的需要
      ↓
    才實體化 System

---

# 十七、完成判定

「未來藍圖完成」不代表所有待辦都打勾。

應分成：

### 規格完成

核心規格、物件、Namespace、Lifecycle、State、Relationship、Trigger、Context、Verification 已凍結。

### Mapping 完成

現有已知資產已被正確翻譯；未知資料保持 UNKNOWN，不猜測。

### 工作循環完成

AI 能在實際工作中：

    Intent
    → Capability Discovery
    → Trigger / Recall
    → Context
    → Provider
    → Execution
    → Verification

### Real-Work Validated

實際工作已證明該流程有效。

### Systemization Needed

只有當實際工作產生重複且結構性的瓶頸，才將人工流程實體化成 System。

因此：

> 「待辦全部完成」不是目標。

真正目標是：

> **建立最低有效的工作循環，並讓真實工作決定下一個需要被工程化的部分。**

---

# 十八、與前三份未來藍圖文件的關係

本文件是未來藍圖的第四份文件。

建議四份文件分工如下：

1. 《AI單人工作室功能導向藍圖交接入口》
   - 交接入口
   - 如何理解未來藍圖
   - 目前狀態
   - 閱讀順序

2. 《AI單人工作室功能導向藍圖地圖-既有資產完整Mapping》
   - 現有資產與未來能力的 Mapping
   - A/B/C/D/K/S 對照
   - Namespace 對照
   - 已知／未知狀態

3. 《AI單人工作室未來藍圖規劃書-功能導向架構》
   - 未來完整能力架構
   - Capability-centric 設計
   - Provider
   - Scenario
   - Evaluation
   - Evolution
   - Migration
   - Distillation
   - 長期架構原則

4. 《AI單人工作室未來藍圖待辦清單》
   - 建設先後順序
   - P0/P1/P2/P3 優先級
   - 規格凍結項目
   - 工作管理與 Trigger / Recall / Context
   - 實際工作驗證
   - 後續 System 實體化條件
   - 明確禁止提前做的事項

四份文件不是四套系統。

它們共同描述同一個「功能導向藍圖」。

---

# 十九、最終核心原則

> **規格先於資料。**
>
> **工作循環先於管理系統。**
>
> **Trigger / Recall / Context 先於 Capability Automation。**
>
> **Mapping 先於 Registry。**
>
> **Evaluation 先於 Replacement。**
>
> **Real Work 先於 Automation。**
>
> **瓶頸先於新系統。**
>
> **證據先於結論。**
>
> **需要才實體化。**

未來藍圖的目的不是建立最多系統，而是讓 AI 單人工作室在模型、工具、資料與工作方式持續變動的情況下，仍能知道：

> 現在要做什麼、應該使用什麼、為什麼使用、使用後是否有效、如果無效問題在哪裡，以及下一步到底值不值得把它工程化。
