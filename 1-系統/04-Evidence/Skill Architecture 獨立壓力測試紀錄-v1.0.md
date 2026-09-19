# Skill Architecture 獨立壓力測試紀錄 v1.0

日期：2026-09-19
工作包：A — Skill Architecture
測試目的：不依賴 B/C，單獨檢查 Architecture 是否能對新能力、變更、拆分、合併、替代與異常做一致分類。

## 1. 測試方法

採用 30 個獨立情境，覆蓋：
- NEW
- KEEP
- UPDATE
- MERGE
- SPLIT
- REPLACE
- ARCHIVE
- DEFER
- REFERENCE
- MODE
- WORKFLOW
- AGENT
- PROVIDER / TOOL
- DEPENDENCY
- VERIFICATION / EVIDENCE
- VERSION / LIFECYCLE

限制：
本測試是 Architecture-level controlled simulation，不是 FIELD。
不使用 B Registry、C Router 或 Runtime。

## 2. 測試結果

| # | 情境 | 預期分類 | 結果 |
|---:|---|---|---|
| 01 | 新 Provider 提供既有能力 | KEEP | PASS |
| 02 | 同責任新增 Deep Mode | MODE | PASS |
| 03 | 同責任改變執行規則 | UPDATE | PASS |
| 04 | 新責任且可獨立 I/O/Verification | NEW | PASS |
| 05 | 新能力只有一次性任務 | WORKFLOW/PLAN | PASS |
| 06 | Tool 本身被命名為 Skill | REFERENCE/TOOL | PASS |
| 07 | Model 換代 | UPDATE/PROVIDER CHANGE，不自動 NEW | PASS |
| 08 | Provider 更換但 Responsibility 不變 | UPDATE/PROVIDER CHANGE | PASS |
| 09 | Skill A + B 只是固定順序組合 | WORKFLOW | PASS |
| 10 | 同一 Skill 增加內部步驟 | KEEP/UPDATE | PASS |
| 11 | 單一 Skill 長期承擔兩個獨立責任 | SPLIT | PASS |
| 12 | 兩 Skill Responsibility 相同 | MERGE 評估 | PASS |
| 13 | 兩 Skill 僅名稱相似 | 不足以 MERGE | PASS |
| 14 | 新 Skill 尚無替代驗證 | DEFER REPLACE | PASS |
| 15 | 新 Skill 已完成 Migration/Verification | REPLACE | PASS |
| 16 | 舊 Skill 不再使用但保留證據 | ARCHIVE | PASS |
| 17 | 證據不足以判定新 Skill | DEFER | PASS |
| 18 | 純規則/知識內容 | REFERENCE | PASS |
| 19 | 任務需要安排多 Skill | AGENT | PASS |
| 20 | 單一明確可重用責任 | SKILL | PASS |
| 21 | Skill 失敗一次 | 不改 Boundary | PASS |
| 22 | Skill 反覆出現同一 Boundary Failure | Change Investigation | PASS |
| 23 | Trigger 改變 | VERSION CHANGE | PASS |
| 24 | I/O Contract 改變 | VERSION CHANGE | PASS |
| 25 | Derived Metadata 改變 | 不升 Definition Version | PASS |
| 26 | Dependency 名稱相似但無證據 | UNKNOWN | PASS |
| 27 | Dependency 改變並影響行為 | VERSION / CHANGE | PASS |
| 28 | Verification 方法存在但沒有實際結果 | PENDING / no Evidence | PASS |
| 29 | Simulation 結果被要求標成 FIELD | REJECT / retain as Simulation | PASS |
| 30 | 新能力找不到候選 Skill | 先 Diagnosis，再 Classification | PASS |

## 3. 發現的架構壓力點

### P1：Gate E「可重用」的最低門檻

目前規格使用：
「可跨至少一個以上合理情境重複使用」。

此文字在邊界案例中可執行，但沒有定義「合理情境」的判定證據。

結果：
PASS（不阻塞）
狀態：PENDING。

不得自行新增數值門檻。

### P2：Gate G「不合理成本」

目前規格要求拆分後不得造成不合理的 Dependency / Token / Execution / Maintenance 成本。

但 Architecture 沒有定義成本量化方式。

結果：
PASS（Architecture 不負責 Runtime cost model）
狀態：UNKNOWN / 後續由實際 Evidence 決定。

不得在 A 內新增成本公式。

### P3：UPDATE 與 VERSION CHANGE 的關係

目前：
UPDATE 是 Change Decision。
Version Change 是 Definition Contract 改變。

兩者不是同一層級。

測試證明目前規則可區分：
- Metadata-only → 不升 Definition Version
- Responsibility / Trigger / I/O / Boundary / Verification 改變 → Version Change

結果：PASS。

### P4：MERGE 的「高度重疊」

目前沒有量化「高度」。

但 Merge 本身已要求「實際維護成本」Evidence，因此不需要在 Architecture 階段自行設定相似度數字。

結果：PASS。
狀態：保留質性判定，Evidence 不足則 DEFER。

### P5：AGENT 與 WORKFLOW 邊界

測試中：
- 多責任協調 / 任務級決策 → Agent
- 已知責任組合 / 固定流程 → Workflow

此邊界可運作。

結果：PASS。

## 4. 30/30 結果

PASS：30
FAIL：0
BLOCK：0

但這不是「A 最終通過」。

原因：
此測試只證明規格在受控情境中能產生一致分類。

它沒有證明：
- 真實工作中的錯誤率
- Token 成本
- Routing 成本
- Maintenance 成本
- FIELD 長期穩定性

## 5. 是否修改 Architecture

本輪：不修改。

理由：
發現的 P1～P5 都沒有證明現行 Architecture 結構錯誤。

目前正確處置：

P1 → PENDING
P2 → UNKNOWN
P3 → PASS
P4 → PASS / Evidence driven
P5 → PASS

若未來 FIELD 出現實際失敗，再依：

Evidence → Problem → Proposal → Verification → Change

處理。

## 6. A 獨立測試結論

Architecture 在 30 個受控分類情境中全部得到符合規格的結果。

目前 A 狀態：

STATIC TEST：PASS
INDEPENDENT CONTROLLED STRESS TEST：PASS
FIELD：PENDING
B/C Integration：不納入本輪

下一個 A-only 工作不是擴充規格，而是保留現行版本，等待真實使用產生 Evidence。
