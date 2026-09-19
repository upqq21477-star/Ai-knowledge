# 演化管理 Skill（Evolution Management Skill） v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
處理系統、Skill、文件與結構的正常演化，以及必要時的 Impact / Migration。

## 2. 核心責任
- 判斷 KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE。
- 分析變更影響。
- 判斷是否需要 Migration。
- 只有相容性、依賴或結構變動時才啟動 Impact / Migration。
- 保留來源責任與可追溯性。

## 3. Input
Change Request、現有結構、依賴、驗證結果、Failure Pattern。

## 4. Output
- Evolution Decision
- Impact Assessment（條件式）
- Migration Plan（必要時）
- Changed Scope

## 5. 邊界
Execution 不決定要不要改；Evolution Management 不直接取代執行。

## 6. 決策規則
不得只依名稱、文件相似度、功能數量或主觀偏好。
至少比較 Purpose、Trigger、Input、Output、Responsibility、Mode、Dependency、Context Cost、Execution Cost、Verification、Actual Usage、Overlap、Migration Cost、Failure Pattern、Long-term Maintenance Cost。

## 7. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`

## 8. 驗收
文件建立：PASS
實際運作：PENDING
