# Skill Control Plane B｜FIELD Registry / Query 驗證規格 v1.0

日期：2026-09-19
工作包：B — Registry View / Control Plane Query
狀態：【FIELD PROTOCOL READY；NATURAL EVIDENCE PENDING】

## 1. 目的

本文件只驗證 B 的 Registry / Query 是否能在自然工作中：

- 以最小必要 Context 找到正確候選
- 正確處理 UNIQUE / MULTIPLE / NONE / INVALID / UNKNOWN
- 在足夠時停止 Query
- 不把 Registry 當 Source of Truth
- 在 Registry Drift / 遺失時由 Source 重建
- 在 Definition Change 後正確同步 Derived View
- 正確區分 DEPENDS_ON 與 AFFECTS

不驗證 A 的 Skill Boundary，也不驗證 C 的 Router / Runtime。

## 2. FIELD 原則

只有自然工作實際發生的 Query / Registry 事件才能形成 FIELD Evidence。

不得：
- 人工製造結果後宣稱 FIELD PASS
- 用 Simulation 取代自然工作
- 沒有實際觀測資料就填寫 Token / 時間 / Accuracy
- 把 Registry 推論當 Source
- 因單一事件直接宣稱整體 B 完成

每筆 Evidence 至少保留：
Case ID / Task / Query Type / Candidate Result / Query Depth / Context / Stop Reason / Source Pointer / Evidence / Result。

## 3. FIELD Case

### B-F1 Identity / Capability / Trigger
自然任務需要尋找既有 Skill。
觀察 Q0/Q1/Q2 是否能在最小 metadata 下定位候選。
記錄：
Candidate、Depth、Stop、NO_MATCH / MATCH / MULTIPLE_MATCH。

### B-F2 I/O / Constraint
自然任務需要排除不相容或不可用 Skill。
觀察 Q3/Q4 是否正確過濾。
不得以名稱相似代替正式 I/O / Constraint。

### B-F3 Multiple Candidate
自然任務自然產生多個候選。
觀察是否：
Minimal Metadata → Minimal Evidence → 仍不明確則 MULTIPLE_MATCH。
不得由 Registry 自行宣判最佳 Skill。

### B-F4 No Candidate
自然任務沒有現成候選。
觀察是否停止 Query 並回退既有 Routing / Agent。
不得自動建立 Skill。

### B-F5 Invalid Candidate
自然工作遇到 Disabled / Invalid Definition / Invalid Dependency / 明確驗證失效候選。
觀察是否排除並保留排除原因。

### B-F6 Query Stop / Cost
記錄自然 Query 的：
- Retrieval Depth
- Context 增量
- Query 次數
- Stop Reason
- 若可觀測則 Token / 時間成本

沒有實測數據時保持 UNKNOWN。

### B-F7 Dependency / Impact
自然變更或依賴查詢發生時，確認：
DEPENDS_ON ≠ AFFECTS。
Impact 必須有 Change Set / AFFECTS relation / Evidence 支持。

### B-F8 Verification / Provenance
自然工作需要確認 Skill 狀態或驗證證據時，觀察：
Simulation 不得升格 FIELD；
UNKNOWN 不得被補成真值；
Source / Derived / Inferred / Unknown 保持區分。

### B-F9 Registry Drift / Rebuild
自然發現 Registry 缺失、過期或不一致時，觀察：
Detect → Source → 必要時 Git History → Derive → Verify → Rebuild → 原 Query 重跑。

若沒有自然 Drift 事件，不得偽造 FIELD 結果；保持 PENDING。

### B-F10 Definition Change Synchronization
自然發生 Skill Definition 變更時，觀察：
Definition → Change Set → Affected Relations → Registry Invalidate / Rebuild → Verification → Reconcile。
確認 Query 可取得新版本。

## 4. FIELD 記錄格式

Case ID：
Task：
Query：
Input：
Expected Scope：
Candidate Result：
Depth：
Context：
Stop Reason：
Source Pointer：
Evidence：
Result：
Token / Time（若可觀測）：
問題：
是否需要 Change Request：

## 5. FIELD 判定

B 不因 Protocol Ready 宣稱 FIELD PASS。

至少需要自然觀察：
1. Candidate 正確性
2. Query Stop
3. Context / Token 成本
4. MULTIPLE / NONE / INVALID 行為
5. Dependency / Impact 邊界
6. Registry Drift / Rebuild
7. Definition Change synchronization

若發現結構性問題：
Evidence → Problem → Proposal → Verification → Change Request。

沒有結構性問題：
維持目前 Query / Registry Contract，不為了產生變更而變更。

## 6. 與 A / C 的隔離

本文件只驗證 B。

A 的 Boundary / Skill Definition 不在本文件判定。
C 的 Router / Runtime Accuracy、Execution、Re-route 不在本文件判定。
跨包接口與 E2E 最終由 D 驗收。

## 7. 目前結果

Registry / Query Static：PASS
Interface Alignment：PASS
FIELD Protocol：READY
Natural FIELD Evidence：PENDING
B Final FIELD：PENDING

## 8. 完成終點

自然工作累積足夠 Evidence，且 Candidate、Stop、Cost、Drift / Rebuild、Definition synchronization 均無未解決結構性問題後，B FIELD 才可判定 PASS。

若發現缺口，建立 Change Request 並重新驗證；不得直接覆寫既有 Evidence。
