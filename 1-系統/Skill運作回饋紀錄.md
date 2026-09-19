# Skill 運作回饋紀錄 v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作累積資料】
用途：把實際運作結果回饋給 Skill 分類判斷、演化與蒸餾。

## 1. 使用紀錄 Usage Record

每次實際使用可記錄：

- Record ID
- 日期
- Task
- Skill
- Trigger
- Mode
- Input Scope
- Output
- Result：PASS / FAIL / INSUFFICIENT
- Context Cost：L / M / H
- Execution Cost：L / M / H
- Notes

## 2. 失敗紀錄 Failure Record

只有發生可分析失敗時建立：

- Failure ID
- Task
- Skill
- Mode
- Expected
- Actual
- Failure Type：Data / Context / Research / Routing / Skill / Provider / Execution / Verification
- Cause
- Impact
- Correction
- Preventive Rule
- Recurrence
- Status

## 3. Skill 生命週期判斷資料

累積資料用於：

Actual Usage
Failure Pattern
Context Cost
Execution Cost
Migration Cost
Maintenance Cost

不得只用單次事件決定 REPLACE / ARCHIVE。

## 4. 回饋路由

Usage / Failure
→ Evidence / Verification
→ Skill 分類判斷 或 Evolution
→ 必要時 Distillation
→ 修改
→ Execution
→ Verification
→ 再記錄

## 5. 成本規則

第一版只記 L / M / H。
尚無可靠數據時標記 UNKNOWN，不製造精確數字。

## 6. 驗收

格式建立：PASS
實際紀錄：PENDING
多案例回饋：PENDING
可支援 Skill 決策：PENDING
