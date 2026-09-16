# AI 個人工程知識系統

## AI Entry Point

這個 repository 是一套給單人工作室使用的 **Personal AI Engineering Knowledge System**。

任何 AI 接手時，建議依下列順序建立理解：

1. `README.md`：知道這個 repository 是什麼，以及目前入口規則。
2. `RULES.md`：正式操作規則。
3. `HANDOFF.md`：目前狀態、歷史決策、已知設計轉折與接手注意事項。
4. 依實際任務讀取 repository 內相關資料夾與文件。
5. 必要時再讀取其他歷史文件。

**重要：不要把 INDEX 當成 repository 的唯一目錄。AI 可以直接讀取資料夾內的文件；repository 的實際檔案樹才是內容的 Source of Truth。**

## 這是什麼

第一次遇到問題時研究、驗證並保存可跨場景重用的 Knowledge；下一次遇到類似問題時優先重用既有 Knowledge，降低重新研究成本。

使用者是一人工作室，因此最高原則是：

> **低維護成本優先於完整性。**

不要為了讓系統看起來完整，而預先建立資料庫、圖譜、索引治理、狀態機或自動化流程。

## 核心架構

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

- **Rules**：定義整套系統怎麼運作。
- **Knowledge**：可獨立理解、可跨場景重用的知識、原理、判斷或方法。
- **System**：在實際使用中反覆證明有價值後，由多份 Knowledge 組合而成的方法／模型。
- **Application**：針對具體需求，組裝 Knowledge / System 的實際應用。

## Repository 結構

```text
README.md
RULES.md
HANDOFF.md
REJECTED-PATHS.md

0-knowledge/
    （正式 Knowledge）

1-systems/
    （正式 System）

2-applications/
    （正式 Application）
```

目前三個內容層都仍為空。

## AI 如何探索 repository

不要依賴預先維護的 INDEX 才能找到文件。

正確原則是：

```text
Repository 實際檔案樹
        ↓
判斷任務需要哪些資料夾／文件
        ↓
直接讀取相關文件
        ↓
必要時擴大閱讀範圍
```

如果需要完整稽核，可以直接遞迴讀取整個 repository 的文字文件；如果只是處理單一問題，則只讀取與問題相關的內容。

「全部讀取」與「每次都全部讀取」是兩件不同的事：前者是能力，後者不是規則。

## 開始建立內容

第一批 Knowledge 不從過去的 K01–K61 清單直接搬運。

應該從使用者過去真正反覆遇到、研究過、驗證過，而且未來可能再次遇到的問題中提取。

System 也不預先建立。只有當多份 Knowledge 在同一類問題中實際反覆組合，才有理由建立 System。

Application 則在出現具體需求時建立。

## 正式規則

所有操作規則以 `RULES.md` 為準。

目前狀態、歷史決策與本次架構重新整理的原因見 `HANDOFF.md`。
