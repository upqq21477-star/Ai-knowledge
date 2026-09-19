# 執行 Skill（Execution Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
執行已確認的動作，不取代決策與演化判斷。

## 2. Trigger
只有存在 Confirmed Action 時執行。
若 Action 未確認、依賴未滿足或目標不明，退回 Task Understanding / Evolution / User Required。

## 3. 核心責任
依確認任務執行。
呼叫必要 Provider / Tool。
建立／修改文件。
回報結果與失敗資訊。
遵守 repository 規則。

## 4. Input
Confirmed Action、必要 Context、Provider / Tool。

## 5. Output
Execution Result
Changed Files
Errors
Operation Evidence
Execution Cost（L / M / H）

## 6. 路由
執行完成 → Evidence / Verification。
執行失敗 → Diagnosis。
需要改變方案 → Evolution。
Provider 不可用 → INSUFFICIENT，不自行換成未知工具。

## 7. 邊界
Evolution 決定是否與如何改變。
Execution 執行已確認動作。
Provider / Tool 不自動成為 Skill。

## 8. 原則
最小必要操作；完成後交給 Verification。

## 9. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`
- `README.md`

## 10. 驗收
文件建立：PASS
實際運作：PENDING
