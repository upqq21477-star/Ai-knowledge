# AI 知識系統 — AI 交接文件

> 文件性質：**AI 接手控制文件（AI Handoff Control Document）**
>
> 本文件負責告訴新 AI：這個 repository 是什麼、目前真實狀態、哪些設計曾經被討論、哪些決策已經確立，以及本次為什麼重新整理架構。
>
> **實際操作規則以 `RULES.md` 為準。Repository 實際檔案樹是內容的 Source of Truth。**

## 1. 本次交接最重要的變更

先前的設計曾經把一個「部分 AI 無法直接瀏覽 GitHub 資料夾樹」的工具限制，當成整套知識系統的架構約束。

因此產生了：

- INDEX 作為主要 Discovery 入口
- 依賴明確 Markdown 連結來讓 AI 逐層進入文件
- 「不要自行進入資料夾」等限制
- 部分原本不必要的 Discovery 設計

現在已確認：本系統所使用的 GitHub 讀取能力可以直接取得 repository 的目錄內容，也可以直接讀取子資料夾中的文件。因此：

> **AI 能否讀取資料夾，不再是本系統的架構約束。**

這是本次重新整理的核心原因。

之前的架構不是因為 Knowledge／System 理念錯誤而需要全部推翻；真正需要修正的是「為了補償資料夾不可讀」而建立的 Discovery 層。

## 2. 目前 repository 的真實內容

截至本次重新整理，repository 實際檔案樹只有：

```text
README.md
RULES.md
HANDOFF.md
REJECTED-PATHS.md

0-knowledge/
    INDEX.md

1-systems/
    INDEX.md

2-applications/
    INDEX.md
```

三個 INDEX 目前沒有正式內容，三個正式內容層也沒有 Knowledge、System、Application。

因此目前仍然是：

| 層級 | 正式內容數量 |
|---|---:|
| Rules | 1 套規則 |
| Knowledge | 0 |
| System | 0 |
| Application | 0 |

GitHub 的 recursive tree 已確認目前沒有其他隱藏在子資料夾中的正式內容；目前整個 repository 的檔案樹只有上述文件。這次重新整理不是因為漏讀了某個子資料夾，而是因為確認了實際讀取能力後，原本的 Discovery 假設需要修正。

## 3. 一句話理解本專案

這是一個 **Personal AI Engineering Knowledge System**：

> 第一次遇到問題時研究、驗證並保存真正可重複使用的 Knowledge；下一次遇到類似問題時優先重用，降低重新研究成本。

使用者是一人工作室，所以最高原則是：

> **低維護成本優先於完整性。**

它不是企業知識管理平台，也不是展示完整架構的研究專案。

## 4. 正式架構沒有被推翻

目前仍保留：

```text
Rules
  ↓
Knowledge
  ↓
System
  ↓
Application
```

對應 repository：

```text
RULES.md
    ↓
0-knowledge/
    ↓
1-systems/
    ↓
2-applications/
```

這四層的理由仍然成立：

- **Rules**：定義系統怎麼運作。
- **Knowledge**：保存可獨立理解、可跨場景重用的基本知識、原理、判斷或方法。
- **System**：將實際使用中反覆證明有價值的多份 Knowledge 組合成可重用方法／模型。
- **Application**：針對具體需求使用 Knowledge／System。

本次變更不是取消四層，而是取消不必要的「AI 導航基礎設施」。

## 5. 新的 Discovery 原則

**Repository 實際檔案樹就是內容的 Source of Truth。**

AI 可以直接讀取：

```text
0-knowledge/ 裡面的文件
1-systems/ 裡面的文件
2-applications/ 裡面的文件
```

甚至可以在需要時遞迴閱讀整個 repository。

因此不再把 INDEX 視為必要 Discovery 層。

正確模型：

```text
                GitHub Repository
                       │
              實際檔案／資料夾
                       │
              ┌────────┴────────┐
              ↓                 ↓
        任務導向閱讀        完整稽核／交接
              ↓                 ↓
        讀相關文件          讀全部相關文件
```

這裡有一個重要區別：

> **可以全部讀，不代表每次都應該全部讀。**

任務導向時控制 Context 成本；完整稽核或交接時，可以直接檢查整個 repository。

## 6. INDEX 的重新定位

現有三份 `INDEX.md` 是歷史上為了補償 AI 導航限制而建立的。

它們不再是：

- AI 唯一入口
- Discovery 必經路徑
- 判斷「repository 有哪些文件」的唯一依據

未來如果實際內容量很小，INDEX 可以完全不需要。

如果未來內容量變大，INDEX 是否有價值，應由實際 Retrieval 成本決定，而不是現在預先假設需要。

因此目前不要為了保留 INDEX 而硬塞內容，也不要建立新的索引系統。

## 7. 文件之間的新分工

| 文件 | 主要回答 |
|---|---|
| `README.md` | 這個 repository 是什麼？怎麼開始理解？ |
| `RULES.md` | 正式操作規則是什麼？ |
| `HANDOFF.md` | 為什麼現在這樣設計？目前狀態是什麼？ |
| `REJECTED-PATHS.md` | 過去哪些方案被否決或暫緩？ |
| `0-knowledge/` | 真正保存的 Knowledge |
| `1-systems/` | 真正保存的 System |
| `2-applications/` | 真正保存的 Application |

Handoff 不再承擔「教 AI 怎麼繞過資料夾」的任務。

## 8. System 建立門檻

這部分沒有因本次重構改變。

不要因為兩份 Knowledge 理論上有關聯就建立 System。

只有在：

> **至少兩份 Knowledge 已經在同一類問題中實際重複組合使用，並證明這個組合值得保存。**

才建立 System。

目的是防止「先設計完整 System，再尋找使用場景」的過度工程化。

## 9. 模型能力補償

仍然採用最小設計。

如果某份 Knowledge 只是補償當時模型的能力限制，可以簡單標註。模型能力改善後，在真正使用到該 Knowledge 時再判斷是否仍有價值。

目前不建立：

- Capability Registry
- Capability Lifecycle
- Capability Audit
- 自動淘汰
- 自動 Pipeline

除非未來真的出現維護成本。

## 10. 過去 K01–K61 / S01–S37 的定位

K01–K61 與 S01–S37 是過去架構設計階段的概念清單。

它們：

- 不是目前正式 Knowledge
- 不是目前正式 System
- 不是下一階段待辦
- 不需要逐項搬進 repository
- 不需要因本次重構重新審查

它們保留的唯一價值，是未來真的遇到相同問題時，可以知道過去曾經考慮過哪些方向。

## 11. 已否決與暫緩

兩者必須分開：

**已否決**：目前有充分理由認定不值得加入。除非出現新的具體反證，不要重新提出。

**暫緩**：目前證據不足，不實作、不正式化、不列為待辦；未來若實際痛點出現，可以重新評估。

具體歷史內容保留在 `REJECTED-PATHS.md`。

## 12. 目前不預先建立的架構

包括但不限於：

- Knowledge ID
- Evidence Source 分級
- 文件 Version History 表格
- Specification Migration
- Capability 分類系統
- Conflict Resolution Pipeline
- Knowledge Graph
- Dependency Database / Registry
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

## 13. 重新啟動條件

未來只有實際問題出現，才擴張架構。

### Gate 1：Retrieval Problem

如果正式內容增加後，AI 或使用者實際找不到需要的文件，且這個成本已經影響工作效率，才重新評估 INDEX、搜尋、分類或其他 Retrieval 機制。

不設定固定檔案數門檻。

### Gate 2：Knowledge Overlap Problem

如果 Knowledge 開始大量重疊，造成實際維護成本、邊界不清或內容分散，才重新評估 Atomic、Aggregation、Deduplication 等機制。

### Gate 3：Capability Maintenance Problem

如果模型能力補償的人工維護已經成為明顯成本，才重新評估 Capability Registry、Audit 或淘汰機制。

### Gate 4：Application／System 重複成本

如果相同的 Application 子機制在不同專案中反覆出現，且手動重建成本已經明顯，才評估抽成 System 或工具化。

核心原則：

> **哪個問題先發生，就只解決哪個問題。**

## 14. 下一階段

現在不應繼續設計架構。

真正的下一步是：

> **從使用者過去實際工作中，建立第一批真正有用的 Knowledge。**

建議第一輪約 5～10 筆，但這只是實驗範圍，不是硬性數量規則。

選擇標準：

- 已經實際研究／驗證過
- 未來可能再次遇到
- 不只服務單一專案
- 能降低下一次重新研究成本

不要從 K01–K61 挑「最漂亮」的概念來填資料庫。

## 15. 第一批 Knowledge 的真正用途

第一批 Knowledge 同時是架構實驗。

要觀察：

- 一份 Knowledge 自然會有多大
- 邊界是否清楚
- 是否自然產生重疊
- AI 是否容易直接找到它
- INDEX 是否真的有必要
- 何時自然形成 System
- System 建立門檻是否合理
- 更新成本是否低
- 模型能力補償是否值得保留

只有實際使用結果，才能決定下一版架構。

## 16. 新 AI 接手後的正確行為

讀取 repository 後，不要先假設需要新的架構。

先確認：

1. repository 實際有哪些文件。
2. 使用者現在要解決什麼問題。
3. 哪些現有 Knowledge／System／Application 真的相關。
4. 是否已經有實際痛點觸發某個 Gate。

如果沒有：

> **直接做工作，不要重新設計知識系統。**

如果需要建立 Knowledge：依 `RULES.md` 建立。

如果需要建立 System：先確認有實際重複使用證據。

如果發現架構問題：先確認問題真的存在，再提出最小修改。

## 17. 對未來 Claude 的定位

Claude 可以作為本系統的**第二審核者（Second Reviewer）**：

- 審核架構是否合理
- 審核新 Knowledge 是否真的屬於 Knowledge
- 審核 System 建立是否有足夠實際證據
- 審核是否出現過度工程化
- 審核新機制是否真的由痛點觸發

但 Claude 的審核不應反過來成為新的架構約束。

尤其不能再因為某個 AI 的工具限制，而設計一套永久存在的 workaround。

## 18. 最終接手原則

```text
Repository 實際內容
        ↓
理解目前任務
        ↓
重用已有 Knowledge / System
        ↓
沒有就研究
        ↓
研究結果有跨場景重用價值才保存
        ↓
重複使用後才抽象成 System
        ↓
實際痛點出現後才演化架構
```

最重要的一句話：

> **不要再為 AI 尚未遇到的問題建立架構；先讓 repository 真正產生有價值的 Knowledge。**
