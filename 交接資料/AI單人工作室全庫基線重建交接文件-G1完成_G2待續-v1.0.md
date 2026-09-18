# AI單人工作室全庫基線重建交接文件-G1完成_G2待續-v1.0

日期：2026-09-18
文件狀態：【CURRENT｜交接文件】
工程階段：G1 全庫資產第一輪盤點完成；G2-01 已完成；G2-02 待開始
用途：供下一個無歷史記憶的 AI 直接接手目前工作，不需要依賴本次對話記憶。

---

## 一、你現在接手的是什麼

這不是「四方案整理工程」而已。

這是一個以 GitHub Repository 作為長期外部記憶與工程證據邊界的 AI 單人工作室（AI Single-Person Studio）知識庫。

Repository：

`upqq21477-star/Ai-knowledge`

目前核心目標是：

> 在不破壞歷史證據的前提下，重建一個乾淨、可追溯、可被無記憶 AI 正確接手的 CURRENT Baseline。

目前正在進行的是：

**主系統資料基線重建（Main System Data Baseline Reconstruction）**

不是建立第五方案，不是重新設計整套系統，也不是現在就做大規模搬檔。

---

## 二、狀態 Scope：兩個狀態不能混用

本文件涉及兩個不同層級的狀態，兩者並不矛盾：

### A. 整體 AI 單人工作室工程 State

權威來源：

`2-方案/完善/目前工程狀態快照-005.md`

目前：**正常工程運作**

FIELD：**待自然觸發**

這描述整個 AI 單人工作室工程。

### B. 本次「主系統資料基線重建」Task State

權威來源：**本交接文件**

目前：**G2-01 完成**

目前游標：**G2-02**

下一步：**G2-02：整體系統企劃版本演化追蹤**

這只描述本次基線重建子工程。

因此：

> 「整體工程正常工程運作」與「基線重建 G2-01 完成、G2-02 待開始」是兩個不同 Scope，不可視為互相衝突。

本文件不取代快照-005，也不建立第二套整體 CURRENT State。

---

## 二、最重要的正式工程狀態

目前正式工程唯一游標：

`2-方案/完善/目前工程狀態快照-005.md`

正式交接鏈：

`README.md`
↓
`交接資料-v2.9.md`
↓
`2-方案/完善/目前工程狀態快照-005.md`
↓
`目前狀態.md`
↓
`規則.md`
↓
`待辦清單.md`
↓
`2-方案/工程運作與持續改進方案-v1.8.md`

不要建立第二套 CURRENT 工程狀態入口。

快照-005 目前確認：

- 方案一 A1～A12：完成
- 方案二 B1～B16：完成
- 方案三 C1～C18：完成
- 方案四 D1～D20：完成
- 四方案模擬／回歸：完成
- FIELD 自然觸發機制：完成
- 交接問題 #2：完成
- 交接問題 #3：完成
- 第二次無記憶交接回歸：8/8 PASS
- FIELD：等待自然工作觸發
- 已確認阻塞：無

禁止因本次基線工程自行建立 A13、B17、C19、D21 或第五方案。

---

## 三、四方案不是整個 Repository

四方案只是正式工程主分支：

- 方案一：整體資料治理 A1～A12
- 方案二：AI 知識管理 B1～B16
- 方案三：知識與資料迭代演化 C1～C18
- 方案四：能力蒸餾與系統重構 D1～D20

Repository 同時包含：

Knowledge、System、Plan、Capability、Rule、Decision、Evidence、Research、Test、Handoff、State、Template、Blueprint、History 等資產。

因此：

**Document Count ≠ Capability Count**

資料夾只是物理儲存位置，不是完整語意本體。

---

## 四、目前已確認的重要 Namespace

- Kxx：Knowledge
- CAP-xxx：Capability
- SYS-xxx：System
- PLN-xxx：Plan
- SCN-xxx：Scenario
- EVD-xxx：Evidence
- DEC-xxx：Decision

目前已確認：

K01～K06 有權威定義。

K07～K61 目前沒有足夠權威定義，禁止猜測。

S01～S10 已確認，可對應正式 SCN-01～SCN-10。

S11～S37 目前沒有足夠權威定義，禁止猜測。

能力 ID 衝突已修正：

- K03 Trigger Registry → CAP-60 Trigger Registry
- D20 Distillation Trigger → CAP-61 Distillation Trigger

不要重新合併回 CAP-55。

Mapping 是 Derived View，不是 Canonical Source。

---

## 五、為什麼現在做 G1/G2

Repository 已經累積大量：

- 正式文件
- 舊版本
- 研究
- 討論
- 測試
- 失效案例
- 候選方案
- 舊交接
- 舊快照
- Mapping
- Blueprint
- 待辦

如果直接開始 Mapping、Registry、Migration，很容易把歷史或候選資料誤當成 CURRENT。

所以先建立乾淨基線。

基線重建規範：

`AI單人工作室主系統資料基線重建規範-v1.0.md`

核心原則：

1. Canonical Source 優先於一般文件。
2. State 優先於路徑。
3. Git Commit 是變更證據，不是 State。
4. Version 不等於 State。
5. 不依資料夾名稱判斷語意。
6. 不直接刪除歷史資料。
7. 不在清理過程偷偷新增正式規格。
8. Distillation 不是摘要，必須保留有效語義、決策、證據與限制。
9. History 不應污染一般 CURRENT Recall。
10. Migration 前必須先完成 Inventory、Source Trace、State 判定與 Recall 驗證。

---

## 六、G1 已經做完什麼

G1 是「全庫資產逐項第一輪盤點」。

主要盤點：

### G1-01～G1-04
- CURRENT 工程入口
- 0-知識
- 1-系統
- 2-方案
- 2-方案/完善

### G1-05
`2-方案/統御/`

已確認共 9 個 Markdown。

重要結論：

**統御目前不是第五方案，也不是正式 CURRENT 方案。**

它是一組候選架構／需求／施工／狀態證據。

其 v1.1 已收斂方向：

System Catalog + Activation Safety / Trigger Registry

並排除了中央 Event Bus、完整 Rule Engine、Workflow Engine、中央 Problem Solver、Best Solution Selector 等擴張方向。

---

## 七、G1 中最重要的 State Conflict

文件：

`2-方案/能力蒸餾與系統重構方案-v1.1.md`

內部仍寫：

「整體重整完成；待最小流程驗收；真實系統能力案例待執行」

但後續已有：

- D1～D4 正式責任整合
- D5～D8 正式責任整合
- D13～D16 正式責任整合
- D17～D20 正式責任整合
- D1～D20 整體模擬／回歸
- 快照-005 明確記錄四方案模擬／回歸完成

因此高度疑似是：

**舊文件 State 沒有同步，而不是目前 D1～D20 尚未完成。**

但不能直接修改 v1.1。

G2 必須完成正式追溯後，才決定 KEEP / UPDATE / SUPERSEDED / HISTORICAL。

---

## 八、G1 研究／紀錄層的重要發現

已盤點：

`討論/`
`紀錄/`

共 12 個項目，其中 11 個實質資產。

重要文件：

- `紀錄/整體架構外部比對與合理性驗證紀錄-2026-09-18.md`
- `紀錄/新內容未問題化處理失效-2026-09-17.md`
- `紀錄/方案四完善-2026-09-17.md`
- `紀錄/統御方案建立錯誤-2026-09-17.md`
- `紀錄/舊模式重疊能力重製映射-v1.0.md`
- `討論/研究會議記錄-001～006`

這些不能全部 Archive。

至少分三類：

1. Failure Evidence
2. Research / External Evidence
3. Engineering Change Record

尤其：

「新內容未問題化處理失效」

證明存在一個重要入口失效：

新內容 → 直接方案化

而正確流程應是：

新內容
→ Problem Intake
→ 問題識別
→ 既有能力檢查
→ 外部研究
→ 比較
→ 反方案
→ 結論
→ 規劃
→ 建立

此案例應保留，未來可作 Regression / Natural-Work Validation Case。

---

## 九、G1 第七批的重要發現

發現 Repository 存在：

`0-knowledge/`

以及：

`0-知識/`

這是目前最高優先級結構問題之一。

不能直接：

- 刪除英文目錄
- 認定中文目錄是正本
- 認定英文目錄是歷史
- 將兩者直接 Merge

必須逐項比對內容與來源。

另外存在：

### 整體企劃演化

`AI單人工作室整體系統企劃書-API版本-v0.1.md`

→ No-API v0.1

→ No-API v0.2

→ No-API v0.3

→ 現行正式工程架構

不能直接認定 v0.3 = CURRENT。

### 舊交接

`交接資料.md`

→ v2.0 ～ v2.8

→ v2.9 CURRENT

舊交接保留歷史與演化證據。

### 舊待辦

待辦只能表示當時計畫。

`TODO ≠ CURRENT STATE`

### 索引

`檔案索引.md`

是 Derived View，不是 Canonical Source。

---

## 十、目前 G1 資產清冊

完整逐項清冊：

`AI單人工作室全庫資產逐項清冊-第一輪-v1.0.md`

此文件是：

**Derived Inventory**

不是 Canonical Source。

目前已加入 G1-001～G1-740 範圍的逐項盤點與批次分析。

不要把清冊本身當成正式架構。

最近一次 G1 完成 Commit：

`bb2349be42d19edec7b93a93306863f53d2ddc2d`

---

## 十一、G2-01 已完成

G2-01 已完成逐項比對，並已建立報告：

`交接資料/G2-01-英文舊知識層與正式中文知識層逐項比對報告-v1.0.md`

主要結果：

- `舊資料/0-knowledge/`：9 個歷史 Markdown，已完整歸檔。
- `0-知識/`：103 個 Markdown。
- 9/9 英文舊文件均找到中文正式對應。
- 中文正式層不是單純複製，而是後續演化後的正式結構。
- `舊資料/0-knowledge/` 已確定為 HISTORICAL / ARCHIVED。
- 已完成 Archive / Move；不刪除歷史內容。
- 「知識分類」與「知識定義與邊界」存在實質規格演化，不能當作單純 Duplicate。

### G2-01 後的禁止事項

- 不刪除 `舊資料/0-knowledge/` 中的歷史內容。
- 不把歷史文件直接 Merge 回 `0-知識/`。
- 不因中文文件存在就把所有中文文件自動升格為 Canonical。
- 不修改歷史文件製造 CURRENT。
- 不跳過 G2-02。

目前工作 Cursor：

**G2-01 完成 → G2-02 待開始**

---

## 十二、下一步：G2 實際施工順序

使用者恢復工作後，下一個實際動作是：

### G2-01
**逐項比較 `0-knowledge/` ↔ `0-知識/`**

回答：

- 是否同源？
- 是否舊版？
- 是否複製？
- 哪些內容不同？
- 哪些內容只有英文目錄有？
- 哪些內容只有中文目錄有？
- 哪些已被正式吸收？
- 哪些是 Canonical Candidate？
- 哪些不能判定？

不得用檔名直接判定。

#### G2-01 完成條件

G2-01 不以「已經看過兩個資料夾」作為完成，而必須形成可驗收的逐項比對結果。每個資產至少回答：

1. 路徑
2. 是否存在對應文件
3. 是否同源
4. 是否內容重複
5. 是否存在內容差異
6. 是否存在只有單方具備的有效內容
7. 是否已被 CURRENT Canonical Source 吸收
8. State
9. Canonical Candidate
10. Evidence / Source
11. 無法判定原因（如有）
12. 暫定處置

至少形成一份 **English ↔ Chinese Knowledge Coverage Matrix** 或等價的可驗收結果。

G2-01 的目的只是：**辨識、比較、追溯、判定。**

G2-01 完成後不得因「看起來重複」就直接 Merge、Delete、Rename 或 Migration；任何實際處置必須進入後續決策與驗證。

### G2-02
追蹤整體企劃：

API v0.1
→ No-API v0.1
→ v0.2
→ v0.3
→ CURRENT

建立 Architecture Coverage Matrix。

每項能力要能回答：

目前在哪裡？
誰負責？
State？
證據？

### G2-03
追蹤：

`能力蒸餾與系統重構方案-v1.1.md`

與 D1～D20 正式整合、回歸、快照-005 的關係。

### G2-04
處理：

`AI知識管理方案-v2.0.md`

檔名 v2.0、內文 v2.1。

以及：

`知識與資料迭代演化方案-v2.0.md`

檔名 v2.0、內文 v2.1。

不能直接改名。

### G2-05
追蹤舊交接：

v2.0～v2.8
→ v2.9

確認哪些問題被真正修復。

### G2-06
追蹤：

快照-001～004
→ 快照-005

建立 State Evolution Matrix。

### G2-07
追蹤：

Research / Evidence
→ Candidate
→ Decision
→ Canonical Source
→ Implementation
→ Verification

確認研究結果是否真正進入正式架構。

### G2-08
建立 Recall Boundary：

CURRENT
→ Relevant Evidence
→ History
→ Research
→ Deprecated / Retired
→ Unknown / Review

最後才能進 Migration。

---

## 十三、G2 驗收標準

G2 不是「文件整理完」就算完成。

必須至少滿足：

1. Source Traceability
2. State Consistency
3. Version Consistency
4. Historical Isolation
5. Recall Safety
6. Memoryless Handoff

也就是：

> 未來一個沒有本次對話記憶的 GPT，只讀正式入口，就能知道現在是什麼；需要追溯時才進入 Evidence / History，而不會把舊方案當成目前規則。

---

## 十四、目前禁止事項

### 架構

- 禁止建立第五方案。
- 禁止把統御候選升格為正式方案。
- 禁止建立第二套 Current State。
- 禁止因研究結果直接修改正式架構。
- 禁止因 Mapping 存在就認定能力已成立。

### 資料治理

- 禁止大規模刪除歷史。
- 禁止大規模搬移。
- 禁止直接 Merge 同名文件。
- 禁止依檔名版本判斷 State。
- 禁止依資料夾判斷語意。
- 禁止 Git Commit = State。
- 禁止 Version = State。

### 驗證

- 禁止重新執行四方案總驗收。
- 禁止建立 D21+。
- 禁止人工製造 FIELD。
- 禁止把歷史測試 PASS 直接等同 CURRENT 能力。

---

## 十五、交接時第一件事

新的 AI 不需要詢問使用者：

「之前做到哪裡？」

直接讀：

1. `README.md`
2. `交接資料-v2.9.md`
3. `2-方案/完善/目前工程狀態快照-005.md`
4. 本文件
5. `AI單人工作室主系統資料基線重建規範-v1.0.md`
6. `AI單人工作室全庫資產逐項清冊-第一輪-v1.0.md`

然後確認：

> 目前不是建立系統階段，而是 G2-01 完成後、等待 G2-02 的基線重建階段。

先讀取：

`交接資料/G2-01-英文舊知識層與正式中文知識層逐項比對報告-v1.0.md`

下一個實際工程動作：

**G2-02：追蹤 API v0.1 → No-API v0.1 → v0.2 → v0.3 → CURRENT，建立 Architecture Coverage Matrix。**

不要跳過 G2-01 直接做 Mapping、Registry、Migration 或新系統設計。

---

## 十六、本次交接結論

目前成果不是「整理完成」。

正確描述是：

> **G1 已完成全庫第一輪資產盤點；G2-01 已完成英文舊知識層與正式中文知識層逐項比對；目前停在 G2-02。**

G2-01 已確認：

> `舊資料/0-knowledge/` 的 9 個歷史 Markdown 均已在 `0-知識/` 找到對應內容，且中文層存在後續規格演化；目前沒有證據支持建立第二套 CURRENT 知識層。

但尚未執行：

> Delete / Merge / Rename / Migration。

下一個 AI 必須延續這條工程線，而不是重新發明架構。

下一個 AI 必須延續這條工程線，而不是重新發明架構。

目前最重要的問題不是：

「還要建立什麼？」

而是：

**「Repository 裡現有的東西，哪些才是真正有效的 CURRENT，以及它們的來源、狀態、證據與 Recall 邊界是什麼？」**

這就是 G2 要解決的問題。
