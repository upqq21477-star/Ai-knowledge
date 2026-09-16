# AI 知識系統 — AI 交接文件

> 文件性質：**AI 接手控制文件（AI Handoff Control Document）**
>
> 本文件負責告訴新 AI：這個 repository 是什麼、目前真實狀態、重要歷史決策、架構轉折，以及接手後應如何判斷下一步。
>
> **正式操作規則以 `RULES.md` 為準。Repository 實際檔案樹是內容的 Source of Truth。**

## 1. 本次架構重整的核心原因

過去曾因部分 AI 工具無法直接瀏覽 GitHub 資料夾，而把這項工具限制當成知識庫架構約束，因此建立 INDEX 與其他 Discovery workaround。

現在已確認：本系統所使用的 GitHub 讀取能力可以直接取得 repository 目錄，也可以直接讀取子資料夾中的文件。因此：

> **AI 能否讀取資料夾，不再是本系統的架構約束。**

這代表原本為了補償「資料夾不可讀」而建立的 Discovery 層應取消；但 `Rules → Knowledge → System → Application` 本身仍然成立。

不要把這次重構理解成整套 Knowledge Architecture 被推翻。真正被推翻的是一個已經不存在的工具限制。

## 2. Repository 現在的真實狀態

目前實際檔案樹：

```text
README.md
RULES.md
HANDOFF.md
REJECTED-PATHS.md

0-knowledge/
    7 筆正式 Knowledge

1-systems/
    空

2-applications/
    空
```

正式內容數量：

| 層級 | 數量 |
|---|---:|
| Rules | 1 |
| Knowledge | 7 |
| System | 0 |
| Application | 0 |

第一批 Knowledge 已建立，目的是開始用真實內容驗證架構，而不是繼續設計架構。

## 3. 正式架構

```text
Rules
  ↓
Knowledge
  ↓
System
  ↓
Application
```

對應：

```text
RULES.md
    ↓
0-knowledge/
    ↓
1-systems/
    ↓
2-applications/
```

四層定義：

- **Rules**：定義系統怎麼運作。
- **Knowledge**：可獨立理解、可跨場景重用的基本原理、知識、判斷或方法。
- **System**：多份 Knowledge 在實際工作中反覆組合並證明有價值後形成的方法／模型。
- **Application**：針對具體需求使用 Knowledge／System 的實際應用。

## 4. Discovery 新規則

**Repository 實際檔案樹就是內容的 Source of Truth。**

AI 可以直接讀取 `0-knowledge/`、`1-systems/`、`2-applications/` 以及其中任意文件。

兩種閱讀模式要區分：

```text
任務導向閱讀
→ 讀相關文件
→ 不必要時不載入全部內容

完整稽核／交接
→ 遞迴檢查 repository
→ 不能因文件位於子資料夾而假設不存在
```

**可以全部讀，不代表每次都應該全部讀。**

INDEX 不再是必要 Discovery 層，也不再維護空的 INDEX 佔位文件。

未來若內容增加後真的出現 Retrieval Problem，再依實際成本決定是否需要 INDEX、搜尋或分類。

## 5. 第一批 Knowledge

目前已建立：

1. `separate-source-and-knowledge.md` — 區分 Source 與 Knowledge
2. `separate-ai-output-and-truth.md` — 區分 AI Output 與 Knowledge Truth
3. `context-economy.md` — Context Economy
4. `separate-current-state-and-design-history.md` — 區分 Current State 與 Design History
5. `evidence-gated-architecture.md` — Evidence-Gated Architecture
6. `model-capability-compensation.md` — 模型能力補償
7. `ai-handoff-document-separation.md` — AI 交接文件分工

這 7 筆不是從舊 K01–K61 清單直接搬運，而是從使用者過去實際反覆處理的 AI 研究、交接、Context、架構與模型能力問題重新提取。

它們現在同時是第一輪架構實驗。

## 6. 第一批 Knowledge 要觀察什麼

不要急著建立更多治理機制。

實際使用這 7 筆後觀察：

- Knowledge 自然大小是否合理。
- Knowledge 邊界是否清楚。
- 不同 Knowledge 是否開始產生實際重疊。
- AI 是否能直接找到需要的文件。
- 是否真的需要 INDEX。
- 是否有兩份以上 Knowledge 在同一類問題中反覆組合。
- 更新成本是否開始增加。
- 模型能力補償標註是否產生維護成本。

只有實際使用結果才能決定下一版架構。

## 7. System 建立門檻

目前 System = 0，這是正確狀態。

不要因為 Knowledge 彼此「看起來有關」就建立 System。

只有：

> **至少兩份 Knowledge 已經在同一類問題中實際重複組合使用，並證明這個組合值得保存。**

才建立 System。

## 8. Application 建立原則

Application 只在出現具體需求時建立。

Application 可以包含專案特有決策；這些決策不應因為只服務單一專案，就被硬抽成 Knowledge。

只有某個 Application 子機制在不同 Application 中反覆出現，才重新評估是否值得抽成 System。

## 9. 已否決與暫緩

兩者必須區分：

**已否決**：目前已有充分理由不加入；除非出現新的具體反證，否則不要重新提出。

**暫緩**：目前證據不足，不實作、不正式化、不列為待辦；未來若實際痛點出現，可以重新評估。

完整歷史方向保留在 `REJECTED-PATHS.md`。

## 10. 舊 K01–K61 / S01–S37

它們是過去架構設計階段的概念清單。

目前：

- 不是正式 Knowledge。
- 不是正式 System。
- 不是待辦事項。
- 不需要逐項搬運。
- 不需要因本次重構重新審查。

未來只有遇到實際問題時，才可以把歷史方案當作背景參考。

## 11. 目前不預先建立的機制

包括：

- Knowledge ID
- Evidence Source 正式分級
- 文件 Version History 表格
- Specification Migration
- Capability 分類／Registry
- 正式 Conflict Resolution Pipeline
- Knowledge Graph / Dependency Database
- 自動 Cascade Update
- 複雜 Retrieval Engine
- 多層 Context Loading
- Atomic Knowledge
- Knowledge Aggregation
- 複雜內容狀態機
- Capability Lifecycle
- 大型 Knowledge Pipeline
- 預先建立 `_archive/`
- 預先建立 Runtime

這些不是待辦事項。

## 12. 架構 Gate

### Gate 1：Retrieval Problem

正式內容增加後，如果 AI 或使用者真的找不到需要的文件，而且已經影響工作效率，才重新評估搜尋、INDEX、分類或其他 Retrieval 機制。不設定固定檔案數門檻。

### Gate 2：Knowledge Overlap Problem

如果 Knowledge 實際開始大量重疊，造成維護成本或邊界問題，才重新評估 Atomic、Aggregation、Deduplication 等方案。

### Gate 3：Capability Maintenance Problem

如果模型能力補償的人工維護已經成為明顯成本，才重新評估 Capability Registry、Audit 或淘汰機制。

### Gate 4：Application／System 重複成本

如果相同子機制在不同 Application 中反覆出現，而且手動重建成本明顯，才評估抽成 System 或工具化。

核心原則：

> **哪個問題先發生，就只解決哪個問題。**

## 13. Claude 的角色

Claude 可以作為第二審核者（Second Reviewer），檢查：

- Knowledge 是否真的可跨場景重用。
- 是否把 Application 特有內容誤升格為 Knowledge。
- 是否把歷史方案誤當成現行規則。
- 是否出現過度工程化。
- 新增的 System 是否真的達到建立門檻。

但 Claude 的工具限制不應再成為 repository 架構的前提。

Repository 的主要 Source of Truth 永遠是實際 GitHub 文件。

## 14. 新 AI 接手後的行為

如果使用者沒有指定具體任務：

1. 讀取 `README.md`。
2. 讀取 `RULES.md`。
3. 讀取 `HANDOFF.md`。
4. 依任務需要直接讀取 repository 中的相關文件。
5. 如果是完整稽核，直接遞迴檢查 repository。
6. 不要重新設計已經存在且沒有痛點的架構。
7. 不要把歷史 K01–K61 / S01–S37 當成待辦。
8. 優先使用現有 Knowledge。
9. 只有實際問題觸發 Gate，才考慮擴張架構。

## 15. 當前最重要的原則

> **不要再設計一個尚不存在的問題；先讓真正有用的 Knowledge 進入實際工作。**

現在已經完成第一批 Knowledge。

下一階段不是再設計 Knowledge Architecture，而是**實際使用這 7 筆 Knowledge，觀察它們是否真的降低下一次重新研究問題的成本。**
