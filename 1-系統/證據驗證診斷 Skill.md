# 證據／驗證／診斷 Skill（Evidence / Verification / Diagnosis Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
處理「依據是否足夠」、「結果是否正確」、「若錯誤為什麼錯」。

## 2. Mode
Evidence：判斷證據是否足夠。
Verification：判斷結果是否正確。
Diagnosis：定位失敗原因。

## 3. Trigger
Evidence：
- 需要支撐結論。
- Research 已取得資料。

Verification：
- 任務結果已產生。
- 文件／程式／方案完成修改。
- 需要判定 PASS / FAIL。

Diagnosis：
- Verification FAIL。
- 發生重複失敗。
- 結果與預期不一致。

## 4. Mode Transition
Research / Execution
→ Evidence
→ Verification

Verification PASS
→ 完成。

Verification FAIL
→ Diagnosis
→ Failure Classification
→ 回到必要 Skill。

Diagnosis 不直接修改系統。

## 5. Input
任務要求、研究結果、執行結果、證據、預期結果。

## 6. Output
Evidence Status
Verification Result
Failure Cause
Correction Target
Confidence / Unknowns
Failure Type

## 7. Failure Type
Data / Context / Research / Routing / Skill / Provider / Execution / Verification。

## 8. 邊界
Verification = 是否正確。
Diagnosis = 為何錯。
Simulation PASS 不等於 Field PASS。

## 9. 原則
證據不足 → UNKNOWN / INSUFFICIENT。
不得用合理性補猜。

## 10. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`

## 11. 驗收
文件建立：PASS
實際運作：PENDING
