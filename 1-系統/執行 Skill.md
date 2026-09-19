# 執行 Skill（Execution Skill） v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
執行已確認的動作，不負責取代決策與演化判斷。

## 2. 核心責任
- 依已確認的 Task 與 Action 執行。
- 呼叫必要 Provider / Tool。
- 建立或修改指定文件。
- 回報執行結果與失敗資訊。
- 遵守 repository 文件修改規則。

## 3. Input
Confirmed Action、必要 Context、Provider / Tool。

## 4. Output
- Execution Result
- Changed Files
- Errors
- Operation Evidence

## 5. 邊界
Evolution Management 決定是否與如何改變；Execution 執行已確認變更。
Provider / Tool 是能力來源，不自動成為 Skill。

## 6. 原則
最小必要操作；完成後交給 Verification。

## 7. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`
- `README.md`

## 8. 驗收
文件建立：PASS
實際運作：PENDING
