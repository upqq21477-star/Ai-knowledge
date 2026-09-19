# A-Skill Architecture Natural FIELD 證據對照紀錄 v1.0

日期：2026-09-19
工作包：A — Skill Architecture
狀態：【NATURAL FIELD EVIDENCE：PARTIAL；不得宣稱 A FIELD PASS】

## 1. 目的

將 Repository 中已自然發生、且可追溯的 G1 Natural FIELD 工作事件，依 A 的 F-A1～F-A8 驗證協議進行對照。

本文件不重新製造案例，不修改原 G1 FIELD 紀錄，也不把 G1 的一般 Routing 驗證直接等同 A FIELD。

## 2. 證據來源

主要來源：
- 1-系統/G1 Skill與Routing FIELD驗收紀錄-v1.0.md
- 1-系統/Skill分類判斷 Skill.md
- 1-系統/Skill建立流程規格.md
- 2-方案/完善/CURRENT Baseline-v1.0.md

判定原則：
- 只有原紀錄明確屬於實際 Repository 工作的案例才納入 Natural FIELD。
- Simulation / 人工推演 / 文件層規則測試不升格。
- 若案例只驗證規則而非自然失敗事件，保留其限制。
- 不因已有案例數量而強行宣稱整體 PASS。

## 3. A F-A1～F-A8 對照

| A Case | 自然證據 | 狀態 | 判定 |
|---|---|---|---|
| F-A1 Provider / Tool | G1-F06、G1-F12：GitHub Tool / Provider 不升格 Skill | Evidence available | PASS（案例層） |
| F-A2 Mode | G1-F09：快速／深度屬同一 Research Responsibility 的 Mode | Evidence available | PASS（案例層） |
| F-A3 Split | 目前尚無實際長期雙責任且完成 Split 的自然事件 | Missing | PENDING |
| F-A4 Merge | G1-F16：形成 Merge Candidate，但尚未實際 Migration / Merge | Partial | PENDING |
| F-A5 Workflow / Agent | G1-F03：多 Skill 串接實際建立 FIELD；但尚不足以完整驗證 Agent / Workflow 全邊界 | Partial | PENDING |
| F-A6 Routing Failure | G1-F11 為規則保護案例，並非自然外部 Routing Failure Event | Partial | PENDING |
| F-A7 No Candidate | G1-F13、F14：實際 Classification Candidate / DEFER 判斷；未任意建立 Skill | Evidence available | PASS（案例層） |
| F-A8 Replacement / Defer | G1-F13/F14：證據不足時 DEFER；尚無實際 REPLACE / Migration | Partial | DEFER PASS；REPLACE PENDING |

## 4. 已形成的 A Natural Evidence

### A-FIELD-E01：Provider / Tool Boundary

來源：G1-F06、G1-F12。

實際工作中提出 GitHub Tool / GitHub 操作作為 Skill 候選。

實際分類：
Provider / Tool，不是獨立 Skill。

結果：
沒有因工具不同建立新 Skill。

A 對照：
符合 A Architecture 的 Provider / Tool Boundary。

狀態：
REAL-WORK EVIDENCE；PASS（案例層）。

### A-FIELD-E02：Mode Boundary

來源：G1-F09。

實際工作中出現快速／深度兩種工作方式。

判斷：
Responsibility 仍為同一 Research Responsibility，因此採 Mode，而不是新 Skill。

狀態：
REAL-WORK EVIDENCE；PASS（案例層）。

### A-FIELD-E03：DEFER / No Candidate Protection

來源：G1-F13、G1-F14。

候選責任尚無足夠 recurring、routing、verification 證據。

處置：
沒有直接 NEW，改為 Classification Candidate / DEFER。

狀態：
REAL-WORK EVIDENCE；PASS（案例層）。

### A-FIELD-E04：UPDATE Boundary

來源：G1-F15。

既有 Skill Responsibility 正確，只增加同一責任內的能力／規則補強。

處置：
UPDATE，而不是 NEW。

狀態：
REAL-WORK EVIDENCE；PASS（案例層）。

### A-FIELD-E05：MERGE Candidate Boundary

來源：G1-F16。

兩候選 Skill 的責任、Trigger、Input / Output 高度重疊。

處置：
形成 MERGE CANDIDATE，但沒有直接修改；要求後續 Evidence / Impact / Migration 驗證。

狀態：
REAL-WORK EVIDENCE；PASS（分類層）；Migration PENDING。

### A-FIELD-E06：Multi-Skill Composition

來源：G1-F03。

實際工作形成：
Context → Skill Routing → Execution → Verification。

多 Skill 串接成立。

限制：
此案例證明 Composition 存在，但不足以單獨完成 Agent / Workflow 自然邊界驗收。

狀態：
REAL-WORK EVIDENCE；PARTIAL。

## 5. 尚未取得的關鍵證據

以下不得用模擬補足：

1. 真正自然發生的 Split。
2. 真正完成 Migration 的 Merge。
3. 真正自然發生的 Routing Failure。
4. 真正自然發生的 Provider / Tool Failure。
5. 真正需要 NEW 並完成建立與驗證的獨立 Responsibility。
6. 真正完成 REPLACE。
7. 真正進入 ARCHIVE 的自然生命週期事件。
8. Agent / Workflow 邊界的長期自然案例。

## 6. A FIELD 現況

Natural Evidence：
已存在。

Coverage：
部分 F-A1 / F-A2 / F-A7 已有直接案例；
F-A4 / F-A5 / F-A6 / F-A8 為部分證據；
F-A3 尚無直接自然證據。

Structural Failure：
目前沒有發現 A Architecture 必須修改的結構性缺口。

因此：
A Architecture v1.0 保持不變。

A FIELD：
【PARTIAL / PENDING】

不得標記：
A FIELD PASS。

## 7. 後續規則

不為了補齊 F-A3～F-A8 而人工製造錯誤或修改架構。

後續自然工作若出現對應事件，直接追加 Evidence。

若發現結構性缺口：
Evidence → Problem → Proposal → Verification → Change Request

若沒有結構性缺口：
保持 A Architecture v1.0。

本文件本身不是 Skill Definition，也不是永久 Registry。
