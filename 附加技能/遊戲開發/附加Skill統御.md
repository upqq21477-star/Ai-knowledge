# 遊戲開發附加 Skill 統御 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃基線；Simulation 待驗；Natural FIELD 待證】

## 1. 定位

本 Skill 是「遊戲開發附加 Skill 層」的統御 Skill。

它不屬於中央 Core System 的一般工作 Skill，也不取代 Agent、AI Control Plane、Skill Registry、Runtime Closure 或中央 Skill Governance。

它負責管理一組只在遊戲開發／特定附加領域需要的 Skill，讓這些 Skill 可以像積木一樣被建立、組合、查詢、停用、驗證與回收。

核心原則：

> 中央系統管理「AI 如何工作」；
> 附加 Skill 統御管理「某個附加領域需要哪些能力」；
> 專案管理「這款遊戲實際用了什麼」。

## 2. 為什麼需要獨立

遊戲開發會逐漸產生大量領域能力，例如：

- Game Concept
- Game Model
- Game System Design
- Combat Calculation
- Attack Pattern
- Balance Analysis
- Progression
- Economy
- Level Design
- Game AI
- Simulation
- Playtest Analysis
- Game Verification
- Skill → Transformation
- Transformation → Code
- Runtime → Skill Reverse Trace

這些能力不是中央 AI 作業系統本身的必要核心。

若全部直接加入中央 Skill 層，中央系統會逐漸被單一應用領域污染，Context、Routing、Registry 與維護成本也會增加。

因此建立正交的「附加 Skill 層」。

## 3. 分層

### L0 中央治理

負責：

Agent
Control Plane
Runtime Closure
Skill Classification
Evolution
Evidence
Verification
Lifecycle
Change
Authority

### L1 附加 Skill 統御

本 Skill 負責：

附加 Skill Catalog
→ Capability 分類
→ Skill 組合
→ Context 範圍
→ 依賴
→ 版本
→ 啟用／停用
→ 驗證狀態
→ 使用紀錄
→ 提升／降級／回收建議

### L2 領域附加 Skills

例如：

Game Concept
Game System
Combat
Balance
Simulation
Transformation
Code Trace
Playtest

### L3 專案 Skill

只服務單一遊戲。

例如：

DEADFLOOR Spatial Threat Analysis

### L4 實體化

Game Model
→ Transformation
→ Code
→ Runtime
→ Evidence

## 4. 與中央 Skill 的邊界

中央 Skill：

- 跨領域
- 不依賴單一遊戲
- 屬於 AI 基礎工作能力
- 具有中央治理價值

附加 Skill：

- 屬於特定領域
- 可整組啟用／停用
- 不需要時不載入
- 可以依領域自行組合
- 預設不修改中央 Skill

專案 Skill：

- 只服務特定專案
- 不自動進入附加 Skill 層
- 不自動進入中央 Skill 層

升格路徑：

Project Skill
→ 使用 Evidence
→ Generalization
→ Evaluation
→ 附加 Skill 候選

附加 Skill
→ 跨多專案 Evidence
→ Generalization
→ Evaluation
→ 中央 Skill 候選

任何升格都必須經既有 Evolution / Verification 治理。

## 5. 統御責任

本 Skill 不直接執行所有遊戲工作。

它負責：

1. 判斷任務是否需要遊戲附加能力。
2. 找出需要的附加 Skill。
3. 建立最小 Skill 組合。
4. 載入必要 Context。
5. 管理 Skill 之間的依賴與順序。
6. 確認中間輸出已驗證後才交給下一 Skill。
7. 記錄使用與 Evidence。
8. 發現附加 Skill 不足時提出 Capability Gap。
9. 防止不必要 Skill 載入。
10. 將可重用成果送入既有 Evolution 流程，而不是直接修改中央系統。

## 6. Skill 組合

附加 Skill 不是固定流水線。

只有當任務真的需要時才組合。

例如：

Game Design
→ Game Model
→ Combat
→ Simulation
→ Verification

Coding：

Game Model
→ Skill
→ Transformation
→ Code
→ Test

Bug：

Runtime
→ Evidence
→ Code
→ Transformation
→ Skill
→ Rule
→ Diagnosis

未使用的 Skill 不進 Context。

## 7. Skill 與 Game Model 的區分

Game Model 是遊戲內容與規則。

Skill 是操作 Game Model 的能力。

例如：

Game Model：
Attack = 30
Defense = 10

Skill：
Damage Calculation

Transformation：
Damage = max(Attack - Defense, 0)

Code：
實際引擎函式

Evidence：
Simulation / Test / Runtime 結果

不得把四者混成同一資產。

## 8. Transformation 管理

附加 Skill 統御可管理「Skill → Transformation」關係，但不把所有 Code 放入統御 Skill。

Transformation 的最小概念：

- Transformation ID
- Skill ID / Version
- Rule / Model Reference
- Implementation Target
- Pattern
- Code Reference
- Verification Reference
- Evidence
- Version
- Dependency / Impact
- Provenance
- Last Validated

優先使用已驗證 Transformation。

沒有適用 Pattern 時才產生候選新 Transformation。

候選必須經 Verification 後才可成為可重用 Pattern。

## 9. Context 與 Token

附加 Skill 層採按需載入：

Task
→ Domain Detection
→ Candidate Skills
→ Minimum Skill Set
→ Required Context
→ Execute

不得因附加 Skill 存在就全部載入。

附加 Skill Catalog 可以很大；Runtime Context 必須保持最小。

## 10. 反向除錯

當遊戲 Runtime 出現問題：

Runtime
→ Evidence
→ Code
→ Transformation
→ Skill
→ Rule
→ Game Model

統御 Skill 負責協助找到正確的附加能力與追蹤入口。

不能直接假設問題一定是 Code Bug。

## 11. 失敗處理

- 沒有適用附加 Skill → 回到 Task Understanding / Capability Gap。
- 多個 Skill 衝突 → 回到中央 Routing / Classification 規則。
- Skill 輸出未驗證 → 不交給下一 Skill 作為已確認事實。
- Transformation 不相容 → 搜尋其他 Pattern 或進入候選建立。
- Project Skill 與附加 Skill 邊界不清 → 保持 Project Scope，先不升格。
- 跨專案重用證據不足 → 保持附加／專案層，不升格中央。

不得因一次缺口就建立大型新 Skill。

## 12. 生命週期

候選：
RESEARCH
→ CANDIDATE
→ SIMULATION
→ FIELD
→ ACTIVE

無使用或證據不足：

DORMANT / DEFERRED

淘汰：

RETIRED

這些狀態必須與中央既有 State / Acceptance Governance 相容，不建立第二套 State Authority。

## 13. 與多專案模式

中央：

提供治理、方法、通用 Skill、驗證與研究方法。

附加 Skill：

提供遊戲開發領域能力集合。

Project：

只載入實際需要的附加 Skill 與自己的 Game Model / Data / Evidence。

理想 Context：

Central Framework（必要部分）
+
Game Add-on Skills（必要部分）
+
Current Project
+
Current Task

其他專案不載入。

## 14. 本 Skill 不負責

- 不取代中央 Agent。
- 不建立第二個 Control Plane。
- 不建立第二個 CURRENT。
- 不建立第二個 Workpool。
- 不建立第二個 Skill Registry Authority。
- 不直接修改中央 Source of Truth。
- 不自動把專案 Skill 升格中央。
- 不要求所有遊戲使用全部附加 Skill。
- 不預先建立大量遊戲 Skill。
- 不把 Code 當作唯一 Source of Truth。

## 15. 最小驗收案例

S01：只需要戰鬥計算時，不載入經濟／任務／地圖 Skill。

S02：Game Concept → Game Model → Combat → Verification 可以形成最小組合。

S03：Project-specific Skill 不會自動進入中央。

S04：已驗證 Transformation 優先重用。

S05：Runtime Bug 可以由 Code 反向追到 Transformation / Skill / Rule。

S06：附加 Skill 缺口可以提出 Capability Gap，而不是直接修改中央。

S07：附加 Skill 統御不會成為第二個 Agent / Control Plane。

S08：Context 只載入目前任務必要的附加能力。

以上先作 Simulation；實際 FIELD 證據後再調整。

## 16. 與目前新增規劃的關係

本 Skill 統御：

《Skill → Transformation → Code 追蹤與反向除錯規劃》

以及未來其他 Game Development Add-on Skills。

它不把上述規劃全部變成 Skill；只管理其中實際形成 Skill 的能力。

最高原則：

> 中央系統保持通用；附加 Skill 按需載入；專案資料保持隔離；可重用能力靠 Evidence 升格。
