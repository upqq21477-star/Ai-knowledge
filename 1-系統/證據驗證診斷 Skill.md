# 證據／驗證／診斷 Skill（Evidence / Verification / Diagnosis Skill） v1.2

版本：v1.3
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition；自然運作 Evidence 持續累積】

## 1. Definition
統一處理三個不同責任：
Evidence：證據是否存在且可追溯。
Verification：結果是否符合預期。
Diagnosis：失敗原因與修正目標。

三者不可互相取代。

## 2. Trigger
Evidence：結論、變更或結果需要來源支撐。
Verification：結果已產生，需要判定 PASS / FAIL。
Diagnosis：Verification FAIL、重複失敗或結果與預期不一致。

## 3. Input
Task Definition、Expected Result、Execution Result、Source Evidence、Change Set、Verification Rule。

## 4. Output
Evidence Status
Verification Result
Failure Cause
Correction Target
Failure Type
Unknowns
Trace Reference

## 5. Procedure
Execution / Research
→ Evidence
→ Verification
→ PASS：Close
→ FAIL：Diagnosis
→ Failure Classification
→ Route back to required Skill

Diagnosis 不直接修改系統。

## 6. Failure Type
Data / Context / Research / Routing / Skill / Provider / Execution / Verification。

## 7. Boundary
Evidence ≠ Verification。
Verification ≠ Diagnosis。
Evidence ≠ Trace。
Simulation ≠ Natural FIELD。
合理推測 ≠ Evidence。

## 8. Evidence Rule
證據不足 → UNKNOWN / INSUFFICIENT。
不得以文件存在、Simulation PASS 或主觀合理性直接宣稱 Natural FIELD PASS。

## 9. Control Plane
可讀取 Evidence / Provenance / Change metadata。
Control Plane 只提供關聯 metadata；原始 Evidence 仍保留於其 Source 文件。

## 10. Stop
Verification PASS → Close。
Verification FAIL → Diagnosis / Re-route。
Evidence 不足 → UNKNOWN / INSUFFICIENT。
