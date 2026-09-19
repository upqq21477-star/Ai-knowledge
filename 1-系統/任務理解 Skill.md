# 任務理解 Skill（Task Understanding Skill） v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
將使用者輸入轉成可執行的任務定義，不負責執行主要工作。

## 2. 核心責任
- 確認任務目標。
- 區分要求、限制、輸出要求與完成條件。
- 識別任務中明確與未知資訊。
- 不因缺資料而自行補猜。
- 判斷是否需要 Context、Research、Verification 或其他 Skill。

## 3. Input
使用者任務、既有工作狀態、必要規則與已知 Context。

## 4. Output
最小可執行 Task Definition：
- Goal
- Required Output
- Constraints
- Known Facts
- Unknowns
- Verification Target
- Next Action

## 5. 邊界
不取代 Research、Context Management、Verification、Execution。
不因名稱相似而自行建立新 Skill。

## 6. 原則
先理解責任，再選擇能力；未知保持 UNKNOWN。

## 7. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`

## 8. 驗收
文件建立：PASS
實際運作：PENDING
