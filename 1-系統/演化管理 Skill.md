# 演化管理 Skill（Evolution Management Skill） v1.2

版本：v1.2
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition】

## 1. Definition
管理已確認的系統、Skill、文件與結構變更，負責 Change Scope、Impact 與必要 Migration；不負責實際修改。

## 2. Trigger
- Skill Classification 結果為 UPDATE / MERGE / REPLACE / ARCHIVE。
- 已確認需要修改既有結構。
- Dependency、Compatibility、Namespace、Path 或結構發生變化。
- Failure Pattern 有充分證據顯示現行結構需要改進。

一次性執行不進 Evolution。

## 3. Input
Change Request、Current Definition、Dependencies、Verification、Failure Pattern、Actual Usage、Authority。

## 4. Output
Evolution Decision
Change Set
Impact Assessment（必要時）
Migration Plan（必要時）
Changed Scope
Migration Cost（L / M / H）

## 5. Procedure
Change Request
→ Validate Authority
→ Define Change Set
→ Check Impact Trigger
→ Migration（必要時）
→ USER CONFIRM
→ Execution
→ Verification
→ Close

## 6. Impact / Migration Boundary
只有相容性、依賴、Namespace、路徑、跨文件／跨 Skill 關係改變時啟動 Impact / Migration。
沒有影響時明確記錄 Not Required，不強制建立分析。

## 7. Responsibility Boundary
Classification：決定應不應改、改成什麼類型。
Evolution：定義怎麼安全改與影響範圍。
Execution：實際修改。
Verification：判定修改是否正確。
Distillation：長期結構壓縮與重組。

## 8. Rules
不得只依名稱、相似度、功能數量或主觀偏好決定。
保留 Source、Change Set、Version、Migration 與可追溯關係。
未經 USER CONFIRM 的結構變更不得直接執行。

## 9. Control Plane
可查 Dependency / Impact / Change / Evidence / Lifecycle / Authority。
Control Plane 提供 metadata，不取代修改後的 Source 文件。

## 10. Stop
無需結構變更 → Close。
Change Set 已明確 → 交 Execution。
需要使用者決策 → USER_REQUIRED。
