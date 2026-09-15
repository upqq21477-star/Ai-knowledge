# AI 個人工程知識系統

## AI Entry Point

> 任何 AI 進入這個 repository，請依序讀取：
> 1. 本文件（README.md）
> 2. RULES.md
> 3. 0-knowledge/INDEX.md
> 4. 1-systems/INDEX.md
> 5. 2-applications/INDEX.md
>
> 讀完後，主動詢問使用者：「你現在要創建知識、建立系統，還是創建應用？」
> 也可以直接從使用者的自然語言描述判斷意圖，不需要等待選項輸入。
> 不要一次讀取所有 Knowledge／System 內容——先看 INDEX，判斷相關，再深讀相關的檔案。

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

Knowledge 不預先建立彼此的關係；關係只在 System 組合時才產生。每一層的更新互不強制連動，細節見 RULES.md 第 6 節。

## 資料夾結構

```
README.md
RULES.md
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
研究 → 驗證 → 判斷是否跨場景可重用 → 依 RULES.md 第 3 節格式寫成 `0-knowledge/xxx.md` → 更新 `0-knowledge/INDEX.md`

**建立 System**
確認至少兩份 Knowledge 已經被同一類問題實際重複組合使用過一次以上 → 依 RULES.md 第 4 節格式寫成 `1-systems/xxx.md` → 更新 `1-systems/INDEX.md`

**建立 Application**
出現具體需求 → 優先掃描 `1-systems/INDEX.md`，涵蓋不到才往下查 `0-knowledge/INDEX.md` → 組裝 → 依 RULES.md 第 5 節格式寫成 `2-applications/xxx.md` → 更新 `2-applications/INDEX.md`

**更新既有內容**
見 RULES.md 第 6 節的更新規則，三層各自獨立判斷。

## 完整規則

見 [RULES.md](./RULES.md)——所有 AI 操作規則都在那裡，不在本文件重複。
