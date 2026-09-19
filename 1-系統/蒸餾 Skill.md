# 蒸餾 Skill（Distillation Skill） v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
進行長期、結構性的壓縮與重組，降低重複、重疊、責任漂移與長期維護成本。

## 2. 核心責任
- 發現重複與重疊能力。
- 發現責任漂移。
- 分析結構性 Context / Execution 成本。
- 將多個歷史版本抽取為目前可用結構。
- 保留必要歷史，不把壓縮誤當刪除。

## 3. Trigger
只有存在結構性證據時才啟動。
不是「問題很大」就自動進入 Distillation。

## 4. Input
多版本資料、重複能力、使用紀錄、Failure Pattern、結構成本。

## 5. Output
- Distillation Candidate
- Preserved Core
- Removed / Merged Redundancy
- Migration / Reference Notes
- Verification Target

## 6. 邊界
一般局部修正屬 Evolution Management；長期結構優化才進入 Distillation。

## 7. 原則
不得因追求壓縮而破壞必要責任、來源與可驗證性。

## 8. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- 本輪「功能盤點 → Skill 聚合 → Agent 化」工程決策。

## 9. 驗收
文件建立：PASS
實際運作：PENDING
