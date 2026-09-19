# Control Plane Registry 規格

版本：v1.2
日期：2026-09-19
狀態：【正式規格；Derived View / Query 已接入現有 Skill；自然運作 Evidence 持續累積】

## 1 Entity

Registry 不建立第二套 Skill Source of Truth；Skill Definition 仍是 Skill 的正式來源。

一般 Entity 欄位：
ID / Type / Name / Path / State / Acceptance / Authority / Version / Lifecycle / Source / Updated / Confidence

Type：
Rule / Knowledge / Memory / System / Skill / Plan / Application / Problem / Evidence / FIELD / Change / Handoff / CURRENT / Document / Tool / Model / Provider / Runtime / Capability

Skill Registry View 的最小欄位：
ID / Name / Family / Capability / Trigger Summary / Input Summary / Output Summary / State / Acceptance / Version / Lifecycle / Dependency Summary / Verification Summary / Path / Updated

可選但不得預設載入：
Authority / Source Pointer / Confidence / Usage Summary / Change Pointer / Impact Pointer

完整 Skill Definition、Execution、Failure、完整 Verification Procedure、Evidence、Trace、Change History 不屬於一般 Router View；需要時由 Query 展開。

## 2 Skill Registry View 邊界

Skill Registry View = 可查詢的衍生 metadata view。

它回答：
「有哪些 Skill 候選、目前是否可用，以及下一步需要查什麼？」

它不回答：
「這個 Skill 的完整執行方法是什麼？」

因此：
Source of Truth = Skill Definition
Registry View = Derived View
Query = 取得必要 View / Relation / Evidence
Runtime = 讀取已選 Skill 的正式 Definition

Registry 遺失不代表 Skill 遺失。

## 3 State

第一版採既有需求可證明的狀態：
CURRENT / HISTORICAL / PENDING / DEFERRED / CLOSED / UNKNOWN / ACTIVE / INACTIVE

正常 Runtime Candidate Filtering 預設排除：
- Disabled / INACTIVE
- Retired / Decommissioned（若由正式 Lifecycle 映射）
- Invalid Definition
- Invalid Dependency
- 明確驗證失效者

Deprecated 是否仍可候選，不由 Registry 自行決定；必須由正式 Lifecycle / Routing 規則定義。

不得因 Registry 建立而新增 PINNED / DORMANT / RETIRED 等未被需求證明的 State。

## 4 Lifecycle

Created → Verified → FIELD → Active → Updated → Superseded → Historical

Lifecycle 描述演變，不取代 State。

Acceptance 另依《工程狀態與驗收最小規則》表示【未】／【驗】／【代】，不與 State 或 Lifecycle 合併。
例如：State=ACTIVE、Acceptance=【代】、Lifecycle=Active。不得把 ACTIVE + 【代】儲存為單一 State。

## 5 Relation

第一版：
DEPENDS_ON / USES / REFERENCES / DERIVED_FROM / VERIFIED_BY / SUMMARIZES / SUPERSEDES / AFFECTS / PART_OF / PRODUCES / CONSUMES

欄位：
Source / Relation / Target / Evidence / Confidence / Updated

Dependency 與 Impact 必須分開：
- DEPENDS_ON = 執行／結構上的直接依賴。
- AFFECTS = 變更後經 Evidence 支持的影響關係。
- 「A 依賴 B」不得直接推導成「修改 A 一定影響 B」。

## 6 Impact

欄位：
Change / Source Entity / Affected Entity / Reason / Evidence / Confidence / Verification

Impact Query 必須能指出：
1. 受影響 Entity。
2. 影響理由。
3. 依據 Evidence。
4. 是否已 Verification。

沒有證據時標記 UNKNOWN，不把猜測寫成 Impact。

## 7 Change

欄位：
Change ID / Reason / Source Problem / Affected Set / Before / After / Verification / Status / Date

Skill Definition 修改流程：
Definition
→ Change
→ Affected Relations
→ Registry Invalidate / Rebuild
→ Verification
→ Reconcile

B 只負責 Registry View / Query 的同步，不修改 Skill Definition 本身。

## 8 Evidence

欄位：
Evidence ID / Type / Source / Target / Result / Date / Confidence / Related Problem / Related Change

Evidence Type：
FIELD / SIMULATION / REAL_WORK / VERIFICATION / RESEARCH / EXTERNAL_SOURCE / HUMAN_DECISION

Simulation 不等於 FIELD。

## 9 Provenance

資料形成鏈：
Source → Event → Analysis → Decision → Change → Verification

Registry 欄位必須可區分：
SOURCE / DERIVED / INFERRED / UNKNOWN

DERIVED / INFERRED 不得偽裝成 SOURCE。

## 10 Authority

Authority：
CURRENT / PRIMARY / DERIVED / SUMMARY / REFERENCE / HISTORICAL

Skill Definition 優先於 Registry。
正式 Evidence 優先於 Summary。
Registry 不得覆寫 Source。

## 11 Query / Progressive Retrieval

Skill Registry 的基本資料流：

Task / Query
→ Trigger / Identity
→ Candidate Skill ID
→ Summary
→ Capability / I/O
→ Relation / Evidence
→ Impact / History（需要時）

正常 Router View 預設只提供最小 metadata。

停止條件：
目前資料已足以完成當前決策 → STOP。

不得因「完整」而自動載入完整 Skill、System、Knowledge 或 History。

## 12 Candidate Filtering

Registry 提供候選，不宣判「最佳 Skill」。

Filter 順序：
1. Identity / Type
2. State / Lifecycle 可用性
3. Definition validity
4. Dependency validity
5. Verification validity
6. Trigger / Capability / I/O 等查詢條件

Multiple Candidate：
回傳候選與必要 metadata，由 Router / Agent 依正式 Routing 規則決定。

No Candidate：
回傳 NO_MATCH + 查詢摘要 + 可用 fallback pointer；不得因無候選自行建立 Skill。

Invalid Candidate：
排除並保留 invalid reason；若所有候選均無效，回傳 NO_VALID_CANDIDATE。

## 13 Registry Family

不得建立單一巨大 Skill Registry。

依查詢頻率與責任可拆成：
- Identity / Trigger
- Summary / Capability
- I/O
- Relation / Dependency / Usage
- Verification / Evidence
- Change / Impact / Evolution

拆分不代表建立多套 Source of Truth；所有 View 均由同一套正式 Source 衍生。

## 14 Rebuild

衍生 Registry 不完整或遺失：

Registry
→ 找 Source
→ 依 Source + Git History + Evidence 重建
→ Verification
→ Registry Reconcile

必須滿足：
Registry 遺失 ≠ Skill 遺失。
重建後 ID / Path / Version / Authority 不得無依據漂移。

Rebuild 不得反向修改 Skill Definition。

## 15 Trace

欄位：
Trace ID / Task / Routing / Context / Skill / Tool / Result / Verification / Date

只保存具有長期診斷價值的最小摘要。

Trace 不是 Skill Definition，也不是 Registry Source。

## 16 不得越權

本規格不建立：
- Ranking Engine
- Embedding / Vector Search
- Graph Database
- Large Capability Registry
- Autonomous Discovery
- Skill Runtime

需要 Ranking / Vector / Graph 時，另建 Future Work / Change Request；不得在 B 階段偷偷加入。

## 17 外部方法採用邊界

外部 Agent Skills 實踐共同採用 progressive disclosure：先提供 Skill 的名稱與描述，再按需載入完整指令與附加資源。這支持本 Registry 將 Router View 壓縮在 metadata 層，而不是預載完整 Skill。

本庫不直接複製外部實作；只採用其與本庫既有 Context 最小化原則一致的設計證據。

參考：
- Anthropic Agent Skills
- Agent Skills open specification
- Microsoft Agent Skills


## B-01 Skill Registry View Contract

Skill Entity 最小 View：ID / Name / Family / Capability / Responsibility Summary / Trigger Summary / Input Summary / Output Summary / Boundary Summary / Mode / State / Acceptance / Version / Lifecycle / Dependency Summary / Verification Summary / Required Context Pointer / Authority / Provenance / Path / Updated。

Registry View 是 Derived metadata，不取代 Skill Definition。

Provenance：SOURCE / DERIVED / INFERRED / UNKNOWN。INFERRED、UNKNOWN 不得偽裝成 SOURCE。

Router View 不預載：完整 Execution / Failure Procedure / 完整 Verification Procedure / Evidence / Trace / Change History。

## B-02 Candidate Filtering

Runtime Query 預設排除：INACTIVE、Invalid Definition、Invalid Dependency、明確驗證失效。
Deprecated 是否可候選由正式 Lifecycle / Routing 規則決定，不由 Router 臨時猜測。

Candidate 結果：UNIQUE / MULTIPLE / NONE / INVALID。
Registry 提供候選與必要 metadata，不宣判最佳 Candidate。

## B-03 Dependency / Impact Boundary

DEPENDS_ON 不等於 AFFECTS。
Impact 必須有 Change Set、AFFECTS relation 或 Evidence 支持；不得由名稱相似或 Dependency 自動推導 Impact。

## B-04 Rebuild

Skill Definition → derive metadata → Registry View → Query。

Registry 遺失或 Drift：Registry → Source → Git History（必要時）→ derive → Verification → Rebuild。
Registry 損壞不代表 Skill 遺失。

## B-05 Drift

優先檢查：Query 涉及 Entity、最近 Definition Change、最近 Verification、已知 Problem、Registry / Source mismatch。
不做每次全庫掃描。

至少區分：Missing Registry Entry / Stale Metadata / Broken Relation / Authority Conflict / Verification Drift。

## B-06 Query Result Boundary

Query 只返回必要 Entity、Relation、Evidence、Source pointer，以及 Scope / Depth / UNKNOWN / Fallback。

## B-07 C Interface

提供：GET SKILL METADATA / GET SKILL STATE / GET ROUTING TERMS / GET REQUIRED CONTEXT POINTER / GET MINIMAL SKILL EVIDENCE / GET DEPENDENCIES / GET VERIFICATION / GET IMPACT / GET CHANGE / GET PROVENANCE / REBUILD SKILL REGISTRY。

Query Result 最小格式：Entity ID + Scope + Authority + Depth + Result + UNKNOWN/Fallback + Source Pointer。

## B-08 Scope Boundary

B 不重新定義 Skill Contract，不決定 Skill / Agent / Workflow 邊界，不建立大型 Ranking、Embedding、Vector Search、Graph DB、Capability Registry 或 Skill Runtime。

## B-09 Current Evidence Gap

目前已具備：Registry View Contract、Query Contract、Candidate Filtering、Query Stop、No Candidate Fallback、Multiple Candidate Handling、Invalid Skill Handling、Dependency Query、Registry Rebuild、Definition Change → Registry Update、Impact Query。

後續只從自然運作累積 Query 成本、Stop 深度、Candidate 正確性、Drift / Rebuild 恢復與 Definition Change synchronization Evidence，不另建測試流程。


## C-07 Interface Reconciliation

A 提供的 C Interface 要求：
Candidate Skill ID / Responsibility / Trigger / Boundary / Input / Output compatibility / Required Context pointer / Mode / Lifecycle / Availability / Minimal Verification target / Source pointer。

B 對 C 的正式輸出因此固定映射為：
- ID → EntityID
- Responsibility / Capability → Capability / Responsibility Summary
- Trigger → Trigger Summary / Routing Terms
- Boundary → Boundary Summary
- Input / Output → Input Summary / Output Summary
- Required Context → Required Context Pointer
- Mode → Mode
- Lifecycle / Availability → Lifecycle / State
- Minimal Verification → Verification Summary / Minimal Skill Evidence
- Source → Source Pointer
- Authority / Provenance → Query Result metadata

若某欄位不存在或無證據，必須回 UNKNOWN，不得由 Router 補猜。

本次只做 Interface Reconciliation，不重新定義 A 的 Skill Contract。
