# AI 單人工作室命名治理規範 v1.0

> 文件定位：Blueprint Governance／Naming Governance
> 文件性質：全庫命名原則、分類語意與後續 Rename Migration 的治理規格。
> 狀態：【CURRENT／藍圖治理規格】
> 建立日期：2026-09-18
> 重要邊界：本文件先凍結「如何命名」的規則，不代表立即對既有 Repository 進行全面改名。

## 一、建立原因

目前 Repository 的部分文件名稱形成於不同工程階段，早期命名較偏向當時的討論語境，後續又逐步加入 System、Capability、Plan、Process、Evidence、Mapping 等不同層級。

因此目前存在以下風險：
1. 從檔名無法立即判斷文件的責任類型。
2. System、Process、Capability、Plan 等概念可能使用相似詞彙。
3. 同一責任可能因不同時期命名而形成多份看似不同的文件。
4. AI 進行 Recall 時，容易因名稱相似而混淆用途。
5. Mapping、State、Version 與 Canonical Source 的判定成本增加。
6. 後續大型系統演化時，Rename、Merge、Split、Replace 的影響範圍難以控制。

因此後續命名治理應從「名稱好不好看」提升為：
> **讓名稱本身提供最低限度的分類與功能訊號，使人與 AI 在未閱讀全文前，就能初步知道「這是什麼類型、負責什麼」。**

## 二、核心原則

### 2.1 類型優先於名稱
新文件命名時，優先表達：類型 → 功能／責任 → 範圍或對象 → 版本。
最低要求：名稱至少能看出「類型」與「主要功能」。

### 2.2 名稱不是內容
正確關係：文件內容 → 判定實際責任 → 判定類型 → 產生名稱。
不得反過來由檔名猜測文件類型。名稱是索引訊號，不是 Canonical Source。

### 2.3 新增優先、既有延後
本規範建立後，新建文件立即遵守新命名規則。既有文件不得因命名不一致就立即批次改名。
既有文件必須先完成內容閱讀、責任判定、State、Canonical 關係、重複／演化關係與引用檢查，再決定是否 Rename。

## 三、建議命名結構
一般文件採：類型＋功能／責任＋對象／範圍＋版本。
其中不是每一層都必須存在。
版本維持既有工程版本格式，例如 -v1.0.md。
不要把 State 放入一般檔名，例如 -CURRENT、-REVIEW、-HISTORICAL；State 應由文件內容、Registry 或正式狀態資料管理。

## 四、正式類型與 Namespace

| 類型 | Namespace | 語意 |
|---|---|---|
| Knowledge | Kxx | 知識資產 |
| Capability | CAP-xxx | 可驗證、可比較、可提供的能力 |
| System | SYS-xxx | 持續性系統責任 |
| Plan | PLN-xxx | 正式工程方案 |
| Scenario | SCN-xxx | 工作情境／測試情境 |
| Evidence | EVD-xxx | 證據資產 |
| Decision | DEC-xxx | 正式決策 |
| Mapping | MAP-xxx（如未來正式建立） | Derived View／對照視圖 |

Namespace 與檔名不是同一層。現階段既有檔案不要求全部立即把 Namespace ID 寫進檔名。

## 五、目前不應任意新增的類型
Registry、Graph、Engine、Orchestrator、Framework、Manager、Core、Hub、Center 等詞可以作為實作或架構角色描述，但在沒有正式 Namespace／責任模型前，不應自行大量建立新的正式 ID。
名稱中出現「系統」不代表它就是 System，必須以實際責任判定。

## 六、功能命名原則
優先使用動作／責任，而不是抽象口號。例如：知識狀態管理、系統目錄管理、觸發條件管理、問題解決、能力蒸餾、版本演化追蹤、證據管理。
避免只使用：統御、核心、中樞、智慧、協調、整合、管理中心，除非該詞本身已有正式且穩定的責任邊界。

「管理」不能單獨作為功能定義。應說明管理什麼、做哪些動作、邊界在哪裡。

「統御」需限制使用，因為它可能同時表示 Orchestration、Governance、Coordination、Control、System Management。新文件除非能明確定義責任，不應單獨使用「統御」作為主要命名依據。

## 七、不同文件類型的命名規則
### 7.1 System
形式：系統＋主要責任。System 描述持續性系統責任，例如系統目錄管理系統、觸發條件管理系統、問題解決系統。

### 7.2 Capability
形式：能力＋可驗證功能。Capability 應避免與 System 名稱完全相同。例如：能力＝觸發條件候選識別；系統＝觸發條件管理系統。

### 7.3 Plan
形式：方案＋工程目的。目前四個正式方案保持既有名稱，不因命名治理建立第五方案。

### 7.4 Process
形式：流程＋目的／工作，例如問題解決流程、新系統建立流程、Migration 驗證流程。

### 7.5 Scenario
形式：情境＋工作目的。正式 Namespace 使用 SCN-xx；歷史 S01–S10 保留作為來源識別。

### 7.6 Evidence
形式：證據＋事件／驗證對象。Evidence 不應被命名成系統。

### 7.7 Decision
形式：決策＋決策主題。應能回答決定了什麼、為什麼、根據哪些 Evidence、影響什麼、是否改變 Canonical Source。

### 7.8 Mapping
形式：Mapping／對照＋來源與目標。Mapping 是 Derived View，不得取代 Canonical Source。

## 八、既有檔案 Rename 判定流程
原始檔名 → 讀取完整內容 → 判定文件類型 → 判定主要責任 → 判定 State → 判定 Canonical／Evolution 關係 → 檢查重複與衝突 → 產生新名稱 → 建立 Rename Mapping → 搜尋 Repository 引用 → Rename → 更新引用 → 驗證 → Git Commit。
不得只看檔名就批次改名。

## 九、Rename Mapping 最低欄位
| 欄位 | 說明 |
|---|---|
| Old Path | 原始路徑 |
| New Path | 新路徑 |
| Type | 文件類型 |
| Function | 實際主要功能 |
| State | CURRENT／REVIEW 等 |
| Canonical ID | 對應正式 ID，如有 |
| Relation | 前身／取代／同責任／分拆等 |
| Reason | 改名原因 |
| References | 受影響引用 |
| Validation | 改名後驗證結果 |
| Commit | Git 證據 |

## 十、命名治理與 P0.5 的關係
命名治理不是獨立於基線重建之外的另一套工程。
建議關係：P0.5 資料盤點 → 確認文件實際語意 → State / Disposition → Canonical 關係 → Naming Governance → Rename Migration → 引用驗證 → 乾淨 Baseline → Mapping。
因此：**命名規則現在先建立；大規模 Rename 不應早於語意盤點完成。**

## 十一、與 Mapping 的關係
Mapping 是 Derived View。命名治理完成後可以提高 Mapping 可讀性，但不能透過改名直接製造 Mapping 結論。
若新名稱與 Mapping 不一致，先回到 Canonical Source 判斷，而不是為了配合 Mapping 修改名稱。

## 十二、與 AI Recall 的關係
命名治理的主要 AI 價值不是美觀，而是降低 Recall 歧義。
名稱提供 Candidate Signal；內容與 State 提供 Applicability 判定。
名稱永遠不能直接觸發 Execute。

## 十三、命名治理的優先順序
第一階段：現在建立規則。立即完成命名原則、類型分類、功能命名規則、Namespace 邊界、Rename 判定流程、Rename Mapping 格式。

第二階段：基線完成後執行。待 P0.5 主系統基線重建完成，再針對主要資產進行語意判定、建立 Rename Mapping、優先處理高歧義／高重複／高風險文件、批次 Rename、更新引用、驗證 Git 歷史與追溯，最後更新 Blueprint Mapping。

## 十四、第一批優先處理對象
1. System／Process／Capability 混用的文件。
2. 名稱高度相似但責任可能不同的文件。
3. 同一責任存在多個名稱的文件。
4. 名稱包含「核心／統御／管理／協調／整合」但責任不清楚的文件。
5. 會直接影響 Mapping 的核心文件。
6. 會影響 AI Recall 的 CURRENT 文件。

目前已發現的高風險群包括：後續工作觸發式順便驗證系統版本群、觸發條件管理系統版本群、系統管理統御分支／系統管理統御分支系統、統御方案系統／統御小系統協調管理系統、AI知識庫基本運作系統、整體資料治理系統、AI知識管理系統、知識迭代與資料演化系統、更新監控與觸發系統、來源與證據分析系統、共同對象與關係目錄系統。
以上只是第一批命名治理候選，不代表現在已判定它們的新名稱或最終 System 邊界。

## 十五、禁止事項
1. 不因名稱不好看就改名。
2. 不只看檔名判定文件類型。
3. 不把所有文件都強行加上 System。
4. 不把所有流程都實體化成 System。
5. 不把 Capability 與 System 混為一談。
6. 不為了命名一致而破壞 Git 歷史。
7. 不直接批次 Rename 而不建立 Rename Mapping。
8. 不在 Canonical Source 尚未確認前建立正式 Namespace。
9. 不因命名治理新增第五方案。
10. 不因命名治理猜測 K07–K61／S11–S37。
11. 不用新名稱反向證明文件已 CURRENT。
12. 不把命名治理當成內容治理的替代品。

## 十六、完成判定
命名治理不是「所有檔名全部改完」才算完成。

規則完成：新文件已能依同一套類型／功能規則命名。
語意完成：既有高風險文件已完成實際責任判定。
Migration 完成：必要 Rename 已執行，引用已更新，Git 歷史可追溯。
Recall 驗證完成：Memoryless AI 能從名稱初步判斷文件類型與功能，再透過內容、State、Canonical Source 判斷是否適用。

真正目標：**讓名稱成為可靠的第一層索引，而不是另一種混亂來源。**

## 十七、與未來藍圖待辦的關係
本規範建立後，應加入未來藍圖待辦，但不應插入 P0 核心物件模型之前。
建議位置：**P0／P0.5 基礎規格與資料基線完成後，作為 Phase 2.5：命名治理與 Rename Migration 執行。**

原因：太早 Rename 會因語意尚未確認而二次改名；太晚則會讓大量 Mapping 固化後產生較大引用與 Derived View 影響。最佳點是規格足以判定類型，但正式 Mapping 大規模固化前。

## 十八、核心原則
> **先判定責任，再命名。**
> **先建立規則，再改舊名。**
> **類型先於功能名稱。**
> **功能名稱先於修飾詞。**
> **名稱提供索引訊號，內容提供語意證據。**
> **Rename 必須可追溯。**
> **Canonical Source 優先於檔名。**
> **新文件立即遵守，舊文件分批遷移。**
> **命名治理服務 Recall、Mapping 與交接，不反過來決定系統架構。**