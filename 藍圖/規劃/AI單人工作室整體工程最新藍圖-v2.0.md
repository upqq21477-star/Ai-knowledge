# AI 單人工作室整體工程最新藍圖 v2.0

版本：v2.0
日期：2026-09-19
狀態：【最新施工藍圖；正式施工依此排序】
前版：藍圖/工程施工總控與收尾計畫-v1.0.md

## 整體系統健檢治理｜2026-09-19

本輪研究確認：整體健檢屬跨系統治理，不升格為獨立 Skill。

固定資料流：
健檢 → Findings → Type / Priority → Problem Registry / Workpool → Verification / Re-test → CURRENT / Blueprint 必要同步。

健檢採「事件觸發＋定期保底」，不設僵化週期。重大架構／Control Plane 變更、自然異常 recurrence、主要工程階段完成、Authority / Source of Truth 變更，以及跨系統依賴／Lifecycle 異常，均可觸發健檢。

Finding 分為：
- BUG_CONFIRMED
- STRUCTURAL_GAP
- RISK
- OBSERVATION
- UNPROVEN

Priority 分為 P0 / P1 / P2 / P3 / Deferred。
P0/P1 進唯一 Workpool；已確認 Bug 進 Problem Registry；未證明假設不得直接列 Bug 或施工。

本輪已確認並修正：
- Handoff Skill Lifecycle 重複／版本不同步。
- State / Acceptance Canonical Source 路徑斷裂。
- G1 FIELD CURRENT count 漏記 F22；F01-F22 實際為 22 cases。

後續健檢重點轉向 Runtime Closure：
Trigger → Capability → Routing → Invocation
→ Context → Execution → Verification
→ Failure / Fallback / Re-route → Final / Stop。

不得因健檢結果自動新增大型 Registry、Automation、Orchestration 或新 Skill；只有自然 Evidence 證明責任獨立且反覆需要時才重新評估。

## 0. 本版目的

本版不是再增加一套架構，而是把目前已建立的 Skill、Agent、Routing、四方案、Problem Registry、Handoff、CURRENT Baseline、Evaluation、Evolution 與 Large Mode，重新整理成一條可實際施工、驗證、收斂的工程路線。

核心原則：

「先讓現有能力真正工作 → 從真實工作取得證據 → 再決定哪些要保留、融合、更新、取代或延後。」

本版取代舊施工總控的「文件建立優先」傾向，改為：

規格穩定
→ CURRENT 基線
→ 實際工作
→ 問題閉環
→ 評估
→ 能力演化
→ 必要時重構
→ 最終收尾。

不以文件數量作為進度。

---

# 一、目前發現的主要問題

## P1｜目前存在多個「狀態入口」

現況同時存在：
- README
- 目前狀態
- 快照-006
- 目前施工交接包
- 舊交接資料
- 施工總控

雖然已經定義權威順序，但實際 FIELD 已多次發生狀態漂移。

證據：
G1-P01～P08 多次出現 Index、CURRENT、README、施工總控、Handoff 不同步。

### 解法

不再增加新的 CURRENT 文件。

固定：
- README：入口
- 交接包：跨 AI 最小恢復
- CURRENT Baseline：正式工程狀態
- 施工藍圖：施工順序
- Problem Registry：問題生命週期
- 歷史文件：只保存證據

後續建立 CURRENT Baseline 後，將快照-006逐步降為歷史證據，不再讓多份文件共同承擔 CURRENT。

---

## P2｜「架構層級」存在三種描述

目前文件中同時出現：

A：
Rules → Knowledge → System → Application

B：
Knowledge / Memory → System → Plan → Software / Tool → Application

C：
Agent as Top-Level Skill
→ Task Understanding → Context → Skill Selection → Execute → Verify → Replan

三者不是完全衝突，但用途不同，若沒有明確分工，接手 AI 容易誤以為存在三套架構。

### 解法

固定成「兩個維度」：

資料／工程資產層：
Rules
→ Knowledge / Memory
→ System
→ Plan
→ Software / Tool
→ Application

AI 運作控制層：
Agent
→ Task Understanding
→ Context
→ Skill Selection
→ Execute
→ Verify
→ Replan

Agent 不取代資料層；Agent 是使用資料層資產的運作控制器。

因此不再討論哪一套是唯一架構，而是明確區分：
「資產怎麼存」與「AI 怎麼工作」。

---

## P3｜G1/G2 太早成為長期主線，CURRENT Baseline 反而延後

目前 Skill / Agent / Routing 已建立正式規格與 FIELD 證據；CURRENT Baseline 已建立並通過 Phase 1 Gate。

風險：
Skill 可能依據尚未整理的舊 System / Plan / Knowledge 建立，後續重構時再產生引用漂移。

### 解法

不停止 G1/G2，但從現在開始改為「短批次持續 FIELD」。

同時提前建立 CURRENT Baseline 第一版。

新順序：

G1/G2 小批次 FIELD
↕
CURRENT Baseline
→ Dependency Mapping
→ Real Work
→ Evaluation。

CURRENT Baseline 不必等 50 次 Real Work 才開始。

---

## P4｜50 次 Real Work 被寫得像硬性門檻

50 次是有用的觀察批次，但不代表 50 次以前不能作判斷。

### 解法

改為「50 次觀察目標，不是完成門檻」。

採 Minimum Sufficient Evidence：

自然案例已足以回答問題
→ 可提前做決策。

證據不足
→ 繼續累積。

50 次完成
→ 做一次批次統計，不代表自動通過。

---

## P5｜Evaluation 是目前最大實質缺口

現在已有：
- Simulation
- FIELD
- Failure Loop
- Re-test
- Handoff Test

但尚未形成完整的：

Scenario
→ Execution
→ Evidence
→ Evaluation
→ Decision

因此目前知道「某些東西能工作」，但還不知道：
- 哪些能力穩定
- 哪些能力浪費 Context
- 哪些能力容易誤路由
- 哪些能力值得保留
- 哪些能力應融合。

### 解法

建立最小 Evaluation Loop，不新增大型 Evaluation 系統。

先直接使用：
G1 FIELD + Real Work + Problem Registry + Skill Feedback。

統計：
- 任務成功
- Routing 錯誤
- Re-routing
- 不必要 Skill
- Verification Failure
- Context 額外成本
- 人工介入
- 最終修正次數
- 是否產生新問題。

---

## P6｜Skill、System、Knowledge、Plan 之間的重複尚未完成依賴驗證

現在已知道「可能有重複」，但不能直接刪除。

### 解法

建立一次性 Dependency Audit：

Skill
→ 使用哪些 System
→ 使用哪些 Knowledge
→ 使用哪些 Plan
→ 是否真的需要
→ 是否重複
→ 是否只屬歷史背景。

結果分為：
KEEP / MERGE / COMPRESS / ARCHIVE / DEFER。

沒有實際依賴證據，不刪。

---

## P7｜Skill Classification 的 NEW / REPLACE / ARCHIVE 證據不足

目前已有 DEFER / UPDATE / MERGE Candidate，但沒有足夠自然案例支持：
NEW / REPLACE / ARCHIVE。

### 解法

不製造案例。

自然工作觸發才記錄。

在沒有證據前：
NEW / REPLACE / ARCHIVE = DEFER。

---

## P8｜大型 Skill / Graph / Automation 有過早工程化風險

Large Mode 已有介面與規格，但目前仍沒有證據證明 Small Mode 已經成為瓶頸。

### 解法

Large Mode 保留接口，不施工。

啟動條件至少出現：
- 重複 Routing 錯誤
- Skill Recall 明顯不足
- 多 Skill Composition 變得難以人工管理
- Dependency 管理成本持續上升
- Context 成本因 Skill 數量而顯著增加
- 維護成本本身成為實際瓶頸。

---

## P9｜「有規則」不等於「操作時會遵守」

P01～P08 最重要的共同發現：

問題不是沒有寫同步規則，而是跨文件修改仍可能分批完成。

### 解法

正式採用：

Change Set
→ 受影響文件集合
→ 全部修改
→ 全部 Re-read
→ 一致性 Gate
→ 才宣告完成。

跨文件修改不得以「每一檔成功」作為完成條件。

---

## P10｜暫行監控已接入，但尚無 FIELD 成本／收益證據

「啟動監控」目前只是可啟動的暫行控制，不代表它值得永久保留。

### 解法

先進行自然 FIELD。

記錄：
- 是否抓到原本會漏掉的問題
- 是否造成額外推理負擔
- 是否造成回答延遲／Context 負擔
- 是否值得長期保留。

若收益低於成本：
降低門檻、降低深度或停止。

---

## P11｜快照-006 已開始承擔過期風險

它目前仍被入口鏈引用，但內容日期為 2026-09-18，且工程已進入 2026-09-19 的新狀態。

### 解法

不是立即刪除。

在 CURRENT Baseline 建立後：
1. 建立新 CURRENT。
2. 驗證新 AI 能否只靠新入口恢復。
3. 將快照-006降為 Historical。
4. 更新入口引用。
5. 執行 Memoryless Takeover Test。

---

## P12｜待辦文件實際缺失，但規則與 README 仍把它當入口

檢查 Repository 時，根目錄沒有找到 `待辦清單.md`，但 `規則.md`、目前狀態與既有文件仍引用它。

### 解法

這不是立即建立第五套狀態系統。

應在本版施工中建立「唯一待辦入口」，內容只保存：
- CURRENT 下一步
- Blocker
- Deferred
- 下一施工游標。

建立後不得再建立第二份待辦。

---

# 二、重新整理後的總體架構

## A. 資產層

Rules
→ Knowledge / Memory
→ System
→ Plan
→ Software / Tool
→ Application

## B. AI 運作層

Agent
→ Task Understanding
→ Context
→ Skill Selection
→ Execute
→ Verify
→ Replan

## C. 治理／控制橫向能力

Problem
Evidence
Version
State
Lifecycle
Traceability
Handoff
Evolution
Change Set / Completion Gate

這些不是新的資料層，而是跨層控制。

---

# 三、重新整理後的工程主線

不再使用「G1 完成後才進 G2、G2 完成後才進 G3」的完全串行方式。

改成五條互相配合的主線：

### Stream A｜Execution
Agent / Skill / Routing / Context / Execution

### Stream B｜Evidence
FIELD / Real Work / Verification / Problem Registry

### Stream C｜Baseline
CURRENT / History / Dependency / Index / Handoff

### Stream D｜Evaluation
Scenario / Test Corpus / KPI / Comparison

### Stream E｜Evolution
Change Signal / Classification / Distillation / Migration

Large Mode 是條件式支線，不是主線。

---

# 四、最新施工階段

## Phase 0｜架構與入口收束
狀態：已完成；進入穩定觀察期

工作：
1. 固定資產層與 AI 運作層的兩維架構。
2. 固定 CURRENT 唯一入口。
3. 固定 Problem Registry。
4. 固定 Handoff。
5. 固定 Change Set / Completion Gate。

Gate：
無第二 CURRENT。
無新的重複總控。
架構語義一致。

---

## Phase 1｜CURRENT Baseline v1

狀態：Gate PASS

優先級：已完成；後續僅維護與更新

工作：
1. 盤點現行文件。
2. 區分 CURRENT / Historical / Deferred / Unknown。
3. 確認 Agent / Skill / System / Knowledge 依賴。
4. 建立乾淨 CURRENT。
5. 驗證 Handoff。
6. 降級快照-006為歷史。
7. 修正待辦入口。

輸出：
CURRENT Baseline v1
+ Dependency Map
+ 唯一待辦入口。

Gate：
無記憶 AI 能從首頁恢復目前工程。
不得依賴舊快照猜測。

---

## Phase 2｜G1/G2 小批次 FIELD

優先級：高

不是追求數量，而是補 Evidence Gap。

優先尋找：
1. Natural Routing Failure
2. Natural Provider / Tool Failure
3. Context 不足
4. Verification Failure
5. 多 Skill Composition
6. Classification Candidate

每批完成：
FIELD
→ Problem Registry
→ Fix
→ Re-test
→ Feedback
→ Change Set Gate。

---

## Phase 3｜Real Work Observation Batch

目標：50 次自然工作觀察。

50 次不是硬 Gate。

每次最少記錄：
Task
Capability
Skill
Routing
Context
Result
Verification
Failure
Re-route
Cost
Human Intervention
Decision。

批次統計：
- 成功率
- Routing Failure
- Re-routing
- 不必要 Skill Chain
- Context Cost
- Verification Failure
- 人工介入
- 重工次數
- 問題類型分布。

---

## Phase 4｜Dependency Audit

在足夠 Real Work 後執行。

逐項確認：

Skill
→ System
→ Knowledge
→ Plan
→ Reference

判斷：
KEEP
MERGE
COMPRESS
ARCHIVE
DEFER。

規則：
沒有使用證據不刪。
只有歷史用途可降為 Archive。
同一責任有雙入口才進 Merge。

---

## Phase 5｜Minimum Evaluation

建立最小可重複 Evaluation。

流程：

Scenario
→ Execute
→ Evidence
→ Evaluate
→ Compare
→ Decision。

比較維度：
Correctness
Completeness
Stability
Context Cost
Time / Workload
Human Intervention
Traceability
Risk
Rework。

不建立大型評測平台。

---

## Phase 6｜Capability Evolution

只有 Phase 5 發現穩定問題才啟動。

流程：

Change Signal
→ Impact
→ Candidate
→ Evaluation
→ Migration
→ Validation
→ Adoption。

Change Signal：
Model
Tool
Workflow
Evidence
Real Work
Requirement
Failure
Data State。

---

## Phase 7｜Distillation / Migration / Refactoring

條件式施工。

只有：
Evaluation 證明有必要
+
Dependency Audit 找到實際重複
+
有可驗證替代方案

才執行。

禁止：
只因「看起來可以更簡單」就刪除。

---

## Phase 8｜Large Mode Decision

不是施工階段，而是決策 Gate。

檢查：
- Small Mode 是否出現持續 Routing 問題？
- Skill 數量是否使人工選擇失效？
- Context 成本是否顯著增加？
- Dependency 是否難以維護？
- Composition 是否成為瓶頸？
- Registry 是否能實際降低成本？

全部沒有充分證據：
保持 Small Mode。

---

## Phase 9｜Final Closure

條件：

CURRENT
+ Handoff
+ Problem
+ FIELD
+ Real Work
+ Evaluation
+ Evolution Decision
+ Index
+ References

全部一致。

最後執行：
1. 全庫狀態盤點
2. OPEN Problem 清零或正式 DEFER
3. CURRENT / Historical 分離
4. 引用掃描
5. Index 檢查
6. Memoryless Takeover
7. 最終 Re-test
8. 建立 Final Baseline。

---

# 五、施工排程

排程採「工作批次 + Gate」，不以日期硬性宣告完成。

## 2026-09-19～09-20｜Batch A
主題：入口與 CURRENT 收束

- 固定兩維架構語義
- 建立 CURRENT Baseline v1 初稿
- 建立唯一待辦入口
- 清查快照-006引用
- 整理 Dependency Audit 範圍
- 保持 G1/G2 少量自然 FIELD

完成條件：
CURRENT 初稿可由無記憶 AI 恢復。

## 2026-09-20～09-22｜Batch B
主題：G1/G2 Evidence 補強

優先取得：
Routing Failure
Provider / Tool Failure
Context Failure
Verification Failure
Classification Candidate

同時驗證：
Atomic Completion Gate 是否降低 P01～P08 類同步問題。

## 2026-09-22～09-26｜Batch C
主題：Real Work Observation

開始累積 50 次自然工作觀察。

不製造失敗。
不為湊數改變任務。

每批約 10 次檢查一次：
- Routing
- Context
- Verification
- Cost
- Problem Recurrence。

## 2026-09-26～09-28｜Batch D
主題：Dependency Audit

使用前期 Real Work 證據確認：
Skill ↔ System ↔ Knowledge ↔ Plan。

輸出：
KEEP / MERGE / COMPRESS / ARCHIVE / DEFER。

## 2026-09-28～09-30｜Batch E
主題：Minimum Evaluation

建立第一批可重複 Scenario / Test Corpus。

完成：
Execution
→ Evidence
→ Evaluation
→ Decision。

## 2026-10-01 起｜Batch F
主題：Evolution / Migration

只有出現 Change Signal 或結構性瓶頸才啟動。

若沒有：
保持現狀，繼續 Real Work。

## 最後階段
主題：Final Closure

沒有固定日期。

必須由 Evidence 決定，而不是日曆決定。

---

# 六、目前優先級

P0：
CURRENT Baseline + 唯一待辦入口 + 架構語義收束

P1：
G1/G2 Natural FIELD

P2：
Real Work Observation

P3：
Dependency Audit

P4：
Minimum Evaluation

P5：
Capability Evolution

P6：
Migration / Refactoring

P7：
Large Mode Decision

P8：
Final Closure

---

# 七、禁止事項

1. 不建立第五治理方案。
2. 不建立第二 CURRENT。
3. 不建立第二待辦入口。
4. 不因單次失敗建立新 Skill。
5. 不因 Provider / Tool / Model 更新直接建立 Skill。
6. 不猜 UNKNOWN Mapping。
7. 不以 Simulation 代替 FIELD。
8. 不以 50 次作為僵硬通過門檻。
9. 不因「看起來重複」直接刪 Knowledge / System。
10. 不提前施工 Graph / Automation；Registry / Query 已進入正式 Small Mode Control Plane。
11. 不為了填滿 Blueprint 而建立新系統。
12. 不把暫行監控視為永久能力，直到有成本／收益證據。
13. 不讓舊快照覆蓋 CURRENT。
14. 不以單一檔案修改成功作為跨文件施工完成。

---

# 八、固定施工閉環

所有實際施工統一：

Task
→ Understand
→ Context
→ Skill
→ Execute
→ Verify
→ Problem Record（若異常）
→ Fix / Re-plan
→ Re-test
→ Feedback
→ Change Set Gate
→ CURRENT / History 更新
→ 下一任務。

若問題沒有結構性證據：
維持原架構。

若問題反覆出現：
進入 Evaluation。

若 Evaluation 證明架構需要改：
進 Evolution。

若 Evolution 證明需要移動資料：
進 Migration。

若 Migration 後驗證通過：
更新 CURRENT。

---

# 九、本版完成判準

v2.0 本身的工作不是「把所有工程做完」，而是完成以下重新排序：

1. 找出目前實際問題。
2. 將問題與解法分開。
3. 把 CURRENT Baseline 提前。
4. 將 G1/G2 改為小批次持續 FIELD。
5. 把 50 次改為 Observation Batch。
6. 把 Evaluation 放到 Real Work 證據之後。
7. 把 Evolution 放到 Evaluation 之後。
8. 把 Migration 放到有證據之後。
9. Large Mode 保持條件式。
10. 不再增加新的總控文件。

本藍圖的最高原則：

「證據決定架構，不是架構要求證據。」

目前狀態：
【正式基線已建立；進入 Phase 2 Natural FIELD / Real Work Observation】

下一施工游標：
Phase 2 → G1/G2 小批次 Natural FIELD。


---

## 2026-09-19｜Blueprint 整體掃描後對齊

本版仍是施工順序與決策框架；目前實際工程狀態以：
`2-方案/完善/CURRENT Baseline-v1.0.md`
為唯一 CURRENT Authority。

本輪掃描已另外建立：
`藍圖/AI單人工作室整體功能藍圖-v1.0.md`

其責任是把本版的未來施工路線，與目前已建立 Skill、Control Plane、既有 CAP Mapping、【代】Skill、以及尚未實體化的 Capability / System / Infrastructure 對齊。

本輪確認：
- Blueprint Governance Skill：已建立，State=ACTIVE、Acceptance=【代】。
- 會議紀錄管理 Skill：已建立，State=ACTIVE、Acceptance=【代】。
- G1 FIELD：目前以 CURRENT Baseline / Workpool 的 G1=22 為準。
- Phase 2 Natural FIELD：目前施工主線。
- Minimum Evaluation、Dependency Audit、Capability Evolution、Migration：仍依 Evidence 推進。
- Capability Registry / Graph / Automation / Orchestration / Large Mode：保持條件式後置，不因藍圖完整而提前施工。
- 未來藍圖中的 Trigger / Recall / Evaluation 等項目，目前不自動升格為新 Skill。

因此，本版的施工順序不因本次 Blueprint 掃描而另建一條平行工程線。

完整功能位置與未來項目對照：
`藍圖/AI單人工作室整體功能藍圖-v1.0.md`


## 2026-09-19｜舊待辦／施工／研究資料蒸餾

本輪將已被後續工程吸收的舊待辦、施工規劃與對照研究壓縮為以下工程足跡；原始文件不再作現行依據。

- **建立前 Gate**：新方案構想先經問題與目標確認、既有能力盤點、外部研究／比較、漏洞與反方案檢查、候選架構、討論修正，確認後才建立。建立、成立、實測、長期有效分開判定。
- **施工與工作記憶**：施工順序以「狀態 → 目標 → 待辦 → 依賴 → 返工風險 → 執行 → 結果 → 更新」閉環；先證明能力缺口，再建立系統；不為驗證而製造案例。
- **共同資料與大型更新**：先穩定共同語義、版本、狀態、關係與接口，再建立依賴其上的上層能力；每一代現行資料維持單一正式格式，舊格式只保留歷史／Migration Source／Regression Test 用途。
- **Control Plane 施工經驗**：設計完成不等於能力完成；先 Natural FIELD／Real Work，再 Dependency Audit、Minimum Evaluation、Evolution、Migration。大型 Graph／Automation／Large Mode 僅在實際瓶頸出現後啟動。
- **Agent／Skill 對照研究**：歷史對照只作架構假設與研究依據；沒有相同 runtime 條件，不宣稱產品優劣。是否擴大測試由自然證據決定。
- **歷史失效教訓**：多入口狀態、跨文件不同步、舊資料覆蓋 CURRENT、過早建立系統與重複待辦均會造成返工；因此現行工程採唯一 Authority、Change Set、完成 Gate、Historical 分離與 Evidence 驅動演化。

蒸餾後原則：**保留決策與失效原因，不保留已被現行藍圖／CURRENT／正式系統取代的施工細節。**

本節為歷史足跡，不新增 CURRENT、Workpool 或第二套規則。


## 2026-09-19｜交接資料生命週期 Blueprint 對齊

本次新增的「交接推進 → 進度驗收 → EXIT-CHECK → 蒸餾 → RETIRED → 刪除」已進入藍圖規劃，不新增獨立系統。

### Blueprint 判定
- **已進入藍圖**：Handoff 作為 Control / Governance 能力的生命週期管理；交接與 CURRENT、待辦、驗收、History 的邊界；完成後蒸餾與退出。
- **已進入既有施工主線**：Phase 0 的 Handoff / Completion Gate、Phase 1 的 CURRENT Baseline、Phase 2 起的 Natural FIELD 證據，以及 Phase 9 的 CURRENT / Historical 分離與最終清理。
- **本次新增的具體規則**：交接主要待辦接近剩 2 項時進入 EXIT-CHECK；這是操作觸發器，不是新的狀態系統或硬性刪除門檻。
- **尚未進入獨立 Blueprint Work Item 的部分**：自動化刪除、完整 Handoff Registry、獨立交接管理平台。現階段沒有證據支持新增這些系統。

### 交接退出驗收
```
Handoff
→ 推進游標
→ 待辦完成
→ 驗收
→ EXIT-CHECK
→ 依賴／入口確認
→ 必要資訊蒸餾
→ RETIRED
→ 刪除
```

因此，本次變更不是新增一條平行工程線，而是把既有 Handoff / State / Workpool / Verification / History 閉環補完整。
## Runtime Closure｜2026-09-19

已完成最小契約蒸餾：Trigger → Capability → Routing → Invocation → Context → Execution → Verification → Final / Stop；並定義 Failure → Diagnosis → Retry / Fallback / Re-route / Stop、Runtime Receipt、Agent-level Retry / Re-route / Chain / Context / Cost 邊界，以及 Multi-Skill Composition 的最小接口。

目前只完成規格與 Simulation 邊界；Natural FIELD 尚未宣稱完成。下一游標為自然工作中的 Agent E2E、Failure Recovery、Receipt 完整度與成本／停止邊界驗證。


## 2026-09-19｜Skill → Transformation → Code 實作追蹤規劃

新增規劃：
`藍圖/規劃/Skill-Transformation-Code追蹤與反向除錯規劃-v1.0.md`

本規劃將遊戲實體化階段定義為：

Game Model → Skill → Transformation → Code → Test / Verification → Runtime Evidence

並建立反向除錯：

Runtime → Evidence → Code → Transformation → Skill → Rule / Game Model → Diagnosis → Fix → Re-test

核心目的：重用已驗證的 Skill → Transformation 實作模式，降低程式漂移與不必要 Context；Bug 發生時，優先透過 Trace 定位到 Skill / Transformation / Rule，而不是直接讀取整片程式碼。

目前狀態：【規劃中；尚未施工／尚未 Natural FIELD】。

本規劃不新增大型 Registry、Generator 或 Bug-to-Skill 平台；先以極小 Damage Calculation 案例驗證最小追蹤單位、查詢成本、正反向 Trace 與重新驗證是否成立。


## 2026-09-19｜方案 A 遊戲開發工作區正式規劃

本輪確認：遊戲開發期間不將遊戲能力提前拆成獨立 Domain Runtime。方案 A 定位為「遊戲開發完整能力工作區」，以開發效率優先；中央系統仍提供完整 Agent、Context、Routing、Runtime Closure、Verification、Evidence、Evolution、Change 與其他共用治理能力。

### 運作模型

```
GAME MODE
→ 讀取方案 A
→ 使用中央系統完整必要能力
→ 使用方案 A 的遊戲專用資料 / Skill / Game Model / Evidence
→ 執行遊戲開發
```

其他專案在 GAME MODE 不載入。方案 A 可讀寫，但不得直接改寫中央治理規格。

### 方案 A 資產分層

方案 A 比照主程式的資料分層概念整理遊戲開發資產：

- `0-知識/`：遊戲領域知識
- `1-系統/`：遊戲專用 System / Skill / Game Model
- `2-方案/`：遊戲開發方案、Transformation、實作規劃
- `3-軟體/`：實際遊戲工具或程式
- `應用/`：實際遊戲專案
- `參考資料/`：外部／補充資料

目前只建立已有需求的層級，不預先建立大型空架構。

### 開發期原則

開發期間允許完整使用中央能力，並將已確認屬於遊戲開發的 Skill 與資料集中於方案 A。此分層主要是遊戲資產的整理與工作區邊界，不是增加第二套 Agent / Control Plane / Runtime。

Context 仍採任務需要的最小載入，以控制 Token 與檢索成本；不以此要求開發期建立額外跨層路由。

### 完成後精簡

方案 A 是開發工作區，不是最終發布結構。遊戲完成後才依真實使用 Evidence 執行：

`使用紀錄 → Dependency Audit → 影響分析 → Evidence 整理 → KEEP / MERGE / COMPRESS / ARCHIVE / DELETE → 可重用能力抽取 → 最終精簡`

哪些 Skill 應保留於專案、哪些可成為共用能力、哪些應壓縮或移除，均由完成後的實際證據決定，不在開發期提前判斷。

### 已完成的資產搬移

遊戲附加 Skill 統御與 Skill → Transformation → Code 遊戲實體化規劃已移入方案 A；舊位置已移除並同步檔案索引。

目前入口：
- `專案A/PROJECT.md`
- `專案A/1-系統/遊戲開發附加Skill統御.md`
- `專案A/2-方案/Skill-Transformation-Code追蹤與反向除錯規劃-v1.0.md`

### 本規劃的下一步

下一階段不是再建立遊戲治理層，而是把「GAME MODE → 讀取方案 A」納入主程式的 Mode / Context 啟動規則，先做 Simulation，再於實際遊戲開發時取得 Natural FIELD 證據。

本項屬目前多專案 Agent / 工作區規劃的延伸，不新增第二套 CURRENT、Workpool 或治理 Authority。
