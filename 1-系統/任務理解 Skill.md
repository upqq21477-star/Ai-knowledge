# 任務理解 Skill（Task Understanding Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
將使用者輸入轉成可執行任務定義，不負責執行主要工作。

## 2. Trigger
使用者提出新任務、修改需求、目標不明、完成條件不明或任務邊界發生變化時觸發。

若任務已具備明確 Goal / Output / Constraint，不重複拆解。

## 3. 核心責任
- 確認任務目標。
- 區分要求、限制、輸出與完成條件。
- 識別 Known / Unknown。
- 不因缺資料自行補猜。
- 判斷是否需要 Context、Research、Verification 或其他 Skill。

## 4. Input
使用者任務、既有工作狀態、必要規則與已知 Context。

## 5. Output
Goal
Required Output
Constraints
Known Facts
Unknowns
Verification Target
Next Action

## 6. 路由
Goal 不清 → 補充 Task Definition。
需要資料 → Research。
需要資料選擇 → Context。
需要判斷正確性 → Evidence / Verification。
已確認動作 → Execution。
需要改變 Skill / 結構 → Skill 分類判斷 / Evolution。

## 7. 邊界
不取代 Research、Context、Verification、Execution。
不因名稱相似建立新 Skill。

## 8. 失敗
若無法確定任務目標 → USER_REQUIRED 或 UNKNOWN，不猜測。

## 9. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`

## 10. 驗收
文件建立：PASS
實際運作：PENDING
