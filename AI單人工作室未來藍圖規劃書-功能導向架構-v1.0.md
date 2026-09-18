# AI 單人工作室未來藍圖規劃書
## 功能導向（Function-Oriented）架構與能力演化藍圖 v1.0

> 文件性質：未來整體藍圖／長期規劃書  
> 文件狀態：【未來規劃／待實體化】  
> 適用環境：目前無 API；GPT／ChatGPT + GitHub  
> 架構關係：本文件不是第五方案，不取代現行四大方案  
> 核心目的：建立一套能隨 GPT、工具、知識與工作方法持續進化，並能快速判斷「新增、重疊、取代、精簡、合併、淘汰」的功能導向架構。

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

未來架構採以下關係：

```
Knowledge
知道什麼
    ↓
Capability
能做什麼
    ↓
System
如何把能力實體化、組合與運作
    ↓
Plan
面對特定問題如何解決
    ↓
Task
目前要完成什麼
```

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

- 自動索引。
- Hybrid Search。
- Embedding。
- Reranking。
- Tool Layer。
- Agent Runtime。
- Webhook。
- Event Bus。
- Scheduler。
- Background Worker。
- Automated Verification。
- Observability。
- Cost Control。
- Model Routing。
- Automated Handoff。

但：

> API 應自動化既有語義，不應重新定義既有資料語義。

---

# 四十六、無 API → API 的基本原則

```
目前：
GPT + GitHub

未來：
GPT + API + Runtime
```

兩者共享：

- Knowledge。
- Capability。
- System。
- Plan。
- Rule。
- Decision。
- Evidence。
- History。
- Lifecycle。
- Canonical Source。

因此：

> 執行層可以升級，資料語義不應因為升級而推翻。

---

# 四十七、第一階段未來實作順序

本藍圖不是要求一次全部建立。

建議順序：

## Phase 1：功能盤點

將：

- K01–K61。
- S01–S37。
- A1–A12。
- B1–B16。
- C1–C18。
- D1–D20。

映射成 Capability。

## Phase 2：去重

建立：

- 相同功能。
- 相似功能。
- 互補功能。
- 依賴功能。

## Phase 3：Capability Registry

只建立真正需要的核心能力。

## Phase 4：Capability ↔ System Mapping

知道每個 System 到底提供什麼。

## Phase 5：建立第一批 Eval

優先選：

- 決策。
- 規劃。
- 搜尋。
- 驗證。
- 交接。

等高價值能力。

## Phase 6：建立 Model Profile

記錄目前模型對上述能力的實際表現。

## Phase 7：第一次蒸餾

根據實際資料：

- 精簡。
- 合併。
- Archive。

## Phase 8：Memoryless Handoff

用新的、沒有歷史記憶的 GPT 驗證。

## Phase 9：自然運作

不再為了測試而製造事件。

等待：

- 真實使用。
- 新模型。
- 真實瓶頸。

## Phase 10：Capability Evolution

正式啟動模型更新與功能重疊測試流程。

---

# 四十八、成功判準

未來架構成功，不是因為文件很多。

而是：

### 1. 能找到

GPT 能快速找到正確資料。

### 2. 能理解

GPT 能分辨：

- Knowledge。
- Capability。
- System。
- Plan。
- Rule。
- History。

### 3. 能比較

新模型出現時，可以快速定位受影響 Capability。

### 4. 能測試

可以執行：

```
GPT Only
vs
GPT + System
```

### 5. 能決策

可以產生：

- RETAIN。
- SIMPLIFY。
- MERGE。
- REPLACE。
- DEPRECATE。
- REMOVE。

### 6. 能回溯

知道為什麼當初做出這個決定。

### 7. 能交接

新 GPT 可以在沒有歷史記憶下恢復工作。

### 8. 能演化

系統會越來越乾淨，而不是越來越複雜。

---

# 四十九、失敗判準

如果未來出現：

- Capability Registry 比 System 本身還難維護。
- 每新增一個功能都要填大量欄位。
- GPT 仍然不知道應該讀什麼。
- Capability 與 System 無法區分。
- 大量功能沒有測試。
- 所謂「重疊」只能靠主觀判斷。
- 新模型更新仍然需要全面人工閱讀。
- CURRENT 與 HISTORY 再次混在一起。
- Archive 被當成 Current。
- 新增的治理機制比實際工作更耗時。

則表示功能導向架構本身需要簡化。

> 架構必須接受自己的 Capability Evaluation。

---

# 五十、最終架構哲學

本藍圖最終不是追求：

> 最完整的 AI 系統。

而是追求：

> **最低有效複雜度下，能長期演化的 AI 工作環境。**

核心關係：

```
Knowledge
=
知道什麼

Capability
=
能做什麼

System
=
如何提供能力

Plan
=
如何解決問題

Rule
=
什麼不能違反

Evidence
=
為什麼相信

Observation
=
實際運作發現什麼

Decision
=
最後採取什麼

Distillation
=
留下真正有價值的東西
```

最終形成：

```
大記憶
+
小 Context

完整歷史
+
乾淨 CURRENT

完整能力
+
最小實體化

模型持續變強
+
系統持續精簡

新功能持續增加
+
舊功能持續被驗證與淘汰
```

---

# 五十一、最終總圖

```
                         USER
                           │
                           ↓
                    ENTRY / INTENT
                           │
                           ↓
                 RESPONSE CONTRACT
                           │
                           ↓
                    ORCHESTRATION
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
          LIBRARY      CAPABILITY      CONTEXT
             │             │
             ↓             ↓
         KNOWLEDGE      PROVIDERS
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
            GPT          SYSTEM         TOOL
                           │
                           ↓
                          PLAN
                           │
                           ↓
                          TASK
                           │
                           ↓
                       EXECUTION
                           │
                           ↓
                      VERIFICATION
                           │
                    ┌──────┴──────┐
                    ↓             ↓
                 EVIDENCE     OBSERVATION
                                  │
                                  ↓
                              EVOLUTION
                                  │
                 ┌────────────────┼────────────────┐
                 ↓                ↓                ↓
              OVERLAP          IMPACT           PRUNING
                 └────────────────┼────────────────┘
                                  ↓
                               DECISION
                                  │
                                  ↓
                            DISTILLATION
                                  │
                                  ↓
                             REFACTORING
                                  │
                                  ↓
                               CURRENT
                                  │
                                  ↓
                               ARCHIVE
```

---

# 五十二、與既有架構的最終關係

本藍圖不推翻目前已確認架構。

它是在既有基礎上增加「功能導向的演化視角」。

既有架構：

```
Entry
Intent
Library
Knowledge
System
Plan
Trigger
Blueprint
Orchestration
Execution
Verification
Evidence
History
Evolution
Distillation
```

現在進一步建立：

```
Capability
    ↓
Provider
    ↓
Capability Evaluation
    ↓
Overlap / Replacement
    ↓
System Refactoring
```

所以真正的新核心不是：

> 再建立一套系統。

而是：

> **讓現有所有系統都可以被拆解成可觀測的功能，並讓這些功能可以隨模型與實際工作結果被重新評估。**

---

# 五十三、文件狀態與後續原則

本文件目前：

**【未來藍圖／規劃中／尚未全面實作】**

不得直接視為：

- 現行工程架構。
- 已完成 Capability Registry。
- 已完成 Model Evaluation。
- 已完成自動重疊偵測。
- 已完成自動淘汰。
- 已完成 API Runtime。

後續採：

```
藍圖
↓
選擇最小實作範圍
↓
實作
↓
實際使用
↓
Observation
↓
驗證
↓
必要時修改藍圖
```

不得因藍圖已經描述，就視為功能已經存在。

---

# 五十四、與前期工程的最終銜接

本藍圖承接前期已確立的工程原則：

1. 四方案維持，不增加第五方案。
2. CURRENT 與 ARCHIVE 分離。
3. 歷史完整保存，但不預設載入。
4. Canonical Source 明確。
5. 大架構、小運行。
6. 最小充分 Context。
7. Intent 優先於 Keyword。
8. Trigger 只做候選召回。
9. Orchestration 保持薄型。
10. Blueprint 依任務規模啟用。
11. 研究、討論、正式採用、實作、驗證分離。
12. Observation 是演化入口。
13. 重大變更必須有 Evidence。
14. 大型格式變更採 Migration / Distillation，而不是新舊格式永久並存。
15. 新系統只有在實際瓶頸證明後才正式實體化。
16. 無 API 階段不提前建立大型基礎設施。
17. 新 GPT 必須能以 Memoryless Handoff 恢復工作。
18. 最終判斷以實際工作結果，而不是架構理論完整度為準。

---

# 五十五、最終目的

最終希望形成的不是一個越來越大的知識庫。

而是一個：

> **能辨認自己有哪些能力、知道這些能力由誰提供、能測試能力是否仍然有價值、能在模型進步後主動找到重疊、能把被取代的功能安全退出 CURRENT，並把歷史完整保存下來的 AI 工作環境。**

最終狀態：

```
一個人
+
GPT 核心
+
GitHub 長期外部記憶
+
Capability Registry
+
可驗證的 System
+
可演化的 Plan
+
Evidence / Observation
+
Distillation / Refactoring
```

而不是：

```
一個人
+
越來越多文件
+
越來越多系統
+
越來越多管理系統
+
最後連 AI 都不知道該用哪一個
```

**核心原則：**

> 大記憶，小 Context。  
> 完整歷史，乾淨 CURRENT。  
> 完整能力，最小實體化。  
> 功能先於文件。  
> 測試先於取代。  
> 證據先於淘汰。  
> 實際瓶頸先於自動化。  
> 模型越強，系統應越精簡，而不是越膨脹。


---

# 五十六、前六次工程討論對照稽核

本節是對本藍圖建立後，依前六次相關工程討論進行的交叉稽核。

稽核目的不是把所有歷史內容重新搬入藍圖，而是確認：

1. 是否遺漏已確立的架構原則。
2. 是否把不同維度錯誤地合併。
3. 是否把「概念能力」誤寫成「正式系統」。
4. 是否把未來規劃誤寫成目前已存在。
5. 是否破壞四方案、職權、交接、資料治理與大型格式變更原則。

稽核後結論：

> 原 v1.0 的 Capability 導向核心成立，但有數項重要語義需要修正與補充，否則長期實作時可能重新產生「能力、系統、方案、資料狀態、Context、職權」混在一起的問題。

---

# 五十七、第一項修正：Knowledge、Capability、System、Plan 不是單一路徑

原本的圖容易被理解成嚴格的上下游流水線。

這是不夠精確的。

正確模型應是：

~~~
                    ┌── Knowledge
                    │
                    ├── Capability
                    │
                    ├── System
                    │
                    ├── Plan
                    │
                    ├── Rule
                    │
                    ├── Project
                    │
                    └── Evidence
                           │
                           ↓
                         Task
~~~

其中：

- Knowledge 是資訊資產。
- Capability 是功能能力。
- System 是能力的正式組合／實體化方式。
- Plan 是解決特定問題的方法。
- Rule 是限制與必須遵守的條件。
- Project 是工作範圍與目標容器。
- Evidence 是對判斷、結果與變更的依據。
- Task 是實際工作單位。

它們存在依賴與組合關係，但不是固定流水線。

---

# 五十八、第二項修正：Data Entity、Data State、Context Loading 必須三維分離

前期討論確認，這三者不能混為同一層。

## Data Entity

回答：「這是什麼東西？」

例如：

- Knowledge
- Memory
- Capability
- System
- Plan
- Rule
- Decision
- Project
- Test
- Evidence
- History

## Data State

回答：「它目前處於什麼狀態？」

例如：

- CURRENT
- PENDING
- DEPRECATED
- SUPERSEDED
- HISTORICAL
- UNCERTAIN
- CONTESTED

## Context Loading

回答：「這次工作需要載入多少？」

例如：

- L0 Entry
- L1 Current
- L2 Task System / Plan
- L3 Necessary Knowledge
- L4 Evidence / History
- L5 Cross-project

因此：

~~~
Knowledge ≠ CURRENT
History ≠ Entity Type only
Archive ≠ Context Level
~~~

任何未來 Capability Registry 都不能把「Capability」與「CURRENT」或「Loaded」混成同一語義。

---

# 五十九、第三項修正：Role 不等於 Capability

原藍圖使用 Provider 模型是正確方向，但需要補充：

~~~
Role
≠
Capability
≠
Provider
~~~

## Role

回答：「誰在這個工作中負責什麼責任？」

例如：

- User
- GPT
- Reviewer
- Maintainer

## Capability

回答：「需要完成什麼功能？」

例如：

- Search
- Compare
- Verify
- Decide
- Distill

## Provider

回答：「目前由誰／什麼提供這個能力？」

例如：

- GPT
- System
- Tool
- Human

因此「使用者負責重大採用」是 Role / Authority 問題，不應被寫成 User 是某個 Capability 的 Provider。

---

# 六十、第四項修正：職權與權限需要獨立於 Capability

原藍圖已寫出使用者、GPT、GitHub 的分工，但仍需要更明確。

職權模型：

~~~
User
↓
方向、需求、重大取捨、正式採用、重大架構決策

GPT
↓
理解、研究、分析、規劃、執行、驗證、建議

GitHub
↓
保存、版本、歷史、Canonical Source、證據載體
~~~

但：

> GitHub 保存資料，不代表 GitHub 擁有「決策權」。

同樣：

> GPT 能提出決策，不代表 GPT 自動擁有重大變更的最終採用權。

重大 Adoption 應經過：

~~~
Analysis
↓
Evidence
↓
Proposal
↓
User / Authorized Human Decision
↓
Implementation
~~~

這條邊界必須長期保留。

---

# 六十一、第五項修正：Verification 不能只分三層

原 v1.0 的三層 Verification 足以作為高階概念，但前期工程討論已將驗證責任進一步拆細。

未來應採「風險驅動的多層 Verification」，至少包含：

1. **Content / Fact Verification**：內容與事實是否正確。
2. **Source / Evidence Verification**：依據是否可靠、可追溯。
3. **Result Verification**：本次輸出是否完成要求。
4. **Behavior Verification**：系統是否按照預期運作。
5. **Integration / Regression Verification**：修改後是否破壞既有能力。
6. **Architecture Verification**：是否造成責任漂移、重複、衝突、Context 膨脹、版本漂移或入口漂移。

不是每次任務都必須全部執行。

原則：

~~~
Risk
↓
選擇必要 Verification 深度
~~~

因此 Verification 本身也應遵守「最低有效複雜度」。

---

# 六十二、第六項修正：Evidence 不等於 Verification

兩者相關，但責任不同。

## Verification

回答：

> 「我們有沒有檢查過？」

## Evidence

回答：

> 「為什麼可以相信這個結果？」

例如：

~~~
Verification
→ 測試通過

Evidence
→ 測試案例、結果、來源、Commit、觀察紀錄
~~~

因此：

> Verification 產生或引用 Evidence，但 Evidence 本身不是 Verification。

未來 Capability Evaluation 必須保留這個區別。

---

# 六十三、第七項補充：Observation 不是 Activity 的附屬品

Activity：

> 發生了什麼。

Observation：

> 從實際運作中發現了什麼。

Observation 是：

~~~
Experience
↓
Observation
↓
Evolution Candidate
~~~

的重要入口。

Evolution 不應只由外部模型更新驅動，也應由：

- 實際使用。
- 使用失敗。
- 重複工作。
- Context 浪費。
- 使用者反覆修正。
- 新模型。
- 新工具。
- 外部研究。

共同觸發。

---

# 六十四、第八項補充：Trigger 必須位於 Intent 之後

前期討論確認：

> Trigger 不能固定成輸入一來就先觸發。

較正確的概念是：

~~~
Input
↓
Intent / Context Understanding
↓
Candidate Trigger
↓
Capability / System Selection
↓
Execution
~~~

Trigger 是候選召回機制。

不是：

- Keyword Rule Engine。
- 自動執行器。
- 決策者。

---

# 六十五、第九項補充：Response Contract 是控制介面

Response Contract 不只是回答格式。

它應控制：

- 詳細程度。
- 是否需要外部研究。
- 是否需要讀 Repository。
- 是否允許修改。
- 是否允許建立新文件。
- 是否需要測試。
- 是否需要正式 Evidence。
- 是否需要使用者確認。

因此：

~~~
Intent
↓
Response Contract
↓
Allowed Work
~~~

Contract 是工作邊界，不是單純輸出格式。

---

# 六十六、第十項補充：Blueprint 必須條件式啟用

Blueprint 不是所有任務的標準前置步驟。

應依：

- 任務規模。
- 依賴數量。
- 風險。
- 跨系統程度。
- 修改範圍。
- 不可逆程度。

決定是否啟用。

否則 Blueprint 本身會成為新的固定流程負擔。

---

# 六十七、第十一項補充：Entropy 是觀測，不是刪除授權

未來如果加入：

- Context Entropy。
- Repository Entropy。
- Architecture Entropy。
- Duplicate Rate。
- Stale Rate。

這些只能作為：

> 「系統可能需要整理」的觀察訊號。

不能直接變成：

> 「因此刪除。」

正式清理仍然必須經過：

~~~
Entropy / Observation
↓
Candidate
↓
Impact Analysis
↓
Evidence
↓
Decision
↓
Change Control
↓
Implementation
~~~

不能因為某文件很少使用，就自動判定它可以刪除。

---

# 六十八、第十二項補充：大型格式變更不是一般 Refactoring

當資料格式、分類模型或 Canonical Schema 發生重大改變時：

~~~
Migration
≠
一般小型修改
~~~

應視為一次受控的資料轉換：

~~~
舊 Canonical
↓
Mapping
↓
Migration / Distillation
↓
新 Canonical
↓
完整驗證
↓
切換
↓
舊資料 Archive
~~~

禁止長期形成新格式、舊格式與半轉換格式混合成 CURRENT。

歷史可以完整保存，但 CURRENT 必須保持單一明確語義。

---

# 六十九、第十三項補充：GitHub 不只是 Storage，也是 Handoff Boundary

GitHub 在目前無 API 架構中的角色應明確分成：

1. Persistent Memory。
2. Version Control。
3. Canonical Source。
4. Evidence / History。
5. Handoff Boundary。

尤其對 Memoryless Handoff：

~~~
Current Entry
+
Current State
+
必要 Context
+
必要 Rules
+
必要 Decisions
+
Next Step
~~~

應能形成最小可攜式交接集合。

必要時可以把這個集合壓縮／下載成最小交接包，而不要求新 GPT 先理解整個 Repository。

這是「完整 Repository」與「最小工作 Context」分離的實際形式。

---

# 七十、第十四項補充：六大維度必須分層，不應互相取代

前期討論確認，整體架構至少存在四組不同分類維度：

## A. 研究／知識領域

回答：「我們在研究什麼？」

## B. 工作職能

回答：「我們能做什麼？」

## C. 資訊／工作產物

回答：「我們現在保存的是什麼種類的東西？」

## D. 四大工程方案

回答：「我們用哪一個工程治理框架管理它？」

因此：

~~~
領域
≠
功能
≠
資料型別
≠
方案
~~~

這一點是未來重建 Repository 分類時的硬性原則。

---

# 七十一、第十五項補充：知識仍然需要內部分層

Knowledge 不能成為一個沒有內部分類的大桶。

前期已確認：

~~~
知識
├── 記憶
├── 管理
├── ...
~~~

其中具體子分類應由後續正式 Knowledge Taxonomy 決定。

本藍圖不在此硬編一套完整分類，但必須保留原則：

> Knowledge 是一級 Entity，但 Knowledge 內部仍需要依資訊性質、用途與生命週期進行合理分類。

例如「長期記憶」與「知識管理規則」不能因為都屬於 Knowledge 就混在同一語義層。

---

# 七十二、第十六項補充：Capability Registry 不應先於 Capability Mapping 大量建立

原 v1.0 的 Phase 3 容易被理解成先建立 Capability Registry。

應修正為：

~~~
既有功能盤點
↓
Capability Mapping
↓
重複／互補／依賴分析
↓
確認哪些 Capability 真正值得成為正式管理單位
↓
建立最小 Capability Registry
~~~

也就是：

> Registry 是 Mapping 的結果之一，不是 Mapping 的前提。

這能避免再次把 K01–K61、S01–S37 一股腦轉成大量新系統。

---

# 七十三、第十七項補充：Capability 狀態與 System 狀態不可混用

Capability 可能是：

~~~
CURRENT
REVIEW
DEPRECATED
~~~

System 也可能是：

~~~
CURRENT
CANDIDATE
DEPRECATED
ARCHIVED
~~~

但：

> 某 Capability 被取代，不代表提供它的整個 System 必須消失。

例如：

~~~
System A
├─ CAP-001 被 GPT 取代
├─ CAP-002 仍有價值
└─ CAP-003 仍有價值
~~~

正確處理可能是：

~~~
System A
↓
移除 CAP-001
↓
保留 CAP-002 / CAP-003
↓
System A 精簡
~~~

---

# 七十四、第十八項補充：功能取代測試需要固定 Test Corpus

A/B Test 不能只比較單次案例。

未來應建立：

> Capability Test Corpus。

包含：

- 正常案例。
- 邊界案例。
- 困難案例。
- 歧義案例。
- 衝突案例。
- 高風險案例。
- 歷史污染案例。
- Context 不完整案例。
- 失敗案例。

同一 Capability 的 Provider 比較應盡可能使用相同 Test Corpus。

否則 GPT Only 與 GPT + System 無法形成可靠結論。

---

# 七十五、第十九項補充：模型更新不是唯一 Evolution Trigger

完整 Evolution Trigger 至少包括：

~~~
新模型
新工具
新研究
實際使用
Repeated Failure
Repeated Correction
Context Waste
Architecture Bottleneck
User Requirement Change
大型格式變更
~~~

因此：

> Model Update → Capability Delta 是重要入口，但不是唯一入口。

---

# 七十六、第二十項補充：FIELD 必須來自自然運作

前期工程已完成多輪模擬與回歸驗收。

未來不能因為「需要測試」而人工製造 FIELD。

正確狀態：

~~~
架構驗收完成
↓
正常工程運作
↓
真實工作
↓
自然產生 Observation / FIELD
↓
才決定是否新增或修改系統
~~~

本藍圖描述的是未來可用的 Capability Evolution 框架，不代表現在要立刻建立全部演化機制。

---

# 七十七、第二十一項補充：新系統正式化門檻

前期已確立的正式化門檻：

~~~
概念
↓
實際使用
↓
Observation
↓
重複瓶頸
↓
Proposal
↓
Stress Test
↓
User / Authorized Confirmation
↓
Build
↓
Regression
↓
正式 Current
~~~

不能因為「理論上可能需要」就直接建立新的 System。

這是防止 Capability 架構自己膨脹的主要防線。

---

# 七十八、第二十二項補充：外部研究的角色

外部工具、模型與其他軟體公司的做法，可以作為：

- Candidate Architecture。
- Design Reference。
- Benchmark。
- Risk Warning。
- Alternative Design。

但：

> 外部方案不是本 Repository 的 Canonical Source。

正式採用仍需要：

~~~
External Research
↓
適用性分析
↓
本系統 Context
↓
Prototype / Stress Test
↓
Evidence
↓
Decision
~~~

「別人有這個系統」不能直接推出「我們也必須建立」。

---

# 七十九、第二十三項補充：目前 Repository 文件很多，不等於未來架構很多

目前 Repository 文件數量偏高，是因為系統剛建立蒸餾流程，舊施工資料尚未全部進入集中 Archive / History。

因此：

~~~
Current File Count
≠
Final Working Interface Complexity
~~~

未來應：

~~~
大量施工資料
↓
Distillation
↓
穩定規則 / Current
+
完整歷史 / Archive
~~~

真正需要觀察的是：

- 每次工作實際載入多少 Context。
- 找資料是否困難。
- Handoff 是否失敗。
- 是否有重複 Capability。
- 維護成本是否上升。

---

# 八十、第二十四項補充：交接文件與藍圖文件的責任不同

未來至少區分：

## Blueprint

回答：「系統未來想成為什麼。」

## Current State

回答：「系統現在是什麼。」

## Handoff

回答：「新 GPT 現在需要知道什麼才能接手。」

## History / Evidence

回答：「系統為什麼變成現在這樣。」

四者不能互相取代。

新 GPT 不應因為讀到 Blueprint，就把「未來規劃」誤認為「已實作功能」。

---

# 八十一、第二十五項補充：目前四方案的工程狀態不因本藍圖改變

本藍圖不是四方案重新驗收文件。

目前工程狀態仍以既有正式驗收與 CURRENT 狀態為準。

本藍圖只提供未來功能導向演化的共同框架。

因此：

- 不重新做四方案總驗收。
- 不因本藍圖建立第五方案。
- 不因本藍圖人工製造新的 FIELD。
- 不以藍圖內容冒充目前已實作能力。

---

# 八十二、第二十六項補充：未來功能比較的最小單位應是「Capability + Scenario」

單獨比較 Capability 名稱仍可能不足。

例如「Decision」在不同情境可能完全不同：

~~~
一般低風險選擇
vs
高風險架構決策
vs
資訊衝突決策
~~~

因此未來 Evaluation 的最小有效比較單位應逐步形成：

~~~
Capability
+
Scenario
+
Test Corpus
+
Provider
+
Result
+
Evidence
~~~

這能避免把「同名功能」誤判成真正重疊。

---

# 八十三、第二十七項補充：Provider Replacement 不等於 System Replacement

未來最容易出現的誤判之一是：

> GPT 已經能做這件事，所以整個 System 可以刪掉。

正確判斷順序：

~~~
Provider Capability 提升
↓
Capability Overlap
↓
Scenario Evaluation
↓
System 中哪些 Capability 被取代？
↓
System 是否仍有其他不可取代能力？
↓
局部精簡
↓
必要時才評估整個 System
~~~

因此真正的淘汰單位可以是：

- Capability。
- Provider。
- System 內部元件。
- 整個 System。

不能預設四者同步淘汰。

---

# 八十四、第二十八項補充：未來的「快速判斷」必須建立在可回溯證據上

使用者要求的核心問題之一是：

> 如何快速知道某功能是否還需要保留？

未來應形成：

~~~
Question
↓
Capability Identification
↓
Existing Provider Mapping
↓
Overlap Candidate
↓
Scenario Selection
↓
Test Corpus
↓
A/B / A/B/C
↓
Result
↓
Evidence
↓
Decision
↓
Impact Analysis
↓
Regression
~~~

「快速」來自於：

- 只測受影響 Capability。
- 固定 Test Corpus。
- 既有 Evidence 可重用。
- 關係圖可直接找到受影響 System / Plan。
- 不需要每次重讀整個 Repository。

而不是降低驗證品質。

---

# 八十五、前六次稽核後的正式修正版核心模型

經本次稽核，未來藍圖的核心模型正式修正為：

~~~
                         ┌──────────────┐
                         │    USER      │
                         └──────┬───────┘
                                ↓
                       Intent / Context
                                ↓
                       Response Contract
                                ↓
                         Orchestration
                                │
          ┌─────────────────────┼─────────────────────┐
          ↓                     ↓                     ↓
      Knowledge              Capability              Rule
          │                     │                     │
          │             ┌───────┼────────┐            │
          │             ↓       ↓        ↓            │
          │            GPT    System    Tool          │
          │             └───────┼────────┘            │
          │                     ↓                     │
          └──────────────→     Plan    ←──────────────┘
                                ↓
                              Task
                                ↓
                            Execution
                                ↓
                          Verification
                           │          │
                           ↓          ↓
                       Evidence   Observation
                                      ↓
                              Evolution / Impact
                                      ↓
                              Evaluation / Decision
                                      ↓
                         Distillation / Refactoring
                              │             │
                              ↓             ↓
                           CURRENT       ARCHIVE
~~~

這個模型不表示所有任務都必須經過全部節點。

它表示這些是不同責任的架構元件，以及它們可能發生的關係。

---

# 八十六、稽核後正式修正的實作原則

本藍圖後續實作時，新增以下硬性原則：

1. 不把 Knowledge、Capability、System、Plan 強制串成單一路徑。
2. Data Entity、Data State、Context Loading 三維分離。
3. Role、Capability、Provider 三者分離。
4. Authority / Permission 不因 Capability Registry 而被吞併。
5. Evidence 與 Verification 分離。
6. Verification 採風險驅動的多層驗證。
7. Observation 是 Evolution 的核心輸入。
8. Trigger 必須在 Intent / Context 理解後提供候選召回。
9. Response Contract 是工作邊界。
10. Blueprint 只有在任務規模與風險需要時啟用。
11. Entropy 只能提出整理候選，不得直接授權刪除。
12. 大型格式變更採 Migration / Distillation / Validation / Cutover / Archive。
13. GitHub 同時是 Persistent Memory 與 Handoff Boundary。
14. Capability Registry 必須晚於初步 Capability Mapping。
15. Capability 狀態與 System 狀態分開管理。
16. 功能取代必須有固定 Test Corpus。
17. Model Update 只是 Evolution Trigger 之一。
18. FIELD 必須來自自然運作，不人工製造。
19. 新 System 必須經過「使用→Observation→重複瓶頸→驗證→確認→建立」。
20. 外部研究提供參考，不直接成為本系統規範。
21. CURRENT、Blueprint、Handoff、History / Evidence 必須保持責任分離。
22. 文件數量不是架構複雜度的直接指標。
23. 最終目標仍是最低有效複雜度，而不是最大功能數。
24. Provider Replacement 不等於 System Replacement。
25. Capability Evaluation 必須逐步加入 Scenario 維度。
26. 快速判斷必須建立在可回溯 Evidence 上。

---

# 八十七、稽核結論

本次對照沒有發現需要推翻「Capability 導向未來藍圖」的核心錯誤。

但原 v1.0 有一個重要風險：

> 如果直接按照原文件施工，可能再次把「功能分類」實體化成大量新 Registry、System、文件與治理流程。

因此本次修正後，正式採用以下優先順序：

~~~
先理解
↓
先 Mapping
↓
先比較
↓
先測試
↓
確認真的需要
↓
才實體化
~~~

而不是：

~~~
藍圖描述了
↓
立即建立文件
↓
立即建立 Registry
↓
立即建立 System
~~~

本文件仍然是：

**【未來藍圖／長期規劃】**

目前工程狀態仍以 Repository 中已確認的 CURRENT、四方案、正式交接資料與既有驗收結果為準。

本次稽核的目的不是增加更多架構，而是讓未來架構具備「能自我約束、不因自身演化而膨脹」的能力。


---

# 八十八、第二次遺漏稽核：與既有實際方案文件交叉比對

第二次稽核不是重新檢查概念，而是將本藍圖與目前 Repository 中已形成的實際方案文件、資料關係語義、舊能力重製判定原則、失敗處理流程交叉比對。

本次發現以下內容雖然部分已被間接涵蓋，但尚未在未來藍圖中明確成為共同原則：

1. 失敗處理閉環。
2. 重疊判定的正式語義維度。
3. 「融合／拆分／部分取代／完全取代／淘汰」之間的精確區別。
4. 實際使用 ≠ 文件存在。
5. Version、State、Git Commit 不得混為一談。
6. 遷移失敗與回復（Rollback / Recovery）。
7. 系統能力的完成度與實戰驗證狀態。
8. 關係的時間、範圍、條件與狀態。
9. 軟體／工具與 System 的邊界。
10. 共同能力 ≠ 共同責任 ≠ 中央巨型系統。
11. 蒸餾候選必須先判斷是否為一次性問題。
12. 新舊能力可以在遷移期間暫時並存，但不能無期限並存。
13. 功能比較需要固定 Baseline，而不只是固定 Test Corpus。
14. Evaluation 的結果不應只有數值，還必須保存案例、條件與限制。
15. 「系統完成」必須與「文件完成」明確分離。

因此，本次不是增加一套新架構，而是把既有工程原則補進未來藍圖，避免未來 Capability 化後遺失已驗證的語義。

---

# 八十九、第二十九項補充：失敗處理必須成為 Capability Evolution 的閉環

目前藍圖已有 Verification、Evidence、Observation，但缺少明確的 FAIL 路徑。

未來完整工作閉環應能表示：

~~~
Execution
↓
Verification
├─ PASS
│   ↓
│ Evidence / Observation
│
└─ FAIL
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
    ├─ PASS → Resolved
    ├─ Partial → Continue
    └─ FAIL → Rediagnose
~~~

這一點非常重要。

> 「修正已完成」不等於「問題已解決」。

Capability Evolution 也必須能區分：

- 資料不足。
- 證據不足。
- 資料衝突。
- Context 不足。
- Context 過量。
- 版本／狀態不適用。
- System Capability 不足。
- Plan 組合錯誤。
- Verification 不足。

不同失敗應回饋到不同責任層。

因此不能所有 FAIL 都導向「新增 System」。

---

# 九十、第三十項補充：重疊分析必須使用完整語義，而非名稱或單一輸出

既有重製判定原則已明確定義，重疊至少比較：

| 維度 | 問題 |
|---|---|
| Purpose | 是否解決同一問題？ |
| Input | 是否接收相同／高度重疊輸入？ |
| Output | 是否產生相同或可替代結果？ |
| Trigger | 是否在相同條件下啟動？ |
| Responsibility | 是否對同一責任負責？ |
| State | 是否維護同一狀態？ |
| Data | 是否保存／修改相同資料？ |
| User / Role | 是否由同類工作使用？ |
| Dependency | 是否依賴相同上下游？ |
| Verification | 是否用相同方式判定成功？ |

因此：

> 名稱相似、輸出相似、或 Capability 名稱相同，都不足以判定真正重疊。

本藍圖原有的 Overlap Detection 應正式採用上述語義作為最低分析基準。

---

# 九十一、第三十一項補充：處置結果必須細分，不能只用 REMOVE / REPLACE

未來功能演化至少需要保留以下處置語義：

~~~
Keep
Extend
Refactor
Merge
Split
Replace
Rebuild
Retain
Retire
Archive
~~~

此外，資料／知識演化還可能存在：

~~~
補充
修正
部分取代
完全取代
融合
拆分
廢棄
前身／歷史
~~~

兩組語義不能完全混成一套。

第一組主要描述：

> 能力／系統／架構如何處置。

第二組主要描述：

> 資料／知識內容如何演化。

這是兩個不同維度。

---

# 九十二、第三十二項補充：使用、支撐、依賴、來源必須分開

未來關係分析不得把所有「有關」都寫成 Dependency。

正式保留：

~~~
使用 ≠ 依賴
支撐 ≠ 依賴
來源 ≠ 支持
比較 ≠ 衝突
分類 ≠ 關係
~~~

其中：

- 使用：工作過程中會用到。
- 依賴：缺少對象會使能力無法正常成立／使用。
- 支撐：提供設計或判斷上的支撐，但不一定是必要依賴。
- 來源：描述資料從哪裡來。
- 支持：描述某來源／證據是否支持某主張。

這會直接影響 Capability Impact Analysis。

錯誤把「使用」當成「依賴」，會造成過度擴大的受影響範圍。

---

# 九十三、第三十三項補充：關係必須保留時間與適用條件

Capability Graph / System Graph 不應只保存：

~~~
A → Depends On → B
~~~

對可能變動的關係，至少應能表達：

~~~
Relationship Type
+
Source
+
Target
+
Time
+
Scope
+
Condition
+
State
~~~

例如：

> Capability A 在某版本、某專案、某條件下依賴 System B。

不能因為今天存在依賴，就推論歷史上與未來永遠存在。

---

# 九十四、第三十四項補充：Version、State、Commit 是三種不同資料

未來藍圖必須明確禁止：

~~~
Version = State = Git Commit
~~~

三者不同：

### Version

回答：

> 「這個物件的哪一個版本？」

### State

回答：

> 「目前處於什麼生命週期狀態？」

例如：

- CURRENT
- REVIEW
- DEPRECATED
- RETIRED
- HISTORICAL

### Git Commit

回答：

> 「Repository 在哪一次版本控制變更中保存了這個狀態？」

因此：

> Git Commit 可以作為 Evidence / Traceability，但不能直接當成 Capability Lifecycle State。

---

# 九十五、第三十五項補充：實際使用必須與文件存在分離

未來 Capability Matrix 不得因為：

> Repository 裡有這個文件。

就判定：

> Capability 正在使用。

至少要區分：

~~~
Defined
Documented
Available
Used
Validated
Production / Real Work Proven
~~~

其中：

- Defined：已定義。
- Documented：已有文件。
- Available：目前可以使用。
- Used：曾經實際使用。
- Validated：經過明確驗證。
- Real Work Proven：已在正常工作中證明具有實際價值。

這能防止「文件數量」被誤當成「能力數量」或「能力成熟度」。

---

# 九十六、第三十六項補充：大型替換必須考慮回復路徑

任何高影響：

- Replace
- Merge
- Split
- Rebuild
- 大型 Migration

都必須回答：

~~~
如果新方案失敗：
如何回復？
回復到什麼狀態？
哪些資料已經轉換？
哪些舊能力仍可用？
如何判定可以重新切換？
~~~

因此大型變更的標準流程應補成：

~~~
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
Regression / Recovery if needed
↓
Final Adoption
↓
Archive
~~~

不應只設計「成功路徑」。

---

# 九十七、第三十七項補充：A/B Test 必須有 Baseline

固定 Test Corpus 是必要條件，但仍不足。

還需要：

> Baseline。

Baseline 用來回答：

> 「新方案相對於什麼狀態改善或退化？」

因此：

~~~
Baseline
+
Test Corpus
+
Scenario
+
Provider
+
Result
+
Evidence
~~~

才形成可比較的 Evaluation。

Baseline 可以是：

- 現行 GPT Only。
- 現行 System。
- 舊版本。
- 已驗證的 Reference Implementation。

不同測試不可任意更換 Baseline，否則不同輪結果難以比較。

---

# 九十八、第三十八項補充：Evaluation 必須保存條件，不只保存結果

未來不能只記：

> A = 90%，B = 94%。

還必須知道：

- 測試日期。
- Model Version。
- System Version。
- Capability Version。
- Test Corpus Version。
- Scenario。
- Context 條件。
- 工具條件。
- 評估方式。
- 已知限制。
- Evidence。

否則模型更新後，即使數值不同，也無法判斷差異究竟來自模型、系統、資料或測試條件。

---

# 九十九、第三十九項補充：非功能性成本必須納入 Capability 評估

功能正確不代表值得保留。

未來 Evaluation 除了：

- 正確性。
- 完整性。
- 穩定性。
- 漏判。
- 錯判。

還應觀察：

- Context 成本。
- 搜尋成本。
- 維護成本。
- 更新成本。
- 同步成本。
- 驗證成本。
- 遷移成本。
- 回復成本。
- 理解成本。
- 依賴成本。
- 複雜度成本。

核心原則：

> 功能價值必須與生命週期成本一起判斷。

---

# 一百、第四十項補充：蒸餾候選首先要判斷是否為一次性問題

不是每一個問題都值得進入蒸餾。

應先判斷：

~~~
Signal
↓
是否一次性？
↓
是否超出正常迭代範圍？
↓
是否涉及多個能力／系統／責任？
↓
是否存在長期結構成本？
↓
才建立 Distillation Candidate
~~~

否則：

> 一次性的 Bug 也會被誤認成架構問題。

這會使方案四與日常工程運作混在一起。

---

# 一○一、第四十一項補充：共同能力不能變成中央巨型系統

跨方案共同 Capability 可以存在。

但：

~~~
共同 Capability
≠
共同責任
≠
中央巨型 System
~~~

例如「Impact Analysis」可以由多個方案共同使用，但不代表建立一個中央 Impact Engine 來接管所有方案。

共同能力應盡可能共享：

- 語義。
- 資料契約。
- 評估方法。
- 關係定義。

而不是自動共享所有執行責任。

---

# 一○二、第四十二項補充：軟體、工具、System、Capability 必須保持邊界

既有交接資料已確認：

~~~
Capability
≠
System
≠
Software
≠
Tool
~~~

建議未來採：

- Capability：能完成什麼。
- System：由多項能力、資料與規則組成的可重複工作結構。
- Tool：提供操作／外部介面的工具。
- Software：實際運行的軟體產品或程式。
- Provider：目前提供某 Capability 的來源。

同一個 Software 可以提供多個 Capability。

同一個 Capability 也可能由 GPT、System、Tool、Human 等不同 Provider 提供。

因此不能因為找到一個 Tool，就把 Tool 本身當成 Capability。

---

# 一○三、第四十三項補充：Capability 演化需要「部分取代」能力

未來不應只有：

~~~
保留
或
取代
~~~

常見實際狀態是：

~~~
A Capability
↓
70% 被 GPT 原生能力覆蓋
30% 仍由 System 提供
~~~

此時可能：

- 保留剩餘部分。
- 精簡 System。
- 拆分 Capability。
- 讓 GPT 成為主要 Provider。
- System 保留特殊情境。

因此 Capability Mapping 必須支援：

> Partial Replacement。

不能把功能重疊理解成二元關係。

---

# 一○四、第四十四項補充：允許「有理由的重複」

Capability 去重的目標不是讓 Repository 中每個功能只出現一次。

有些重複具有正當理由：

- 不同責任。
- 不同風險邊界。
- 不同可靠性要求。
- 不同隔離需求。
- 不同使用情境。
- 不同驗證方式。
- 不同失敗成本。

因此：

> Duplicate ≠ Redundant。

真正需要處理的是：

> Unjustified Redundancy。

---

# 一○五、第四十五項補充：新舊能力在遷移期間可以暫時並存

大型 Migration 不一定能一次完成。

可以存在：

~~~
Old Capability
+
New Capability
↓
Parallel Validation
↓
Cutover
↓
Old Retire
~~~

但必須明確：

- 哪個是 CURRENT。
- 哪個是 Candidate。
- 哪個只用於驗證。
- 何時停止舊路徑。
- 退役條件。
- 回復方式。

因此「新舊並存」本身不是錯誤；「無期限、無狀態的新舊混存」才是問題。

---

# 一○六、第四十六項補充：Capability Evaluation 必須有停止條件

評估也可能無限膨脹。

因此需要：

~~~
Evaluation Goal
↓
Minimum Sufficient Test
↓
Result
↓
Uncertainty
↓
是否仍影響決策？
├─ 否 → Stop
└─ 是 → Additional Test
~~~

不是所有 Capability 都需要大量測試。

測試深度應由：

- 風險。
- 決策影響。
- 不確定性。
- 變更不可逆程度。

決定。

這與 Blueprint、Verification 的「最低有效複雜度」原則一致。

---

# 一○七、第四十七項補充：完成度必須分層

未來 Capability、System、Plan 不應只有：

~~~
完成 / 未完成
~~~

至少可以區分：

~~~
DESIGNED
↓
BUILT
↓
SIMULATION-VALIDATED
↓
REAL-WORK-VALIDATED
↓
CURRENT
~~~

而：

> CURRENT 不一定代表永久正確，只代表目前正式採用。

同時：

> Archive 不代表錯誤，也可能只是歷史上曾經正式有效。

這能防止把「歷史版本」與「錯誤版本」混為一談。

---

# 一○八、第四十八項補充：未來功能導向架構仍必須服從停止擴充原則

既有方案二已確立：

> 當主要責任、成功路徑、失敗閉環與驗收方法已經形成，就應停止結構性擴充，進入實際工作驗證。

因此 Capability 架構也必須遵守：

~~~
能力已能描述
+
真正需要的資料已存在
+
最小工作閉環成立
+
驗收方式已定義
↓
停止結構性擴充
↓
真實工作
↓
Observation
↓
再決定是否需要增加能力
~~~

不能因為還能列出新的 Capability 名稱，就繼續建立架構。

---

# 一○九、第二次稽核後的補充結論

第二次交叉檢查後，確認目前未來藍圖的核心沒有需要推翻的部分。

但原本仍存在一個明顯缺口：

> 第一版藍圖比較完整描述了「如何比較功能」，但還沒有完整描述「如何處理比較失敗、資料關係語義、遷移風險、回復、成熟度與停止條件」。

本次補充後，未來功能導向架構的完整閉環應理解為：

~~~
需求／模型／工具／實際工作變化
↓
Intent / Context
↓
Capability Mapping
↓
Overlap Candidate
↓
Scenario + Baseline + Test Corpus
↓
Evaluation
↓
Evidence
↓
Decision
↓
Impact Analysis
↓
Migration / Refactoring
↓
Verification
↓
Cutover
↓
Observation
↓
Real-Work Validation
↓
Distillation
↓
CURRENT / ARCHIVE
~~~

其中任何一步失敗，都可以回到：

~~~
Failure Classification
↓
Diagnosis
↓
Problem Solving
↓
Revalidation
~~~

因此未來藍圖現在不只是「功能清單管理架構」，而是：

> **以 Capability 為比較單位、以 Scenario 為情境、以 Baseline 為比較基準、以 Test Corpus 為測試基礎、以 Evidence 為證據、以 Impact Analysis 為影響邊界、以 Change Control 為採用門檻、以 Real-Work Observation 為長期演化依據的功能生命週期架構。**

這仍然是未來藍圖，不代表上述全部機制現在已經實體化。

目前工程仍以既有四方案 CURRENT、既有交接資料與正式驗收結果為準。
