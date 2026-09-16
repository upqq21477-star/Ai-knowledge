# AI 知識系統 — AI 交接文件

> 文件性質：**AI 接手控制文件（AI Handoff Control Document）**
>
> 本文件不是 `README.md` 或 `RULES.md` 的替代品，而是提供新 AI 所需的目前狀態、決策背景、歷史方案、暫緩條件、架構 Gate 與接手行為。
>
> **實際操作規則以 `RULES.md` 為準。**

## 1. 接手入口

Repository：`https://github.com/upqq21477-star/Ai-knowledge`

AI 接手後依序讀取：

1. `README.md`
2. `RULES.md`
3. `HANDOFF.md`
4. `0-knowledge/INDEX.md`
5. `1-systems/INDEX.md`
6. `2-applications/INDEX.md`
7. 只有在需要時，再讀取具體 Knowledge / System / Application。

不要一次讀取整個 Repository。

## 2. 一句話理解本專案

這是一個**個人 AI 工程知識系統（Personal AI Engineering Knowledge System）**。

目的：第一次遇到問題時研究、驗證並保存可重複使用的 Knowledge；下一次遇到類似問題時優先重用既有 Knowledge，降低重新研究成本。

使用者是一人工作室，因此最高設計原則是：

> **低維護成本優先於完整性。**

不是企業級知識管理平台，也不是為展示完整架構而建立的研究專案。

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

Repository 對應：

```text
RULES.md
    ↓
0-knowledge/
    ↓
1-systems/
    ↓
2-applications/
```

- **Rules**：定義整套系統如何運作。正式操作規則以 `RULES.md` 為準。
- **Knowledge**：可獨立理解、跨場景重複使用的知識、原理、判斷或方法。位置：`0-knowledge/`。
- **System**：將多份 Knowledge 組合成可重複使用的方法、模型或能力。位置：`1-systems/`。
- **Application**：針對具體需求，組裝既有 Knowledge / System 所形成的實際應用。位置：`2-applications/`。

## 4. 目前真實狀態

| 項目 | 狀態 |
|---|---|
| Rules | 已建立 |
| Knowledge | 0 |
| System | 0 |
| Application | 0 |
| Knowledge INDEX | 已建立，目前無正式 Knowledge |
| System INDEX | 已建立，目前無正式 System |
| Application INDEX | 已建立，目前無正式 Application |
| Repository 架構 | 已建立 |
| 實際知識庫內容 | 尚未開始累積 |

因此：

> **這是一個「架構已建立、實際 Knowledge 尚未累積」的早期系統。**

過去的 K01–K61、S01–S37 等設計清單不是現有 Knowledge / System。

## 5. 核心設計思想

> **不要為尚未發生的問題建立機制。**

正確流程：

```text
先實際使用
    ↓
發現持續存在的問題
    ↓
確認問題造成成本
    ↓
建立最小解法
    ↓
驗證
    ↓
必要時才升級架構
```

不是預測所有未來問題後先建立完整架構。

## 6. 為什麼有 System 層

Knowledge 不預先建立固定關係，因為關係通常取決於當時要解決的問題。

```text
Knowledge
= 可重用的獨立內容

System
= 在特定問題脈絡下，將多份 Knowledge 組合成可重用方法
```

因此目前不建立中央 Knowledge Graph 或 Dependency Database。

## 7. System 建立門檻

不因為「未來可能會一起使用」而建立 System。

目前正式門檻：

> **至少兩份 Knowledge 已經在同一類問題中實際重複組合使用過一次以上。**

只有理論上的關聯不足以建立 System。具體操作細節以 `RULES.md` 為準。

## 8. 模型能力補償

部分 Knowledge 可能只是為補償當時模型限制，例如防止特定幻覺、限制回答範圍或彌補推理缺陷。

模型能力進步後，原本的補償可能失去價值。現在只在實際使用時判斷是否仍需要，不建立 Capability Registry、Pipeline、自動稽核或自動淘汰系統，除非未來真的出現維護成本。

## 9. 目前正式有效的設計決策

以下是接手 AI 必須知道的正式決策摘要；完整操作細節仍以 `RULES.md` 為準。

1. 四層架構：`Rules → Knowledge → System → Application`。
2. Knowledge 先於 System。
3. System 必須有實際重複使用證據。
4. Knowledge、System、Application 各自獨立更新，不強制連動。
5. 如果兩種方案都能解決問題，優先選擇維護成本較低的方案。
6. 模型能力補償保持簡單，目前只標註，不建立完整生命週期系統。

## 10. 暫緩中的架構，不是正式規則

以下內容曾經被提出，但目前：**不實作、不正式化、不當成待辦事項。**

- Atomic Knowledge
- Knowledge Aggregation
- PINNED / ACTIVE / DORMANT / RETIRED
- 第二個 Knowledge Repository
- K01–K61
- S01–S37
- Knowledge Graph
- Dependency Graph / Database
- 複雜 Retrieval Engine
- Capability Lifecycle
- Capability-Driven Pruning
- 大型自動化 Knowledge Pipeline

目前正確狀態：

> **候選設計／歷史方案，證據不足，暫時擱置。**

不能理解成「永遠錯」，也不能理解成「下一階段待辦」。

## 11. 「否決」與「暫緩」必須區分

**已否決**：目前已有充分理由認定不值得加入現行系統；除非出現新的具體反證，否則不要重新提出。

**暫緩**：目前沒有足夠實際證據證明需要，但未來可能因規模或實際痛點重新評估。

Atomic Knowledge 等目前屬於：

> **暫緩，不是永久否決。**

`REJECTED-PATHS.md` 是歷史參考文件；其中標示「暫緩」的項目不得被誤讀成永久否決。

## 12. 架構重新啟動 Gate

### Gate 1：Knowledge Retrieval Problem

只有當 INDEX、檔案定位或 AI 選擇相關 Knowledge 的成本已經明顯影響工作效率，才重新評估 Retrieval / Index / Classification。

不設定死的檔案數門檻。

### Gate 2：Knowledge Overlap Problem

只有當高度重疊 Knowledge 已造成實際維護成本、邊界難以維持或內容持續分散，才重新評估 Atomic Knowledge、Aggregation、Deduplication 等方案。

單純發現兩筆內容相似，不足以啟動此 Gate。

### Gate 3：Capability Maintenance Problem

只有當人工逐一確認模型能力補償是否仍有效已成為明顯維護負擔，才重新評估 Capability Registry、Audit、自動檢查或淘汰機制。

## 13. Gate 的最重要原則

哪個問題先發生，就只處理哪個問題。

```text
問題
↓
確認問題真的存在
↓
找最小解法
↓
驗證
↓
仍不足才增加機制
```

不能因為一個 Gate 被觸發，就一次導入 Atomic、Aggregation、Status、Graph、Pipeline 等全部機制。

## 14. K01–K61 / S01–S37 的正確定位

K01–K61 與 S01–S37 是過去架構設計階段的概念清單。

它們：

- 不是目前 Knowledge
- 不是目前 System
- 不是下一階段待辦
- 不需要逐項實作
- 不需要現在重新檢查

保留它們只為未來真的出現問題時，可回看過去曾考慮過哪些方案。

## 15. 第一階段真正要做的事情

現在不要繼續設計 Knowledge Architecture。

目前唯一優先任務：

> **建立第一批 5～10 筆真正可重用的 Knowledge。**

來源不是 K01–K61，而是使用者過去真正遇到、研究過、驗證過、未來可能再次遇到且可跨場景重用的問題。

## 16. 第一批 Knowledge 的目的

這 5～10 筆不是單純填資料，而是第一輪架構實驗。

觀察：

- Knowledge 合理大小
- `RULES.md` 格式是否好用
- Knowledge 邊界與重複情況
- INDEX 是否容易找
- AI 能否快速定位
- 何時自然出現 System
- System 建立門檻是否合理
- 更新 Knowledge 是否容易
- 是否真的需要額外 metadata
- 模型能力補償標註是否產生維護成本

## 17. 第一批 Knowledge 的選擇原則

不要問：

> 「K01–K61 哪五個應該先做？」

應該問：

> **「過去哪些問題，我已經反覆解決過，而且下一次很可能還會遇到？」**

可考慮的方向包括 AI 輸出與 Knowledge Truth 的區分、Source 與 Knowledge 的區分、搜尋前的問題分解、Context Economy、相似內容是否真的相同、新資料是否推翻舊結論、模型能力補償、過度工程化判斷、架構何時值得建立，以及如何判斷研究結果是否值得保存。

這些只是候選方向，不是預先指定的 Knowledge。

## 18. Handoff 不應取代 Repository

| 文件 | 回答的問題 |
|---|---|
| README | Repository 怎麼進入？ |
| RULES | 實際操作規則是什麼？ |
| HANDOFF | 我們為什麼現在這樣做？目前是什麼狀態？ |
| INDEX | 目前有哪些正式內容？ |
| Knowledge / System / Application | 真正保存了什麼？ |

Handoff 的功能是讓新 AI 不會因為缺乏前情而重新走一遍錯誤的設計路線。

## 19. 接手後的實際行為

讀完 Repository 後，新 AI 應得到以下結論：

> **這個系統已經有基本架構，但內容庫還是空的。**

因此不要：

- 重新設計架構
- 重新提出 Atomic Knowledge
- 重新建立 K01–K61
- 建立大量 System
- 建立 Graph
- 建立 Retrieval Engine
- 建立 Capability Pipeline

應該協助使用者從真實過去工作中找出第一批可重用 Knowledge。

## 20. 接手後第一個問題

如果使用者沒有直接指定任務，可以詢問：

> **「目前 Repository 的正式 Knowledge / System / Application 都還是 0。下一步應該先從你過去實際反覆遇到的問題中挑選第一批 Knowledge，而不是繼續設計架構。要我先協助整理候選問題嗎？」**

如果使用者已經提供具體問題，則直接依 `RULES.md` 判斷，不必重複詢問。

## 21. 最重要的防誤判

- 不要把「設計過」當成「已實作」。
- 不要把「暫緩」當成「否決」。
- 不要把「候選方案」當成「待辦事項」。
- 不要因為 Repository 還很空，就認為需要增加更多架構。
- 不要在沒有實際痛點之前建立複雜機制。

## 22. 當前狀態總結

```text
                    ┌─────────────┐
                    │   RULES     │
                    │   已建立     │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │  KNOWLEDGE  │
                    │     0       │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │   SYSTEM    │
                    │     0       │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │ APPLICATION │
                    │     0       │
                    └─────────────┘
```

架構：已建立。

內容：尚未開始累積。

複雜架構：暫不建立。

下一步：建立第一批 5～10 個真實 Knowledge。

重新設計的條件：等待實際 Gate。

## 23. 最終接手指令

1. 以 `RULES.md` 作為正式操作規則。
2. 以本文件作為目前狀態與歷史決策背景。
3. 以 `README.md` 作為 Repository 入口說明。
4. 以三份 `INDEX.md` 判斷目前正式內容。
5. 不把 K01–K61 / S01–S37 當成待辦事項。
6. 不主動啟用 Atomic Knowledge 或其他暫緩架構。
7. 不在沒有實際痛點時擴張系統。
8. 優先建立第一批真實 Knowledge。
9. 實際使用後才根據 Gate 判斷是否需要架構演化。
10. 如果本文件與 `RULES.md` 對實際操作方式有衝突，以 `RULES.md` 為準。
11. 如果舊歷史與本文件的目前狀態有衝突，以本文件的最新狀態為準。

> **不要再設計一個尚不存在的問題；先讓第一批真正有用的 Knowledge 進入系統。**
