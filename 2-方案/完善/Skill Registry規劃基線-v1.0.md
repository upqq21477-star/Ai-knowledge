# Skill Registry 規劃基線 v1.0

日期：2026-09-19
狀態：【規劃完成；尚未施工】
定位：AI Control Plane 後台管理層中的 Skill Registry Family 規劃與施工基線。

## 1. 目的

建立可查詢、可追蹤、可重建的 Skill 後台資料層，使系統能在不載入整個 Repository 的情況下，知道：

- 某個 Skill 是什麼
- 能做什麼
- 何時觸發
- 使用哪些資料／知識／系統
- 依賴什麼
- 被哪些 Skill / System / Plan 使用
- 輸入與輸出
- 如何驗證
- 目前版本與生命週期
- 最近發生哪些變更
- 變更可能涉及哪些影響範圍
- 是否存在相似、遷移、蒸餾或取代關係
- 上述資料來自哪個 Evidence

核心目標不是「把所有資料集中在一起」，而是「讓所有需要的資料可被定位並按需取得」。

## 2. 主要功能

Skill Registry 採 Registry Family，而非單一巨大 Registry。

### Identity
Skill 身份、位置、狀態、版本、Authority。

### Trigger Index
觸發條件、觸發詞、目標 Skill ID、Boundary。

這是最高頻率、最低成本的 Router 入口，獨立於其他 Registry。

### Summary
最小能力摘要與邊界，用於多候選 Skill 的低成本比較。

### Capability
Purpose、Responsibility、Boundary。

### I/O
Skill 的 Input / Output。

### Relation / Dependency
追蹤 Skill 與 Knowledge、System、Skill、Plan、Tool 等關係。

### Usage
追蹤誰使用此 Skill，以及實際使用情況。

### Verification / Evidence
記錄驗證、證據、來源、結果、Confidence。

### Lifecycle
Created → Tested → FIELD → Active → Updated → Superseded → Historical。

### Change
記錄 Skill 的變更及其前後狀態。

### Impact
記錄經 Evidence 支持的變更影響範圍。

### Evolution
記錄 Similar、Merge、Replace、Migrate、Distill 等演化關係與分析結果。

## 3. 防止的問題

本系統主要防止：

- Skill 功能逐漸失去可追蹤性。
- 相似功能重複建立。
- 修改 Skill 時無法快速定位影響範圍。
- 蒸餾或遷移時必須重新掃描整個 Repository。
- Trigger 與 Skill 實際能力逐漸脫節。
- 把所有 Registry 資料塞進單一巨大表造成 Context 與運算浪費。
- Registry 被誤當成 Source of Truth。
- Derived Registry 與 Source 不一致卻無法發現。
- 把 Dependency 錯誤當成 Impact。
- 因名稱相似就錯誤判定 Skill 應融合或取代。
- CURRENT、Historical、Pending 等狀態混淆。
- 變更後只同步部分文件，形成範圍同步缺口。

## 4. 核心原理

### Source Truth > Registry > Cache

Source 才是權威來源。

Registry 是可查詢的衍生管理資料層。

Cache / Index / Graph 均可重建，不得成為不可替代的唯一真相。

### Registry Family

資料依使用頻率與責任拆開，不建立單一巨大資料表。

### Progressive Retrieval

依目前任務需要逐層取得資料：

Task → Trigger → Skill ID → Summary → Capability → Relation / Evidence → Impact / History。

取得足以完成目前決策的資料後立即停止。

### Hot / Warm / Cold

HOT：
Trigger / Identity / Summary

WARM：
Capability / I/O / Relation / Dependency / Usage

COLD：
Evidence / Verification / Change / Impact / Evolution / History

HOT/WARM/COLD 是資料溫度與查詢成本概念；不取代既有 Context L0-L5。

### Provenance

每個 Registry 資料應能區分：

SOURCE / DERIVED / INFERRED / UNKNOWN。

Derived / Inferred 關係不得偽裝成原始事實。

### 可重建

Trigger Index、Summary、Graph、Cache 等衍生資料，應能從 Source + Git History + Evidence 重建。

## 5. 運作流程

### 正常路由

Task
→ Trigger Index
→ Candidate Skill ID
→ Skill Summary
→ 必要時 Capability
→ Execute

### 修改

Skill ID
→ Dependency / Usage
→ Verification / Evidence
→ Change
→ Impact
→ Verification
→ Reconcile

### 蒸餾／遷移

Skill ID
→ Capability
→ Trigger
→ I/O
→ Dependency
→ Usage
→ Verification / Evidence
→ Comparison
→ Distillation / Migration Candidate

Registry 提供資料；Skill Classification / Distillation / Evolution Skill 負責判斷。

## 6. 與既有系統的關係

Agent Skill：
負責協調與執行，不維護 Registry。

Agent Skill Semantic Router：
使用 Trigger Index → Summary → Capability 進行低成本分流。

Skill Classification：
使用 Registry 資料進行 Create / Merge / Update / Replace / Defer / Archive 等判斷。

Distillation Skill：
使用 Registry 結構化資料進行能力比較與蒸餾。

Evolution Management：
使用 Dependency / Usage / Change / Impact / Evidence 進行演化分析。

Control Plane：
提供查詢、狀態、關係、影響與資料治理能力。

CURRENT Authority：
仍是工程狀態的權威來源，不由 Registry 取代。

Problem Registry：
仍負責問題生命週期，不由 Skill Registry 取代。

## 7. Change Set

本規劃下一階段預定施工 8 個文件：

1. `1-系統/AI Control Plane.md`
2. `1-系統/Control Plane Registry 規格.md`
3. `1-系統/Control Plane Query 規格.md`
4. `1-系統/Agent Skill.md`
5. `1-系統/Agent Skill語意路由系統.md`
6. `1-系統/Skill分類判斷 Skill.md`
7. `1-系統/蒸餾 Skill.md`
8. `1-系統/演化管理 Skill.md`

施工前仍須依 Change Set 規則確認實際修改範圍。

## 8. 明確暫不修改

目前沒有足夠證據要求修改：

- 研究 Skill
- 知識管理 Skill
- 執行 Skill
- 任務理解 Skill
- Context管理 Skill
- 證據驗證診斷 Skill
- 現有系統目錄與系統登錄原理文件

FIELD 若證明存在查詢缺口，再建立新的 Change Set。

## 9. 驗證目標

至少驗證：

1. Trigger → Skill ID 是否可正常路由。
2. 多候選 Skill 是否可透過 Summary / Capability 進一步判斷。
3. 修改 Skill 是否能定位 Dependency / Usage / Impact。
4. 蒸餾是否能直接取得比較所需資料。
5. Registry 與 Source 不一致時是否能發現 Drift。
6. Registry 衍生資料是否可以由 Source 重建。
7. 正常路由是否避免載入完整 Skill / Repository。
8. 不同 Registry 間是否維持一致 Skill ID。
9. Dependency 是否沒有被直接冒充為 Impact。
10. Similar 是否沒有直接被當成 Merge / Replace 決策。

## 10. 參考資料

本規劃參考並比較：

- GitHub Dependency Graph / Dependency Review：依賴關係與變更檢視。
- Unreal Engine Asset Registry / Reference Viewer：資產身份、引用與依賴查詢。
- Unity AssetDatabase Dependency Model：直接／遞迴依賴取得。
- Microsoft Architecture / Dependency Analysis：依賴、影響與架構驗證。
- ServiceNow CMDB：Configuration Item、關係與影響分析。
- Backstage Catalog：元件／服務目錄與 metadata 管理。
- DataHub / OpenMetadata：metadata、lineage、ownership 與治理。
- OpenTelemetry：Trace、事件與可追蹤性概念。
- 本 Repository 既有「系統目錄與系統登錄」、「系統穩定識別」、「系統與知識關係」、「Skill 分類」、「知識重疊與資料演化」等原則。

參考資料只提供設計依據，不直接複製外部系統；本方案仍以本 Repository 的 Source Truth、Evidence、Change Set、FIELD 驗證與 Context 成本原則為準。

## 11. 目前狀態

【規劃完成；尚未施工】

已完成：
- 功能需求整理。
- Registry Family 拆分。
- Trigger Index 獨立化。
- Hot / Warm / Cold 分層。
- Query / Stop Rule 設計。
- Change Set 定義。
- 驗證目標定義。
- 參考系統比較。

未完成：
- 8 個文件正式施工。
- FIELD 驗證。
- Registry Drift / Rebuild 實測。
- 實際 Skill 相似功能遷移／蒸餾驗證。

下一游標：
先完成交接；後續確認 Change Set 後再施工。
