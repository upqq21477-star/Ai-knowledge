# 知識管理 Skill（Knowledge Management Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
管理可長期引用資料的生命週期、來源與結構，不決定目前任務載入哪些 Context。

## 2. Trigger
- 驗證後資訊具有長期重用價值。
- 需要更新既有 Knowledge。
- 發現來源、版本或生命週期問題。
- 需要建立 Derived View。
- 需要清理過時或錯誤資料。

一次性工作結果若無長期價值，不自動寫入 Knowledge。

## 3. 核心責任
保存 Knowledge。
區分 Canonical Source / Derived View。
管理 Source、Version、Lifecycle。
避免一次性決策永久化。
未知保持 UNKNOWN。

## 4. Input
驗證後資訊、既有 Knowledge、來源、版本資料。

## 5. Output
Knowledge Item
Source / Provenance
Version
Lifecycle Status
Derived View

## 6. 路由
資料尚未驗證 → Evidence / Verification。
只是當前任務 Context → Context Management。
長期結構變更 → Evolution / Distillation。
來源衝突 → Verification，不直接覆寫 Canonical。

## 7. 邊界
Context = 現在載入什麼。
Knowledge = 資料如何保存與管理。

## 8. 原則
Mapping 不等於 Canonical Source。
不得建立第二套真實資料庫。

## 9. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `README.md`

## 10. 驗收
文件建立：PASS
實際運作：PENDING
