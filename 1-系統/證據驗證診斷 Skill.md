# 證據／驗證／診斷 Skill（Evidence / Verification / Diagnosis Skill） v1.0

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
處理「依據是否足夠」、「結果是否正確」與「若錯誤，為什麼錯」三種責任。

## 2. 三個 Mode
Evidence Mode：整理與判斷可用證據。
Verification Mode：檢查結果是否符合目標與證據。
Diagnosis Mode：定位失敗原因與錯誤層面。

三者共享核心能力，但不得因共享資料結構而消除責任邊界。

## 3. Input
任務要求、研究結果、執行結果、證據、預期結果。

## 4. Output
- Evidence Status
- Verification Result
- Failure Cause
- Correction Target
- Confidence / Unknowns

## 5. 邊界
Verification 回答「是否正確」；Diagnosis 回答「為何錯」。
不能把 Simulation PASS 寫成 Field PASS。

## 6. 原則
證據不足即標記 UNKNOWN／INSUFFICIENT，不用合理性補猜。

## 7. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `1-系統/Agent Skill.md`

## 8. 驗收
文件建立：PASS
實際運作：PENDING
