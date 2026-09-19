# Control Plane Query 規格

版本：v1.3
日期：2026-09-19
狀態：【Skill Registry B 工作包施工中；Query Contract 已收束】

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
