# AI 單人工作室未來藍圖規劃書
## 功能導向（Function-Oriented）架構與能力演化藍圖 v1.0

> 文件性質：未來整體藍圖／長期規劃書  
> 文件狀態：【未來規劃／待實體化】  
> 適用環境：目前無 API；GPT／ChatGPT + GitHub  
> 架構關係：本文件不是第五方案，不取代現行四大方案  
> 核心目的：建立一套能隨 GPT、工具、知識與工作方法持續進化，並能快速判斷「新增、重疊、取代、精簡、合併、淘汰」的功能導向架構。

---

# 【置頂硬規範】功能「存在／完成」判定標準

本藍圖及其後續工程工作，**不得再以「規範、企劃書、設計文件、Mapping、流程文件已建立」直接判定一項方案、系統或功能已存在或完成。**

## 一、核心原則

> **文件存在 ≠ 知識存在 ≠ 系統存在 ≠ 運行方案存在 ≠ 實際執行 ≠ 驗證完成。**

一項功能若要宣稱「已存在／已完成」，必須檢查完整功能鏈：

```
Knowledge / 知識
        ↓
Specification / 規格
        ↓
System / Tool / 實際承載機制
        ↓
Operation / 運行方案
        ↓
Execution / 實際執行
        ↓
Evidence / 執行證據
        ↓
Validation / 驗證
```

缺少其中必要環節時，不得把較前面的文件或設計成果直接升格為完整方案。

## 二、各層級的正確語義

- **Knowledge／知識**：AI 實際需要知道的原理、定義、判定方法與經驗。
- **Specification／規格**：規定應該如何工作的規則、要求與設計。
- **System／Tool／系統或工具**：實際承載功能、可以被操作或執行的機制。
- **Operation／運行方案**：明確說明如何啟動、輸入什麼、依什麼流程運行、輸出什麼、遇到例外如何處理、完成後如何收尾。
- **Execution／實際執行**：該功能真的被使用，而不是僅存在於文件。
- **Evidence／證據**：留下實際執行結果、案例、紀錄或可追溯成果。
- **Validation／驗證**：根據明確驗收條件確認結果有效。

## 三、不得混淆的典型情況

以下均**不能單獨宣稱方案／系統完成**：

```
規範文件已建立
→ 只能證明 Specification 存在

企劃書已建立
→ 只能證明 Planning / Design 存在

流程圖已建立
→ 只能證明 Process Design 存在

Capability Mapping 已建立
→ 只能證明 Mapping / Derived View 存在

Knowledge 文件已建立
→ 不自動證明 Knowledge Capability 已可運行

System 文件已建立
→ 不自動證明 System 已實作

模擬通過
→ 只能證明 Simulation-Validated
→ 不等於 Real-Work-Validated

曾經執行
→ 不自動等於已驗證
```

## 四、完成度必須分層

除非有證據支持，不得將下列狀態混為一談：

```
DESIGNED
↓
DOCUMENTED / DEFINED
↓
BUILT / AVAILABLE
↓
EXECUTED / USED
↓
SIMULATION-VALIDATED
↓
REAL-WORK-VALIDATED
↓
CURRENT
```

其中：

- **DESIGNED**：已設計。
- **DOCUMENTED / DEFINED**：已有明確知識或規格定義。
- **BUILT / AVAILABLE**：實際承載機制已建立並可使用。
- **EXECUTED / USED**：已實際運行。
- **SIMULATION-VALIDATED**：通過模擬／回歸驗證。
- **REAL-WORK-VALIDATED**：通過自然工作中的真實使用驗證。
- **CURRENT**：目前正式採用中的有效狀態。

**BUILT 不得只因文件存在、Mapping 完成或企劃完成而成立。**

## 五、方案存在的最低判定

若使用「方案已存在／系統已存在／功能已完成」等工程語句，至少必須能回答：

1. 知識在哪裡？
2. 實際系統／工具／承載機制在哪裡？
3. 運行方案在哪裡？
4. 如何啟動？
5. 輸入與輸出是什麼？
6. 實際跑過嗎？
7. 證據在哪裡？
8. 如何驗證？
9. 目前處於什麼 Lifecycle State？

若無法回答，應使用較低階、精確的狀態，例如：

- 規格已建立
- 企劃已建立
- 設計完成
- Mapping 已建立
- Candidate
- 待實體化
- 待實際運行
- 待驗證

不得直接寫成「系統已完成」或「方案已存在」。

## 六、運行方案是必要工程資產

任何準備從「規格／設計」進入「可運行」的功能，都必須有對應的 **Operation / 運行方案**。

運行方案至少說明：

```
Trigger / 觸發
↓
Input / 輸入
↓
Context / 必要上下文
↓
Process / 執行流程
↓
Tool / System / Provider
↓
Output / 輸出
↓
Exception / 例外處理
↓
Verification / 驗證
↓
Evidence / 證據
↓
State Update / 狀態更新
```

沒有這條鏈時，不能因為「已經寫好怎麼做」就宣稱功能已具備實際運行能力。

## 七、Mapping 與 Blueprint 的特殊規則

**Mapping 是 Derived View，不是自動實體化的 System。**

**Blueprint 是未來架構與規劃，不是目前已實作系統。**

因此：

```
Blueprint 完成
≠ System 完成

Mapping 完成
≠ Capability System 完成

Capability 定義完成
≠ Capability Provider 已建立

規範完成
≠ 功能完成
```

## 八、後續所有藍圖進度盤點必須遵守

未來檢查 Phase、BUILT、完成率或工程進度時，必須以：

> **實際功能鏈與 Evidence**

而不是文件數量作為判定基礎。

若某項目目前只有規範、企劃、設計或 Mapping，應明確標示其實際層級，不得為了進度統計將其算入完整功能完成。

---

# 一、文件定位

本文件是目前「AI 單人工作室整體系統企劃書」之後的未來藍圖。

它不是立即施工規格，也不是現行 Repository 的狀態文件。

它的用途是回答一個長期問題：

> 當 GPT、其他模型、工具與我們自己的系統持續變強時，如何知道哪些功能仍然值得保留，哪些功能已經重疊，哪些可以被原生模型取代，以及哪些系統應該被精簡或重構？

前期企劃已經確立：

- GPT 是主要智慧與推理核心。
- GitHub 是長期外部記憶與版本控制中心。
- 知識、系統、方案、規則、證據、歷史具有不同責任。
- CURRENT 與 HISTORY 必須分離。
- 大型 Repository 不代表每次任務都應載入大型 Context。
- 四大方案是正式工程治理架構，不增加第五方案。
- 無 API 階段不預先建立不必要的 Agent Runtime、Vector DB、Event Bus、Scheduler 等基礎設施。
- 新能力必須透過實際使用、Observation、測試與驗證後，才正式進入架構。

本藍圖在上述基礎上增加一個核心觀念：

> **Capability（能力）是未來比較、測試、重疊分析與系統演化的基本功能單位。**

---

# 二、為什麼需要重新建立功能導向架構

傳統文件式架構容易以：

- 文件名稱
- 系統名稱
- 資料夾
- 版本
- 方案名稱

作為管理單位。

長期運作後容易發生：

1. 不同系統其實提供相同功能。
2. 同一功能被不同方案重複建立。
3. GPT 原生能力提升後，舊系統仍然存在。
4. 舊系統沒有被刪除，但也沒有人知道為什麼保留。
5. 新模型更新時，只能重新閱讀大量文件判斷影響。
6. 大型格式變更時，新舊格式長期混存。
7. 文件數量增加後，Context 成本上升。
8. 系統責任逐漸漂移。
9. 新增一個「管理系統」反而增加管理成本。

因此未來不應只問：

> 「我們有哪些系統？」

還必須問：

> 「我們有哪些 Capability？每個 Capability 目前由誰提供？是否重複？是否有測試？是否仍有必要實體化？」

---

# 三、核心模型

未來架構不採用「Knowledge → Capability → System → Plan → Task」的強制線性 Pipeline。

這些是不同的資料／責任實體，彼此可以存在多種關係：

```
Knowledge / 知識
   │ 定義、證據、支撐
   ↓
Capability / 能力 ←── Provider（GPT／System／Tool／Human）
   │
   ├── 被 System 組合與實體化
   ├── 被 Plan 使用／調度
   └── 可直接支援 Task

Plan / 方案 ──調度／組合──→ Capability / System
Task / 任務 ──執行需求──→ Plan / Capability / System
```

箭頭表示可能的「定義／支撐／使用／提供／調度」關係，不表示每個任務都必須依序經過所有節點。

四者不可互相取代。

## Knowledge

回答：

> 我們知道什麼？

例如：

- 某個技術的定義。
- 某個研究結果。
- 某個專案規則。
- 某次測試發現。
- 某個歷史決策的依據。

## Capability

回答：

> 我們能做什麼？

例如：

- 搜尋。
- 分類。
- 比較。
- 決策。
- 規劃。
- 驗證。
- 蒸餾。
- 交接。

## System

回答：

> 如何把一組 Capability 組合成可以重複運作的功能？

## Plan

回答：

> 面對一個具體問題，如何調度 Knowledge、Capability、System 與人工決策完成目標？

---

# 四、Capability 的正式定位

Capability 是：

> 可以被單獨描述、定位、測試、比較、觀察與替換的功能單位。

Capability 不等於一個文件，也不等於一個 System。

例如：

```
CAP-DEC-005
下一步決策
```

可以由：

- GPT
- 決策系統
- 其他模型
- 人工
- Tool

提供。

因此：

> Capability 是功能本身；Provider 是提供功能的方法。

這使模型更新時不必重新設計整套架構。

只需要分析：

```
Model Update
↓
Capability Delta
↓
受影響 Capability
↓
受影響 System
↓
受影響 Plan
```

---

# 五、Capability 的標準資料

正式 Capability 原則上應具有：

```
Capability ID
名稱
功能定義
分類
輸入
輸出
適用情境
限制
依賴 Knowledge
依賴 Capability
提供 System
提供 Model
提供 Tool
Provider 狀態
測試集
測試結果
Evidence
版本
Lifecycle
最後評估日期
替代候選
重疊候選
```

目前不要求一次把全部欄位制度化。

應先建立真正需要的最小結構，再由實際使用增加欄位。

---

# 六、Capability 的功能分類

初步建立以下功能分類。

## 6.1 理解能力

- 問題理解
- Intent Recognition
- Context Understanding
- 需求解析
- 分類
- 抽象化

## 6.2 探索能力

- Search
- Discovery
- Retrieval
- Source Finding
- Cross-domain Search

## 6.3 知識能力

- Knowledge Creation
- Knowledge Update
- Knowledge Integration
- Knowledge Linking
- Conflict Detection
- Knowledge Status
- Knowledge Distillation

## 6.4 記憶能力

- Memory
- Long-term Memory
- Project Memory
- Historical Recall
- Handoff Recovery

## 6.5 規劃能力

- Decomposition
- Planning
- Blueprint
- Dependency Analysis
- Risk Analysis
- Priority
- Execution Order

## 6.6 決策能力

- Candidate Generation
- Comparison
- Constraint Checking
- Risk Evaluation
- Selection
- Next Action

## 6.7 執行能力

- Repository Operation
- File Creation
- File Modification
- Tool Invocation
- Research Execution
- Task Execution

## 6.8 驗證能力

- Result Verification
- Source Verification
- Consistency Check
- Regression
- Stress Test
- Architecture Health Check

## 6.9 治理能力

- Permission
- Change Control
- Canonical Source
- Version Control
- State Control
- Decision Recording

## 6.10 演化能力

- Observation
- Impact Analysis
- Overlap Detection
- Replacement Detection
- Pruning
- Distillation
- Refactoring
- Deprecation
- Archive

## 6.11 交接能力

- State Recovery
- Architecture Recovery
- Decision Recovery
- Current State Recovery
- Next Step Recovery
- Memoryless Handoff

這些是功能分類，不是新的方案。

---

# 七、Atomic Repository 原則

前期架構已提出 Atomic Repository。

未來應將 Atomic 理解為：

> 可獨立理解、引用、驗證與更新的最小充分語義單位。

不是：

> 越小越好。

可以存在：

```
Knowledge Atom
Capability Atom
Rule Atom
Decision Atom
Evidence Atom
```

然後再組合成：

```
System
Plan
Project
```

Atomic 的目的，是讓大型架構可以進行局部修改，而不是每次都重寫整份文件。

---

# 八、既有 K01–K61 / S01–S37 的處理方式

既有功能盤點不應直接變成：

```
61 個 Knowledge System
+
37 個 System
```

這會造成過度實體化。

正確流程：

```
K01–K61
↓
功能語義整理
↓
重複分析
↓
Capability Mapping
↓
真正需要的 Knowledge
```

以及：

```
S01–S37
↓
功能語義整理
↓
責任重疊分析
↓
Capability Mapping
↓
真正需要的 System
```

因此：

> 舊功能編號是盤點資產，不是要求未來一對一建立系統的命令。

---

# 九、四方案 A/B/C/D 的關係

目前正式工程架構仍然只有四方案：

1. 方案一：整體資料治理。
2. 方案二：AI 知識管理。
3. 方案三：知識與資料迭代演化。
4. 方案四：能力蒸餾與系統重構。

本藍圖不增加第五方案。

Capability 是四方案共同使用的「功能描述與評估單位」。

可理解為：

```
方案一
管理資料身份、狀態、版本、Canonical Source、Archive

方案二
管理 Knowledge、Memory、Library、Retrieval、Context、Handoff

方案三
管理 Observation、外部變化、Model Update、Capability Delta、Evaluation

方案四
管理 Pruning、Simplification、Merge、Replacement、Refactoring、Distillation
```

---

# 十、Capability Matrix

未來最重要的基礎資產之一是：

> Capability Matrix。

它回答：

> 每個能力目前由誰提供？

例如：

| Capability | GPT | System | Tool | Human | Eval | 狀態 |
|---|---|---|---|---|---|---|
| Intent | ✓ | | | | 有 | CURRENT |
| Search | ✓ | ✓ | ✓ | | 有 | CURRENT |
| Planning | ✓ | ✓ | | ✓ | 有 | CURRENT |
| Decision | ✓ | ✓ | | ✓ | 有 | REVIEW |
| Verification | ✓ | ✓ | | ✓ | 有 | CURRENT |
| Memory | △ | ✓ | | ✓ | 有 | CURRENT |
| Distillation | ✓ | ✓ | | ✓ | 有 | CURRENT |

這不是最終表格格式，而是未來功能管理的核心概念。

---

# 十一、Model Profile

每一個重要模型版本都應有：

> Model Capability Profile。

至少記錄：

- 模型名稱。
- 版本。
- 官方能力。
- 官方限制。
- Relevant Capability。
- 我們自己的測試結果。
- 受影響 System。
- 受影響 Plan。
- 已知替代能力。
- 評估日期。

必須區分：

```
官方宣稱能力
≠
我們實際工作中的能力
```

官方資料只能產生「候選影響」。

是否真的可以取代現有系統，必須由我們自己的 Evaluation 決定。

---

# 十二、Model Update 的標準流程

未來每次重要模型更新，不再只寫一份「更新了什麼」。

標準流程：

```
① Model Update Report
        ↓
② Model Capability Profile
        ↓
③ Capability Delta
        ↓
④ Mapping 到現有 Capability
        ↓
⑤ Overlap Detection
        ↓
⑥ 找受影響 System
        ↓
⑦ 找受影響 Plan
        ↓
⑧ 啟動相關 Eval
        ↓
⑨ A/B Test
        ↓
⑩ Decision
        ↓
⑪ Refactoring
        ↓
⑫ Regression
        ↓
⑬ Evidence
        ↓
⑭ Distillation
```

只有真正受到影響的能力才需要進入深度測試。

---

# 十三、功能重疊偵測

當：

```
GPT
提供 CAP-A

SYS-001
也提供 CAP-A
```

不能直接判斷：

> System 已經沒用了。

應先建立：

```
OVERLAP-CANDIDATE
```

再比較：

- 正確性。
- 一致性。
- 穩定性。
- 特殊案例。
- Context 成本。
- 時間成本。
- 維護成本。
- 系統複雜度。
- 依賴數量。
- 使用頻率。

---

# 十四、功能取代測試

以「決策系統」為例。

建立：

### A 組

```
GPT Only
沒有外部決策系統
```

### B 組

```
GPT
+
完整決策系統
```

### C 組

```
GPT
+
精簡決策系統
```

固定使用同一組測試案例。

比較：

```
正確率
穩定性
漏判
錯判
完整性
決策品質
Context 成本
執行時間
維護成本
```

這樣才可以回答：

> 「決策系統是否仍有保留必要？」

而不是依靠主觀感覺。

---

# 十五、功能存廢的正式結果

測試後不只存在「保留／刪除」。

至少：

```
RETAIN
保留

SIMPLIFY
精簡

MERGE
合併

REPLACE
取代

DEPRECATE
棄用

REMOVE
移除

HOLD
暫不決定
```

其中：

> REMOVE 不等於刪除歷史。

而是：

```
CURRENT
↓
退出 CURRENT
↓
ARCHIVE / HISTORY
```

---

# 十六、Capability-Driven Pruning

未來系統清理不應以：

> 文件很久沒修改。

作為主要判斷。

而應以：

```
Capability
↓
實際使用
↓
Observation
↓
價值
↓
重疊
↓
維護成本
↓
Pruning Candidate
```

判斷。

因此：

> 文件存在時間不是淘汰依據；能力價值才是。

---

# 十七、Activity 與 Observation

系統必須區分：

## Activity

記錄：

> 發生了什麼。

例如：

- 某 Capability 被使用。
- 某 System 被呼叫。
- 某測試被執行。

## Observation

記錄：

> 使用後發現了什麼。

例如：

```
使用決策系統 20 次。

18 次 GPT 原生能力已能完成。
2 次外部系統提供額外價值。

額外價值主要集中在：
高約束、多候選、資訊衝突案例。
```

這才是後續重構的依據。

---

# 十八、Impact Analysis

修改一個 Capability 時，不應掃描整個 Repository。

應使用關係追蹤：

```
Capability
↓
System
↓
Plan
↓
Task
↓
Evaluation
↓
Evidence
```

只驗證真正受影響的範圍。

這是大型 Repository 長期可維護的重要條件。

---

# 十九、Intent 與 Response Contract

使用者說：

> 「決策系統是不是可以不要？」

真正的任務不是簡單的：

```
keyword = 決策
```

而應理解：

```
Intent = REVIEW
Target = Decision System
Purpose = Redundancy / Replacement Evaluation
Action = EVALUATE
```

同時建立 Response Contract：

- 是否需要研究？
- 是否讀 Repository？
- 是否搜尋外部資料？
- 是否允許修改？
- 是否需要測試？
- 是否需要建立正式文件？

---

# 二十、Trigger

Trigger 只負責：

> 找出可能相關的 Capability / System / Plan。

Trigger 不是自動執行器。

流程：

```
Input
↓
Intent
↓
Context
↓
Trigger Candidate
↓
Capability Selection
↓
Execution
```

而不是：

```
看到關鍵字
↓
直接執行
```

---

# 二十一、Orchestration

統御核心負責：

- 理解目前目標。
- 取得必要 Context。
- 判斷需要哪些 Capability。
- 選擇 Provider。
- 調度工作。
- 決定是否需要 Blueprint。
- 決定是否需要 Verification。
- 將結果送入 Evidence / Observation。

統御核心不是：

> 一個巨大知識庫。

也不是：

> 所有業務邏輯的集中地。

它是薄型 Control / Orchestration Layer。

---

# 二十二、Blueprint

Blueprint 依任務規模使用。

### 小型任務

直接執行。

### 中型任務

簡單 Plan。

### 大型任務

完整 Blueprint：

```
Goal
↓
Decomposition
↓
Scope
↓
Dependencies
↓
Risks
↓
Priority
↓
Execution Order
↓
Verification
```

Blueprint 本身是一項 Capability，不代表每次任務都必須建立 Blueprint。

---

# 二十三、Knowledge / Library / Capability 三者不能混淆

這是未來最容易再次發生的架構錯誤之一。

```
Knowledge
=
知道什麼

Library
=
去哪裡找

Capability
=
找到之後能做什麼
```

例如：

```
Library 找到「決策理論」

Knowledge 提供「決策理論內容」

Capability 執行「方案比較」

System 組合多項 Capability

Plan 決定本次專案如何使用它們
```

---

# 二十四、System Graph

未來不應只使用資料夾樹。

應建立概念上的 System Graph：

```
System A
 ├─ CAP-001
 ├─ CAP-002
 └─ CAP-003

System B
 ├─ CAP-002
 ├─ CAP-003
 └─ CAP-004
```

因此：

```
CAP-002
CAP-003
```

會直接顯示為重疊能力。

這比：

```
系統 A.md
系統 B.md
```

更容易進行架構演化。

---

# 二十五、Canonical Source

未來仍然維持：

> 一項事實可以有很多 Derived View，但必須知道哪裡是 Canonical Source。

例如：

```
Capability Definition
↓
Canonical Source

Index
Summary
Handoff
Model Report
System Registry
Search View
↓
Derived View
```

這樣可以避免：

> 同一個 Capability 在五份文件中各寫一套版本。

---

# 二十六、CURRENT / ARCHIVE

未來架構必須明確區分：

```
CURRENT
目前正式有效資料

ARCHIVE / HISTORY
完整歷史資料
```

歷史資料：

- 不刪除。
- 不作為預設 Context。
- 不應被 AI 誤認為 CURRENT。
- 可在驗證、研究、回溯與決策時重新讀取。

核心原則：

> 完整歷史，乾淨現在。

---

# 二十七、大型格式更新

當核心格式發生重大變更時，不應長期維持：

```
舊格式
+
新格式
+
半轉換格式
+
相容層
```

而應：

```
舊格式
↓
Migration / Distillation
↓
新 Canonical Format
↓
驗證
↓
正式切換
↓
舊格式 Archive
```

這是大型系統更新的正式策略。

---

# 二十八、職權模型

## 使用者

負責：

- 方向。
- 需求。
- 重大取捨。
- 高風險判斷。
- 正式採用。
- 重大架構決策。

## GPT

負責：

- 理解。
- 研究。
- 分析。
- 規劃。
- 執行。
- 驗證。
- 建議重構。
- 建立證據。
- 交接。

## GitHub

負責：

- 長期保存。
- Version Control。
- Canonical Source。
- History。
- Evidence。
- Current State。
- Handoff。

因此：

> GPT 可以提出「移除決策系統」，但重大正式變更仍需依照既定 Change Control。

---

# 二十九、Change Control

重大變更：

```
Proposal
↓
Impact Analysis
↓
Research
↓
Evaluation
↓
Decision
↓
Approval
↓
Implementation
↓
Regression
↓
Evidence
↓
Archive
```

研究結果不直接等於正式採用。

---

# 三十、Verification

至少三層：

## Result Verification

結果是否正確。

## Behavior Verification

系統是否按照預期工作。

## Architecture Verification

是否造成：

- 重複。
- 衝突。
- 責任漂移。
- 依賴錯誤。
- Context 膨脹。
- 版本漂移。
- 入口漂移。

---

# 三十一、四大方案的功能導向化

## 方案一：整體資料治理

功能重點：

- Data Identity
- Lifecycle
- State
- Version
- Canonical Source
- Change Control
- Archive
- Impact Metadata

## 方案二：AI 知識管理

功能重點：

- Knowledge
- Memory
- Library
- Retrieval
- Context
- Handoff
- Knowledge Relation

## 方案三：知識與資料迭代演化

功能重點：

- Observation
- Activity
- Model Update
- Capability Delta
- External Research
- Overlap Detection
- Evaluation
- Impact Analysis

## 方案四：能力蒸餾與系統重構

功能重點：

- Pruning
- Simplification
- Merge
- Replacement
- Refactoring
- Distillation
- CURRENT 重建
- Archive

---

# 三十二、與既有 A1–A12 / B1–B16 / C1–C18 / D1–D20 的關係

四方案既有功能編號是正式工程資產。

未來不直接推翻。

新增一層：

```
A/B/C/D 功能
↓
Capability Mapping
```

目的：

1. 發現跨方案重複。
2. 找出真正共用的 Capability。
3. 找出只有歷史原因才存在的重複功能。
4. 找出可以抽成共用能力的部分。
5. 找出已經由 GPT 原生能力取代的部分。
6. 找出仍需要正式 System 的部分。

因此：

> Capability Mapping 是下一階段整體重構的重要入口。

---

# 三十三、Memoryless Handoff 驗收

功能導向架構最後必須接受實際驗收：

> 沒有任何歷史記憶的新 GPT，能否只透過 CURRENT + Entry + 必要 Context 恢復工作？

至少要恢復：

- 專案目的。
- 架構。
- 四方案。
- 目前狀態。
- 正式規則。
- Capability。
- 重要 Decision。
- 禁止事項。
- 下一步。
- 必要 Evidence。

如果必須讀大量施工歷史才能理解 CURRENT：

> Context 架構仍然不合格。

---

# 三十四、Context Loading

標準載入層：

```
L0 Entry
↓
L1 Current
↓
L2 Current Task
↓
L3 Relevant Capability / System / Plan
↓
L4 Necessary Knowledge
↓
L5 Evidence / History
↓
L6 Cross-project
```

原則：

> 大記憶，小 Context。

---

# 三十五、Capability Evaluation

每個核心 Capability 都應逐步建立 Eval。

測試至少包括：

- 正常案例。
- 邊界案例。
- 資訊不足。
- 資訊衝突。
- 多方案。
- 高風險。
- 歷史資料干擾。
- 錯誤資訊。
- Context 不完整。

模型更新時，只重跑受到影響的 Eval。

---

# 三十六、Capability Evaluation 的 A/B 模式

基本比較：

```
A = GPT Only

B = GPT + System

C = GPT + 精簡 System
```

比較：

- Accuracy。
- Consistency。
- Completeness。
- Error Rate。
- Stability。
- Context Cost。
- Time Cost。
- Maintenance Cost。
- Complexity。
- Special-case coverage。

最後產生：

```
Decision
+
Evidence
```

而不是單純主觀評價。

---

# 三十七、為什麼這能解決「模型越來越強」的問題

傳統做法：

```
新模型
↓
重新設計系統
```

本架構：

```
新模型
↓
Model Profile
↓
Capability Delta
↓
Affected Capability
↓
Targeted Eval
↓
局部決策
```

因此模型能力提升不會自動造成整個 Repository 震盪。

---

# 三十八、為什麼也能解決「自己建立太多系統」的問題

未來新增一個系統前：

```
提出新 System
↓
列出提供的 Capability
↓
搜尋既有 Capability
↓
發現重疊？
↓
有
→ 先比較現有 Provider
↓
沒有
→ 才進入 System 建立
```

因此：

> Capability Registry 是防止系統膨脹的前置檢查。

---

# 三十九、能力生命週期

```
DISCOVERED
↓
CANDIDATE
↓
DEFINED
↓
TESTING
↓
CONFIRMED
↓
CURRENT
↓
OBSERVED
↓
OVERLAP
↓
REVIEW
↓
RETAIN / SIMPLIFY / MERGE / REPLACE
↓
DEPRECATED / RETIRED
↓
HISTORICAL
```

---

# 四十、System 生命週期

```
Proposal
↓
Candidate
↓
Confirmed
↓
Build
↓
Verify
↓
Current
↓
Use
↓
Observation
↓
Improvement
↓
Distillation / Refactoring
↓
Deprecated
↓
Archive
```

---

# 四十一、Knowledge 生命週期

```
Discover
↓
Research
↓
Verify
↓
Store
↓
Index
↓
Use
↓
Observation
↓
Update
↓
Supersede / Deprecate
↓
History
```

---

# 四十二、完整演化閉環

整個未來架構最後形成：

```
外部世界
│
├─ 新模型
├─ 新工具
├─ 新研究
└─ 實際工作
        ↓
Observation
        ↓
Capability Change
        ↓
Impact Analysis
        ↓
Overlap Detection
        ↓
Evaluation
        ↓
Decision
        ↓
┌───────┼────────┐
保留    精簡     合併
                  │
                  ↓
                取代
                  │
                  ↓
                淘汰
                  ↓
              Refactoring
                  ↓
              Regression
                  ↓
               Evidence
                  ↓
             Distillation
                  ↓
               CURRENT
                  ↓
               ARCHIVE
```

---

# 四十三、未來 Repository 的概念結構

實際目錄仍可依目前工程需求調整，但概念上至少存在：

```
/
├── 入口與狀態
├── 知識
├── 能力
├── 系統
├── 方案
├── 規則
├── 專案
├── 測試
├── 證據
├── 交接
├── 紀錄
└── Archive / History
```

這是概念藍圖，不要求現在立即按照此目錄全部建立。

---

# 四十四、哪些東西現在不應建立

在沒有實際瓶頸之前，不建立：

- Vector Database。
- Embedding Server。
- Memory Server。
- Agent Runtime。
- Multi-Agent Framework。
- Event Bus。
- Scheduler。
- Background Worker。
- 大型 Trigger Engine。
- 大型 Intent Engine。
- 自動 Orchestrator。
- 自動 Distillation。
- 複雜永久 Context Pipeline。

原則：

> 先證明瓶頸，再實體化解法。

---

# 四十五、未來 API 升級

API 版本可以增加：
