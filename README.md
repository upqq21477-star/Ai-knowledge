# AI 個人工程知識系統

## AI Entry Point

這個 repository 是一套給單人工作室使用的 **Personal AI Engineering Knowledge System**。

任何 AI 接手時，建議依下列順序建立理解：

1. `README.md`：知道這個 repository 是什麼。
2. `RULES.md`：正式操作規則。
3. `HANDOFF.md`：目前狀態、歷史決策、架構轉折與接手注意事項。
4. 依實際任務直接讀取 repository 內相關資料夾與文件。
5. 完整稽核時，可以遞迴讀取整個 repository。

**重要：Repository 實際檔案樹是內容的 Source of Truth。AI 可以直接讀取資料夾內文件，不需要依賴 INDEX 才能找到內容。**

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
    （目前 7 筆正式 Knowledge）

1-systems/
    （目前 0 筆）

2-applications/
    （目前 0 筆）
```

目前第一批 7 筆 Knowledge 已建立；System 與 Application 尚未建立。

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

## 第一批 Knowledge

目前第一批 Knowledge 來自使用者過去實際反覆遇到的問題，而不是直接搬運 K01–K61。

它們目前用於驗證：

- Knowledge 的自然大小與邊界。
- 不同 Knowledge 是否產生實際重疊。
- AI 是否能直接找到需要的文件。
- 是否真的需要 INDEX。
- 何時自然形成 System。
- 更新與維護成本是否開始增加。

## System 與 Application

System 不預先建立。只有當多份 Knowledge 在同一類問題中實際反覆組合，並證明組合值得保存，才建立 System。

Application 在出現具體需求時建立，可以包含專案特有決策。

## 正式規則

所有操作規則以 `RULES.md` 為準。

目前狀態、歷史決策與架構重新整理原因見 `HANDOFF.md`。

歷史方案與目前不採用方向見 `REJECTED-PATHS.md`。
