# 研究 Skill（Research Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
取得、整理、比較任務所需資訊；Search 是快速模式，Deep Research 是深度模式。

## 2. Trigger
- 缺少完成任務所需資訊。
- 需要確認外部／歷史資料。
- 需要多來源比較。
- 現有 Knowledge 不足以支持結論。
- 新資訊可能改變目前判斷。

若已有充分、可驗證資料，不重複搜尋。

## 3. Mode
Search：快速取得候選資訊。
Deep Research：多來源、交叉比較、完整研究。

模式不同不自動建立新 Skill。

## 4. Input
Task Definition、搜尋條件、必要 Context。

## 5. Output
Research Result
Sources
Evidence Candidates
Comparison
Remaining Unknowns

## 6. 路由
搜尋完成 → Evidence / Verification。
搜尋不足 → 擴大 Research。
來源衝突 → Evidence / Verification。
研究結果改變任務理解 → Task Understanding。
需要保存成長期資料 → Knowledge Management。

## 7. 邊界
Research 取得與整理資訊。
Evidence / Verification 判斷證據與正確性。

## 8. 失敗
搜尋不足不得以合理性補空缺；標記 UNKNOWN，或改變搜尋路徑。

## 9. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`

## 10. 驗收
文件建立：PASS
實際運作：PENDING
