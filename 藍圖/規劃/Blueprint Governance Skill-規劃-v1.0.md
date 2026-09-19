# Blueprint Governance Skill 規劃 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃中；尚未建立正式 Skill】
定位：藍圖治理／藍圖一致性／藍圖演化管理
前置研究：Architecture Governance、ADR、Dependency Management、Roadmap / Backlog、Architecture Drift、Game Production

---

## 0. 本文件目的

本文件用來建立「Blueprint Governance Skill（藍圖治理 Skill）」的正式規劃。

本 Skill 的任務不是重新建立一套總控架構，而是：

> 當系統出現新規劃、新資料夾、新 Skill、新 System、新流程、新依賴或重大變更時，檢查它是否能正確進入整體藍圖，並判定是否需要更新藍圖地圖、藍圖紀錄與藍圖待辦。

核心問題：

1. 新東西應該放在哪裡？
2. 它與現有能力的關係是什麼？
3. 是否與其他 Skill / System 重複？
4. 是否應該由其他 Skill 協作，而不是新增能力？
5. 是否改變既有工作流程？
6. 是否造成新的依賴或下游影響？
7. 是否需要修改藍圖地圖？
8. 是否需要留下藍圖變更紀錄？
9. 是否產生新的藍圖待辦？
10. 是否造成 Blueprint Drift？
11. 是否改變既有施工順序？
12. 是否已經有足夠證據支持正式納入藍圖？

本 Skill 不負責自行決定所有架構方案；它負責產生結構化檢查、影響分析、協作判定與藍圖變更建議。

---

# 一、研究依據

## 1. Architecture Decision Records

公開 ADR 實踐將重要架構決策視為需要長期保存的知識，通常記錄 Context、Decision、Consequences、Alternatives、Status 等內容。

Microsoft Azure Well-Architected Framework 明確指出：架構是過去決策累積形成的結果，因此 ADR 是追蹤系統如何形成目前狀態的重要紀錄；重大架構決策才需要記錄，不應把每個實作細節都變成 ADR。

來源：
- https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- https://github.com/architecture-decision-record/architecture-decision-record

本 Skill 對應：
Blueprint Change Record。

---

## 2. Decision / Dependency Graph

公開工具 DecisionGraph 將決策、政策、事件與規格建立成可追蹤關係，並以 dependency graph / backlinks 顯示「某決策影響什麼」以及「為什麼形成目前狀態」。

來源：
- https://github.com/decisiongraph/dg

本 Skill 對應：
Blueprint Relationship / Dependency / Impact。

但目前不因此建立 Graph 實體系統。

---

## 3. Game Production / Roadmap / Dependency

Riot Games 公開職務說明中明確包含：
- multi-team work systems
- dependency management
- product / feature roadmap
- milestone / phase
- current / future work status
- strategic alignment

來源：
- https://www.riotgames.com/en/j/6319372

這支持本 Skill 必須處理：
Dependency、Roadmap、Current State、Execution Order。

---

## 4. Architecture Governance / Drift

ADR 生態中已存在：
- architecture views
- fitness functions
- architecture unit testing
- decision guardrails
- decision-to-work traceability

來源：
- https://github.com/architecture-decision-record/architecture-decision-record

本 Skill 對應：
Blueprint Consistency / Drift / Gate。

---

# 二、正式定位

## Skill 名稱

英文：
Blueprint Governance Skill

中文：
藍圖治理 Skill

核心職責：

> 維持「整體藍圖」與「實際系統演化」之間的可追蹤、一致、可解釋關係。

---

# 三、責任邊界

## 本 Skill 負責

1. Blueprint Mapping
2. Blueprint Consistency Check
3. Blueprint Change Impact
4. Blueprint Change Record
5. Blueprint TODO Derivation
6. Dependency / Relationship Analysis
7. Skill / System Overlap Analysis
8. Cross-Skill Collaboration Analysis
9. Blueprint Drift Detection
10. Blueprint Closure Check
11. Blueprint Update Proposal
12. Blueprint Execution Order Analysis

## 本 Skill 不負責

1. 不取代 Skill Registry。
2. 不建立 Skill 本身。
3. 不執行 Skill 的主要業務能力。
4. 不取代 Problem Registry。
5. 不取代 Evaluation。
6. 不取代 Verification。
7. 不取代 CURRENT Baseline。
8. 不直接決定所有 Skill 是否成立。
9. 不因發現概念就直接實體化 Registry / Graph / Automation。
10. 不為了讓 Blueprint 看起來完整而新增系統。
11. 不猜測 UNKNOWN 的架構關係。
12. 不把 Simulation 當成 Real Work Evidence。

---

# 四、與現有系統的責任分工

| 能力 | 主要責任 | Blueprint Governance 關係 |
|---|---|---|
| Skill Registry | Skill 身份、能力、觸發、依賴、輸入輸出、版本、生命週期 | 讀取／比對 |
| Registry Query | 找到 Skill / Capability | 協作輸入 |
| Trigger | 判斷何時啟動某能力 | 檢查新 Skill 是否有合理觸發 |
| Recall | 找到適用能力與資料 | 檢查 Blueprint 是否可被找到 |
| Context | 選擇工作 Context | 檢查新能力是否改變 Context 依賴 |
| Verification | 驗證結果 | 提供 Blueprint 變更證據 |
| Problem Registry | 記錄實際問題 | 提供 Change Signal |
| Evaluation | 比較方案／能力 | 提供是否需要結構變更的證據 |
| CURRENT Baseline | 當前正式狀態 | Blueprint 的重要 Canonical Input |
| Handoff | 跨 AI 恢復工作 | 驗證 Blueprint 是否可被恢復 |
| Evolution | 能力演化 | 接收 Blueprint 變更訊號 |
| Blueprint Governance | 整體結構、關係、變更、待辦、漂移 | 本 Skill 核心 |

核心邊界：

> Registry 管「這個東西是什麼」。
>
> Blueprint Governance 管「這個東西在整體系統中是什麼位置，以及它改變後整體會發生什麼」。

---

# 五、所需功能總表

## BG-01 Blueprint Mapping

目的：
將新 Skill / System / Folder / Process / Plan 映射到現有 Blueprint。

輸入：
- 新增項目
- CURRENT
- Blueprint Map
- Registry / Capability 資料
- 相關依賴

輸出：
- Layer
- Parent
- Related Nodes
- Relationship
- Mapping Confidence
- Unknown

邊界：
若無足夠證據，不得猜測 Mapping。

---

## BG-02 Blueprint Consistency Check

目的：
檢查新變更是否與現有 Blueprint 語義衝突。

檢查：
- Layer 衝突
- Responsibility 衝突
- Workflow 衝突
- Dependency 衝突
- Namespace 衝突
- State / Lifecycle 衝突
- Canonical Source 衝突

輸出：
PASS / CONFLICT / UNKNOWN。

---

## BG-03 Change Impact Analysis

目的：
分析變更造成的直接與間接影響。

至少檢查：
- Direct Impact
- Indirect Impact
- Dependency Impact
- Workflow Impact
- Documentation Impact
- TODO Impact
- Evaluation Impact
- Handoff Impact
- CURRENT Impact

---

## BG-04 Blueprint Change Record

目的：
保存藍圖變更歷史。

最低欄位：
- Change ID
- Date
- Trigger
- Context
- Change
- Reason
- Affected Nodes
- Dependencies
- Consequences
- Evidence
- Previous State
- New State
- Status
- Related Files
- Supersedes / Related

規則：
歷史紀錄不可直接改寫成「最新真相」。
若決策改變，建立新紀錄並連結舊紀錄。

---

## BG-05 Blueprint TODO Derivation

目的：
從 Blueprint 缺口與依賴推導未完成工作。

流程：
Blueprint
→ Missing Node / Missing Relation / Missing Evidence
→ Dependency
→ Candidate TODO
→ Priority
→ Execution Order

注意：
Blueprint TODO 不是普通任務清單。

---

## BG-06 Dependency / Relationship Analysis

目的：
理解：
- depends-on
- uses
- produces
- triggers
- verifies
- replaces
- extends
- conflicts
- supersedes
- belongs-to
- related-to

輸出：
Dependency Chain / Relationship Map。

目前只維持文件／Derived View，不提前建立 Graph Database。

---

## BG-07 Skill / System Overlap Analysis

目的：
避免新增 Skill / System 與現有能力責任重疊。

比較：
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

結果：
- NO OVERLAP
- COLLABORATION
- PARTIAL OVERLAP
- MERGE CANDIDATE
- REPLACE CANDIDATE
- UNKNOWN

重要規則：

> Duplicate ≠ Redundant。

只有責任無法合理區隔且有實際維護成本時，才進入 Merge / Replace 評估。

---

## BG-08 Cross-Skill Collaboration Analysis

目的：
當新 Skill 與既有 Skill 有交集時，判斷是否應協作，而不是重複建立。

分析：
- Trigger 前後關係
- Input / Output
- Shared Context
- Dependency
- Verification
- Handoff
- Failure Handling

輸出：
- Upstream Skill
- Downstream Skill
- Optional Collaborator
- Mutual Dependency
- Forbidden Direct Coupling

---

## BG-09 Trigger Boundary Definition

目的：
為 Blueprint Governance 建立啟動條件，並檢查其他 Skill 是否應先處理。

主要 Trigger：

### T1 新 Skill 提案
啟動。

### T2 新 System 提案
啟動。

### T3 新主要資料夾／架構層提案
啟動。

### T4 修改主要 Workflow
啟動。

### T5 修改跨層 Dependency
啟動。

### T6 新增／刪除／取代重大能力
啟動。

### T7 Blueprint Map 修改
啟動 Change Record。

### T8 發現 Blueprint Drift
啟動。

### T9 Evaluation 證明現有架構不足
啟動。

### T10 Problem Registry 出現反覆結構性問題
啟動。

---

# 六、不應觸發的情況

以下情況原則上不觸發 Blueprint Governance：

1. 單純文字修正。
2. 不改變語義的拼字修正。
3. 單一文件格式整理。
4. 不改變責任的內部實作調整。
5. 單次一般工作失敗。
6. 尚未形成結構性問題的自然錯誤。
7. 純歷史文件整理。
8. 一般內容新增但不改變架構關係。
9. Provider 單次輸出品質差異。
10. 尚無證據支持的架構猜測。

但如果上述修改實際造成：
Layer / Responsibility / Dependency / Workflow / Lifecycle 改變，
則重新進入 Trigger。

---

# 七、與其他 Skill 的協作規則

## 1. 新 Skill

流程：

New Skill Proposal
→ Skill Registry / Classification
→ Blueprint Governance
→ Overlap Analysis
→ Dependency
→ Impact
→ Blueprint Decision

Boundary：

Skill Registry 判斷「Skill 定義」。
Blueprint Governance 判斷「整體位置」。

不得互相取代。

---

## 2. Problem Skill / Problem Registry

Problem 出現：

Problem
→ 是否單次問題？
→ 是否重複？
→ 是否結構性？
→ 若是 → Blueprint Governance

只有結構性證據才改 Blueprint。

---

## 3. Evaluation

Evaluation 發現：

架構不足
→ Change Signal
→ Blueprint Governance

Blueprint Governance 不自行製造 Evaluation 結果。

---

## 4. Verification

Verification 負責：
「變更後是否符合驗收條件」。

Blueprint Governance 負責：
「為什麼需要變更，以及變更影響什麼」。

---

## 5. CURRENT Baseline

CURRENT 是重要輸入。

如果：
Blueprint ≠ CURRENT

不要直接修改其中一個。

先建立：
Drift / Conflict Record。

再判斷 Canonical Source。

---

## 6. Handoff

Blueprint Governance 必須讓新 AI 能理解：

- Blueprint 現況
- 最近變更
- 未完成 Blueprint TODO
- 下一個重要依賴
- 目前是否存在 Drift

但不新增第二套 Handoff。

---

# 八、Blueprint Drift Detection

定義：

> Blueprint 所描述的結構與 CURRENT / Registry / 實際 Repository 狀態不一致。

至少比較：

Blueprint Map
vs
CURRENT
vs
Registry
vs
Relevant Files

結果：

- ALIGNED
- MINOR DRIFT
- STRUCTURAL DRIFT
- CONFLICT
- UNKNOWN

規則：

UNKNOWN 不等於 DRIFT。

沒有足夠資料只能標記 UNKNOWN。

---

# 九、Blueprint TODO 排序規則

不能只用「重要程度」。

至少使用：

1. Dependency
2. Blocking Effect
3. Risk
4. Evidence
5. Scope
6. Reversibility
7. Current Phase

基本排序：

Dependency Blocker
→ Required Foundation
→ High Impact
→ Evidence Gap
→ Optimization
→ Optional Expansion

若 A 依賴 B：

B 必須優先於 A。

若兩者無依賴，可以平行。

---

# 十、Blueprint Change Gate

重大 Blueprint Change 必須至少回答：

1. 改了什麼？
2. 為什麼改？
3. 依據什麼？
4. 影響哪些節點？
5. 是否產生新依賴？
6. 是否與現有 Skill 重疊？
7. 是否需要其他 Skill 協作？
8. 是否改變工作流程？
9. 是否產生新的 TODO？
10. 是否需要 Evaluation？
11. 是否需要 Verification？
12. 是否改變 CURRENT？
13. 是否需要 Handoff 更新？

任何無法回答的重要欄位：

標記 UNKNOWN / EVIDENCE GAP。

不得自行補完。

---

# 十一、重大變更分級

## Level 0：無架構影響

不建立 Change Record。

## Level 1：局部 Blueprint 變更

建立簡短 Change Record。

## Level 2：跨 System / Skill 變更

完整 Impact Analysis。

## Level 3：架構／工作流重大變更

需要：
- Change Record
- Impact
- Dependency
- Evaluation
- Verification Plan

## Level 4：Blueprint 重構

需要：
- Migration Plan
- Validation
- Recovery / Rollback
- CURRENT 更新
- Handoff 更新
- Final Consistency Gate

---

# 十二、與「新增 Skill」的標準流程

新 Skill 不得直接寫入 Blueprint。

流程固定：

New Skill Proposal
→ Skill Definition
→ Existing Capability Search
→ Overlap Analysis
→ Collaboration Analysis
→ Trigger Boundary
→ Dependency Analysis
→ Blueprint Mapping
→ Impact Analysis
→ Evidence Check
→ Blueprint Decision
→ Change Record（必要時）
→ Blueprint TODO（必要時）
→ Registry / Implementation

其中：

「Skill 是否應成立」
與
「Skill 成立後應放在哪裡」

是兩個不同問題。

---

# 十三、核心輸出格式

每次執行 Blueprint Governance，最低輸出：

## A. Classification

- Item
- Type
- Status

## B. Mapping

- Layer
- Parent
- Related Nodes
- Relationship
- Confidence

## C. Overlap

- Existing Skills
- Existing Systems
- Overlap Type
- Collaboration Candidate

## D. Impact

- Direct
- Indirect
- Dependency
- Workflow
- CURRENT
- TODO

## E. Decision

- No Blueprint Change
- Update Blueprint
- Defer
- Need Evidence
- Conflict

## F. Follow-up

- Change Record
- TODO
- Verification
- Evaluation
- Handoff
- Registry Update

---

# 十四、禁止行為

1. 不因新 Skill 名稱相似就判定重複。
2. 不因兩個 Skill 都使用同一 Knowledge 就判定重複。
3. 不因 Blueprint 缺一個節點就自動建立 System。
4. 不因 TODO 存在就立即施工。
5. 不因架構圖看起來不完整就補未知資料。
6. 不猜測 UNKNOWN。
7. 不把歷史文件當 CURRENT。
8. 不直接修改其他 Skill 的責任邊界。
9. 不把 Blueprint Governance 變成全庫 Registry。
10. 不把所有變更都升級成 Architecture Change。
11. 不以單次失敗改 Blueprint。
12. 不以 Simulation 宣稱 Real Work 證據。
13. 不因「業界有人這樣做」直接導入本系統。
14. 不因新模型／新 Provider 出現就直接改 Blueprint。
15. 不讓 Blueprint Governance 反過來強迫工作流程使用不適用的 Skill。

---

# 十五、最小資料模型

第一版只需要：

Blueprint Node：

- Node ID
- Name
- Type
- Layer
- Parent
- Status
- Source
- Related Nodes

Relationship：

- From
- To
- Relation Type
- Evidence
- Status

Change Record：

- Change ID
- Trigger
- Context
- Change
- Reason
- Impact
- Evidence
- Decision
- Related Nodes
- Related Files
- Status

Blueprint TODO：

- TODO ID
- Problem / Gap
- Required Dependency
- Blocking
- Priority
- Evidence
- Status
- Next Action

第一版不建立資料庫。

---

# 十六、第一版不實體化的功能

以下保留為規劃，不直接建立：

- Blueprint Graph Database
- Automatic Full Repository Graph
- Automatic Architecture Refactoring
- Automatic Blueprint Rewrite
- Full Orchestration
- Automatic Architecture Decision Approval
- Automatic Skill Creation
- Automatic Skill Deletion

原因：

目前沒有足夠 Real Work Evidence 證明需要。

---

# 十七、Skill 建立後的驗收案例

## Case A：新增 Skill

確認：
- 是否觸發
- 是否找既有能力
- 是否檢查重疊
- 是否檢查協作
- 是否建立 Mapping
- 是否判斷 Blueprint Change

## Case B：新增 System

確認：
- 是否檢查現有 System
- 是否檢查 Dependency
- 是否檢查 Blueprint Layer
- 是否產生 Impact

## Case C：新增資料夾

確認：
- 是否能區分 Storage / System / Layer
- 是否避免把普通資料夾升級成架構節點

## Case D：修改 Workflow

確認：
- 是否識別跨層影響
- 是否要求 Change Record
- 是否檢查相關 Skill

## Case E：Skill 重疊

確認：
- 是否輸出 Collaboration
- 是否區分 Partial Overlap
- 是否避免直接 Merge

## Case F：Blueprint Drift

確認：
- Blueprint 與 CURRENT 不一致時能否抓出
- UNKNOWN 是否不被誤判為 Drift

## Case G：Dependency TODO

確認：
- 能否從 A depends B depends C 推導 C → B → A
- 無依賴項目能否保持平行

## Case H：重大 Blueprint Change

確認：
- 是否啟動完整 Gate
- 是否產生 Change Record
- 是否要求必要 Evaluation / Verification

---

# 十八、第一版完成條件

Blueprint Governance Skill v1.0 必須能完成：

1. 新 Skill Mapping。
2. 新 System Mapping。
3. 新主要資料夾 Mapping。
4. Overlap Analysis。
5. Collaboration Analysis。
6. Dependency Analysis。
7. Impact Analysis。
8. Blueprint Change 判斷。
9. Blueprint Change Record。
10. Blueprint TODO 推導。
11. TODO Dependency 排序。
12. Blueprint Drift Detection。
13. Trigger Boundary。
14. 與 Registry / Problem / Evaluation / Verification / CURRENT / Handoff 的責任分離。
15. 不因 UNKNOWN 自動補完。
16. 不因單次問題改變 Blueprint。

---

# 十九、目前實作順序

## Stage 1：規格

完成：
- 功能邊界
- 物件
- Trigger
- Boundary
- Relationship
- Change Level
- Output Contract

## Stage 2：文件結構

建立：
- Blueprint Map
- Blueprint Change Record
- Blueprint TODO

但不建立第二套 Blueprint。

## Stage 3：Skill Definition

建立正式：
Blueprint Governance Skill

## Stage 4：協作接口

定義：
- Skill Registry → Blueprint Governance
- Problem Registry → Blueprint Governance
- Evaluation → Blueprint Governance
- Verification → Blueprint Governance
- CURRENT → Blueprint Governance
- Blueprint Governance → Blueprint Map / Change Log / TODO

## Stage 5：模擬驗收

先全部使用 Simulation。

標記：
（代）

## Stage 6：自然工作觀察

進入 Real Work 後：
- 驗證 Trigger
- 驗證 Mapping
- 驗證 Overlap
- 驗證 Collaboration
- 驗證 Drift
- 驗證 TODO

實際運作穩定後取消「（代）」。

---

# 二十、最高原則

> Blueprint 是整體系統的簡略地圖，不是所有細節的資料庫。

> Blueprint Change Record 是演化歷史，不是 CURRENT 狀態替代品。

> Blueprint TODO 是依賴導向的未來工作，不是普通任務堆積。

> Blueprint Governance 是治理層，不是新的總控系統。

> Registry 管物件；Blueprint Governance 管結構。

> Problem 提供問題；Evaluation 提供證據；Blueprint Governance 判斷結構影響。

> 不確定就標 UNKNOWN，不猜。

> 有概念不代表要實體化。

> 有新 Skill 不代表一定要修改 Blueprint。

> 有 Blueprint 變更不代表一定要新增 System。

> 只有當實際證據支持結構改變，才推動架構演化。

最高原則：

「證據決定藍圖，不是藍圖要求系統產生證據。」
