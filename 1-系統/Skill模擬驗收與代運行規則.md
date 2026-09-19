# Skill 模擬驗收與代運行規則 v1.2

## 1. 目的

將「必須等待實際驗收才能運行」改為：

> 模擬驗收 PASS → 正式准入運行 → 【代】追蹤 → 自然工作 Evidence → 移除【代】。

本文件只管理這條運行流程；State 的共同語義見《工程狀態與驗收最小規則》。

## 2. 正式流程

```
Skill Definition 完成
        ↓
模擬驗收
   ├─ FAIL → 修正 → 再驗
   └─ PASS
        ↓
正式准入
        ↓
Acceptance = 【代】
        ↓
自然工作／實際運行
   ├─ Evidence 不足 → 保持【代】
   ├─ 正常且證據足夠 → 移除【代】
   └─ 發現問題 → 進入問題流程 → 【驗】
```

## 3. 模擬驗收最低條件

至少確認：

1. Trigger 正常。
2. Responsibility Boundary 正常。
3. Input / Output 正常。
4. Delegation／協作正常。
5. 無 Routing Loop 或責任衝突。
6. 正常案例與主要失敗案例可處理。
7. Stop / Unknown / Insufficient 條件正常。

PASS 只代表可以准入運行，不代表已取得自然工作 Evidence。

## 4. 【代】規則

【代】表示：

> 功能已完成、模擬驗收已通過、可以運行，但尚缺足夠實際運行證據。

【代】不是：
- Skill 類型。
- State。
- Lifecycle。
- DEFER。
- 未完成。

實際運行正常且證據充分後移除【代】。

實際運行發現需要修正的問題時回【驗】，進入問題／診斷／演化流程。

## 5. 實際 Evidence

解除【代】不使用固定次數。

至少應有：
- 可追溯的實際 Operation / Observation。
- 涵蓋主要 Trigger / 使用情境。
- 沒有尚未處理的關鍵異常。
- Verification / Feedback 已回寫。
- 證據足以支持目前正常運作的判定。

證據不足就保持【代】。

## 6. 責任

- Skill Definition：功能 Source of Truth。
- 模擬驗收：Verification / 診斷能力。
- 實際運行：正常工程工作。
- Evidence：保存自然工作證據。
- 問題修正：問題／診斷／分類／演化／執行流程。
- State / Acceptance 共同語義：由《工程狀態與驗收最小規則》提供。

任何單一 Skill 不得自行宣告實際驗收成功或自行解除【代】。

## 7. 適用範圍

適用於：
- 新 Skill。
- Skill 更新。
- 需要先取得運行資格的 System / Plan 等工程能力。

對方案而言，模擬 PASS 只表示可以進入正常工程運行，不表示方案已完成實戰驗證。

## 8. 歷史規則

2026-09-19 起，前置實際驗收改以模擬驗收作為准入前檢查。

舊文件中的歷史驗收狀態不因本次蒸餾而改寫；若舊語義與現行規則衝突，現行規則優先。
