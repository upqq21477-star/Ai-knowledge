# 蒸餾 Skill（Distillation Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
進行長期、結構性的壓縮與重組，降低重複、重疊、責任漂移與長期維護成本。

## 2. Trigger
至少存在一項持續性結構證據：
- Repeated Duplication：重複能力持續出現。
- Responsibility Drift：Skill 職責持續膨脹或偏移。
- Structural Cost：Context / Execution / Maintenance 成本持續偏高。

單次問題不自動觸發 Distillation。

## 3. 核心責任
發現重複與重疊。
發現責任漂移。
分析結構成本。
從多版本抽取目前可用結構。
保留必要歷史。

## 4. Input
多版本資料、Usage Record、Failure Pattern、結構成本、Evolution 結果。

## 5. Output
Distillation Candidate
Preserved Core
Removed / Merged Redundancy
Migration / Reference Notes
Verification Target

## 6. 路由
一般局部修改 → Evolution。
有長期結構證據 → Distillation。
蒸餾完成 → Verification。
Verification FAIL → Diagnosis → Evolution 或重新 Distillation。

## 7. 邊界
Distillation 不是刪除歷史。
不因追求壓縮破壞責任、來源或可驗證性。

## 8. 原則
先證據、後結構重組。
不足 → DEFER。

## 9. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- 本輪「功能盤點 → Skill 聚合 → Agent 化」工程決策。

## 10. 驗收
文件建立：PASS
實際運作：PENDING
