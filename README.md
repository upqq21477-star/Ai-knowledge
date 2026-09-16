# AI 個人工程知識系統

## AI Entry Point

> 任何 AI 進入這個 repository，請依序讀取：
> 1. 本文件（README.md）
> 2. [RULES.md](./RULES.md)
> 3. [HANDOFF.md](./HANDOFF.md)
> 4. [0-knowledge/INDEX.md](./0-knowledge/INDEX.md)
> 5. [1-systems/INDEX.md](./1-systems/INDEX.md)
> 6. [2-applications/INDEX.md](./2-applications/INDEX.md)
>
> `HANDOFF.md` 負責目前狀態、歷史決策與架構重新啟動條件；`RULES.md` 是正式操作規則。
>
> 讀完後，若使用者沒有指定任務，先依 HANDOFF.md 判斷目前階段：目前正式 Knowledge / System / Application 都是 0，優先協助從真實過去工作中找出第一批可重用 Knowledge，而不是重新設計架構。
>
> 也可以直接從使用者的自然語言描述判斷意圖，不需要等待選項輸入。
> 不要一次讀取所有 Knowledge／System 內容——先看 INDEX，判斷相關，再深讀相關的檔案。
>
> **AI 可讀性提醒**：若你是透過網頁抓取（而非本地檔案系統）讀取這個 repository，通常無法瀏覽資料夾樹狀頁面，只能跟隨頁面裡已經存在的明確連結。上面第 2-6 項已經是可跟隨的連結；要深入某份 Knowledge／System／Application，一律從對應 INDEX.md 裡的連結點進去，不要自行組合網址。

## 這是什麼

一套個人工程知識系統：把已經研究、驗證過的問題整理成可重複使用的知識，下一次遇到類似問題時，先找既有知識，必要時查最新資料，避免重新研究。

使用者是一人工作室，不是企業或團隊。所有設計以「低維護成本」為最高原則：夠用優先於齊全，能不建立的機制就不建立。

## 核心架構

```
L0  Rules         定義系統怎麼運作（見 RULES.md）
    ↓
L1  Knowledge     基本定律／原理，獨立、可重用（0-knowledge/）
    ↓
L2  System        由多份 Knowledge 組成的模型／方法（1-systems/）
    ↓
L3  Application   組裝 System／Knowledge 解決具體需求（2-applications/）
```

Knowledge 不預先建立彼此的關係；關係只在 System 組合時才產生。每一層的更新互不強制連動，細節見 RULES.md 第 7 節。

## 資料夾結構

```
README.md
RULES.md
HANDOFF.md
REJECTED-PATHS.md
0-knowledge/
    INDEX.md
    （各份 Knowledge .md 檔）
1-systems/
    INDEX.md
    （各份 System .md 檔）
2-applications/
    INDEX.md
    （各份 Application .md 檔或資料夾）
```

## 快速開始

**新增 Knowledge**
研究 → 驗證 → 判斷是否跨場景可重用 → 依 RULES.md 第 4 節格式寫成 `0-knowledge/xxx.md` → 更新 `0-knowledge/INDEX.md`（檔名欄位記得用連結格式，見 RULES.md 第 3 節）

**建立 System**
確認至少兩份 Knowledge 已經被同一類問題實際重複組合使用過一次以上 → 依 RULES.md 第 5 節格式寫成 `1-systems/xxx.md` → 更新 `1-systems/INDEX.md`

**建立 Application**
出現具體需求 → 優先掃描 `1-systems/INDEX.md`，涵蓋不到才往下查 `0-knowledge/INDEX.md` → 組裝 → 依 RULES.md 第 6 節格式寫成 `2-applications/xxx.md` → 更新 `2-applications/INDEX.md`

**更新既有內容**
見 RULES.md 第 7 節的更新規則，三層各自獨立判斷。

## 完整規則

見 [RULES.md](./RULES.md)——所有 AI 操作規則都在那裡；設計背景與目前狀態見 [HANDOFF.md](./HANDOFF.md)。
