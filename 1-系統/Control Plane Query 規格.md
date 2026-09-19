# Control Plane Query 規格

版本：v1.4
日期：2026-09-19
狀態：【正式規格；Query Contract 已收束；已接入現有 Skill；自然運作 Evidence 持續累積】

## 1 目的

以最低 Context 成本取得完成任務所需的最小後台資訊。

Query 不取代 Skill Routing，不取代 Semantic Router，也不成為 Skill Source of Truth。

## 2 Query Contract

每個 Query 必須明確定義：
- Input：查詢條件與必要識別資訊。
- Output：回傳欄位與狀態。
- Scope：查詢範圍與最大深度。
- Authority：資料來源權威層級。
- Stop Condition：何時停止擴展。
- Filtering：哪些候選必須排除。
- UNKNOWN：資料不足、衝突或無法證明時如何表示。
- Fallback：查不到或無法判定時下一步。

## 3 Skill Registry Query

### Q0 Identity
Input：Skill ID / Name / Path / Type
Output：ID / Name / Family / Path / State / Authority / Version / Lifecycle / Updated
Scope：單一 Entity。
Stop：Identity 已唯一確認。
UNKNOWN：缺少唯一識別資訊時不得猜測。
Fallback：改用 Q1/Q2 等能力或觸發查詢；仍無法定位則 NO_MATCH。

### Q1 Capability
Input：Capability / Responsibility / Purpose
Output：Candidate Skill ID + Name + Capability Summary + State + Version
Scope：Skill Candidate。
Stop：唯一且可用候選；或已確認無候選。
Fallback：多候選進 Q1 擴展或 Q3/Q4 最小消歧。

### Q2 Trigger
Input：Trigger / Observation Terms / Task Type
Output：Candidate Skill ID + Trigger Summary + Boundary + State
Scope：Trigger View。
Stop：唯一且可用候選；或無候選。
不得把單一關鍵字命中直接視為最終路由真值。

### Q3 I/O
Input：Required Input / Expected Output
Output：Candidate Skill ID + Input Summary + Output Summary + Compatibility
Scope：候選 Skill。
Stop：I/O 足以排除不相容候選。
Fallback：仍相近則取得最小 Capability / Boundary 證據。

### Q4 Constraint
Input：State / Lifecycle / Provider / Tool / Mode / Context / Cost / Verification constraint（僅查正式存在者）
Output：Filtered Candidate Set + Exclusion Reason
Scope：候選集合。
Stop：完成必要過濾。
UNKNOWN：不存在正式規則的 Constraint 不得由 Query 臨時創造。

### Q5 Dependency
Input：Skill / Entity ID + depth / breadth limits
Output：直接 DEPENDS_ON 關係 + Target metadata + Evidence / Confidence
Scope：預設直接關係；只有結果不足時才增加深度。
Stop：直接依賴已足夠回答問題。
Fallback：需要遞迴依賴時明確提高 depth；不得無限制遍歷。

### Q6 Verification
Input：Skill / Evidence / Verification target
Output：Verification rule pointer + latest relevant result + Evidence pointer + State
Scope：與目標直接相關的 Verification / Evidence。
Stop：已有足夠證據回答當前驗證問題。
Simulation 不得被回傳為 FIELD。

### Q7 History
Input：Skill / Change / Entity + time / version scope
Output：必要 Version / Change / History pointer
Scope：限定版本或時間範圍。
Stop：已取得回答當前問題所需歷史。
Fallback：若範圍過大，縮小 time / version scope；不得載入完整歷史。

### Q8 Impact
Input：Change ID / Source Entity / Affected Entity
Output：Affected Set + Reason + Evidence + Confidence + Verification
Scope：Change Set 所涉及的直接或經明確規則擴展的影響範圍。
Stop：已取得完成 Change Verification 所需的影響集合。
UNKNOWN：無 Evidence 支持的影響標記 UNKNOWN。
不得把 DEPENDS_ON 直接當作 AFFECTS。

## 4 Semantic Router 前置查詢

Semantic Router 優先只查：
GET CAPABILITY METADATA
GET SKILL METADATA
GET SKILL STATE
GET ROUTING TERMS
GET REQUIRED CONTEXT POINTER

L1 不足以唯一判斷時，才追加：
GET MINIMAL SKILL EVIDENCE

最小證據最多返回路由所需的：
Responsibility / Trigger / Boundary / Input / Output

不得返回完整 Skill Definition。

## 5 Candidate Filtering

正常 Runtime Query 預設排除：
- Disabled / INACTIVE
- Retired / Decommissioned
- Invalid Definition
- Invalid Dependency
- 明確驗證失效者

Deprecated 是否可候選，必須由正式 Lifecycle / Routing 規則提供。
Query 不自行新增 State 或 Routing Policy。

## 6 Query 結果狀態

標準結果至少區分：
MATCH
MULTIPLE_MATCH
NO_MATCH
NO_VALID_CANDIDATE
UNKNOWN
INVALID_QUERY

MULTIPLE_MATCH 不代表 Query 失敗；它表示候選仍需由 Router / Agent 消歧。

NO_MATCH：
停止查詢，回退 Agent / 既有 Routing。

NO_VALID_CANDIDATE：
停止查詢，回退 Agent / 既有 Routing；同時保留排除原因。

UNKNOWN：
停止在目前 scope，不把未知補成真值；必要時由上層決定是否提高 Query 深度。

## 7 Query Stop Rules

唯一候選：
找到唯一且可用 Skill → STOP。

多候選：
只增加必要 metadata → 若仍不足，再取得最小候選證據 → 仍不明確則 STOP + MULTIPLE_MATCH，交 Router / Agent。

無候選：
NO_MATCH → STOP → fallback。

資料無效：
排除 invalid candidate；若無有效候選 → NO_VALID_CANDIDATE → STOP。

Context 不足：
只增加能解除當前不確定性的最小 Query；不得轉成全庫搜尋。

## 8 Retrieval Depth

L0：現有 Context
L1：Entity metadata / State / Authority
L2：直接 Dependency / Impact
L3：Evidence / Provenance / Problem
L4：Source
L5：History

一般 Router：
L0 → L1 → 必要時最小 L2/L3。

足夠即停止。

## 9 Traversal Limits

任何關係查詢必須能限制：
- depth
- breadth
- entity count
- evidence count
- history depth

預設只查直接關係。

## 10 Context 最小化

Query 結果只返回：
必要 Entity
必要關係
必要證據
必要 Source Pointer

不得因存在 Registry 就自動載入 Registry。
Router 階段禁止返回完整 Skill / System / Knowledge。

## 11 Rebuild Query

Registry 不完整：

Registry
→ 找 Source
→ 找 Git History
→ 重建 metadata / relation view
→ Verification
→ Reconcile

Rebuild 結果必須可驗證，且不能反向改寫 Source。

## 12 Change / Impact Query

Skill Definition 修改：

Definition
→ Change
→ Affected Relations
→ Registry Invalidate / Rebuild
→ Verification
→ Reconcile

B 負責 Query / View；不負責修改 Skill Definition。

## 13 Cache

Search / Registry View / Query Result 可快取。

Cache：
- 非 Source of Truth。
- 可刪除。
- 可重建。
- 不得在 Cache 與 Source 衝突時覆寫 Source。

## 14 Drift Query

優先檢查：
1. 目前任務涉及 Entity。
2. 最近修改文件。
3. 已知 Problem。
4. 最近 Verification。
5. Registry 與 Source 的差異。

不把每次 Drift Query 變成全庫掃描。

## 15 Query Cost

Router：
最低成本 metadata；Metadata 不足才追加最小候選證據。

一般工作：
L0-L1。

關係問題：
L2。

異常／驗證：
L3-L4。

歷史研究／大型重構：
L5。

目前只建立成本模型，不宣稱固定 Token / 時間節省比例；FIELD 才能驗證實際收益。

## 16 禁止

- 不全庫預載。
- 不把完整 Graph 放入 Context。
- 不把所有 History 放入 Context。
- 不因查詢便利複製全文。
- 不為 Semantic Router 載入完整 Skill / System / Knowledge。
- 不因多候選而建立大型 Ranking。
- 不因無候選而自動建立 Skill。
- 不把 Query 推論當 Source of Truth。


## B-01 Query Contract

每個 Query 固定：Input / Scope / Authority / Filter / Output / Stop Condition / UNKNOWN 行為 / Fallback。

## B-02 Q0-Q8

Q0 Identity：ID / Name / Family / Path / Source / Authority / Version。缺唯一 ID 不猜，回 Source。

Q1 Capability：Capability / Responsibility / Boundary。缺 Capability 回 UNKNOWN，不以 Name 猜測。

Q2 Trigger：Trigger Summary / Observation Terms / Boundary。不足時 Minimal Evidence → Skill Routing。

Q3 I/O：Input Summary / Output Summary / Compatibility。缺資料標 UNKNOWN，必要時回 Source Definition。

Q4 Constraint：State / Boundary / Required Context / Availability。排除不可用 Entity。

Q5 Dependency：直接 DEPENDS_ON / USES / REFERENCES。未知不猜；Dependency 不等於 Impact。

Q6 Verification：最近有效 Verification / FIELD Evidence。沒有有效 Evidence → UNKNOWN / PENDING；Simulation 不等於 FIELD。

Q7 History：必要 Change / Version / Before / After。只取得回答問題所需最小歷史。

Q8 Impact：Affected Entity / Reason / Evidence / Confidence / Verification。沒有 Evidence 支持 → UNKNOWN。

## B-03 Candidate / Stop

UNIQUE → STOP。
MULTIPLE → Minimal Metadata → Minimal Evidence → 仍不明確則既有 Skill Routing / Agent。
NONE → Agent fallback。
INVALID → EXCLUDED，不進正常 Candidate。

Progressive Retrieval：L0 Task / Context → L1 Entity Metadata → L2 Direct Relation / Minimal Evidence → L3 Evidence / Provenance → L4 Source → L5 History。足以完成目前決策即 STOP。

## B-04 Rebuild / Change

Registry 缺失或 Drift：Detect → Source → Git History（必要時）→ Derive → Verify → Rebuild → 原 Query 重跑。

Definition Change：Definition → Change Set → Affected Relations → Registry Invalidate / Rebuild → Verification。
Query 層只暴露結果，不修改 Definition。

## B-05 C Interface

C 只需消費：GET SKILL METADATA / GET SKILL STATE / GET ROUTING TERMS / GET REQUIRED CONTEXT POINTER / GET MINIMAL SKILL EVIDENCE。

最小結果格式：EntityID / Scope / Authority / Depth / Result / Unknowns / Fallback / SourcePointer。
C 不需要知道 Registry 儲存方式。

## B-06 Boundary

不得全庫預載、複製全文、把 Inferred 當 Source、把 Dependency 當 Impact、因 Multiple Candidate 自動建立 Skill、建立大型 Ranking / Embedding / Vector DB / Server。

## B-07 Current Operating Boundary

已定義 Q0-Q8、Filtering、Stop、NONE fallback、MULTIPLE handling、INVALID handling、Rebuild、Definition Change → Registry Update、Impact Query。
FIELD 仍待自然工作驗證：Context / Token 成本、實際 Stop 深度、Candidate 正確率、Drift detection、Rebuild recovery、Change synchronization。


## C-08 Interface Reconciliation

C 所需的 Skill Interface 以 A 的 Interface Requirements 為上游契約，B 提供 Derived Query View。

正式最小取得鏈：
GET SKILL METADATA
→ GET SKILL STATE
→ GET ROUTING TERMS
→ GET REQUIRED CONTEXT POINTER
→ 必要時 GET MINIMAL SKILL EVIDENCE

最小可路由資料：
ID / Responsibility / Trigger / Boundary / Input / Output / Mode / Lifecycle / Availability / Required Context / Minimal Verification / Source Pointer / Authority / Provenance。

若資料不足：
UNKNOWN → 最小必要 Query → 仍不足則交 Router / Agent；不得自行補值。

C 不需要知道 Registry 儲存結構。
