# Context 管理 Skill（Context Management Skill） v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
決定目前任務需要載入哪些 Context，控制上下文邊界與成本。

## 2. 核心責任
- 判斷必要文件與資料。
- 控制 Context 載入範圍。
- 避免預載整個 repository。
- 發現來源衝突時回到現行入口與 Canonical Source。
- 在上下文重置後恢復必要工作狀態。

## 3. Input
Task Definition、目前工作狀態、Repository 入口與文件索引。

## 4. Output
- Required Context
- Context Boundary
- Loaded Sources
- Missing Context
- Conflict Flags

## 5. 邊界
Knowledge Management 管資料生命週期；Context Management 管目前任務載入什麼。

## 6. 成本原則
只載入當前任務必要內容，降低 Context Cost。

## 7. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `README.md`
- `1-系統/Agent Skill.md`

## 8. 驗收
文件建立：PASS
實際運作：PENDING
