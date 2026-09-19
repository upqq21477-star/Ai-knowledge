# Skill 分類判斷 Skill（Skill Classification & Lifecycle Judge） v1.3

版本：v1.4
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition；自然運作 Evidence 持續累積】

## 1. Definition
判斷新能力、新 Skill 候選或既有 Skill 結構變更應採 KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE。

本 Skill 不負責一般任務的 Skill Routing，也不直接修改檔案。

## 2. Trigger
- 新 Skill 候選。
- 新能力與既有 Skill 疑似重疊。
- Provider / Tool / Model 被提出為 Skill。
- Skill 責任膨脹、重複、失效或漂移。
- Failure Pattern 顯示邊界可能錯誤。
- Actual Usage 長期改變。
- 需要融合、更新、取代或封存。

一般工作只是選擇既有 Skill → Skill Routing，不觸發本 Skill。

## 3. Input / Output
Input：Candidate、Research D3 結果、既有 Skill metadata、Usage、Failure Pattern、Dependencies、Cost。
Output：Candidate、Existing Match、Responsibility Comparison、Classification、Action、Reason、Unknowns、Dependencies、Migration Needed、Verification Target。

## 4. Classification Procedure
Candidate
→ 排除 Task / Context / Capability / Retrieval / Routing / Provider / Verification 問題
→ Responsibility Boundary
→ Existing Match
→ Mode / Workflow / Shared Capability / Reference 判斷
→ Independent Responsibility 判斷
→ Classification
→ Evolution

「路由不到」本身不是建立 Skill 的證據。

## 5. Classification Rules
Capability：完成什麼。
Provider：誰提供。
Tool：如何操作。
Mode：同一責任的不同運作方式。
Workflow：多個既有責任的組合。
Skill：可重複且可獨立路由的工作責任。
Reference / Rule / Knowledge：提供依據。

新 Provider、Tool、Model、名稱或單次失敗不足以建立 Skill。

## 6. Decision Criteria
Purpose、Trigger、Input、Output、Responsibility、Mode、Dependency、Context Cost、Execution Cost、Verification、Actual Usage、Overlap、Migration Cost、Failure Pattern、Maintenance Cost。

缺資料 → UNKNOWN。

## 7. Actions
KEEP：獨立責任且不重疊。
MERGE：可由既有 Skill + Mode 承接。
UPDATE：責任仍正確，只需修改規則。
REPLACE：已有充分證據證明新結構承接舊責任。
REFERENCE：非工作責任。
DEFER：證據不足。
ARCHIVE：退出現行結構但保留歷史。

建立新 Skill 必須有獨立 Responsibility、Trigger / Routing Need、Input / Output，且無合理既有承接方式。

## 8. Routing
新結構候選 → Research D3 → 本 Skill。
確認結構變更 → Evolution → Execution → Evidence / Verification。
長期重複結構成本 → Distillation 評估。

## 9. Control Plane
查詢 Skill Identity、Lifecycle、Dependency、Impact、Evidence、Change、Authority。
Registry 是 derived metadata，不是 Source of Truth。

## 10. Stop
證據不足 → DEFER。
Classification 已足以形成 Change Request → 停止，不直接修改。
