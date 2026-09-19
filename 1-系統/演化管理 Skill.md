# 演化管理 Skill（Evolution Management Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
處理系統、Skill、文件與結構的正常演化，以及必要時的 Impact / Migration。

## 2. Trigger
- 已確認需要修改既有結構。
- Skill 分類判斷結果為 UPDATE / MERGE / REPLACE / ARCHIVE。
- 依賴、相容性或結構發生變化。
- Failure Pattern 顯示現行結構需要改進。

若只是一次性執行，不進 Evolution。

## 3. 核心責任
KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE。
分析影響。
必要時 Migration。
保留來源與可追溯性。

## 4. Input
Change Request、現有結構、依賴、Verification、Failure Pattern、Actual Usage。

## 5. Output
Evolution Decision
Impact Assessment（條件式）
Migration Plan（必要時）
Changed Scope
Migration Cost（L / M / H）

## 6. Decision Boundary
局部規則或文件修正 → Evolution。
長期重複、責任漂移、結構性成本 → Distillation 評估。
實際修改 → Execution。
修改後 → Verification。

## 7. Impact / Migration
只有相容性、依賴、Namespace、路徑或結構變動時啟動。
沒有影響時跳過，不固定執行。

## 8. 判斷依據
Purpose、Trigger、Input、Output、Responsibility、Mode、Dependency、Context Cost、Execution Cost、Verification、Actual Usage、Overlap、Migration Cost、Failure Pattern、Long-term Maintenance Cost。

## 9. 原則
不得只依名稱、文件相似度、功能數量或主觀偏好決定。

## 10. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`

## 11. 驗收
文件建立：PASS
實際運作：PENDING

## 12. AI Control Plane 整合

涉及結構變更時，可查 Dependency / Impact / Change / Evidence / Lifecycle / Authority。
標準流程：Problem → Impact → Change Set → USER CONFIRM → Modify → Verify → Close。
