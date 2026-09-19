# 知識管理 Skill（Knowledge Management Skill） v1.2

版本：v1.2
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition】

## 1. Definition
管理可長期引用資料的生命週期、來源、版本與 Derived View；不決定本次任務載入哪些 Context。

## 2. Trigger
- 驗證後資訊具有長期重用價值。
- 更新既有 Knowledge。
- 發現 Source / Version / Lifecycle 問題。
- 建立或更新 Derived View。
- 清理過時或錯誤資料。

一次性結果若無長期價值，不自動寫入 Knowledge。

## 3. Input
Verified Information、Existing Knowledge、Source / Provenance、Version、Lifecycle。

## 4. Output
Knowledge Item
Canonical Source / Provenance
Version
Lifecycle Status
Derived View
Unknowns

## 5. Procedure
Verify
→ Identify Long-term Value
→ Locate Canonical Source
→ Create / Update Knowledge
→ Attach Provenance / Version
→ Set Lifecycle
→ Produce Derived View（必要時）

## 6. Boundary
Knowledge：資料如何保存與管理。
Context：現在載入什麼。
Evidence：資料是否足以支撐。
Evolution：結構是否需要改變。

來源衝突 → Evidence / Verification，不直接覆寫 Canonical。

## 7. Canonical Rule
Derived View ≠ Canonical Source。
Registry ≠ Canonical Source。
不得建立第二套真實資料庫。
UNKNOWN 必須保留，不以推測填補。

## 8. Lifecycle
CURRENT / DEFERRED / HISTORICAL / RETIRED 等狀態依現行 Knowledge 規範使用；狀態變更需保留來源與理由。

## 9. Control Plane
可查詢 Entity / State / Provenance / Authority / Version metadata。
Knowledge 保留實際 Source；Control Plane 只管理關係與狀態 metadata。

## 10. Stop
無長期重用價值 → 不寫入 Knowledge。
Source 未驗證 → Evidence / Verification。
結構變更 → Evolution / Distillation。
