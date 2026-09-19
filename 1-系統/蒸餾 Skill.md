# 蒸餾 Skill（Distillation Skill） v1.2

版本：v1.2
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition】

## 1. Definition
在累積結構性證據後，對重複、重疊、責任漂移與長期成本進行壓縮與重組；不是一般修改，也不是單純刪除歷史。

## 2. Trigger
至少存在持續性證據之一：
- Repeated Duplication。
- Responsibility Drift。
- Structural Cost 持續偏高。
- 多版本演化造成可維護性下降。

單次問題、單次失敗或單一文件過長，不自動觸發。

## 3. Input
多版本資料、Usage Record、Failure Pattern、Structure Cost、Evolution 結果、Dependency / Impact metadata。

## 4. Output
Distillation Candidate
Preserved Core
Merged / Removed Redundancy
Migration / Reference Notes
Verification Target
Unknowns

## 5. Procedure
Collect Evidence
→ Confirm Structural Pattern
→ Compare Responsibilities
→ Define Preserved Core
→ Merge / Compress
→ Migration / Reference
→ Verification

## 6. Boundary
Evolution：正常局部／結構演化。
Distillation：累積證據後的長期結構重組。
Classification：判斷應採何種結構處置。
Execution：實際修改。
Verification：判定結果。

Distillation 不因追求壓縮而破壞責任、來源、版本或可驗證性。

## 7. Decision Rule
證據不足 → DEFER。
若問題可由局部 UPDATE 解決 → Evolution，不進 Distillation。
若已形成持續性結構成本 → Distillation。

## 8. Control Plane
可查 Dependency / Impact / Lifecycle / Usage / Evidence / Change metadata。
Registry 只提供查詢視圖，不作為蒸餾的唯一真實來源。

## 9. Stop
結構性問題尚未被證明 → DEFER。
Preserved Core 與 Change Scope 明確 → 交 Evolution / Execution。
蒸餾完成 → Evidence / Verification。
