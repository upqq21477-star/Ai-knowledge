# G2-07 Research → Evidence → Candidate → Decision → Canonical Source → Implementation → Verification 追溯矩陣

版本：v1.0
日期：2026-09-18
狀態：【G2-07 完成】
性質：Derived Traceability / Evidence Audit

## 一、稽核目的

依基線重建交接文件 G2-07 要求，追蹤：

Research / Evidence
→ Candidate
→ Decision
→ Canonical Source
→ Implementation
→ Verification

核心不是「研究文件有沒有提出好概念」，而是確認研究是否真正進入正式架構、實體工程與驗證。

## 二、判定規則

| 狀態 | 定義 |
|---|---|
| RESEARCH | 研究、外部案例、問題探索或研究會議結果 |
| EVIDENCE | 可支持判斷的外部資料、測試、回歸、實際事件或紀錄 |
| CANDIDATE | 可能採用的設計／能力／架構候選，尚未成為正式真相 |
| DECISION | 已明確保留、修改、部分採用、不採用或暫緩 |
| CANONICAL | 決策已落入正式權威文件／正式狀態來源 |
| IMPLEMENTED | 已進入實際工程流程、檔案結構或可操作機制 |
| VERIFIED | 有測試、回歸、實測或其他可追溯驗證證據 |
| FIELD-PENDING | 尚未由自然工作場景驗證 |

重要規則：

「文件存在」≠「決策成立」≠「系統已建立」≠「能力已驗證」。

## 三、主要研究來源

全庫第一輪資產清冊已將六份研究會議記錄標為 RESEARCH / CANDIDATE INPUT：

| 研究 | 主題 | 核心結果 |
|---|---|---|
| 001 | 知識與資料基礎層 | Library / System Library / Plan Library；Discovery 與內容分離；不因 RAG 成熟而提前建立 Vector DB |
| 002 | AI 決策與控制層 | Trigger、Intent、Contract、Blueprint、Orchestration、Role 分責任；Blueprint 條件式啟動 |
| 003 | 品質與可信度層 | Verification 必須獨立；GPT 自我檢查不能直接等同可靠驗證；Evidence / Artifact 需保留 |
| 004 | 時間與上下文層 | Current / History、Handoff、Context Control、No-API Retrieval |
| 005 | 決策治理層 | Research → Adoption；Evidence → Proposal → Decision → Implementation → Verification；Adoption Gate |
| 006 | 長期演化層 | System / Knowledge Lifecycle、System Entropy、持續演化 |

六份研究文件本身均不能直接視為正式架構。

## 四、逐項追溯

### 研究 001

研究結論仍屬 CANDIDATE。研究本身明確表示尚未完成正式採用判定、最終資料結構與實作。

後續外部架構比對吸收了「大記憶、小 Context」、「Library 與 Source 分離」、「Knowledge / System / Plan 分責任」等方向。

判定：RESEARCH → CANDIDATE → 部分 DECISION。

尚不能宣稱 001 全部已實作。

### 研究 002

研究提出：

Intent
→ Trigger / Capability Discovery
→ Control Core
→ Blueprint（必要時）
→ Role / Capability Context
→ Execution
→ Evidence / Observation
→ Verification

其中 Trigger 是候選能力發現，不是完整執行引擎；Blueprint 是條件式能力；Role 與 Capability 分離。

後續外部比對明確吸收「Trigger = Candidate Recall」等原則，但沒有證據支持已建立大型 Trigger／Intent／Orchestration 引擎。

判定：RESEARCH → CANDIDATE → DECISION → 部分 IMPLEMENTATION → FIELD-PENDING。

### 研究 003

研究把 Verification 提升為獨立工程問題，並區分結構、規則、內容／證據等驗證。

後續正式架構已將 Verification、Evidence、History 視為必要閉環，並存在方案驗收、回歸測試、交接驗證與工程紀錄。

判定：RESEARCH → CANDIDATE → DECISION → IMPLEMENTED → VERIFIED（Simulation / Regression）。

仍不能宣稱完成 FIELD。

### 研究 004

研究方向與目前工程基線高度相關。

目前已實體化：

- CURRENT / HISTORY 分離
- 快照-005作為唯一目前工程執行位置
- 舊快照與舊交接保留為歷史證據
- AI 上下文與交接系統採分層讀取
- 無記憶交接回歸

判定：RESEARCH → DECISION → CANONICAL → IMPLEMENTED → VERIFIED。

FIELD 仍待自然觸發。

### 研究 005

研究提出 Evidence → Proposal → Decision → Implementation → Verification 與 Adoption Gate。

後續 G2 系列實際採用了這種治理思路：研究結果不能自行改變正式架構，必須經決策、正式來源與驗證。

但沒有證據支持已建立獨立 Adoption Engine。

判定：RESEARCH → DECISION MODEL 已吸收 → PROCESS IMPLEMENTED → VERIFIED（流程級）。

### 研究 006

研究提出 System / Knowledge Lifecycle 與 System Entropy。

後續正式外部比對將 Continuous Distillation、Refactoring、Deprecation、Archive、Observation → 問題 → 改善 → 蒸餾列為長期方向。

目前已有盤點、蒸餾、狀態演化與歷史整理，但尚未建立完整自動化 Lifecycle Engine。

判定：RESEARCH → DECISION → PARTIAL IMPLEMENTATION → FIELD-PENDING。

## 五、Decision → Canonical Source

目前不存在「一份文件統治全部事實」的模型。

| 事實類型 | 目前主要權威來源 |
|---|---|
| 目前工程位置 | 2-方案/完善/目前工程狀態快照-005.md |
| 高階專案／架構總覽 | 目前狀態.md |
| 現行規則 | 規則.md |
| 現行待辦 | 待辦清單.md |
| 目前交接背景 | 交接資料-v2.9.md |
| 上下文／交接責任 | 1-系統/AI上下文與交接系統.md |
| 工程運作基準 | 2-方案/工程運作與持續改進方案-v1.8.md |
| 知識本體 | 0-知識/ 下的個別正式知識文件 |
| 研究／外部證據 | 討論/、紀錄/ 對應文件 |
| G2 基線重建狀態 | 交接資料/AI單人工作室全庫基線重建交接文件-G1完成_G2待續-v1.0.md |

Canonical Source 是「某項正式事實的權威來源」，不是「整個 Repository 只能有一份文件」。

## 六、Canonical → Implementation

### A. Current / History

已實體化：

- 快照-005作為唯一 CURRENT 工程游標。
- 舊快照 001–004 保留為 HISTORY / EVIDENCE。
- 舊交接 v2.0–v2.8 保留為 HISTORY / EVIDENCE。
- 舊 0-knowledge 已移至根目錄 舊資料/0-knowledge/。
- 0-知識/ 為目前正式中文 Knowledge Namespace。

狀態：IMPLEMENTED。

### B. Handoff / Context Control

已實體化：

README → 交接-v2.9 → 快照-005 → 目前狀態／規則／待辦 → 工程運作方案 → 任務文件。

AI 上下文系統採分層讀取；新 AI 先恢復 CURRENT，再按任務擴大 Context；歷史資料不是預設 CURRENT Context。

狀態：IMPLEMENTED。

### C. Verification / Regression

已有：

- A1–A12、B1–B16、C1–C18、D1–D20 的模擬／回歸成果。
- D1–D20 整體回歸 70/70 PASS 的 Simulation Regression。
- 第二次無記憶交接問題修正後 8/8 PASS。

狀態：IMPLEMENTED + VERIFIED（Simulation / Regression）。

不是 FIELD-PASSED。

### D. Evidence / Research Trace

已實體化：

- 討論/ 保存研究會議記錄。
- 紀錄/ 保存外部比對、失效案例、工程變更等證據。
- G2-01～G2-07 保存本次基線重建的 Derived Evidence。
- 歷史文件不直接改寫成 CURRENT。

狀態：IMPLEMENTED。

### E. Continuous Distillation / Lifecycle

目前已有：

- 舊資料盤點
- CURRENT / HISTORY 判定
- 舊知識層與正式中文知識層比對
- Handoff Evolution Matrix
- State Evolution Matrix
- Architecture Coverage Matrix
- Research-to-Verification Traceability

但尚未證明存在完全自動化、持續運作的蒸餾引擎。

狀態：PARTIAL IMPLEMENTATION / FIELD-PENDING。

## 七、Implementation → Verification

| 驗證層 | 現有證據 | 狀態 |
|---|---|---|
| 文件結構 | G1 全庫清冊、G2 矩陣、版本／路徑追蹤 | VERIFIED |
| 架構邏輯 | Architecture Coverage、外部比對、責任／狀態追蹤 | VERIFIED（分析／模擬層） |
| 回歸 | A/B/C/D、D1–D20、8/8 交接回歸、70/70 Simulation Regression | VERIFIED（Simulation / Regression） |
| 自然 FIELD | 尚未自然觸發 | FIELD-PENDING |

因此不能寫成「整個新架構已被 FIELD 證明」。

正確狀態是：

「目前核心工程鏈已經過文件級、模擬級、回歸級驗證；自然 FIELD 驗證仍待實際工作觸發。」

## 八、完整追溯矩陣

| 主題 | Research | Candidate | Decision | Canonical | Implementation | Verification | 最終狀態 |
|---|---|---|---|---|---|---|---|
| Library / Discovery | 001 | 有 | 部分 | 架構／知識相關文件 | 部分 | 尚缺自然工作量測 | FIELD-PENDING |
| Knowledge / System / Plan | 001、外部研究 | 有 | 已確認 | 0-知識、1-系統、2-方案依責任承接 | 已存在 | 結構／交接驗證 | VERIFIED（結構級） |
| Trigger = Candidate Recall | 002、外部比對 | 有 | 已確認原則 | 規則／系統文件 | 部分 | 尚缺大量自然案例 | FIELD-PENDING |
| Intent | 002 | 有 | 概念保留 | 架構文件 | 部分 | 尚缺系統化 FIELD | FIELD-PENDING |
| Blueprint 條件式啟動 | 002 | 有 | 已確認原則 | 架構／藍圖文件 | 部分 | 尚缺自然工作驗證 | FIELD-PENDING |
| Verification | 003 | 有 | 已確認必要 | 規則、方案／驗收文件 | 已實體化 | 多輪回歸 | VERIFIED（非 FIELD） |
| Evidence | 003 | 有 | 已確認必要 | 紀錄／證據相關文件 | 已實體化 | 有研究／回歸證據 | VERIFIED（非全自動） |
| Current / History | 004 | 有 | 已確認 | 快照-005、v2.9、目前狀態等 | 已實體化 | 8/8 交接回歸 | VERIFIED（非 FIELD） |
| Context Control / Handoff | 004 | 有 | 已確認 | AI上下文與交接系統 + 現行入口鏈 | 已實體化 | 兩次無記憶交接回歸 | VERIFIED（非 FIELD） |
| Research → Adoption Governance | 005 | 有 | 治理原則已吸收 | 規則／工程流程 | 流程承載，非獨立引擎 | 本輪可追溯 | VERIFIED（流程級） |
| Lifecycle / Distillation | 006 | 有 | 長期方向確認 | 蒸餾／重構／更新文件 | 部分 | 尚缺自然 FIELD | FIELD-PENDING |
| 不提前建立大型基礎設施 | 001、002、006 + 外部比對 | 有 | 明確不採用／暫緩 | 架構決策文件 | 已反映架構邊界 | 架構稽核 | VERIFIED（決策級） |

## 九、主要缺口

### 缺口 1：研究沒有逐項 Decision ID

研究 001–006 已有研究結論，但不是每個研究項目都有獨立的：

Research ID → Candidate ID → Decision ID → Canonical Source → Verification ID。

目前仍依文件內容與後續架構證據追溯。

這是可追溯性不足，不代表架構錯誤。

### 缺口 2：部分研究已有吸收點，但缺少明確「吸收點」

例如 Progressive Disclosure、Trigger = Candidate Recall、Blueprint 條件式啟動、Role / Capability 分離、Lifecycle / Entropy，已出現在後續架構討論與外部比對，但尚未全部具有獨立正式 Canonical Knowledge 條目。

### 缺口 3：Verification 主要仍是 Simulation / Regression

大量回歸不等於自然 FIELD。

不得把 SIMULATION-PASSED 改寫成 FIELD-PASSED。

### 缺口 4：研究與正式架構之間仍存在 Derived Layer

例如外部比對紀錄可以形成 Decision Evidence，但不能取代規則、目前工程狀態、個別正式知識、正式系統／方案。

## 十、負面結論

目前沒有證據支持：

1. 所有研究結果都已正式採用。
2. 所有研究結果都已實作。
3. 所有正式架構都有一對一研究來源。
4. 目前已完成 FIELD。
5. 需要建立大型 Research / Decision / Adoption 自動化平台。
6. 研究文件可以直接當 CURRENT。

## 十一、G2-07 最終判定

【已確認】

1. Research 與正式架構已存在實際承接，不是完全斷裂。
2. 最明確的承接鏈為：
   Research → Evidence → Decision → Canonical Source → Implementation → Simulation / Regression Verification。
3. Current / History / Handoff / Verification 已形成較完整閉環。
4. 部分研究仍停留在 Candidate / Decision / Partial Implementation，不應誤標 CURRENT。
5. 目前主要問題不是缺研究，而是研究到正式採用之間的逐項追溯粒度不足。
6. FIELD 仍未完成。

【最終狀態】

G2-07：PASS（Traceability Audit 完成）。

但「Research-to-Verification 全庫逐項一對一追溯」尚未達完全 ID 化程度。

## 十二、後續工程限制

本輪完成後，不應立即建立：

- Research Registry 大型系統
- Decision Engine
- Adoption Engine
- 自動 Traceability Platform
- 大型 Evidence Graph

目前缺口是追溯粒度不足，而不是已證明需要大型自動化基礎設施。

應先觀察實際工程是否反覆產生：

- 錯誤採用
- 重複研究
- 決策遺失
- Canonical Source 找不到
- 驗證無法回溯

只有問題重複出現，才依「以證據決定架構」原則增加機制。

## 十三、下一步

G2-01～G2-07 已完成。

下一步必須重新讀取基線重建交接文件的 G2-08 定義，依其明確順序繼續。

不得：

- 把本報告升格為新的 Canonical Architecture。
- 提前製造 FIELD。
- 因追溯缺口就建立大型新系統。
- 改寫歷史文件成 CURRENT。

## 十四、主要證據來源

- AI單人工作室全庫資產逐項清冊-第一輪-v1.0.md
- G2-01～G2-06 追溯／演化／權威矩陣
- 討論/研究會議記錄-001～006
- 紀錄/整體架構外部比對與合理性驗證紀錄-2026-09-18.md
- 1-系統/AI上下文與交接系統.md
- 2-方案/完善/目前工程狀態快照-005.md
- 2-方案/工程運作與持續改進方案-v1.8.md
- 規則.md
- 目前狀態.md
- 交接資料-v2.9.md

本報告是 Derived Traceability，不取代上述 Canonical Source。
