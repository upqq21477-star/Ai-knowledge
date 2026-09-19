# Blueprint 功能地圖 v1.1

版本：v1.1
日期：2026-09-19
狀態：【Blueprint Map；最小可導航地圖】

## 1. 核心定位

Blueprint 是大型規劃與正式系統的「地圖層」。

它不取代規劃內容，也不取代 Registry、CURRENT、Verification 或 Evidence。

它只讓 AI 先知道：
- 有哪些主要功能。
- 位於哪裡。
- 做什麼。
- 彼此怎麼連接。
- 現在是什麼狀態。
- 要深入時去哪一份規劃／紀錄。

> Blueprint 是地圖；Planning / Meeting Record 是詳細內容。

## 2. 核心流程

Skill Registry
    │
    │ 提供 Skill 資訊
    ↓
Blueprint
    │
    │ 顯示整體位置、功能與關係
    ↓
Verification
    │
    │ 驗證結果
    ↓
Evidence

注意：這是「主要資訊流／責任關係」，不是宣告四者都是同層級獨立 System。

## 3. 深入導航

Blueprint
   │
   ├── Skill Registry
   │      └── 詳細規格 → 2-方案/完善/Skill Registry規劃基線-v1.0.md
   │
   ├── Verification
   │      ├── 狀態：已有正式 Verification 能力；是否作為獨立 Blueprint 節點依地圖層級判定
   │      ├── 功能：驗證系統／Skill 是否符合既定條件
   │      └── 詳細規格 → 1-系統/證據驗證診斷 Skill.md
   │
   ├── Blueprint Governance
   │      ├── State：ACTIVE
   │      ├── Acceptance Stage：【代】
   │      ├── 功能：維護 Blueprint 地圖、狀態、關係、一致性與詳細來源入口
   │      └── 詳細規格 → 1-系統/Blueprint Governance Skill（代）.md
   │
   ├── 會議紀錄管理
   │      ├── State：ACTIVE
   │      ├── Acceptance Stage：【代】
   │      ├── 功能：管理討論成果保存、轉換與過渡紀錄
   │      └── 詳細規格 → 1-系統/會議紀錄管理 Skill（代）.md
   │
   └── Evidence
          ├── 狀態：已有正式 Evidence 能力／Control Plane 資料能力；不是因此宣告為獨立 Evidence System
          ├── 功能：保存、引用與追蹤驗證依據
          └── 詳細來源 → 1-系統/AI Control Plane.md、1-系統/Control Plane Registry 規格.md

## 4. 目前主要節點

| 節點 | 狀態 | 最小作用 | 詳細入口 |
|---|---|---|---|
| Skill Registry | 【已建立／正式接入】 | 提供 Skill 可查詢資訊 | 2-方案/完善/Skill Registry規劃基線-v1.0.md；1-系統/Control Plane Registry 規格.md |
| Blueprint Governance | State=ACTIVE；Acceptance Stage=【代】 | 維護 Blueprint 地圖與一致性 | 1-系統/Blueprint Governance Skill（代）.md |
| 會議紀錄管理 | State=ACTIVE；Acceptance Stage=【代】 | 管理會議紀錄保存與轉換 | 1-系統/會議紀錄管理 Skill（代）.md |
| Blueprint | 【本地圖】 | 顯示整體功能位置與關係 | 本文件 |
| Verification | 【已有正式能力；地圖節點依層級判定】 | 驗證系統／Skill 是否符合條件 | 1-系統/證據驗證診斷 Skill.md |
| Evidence | 【已有正式能力；非獨立 Evidence System】 | 保存／引用驗證依據 | 1-系統/AI Control Plane.md；1-系統/Control Plane Registry 規格.md |

## 5. 未實作功能規則

若未來出現真正尚未實作的主要功能，必須明確標記：

功能名稱【未實作】
    │
    ├── 功能：一句話最小說明
    └── 詳細規劃 → XXX規劃.md

不能只寫功能名稱。

「有規劃文件」不等於「已實作」。

「已有相關能力」也不等於「已形成獨立 System」。

## 6. 狀態語義與驗收階段

Blueprint 必須區分 Acceptance Stage 與正式 State / Lifecycle。完整共同規格見《工程資產狀態與驗收控制規格》。

### 6.1 Acceptance Stage；State / Lifecycle 分離

| 狀態 | 定義 | 判定／執行責任 | 下一步 |
|---|---|---|---|
| 【未】 | 目前只有 Blueprint 上的一句功能描述與相關會議紀錄／規劃線索，連第一次正式建立都尚未開始。 | Blueprint Governance 負責標記；Planning／會議紀錄負責是否形成正式規劃。 | 建立正式規劃與實作入口後，轉【驗】。 |
| 【驗】 | 已有正式規劃，但功能尚未完成，或尚未走到「只剩實際驗收」的階段。 | Skill／System 實作者負責建立與完成；Blueprint Governance 負責同步狀態。 | 功能全部完成、只剩實際驗收時，轉【代】。 |
| 【代】 | Skill／功能本身已完成，規劃中的功能全部具備，只剩最後的實際驗收。「代」代表以模擬驗收代替尚未發生的實際驗收。 | Verification 負責實際驗收；Blueprint Governance 負責記錄【代】與驗收後移除標記。 | 實際驗收成功後移除「【代】」，回到正式完成狀態。 |

### 6.2 狀態順序

【未】 → 【驗】 → 【代】 → 【已建立】

- 【未】不是「功能未完成」的泛稱，而是「尚未正式開始建立」。
- 【驗】不是「已經完成等待驗收」，而是「已有正式規劃，但仍在建立／實作／整合，或尚未達到驗收前狀態」。
- 【代】才是「全部功能已完成，只差實際驗收」。
- 實際驗收成功後，移除階段標記，回到正常正式狀態。

Blueprint 不自行判斷功能是否真的完成；它依據 Planning／Implementation／Verification 結果同步狀態。正式完成與否以正式來源及驗收 Evidence 為準。

### 6.3 責任邊界

- **Blueprint Governance**：維護地圖上的狀態、位置、關係與來源；不代替實作者完成功能，也不代替 Verification 做正式驗收。
- **Planning / Meeting Record**：負責把【未】的功能線索發展成可執行的正式規劃。
- **Skill / System 實作者**：負責【驗】階段的功能建立、整合、修正與完成；完成全部功能後提出進入【代】。
- **Verification**：負責【代】階段的最後實際驗收，產生驗收 Evidence；失敗則退回【驗】。
- **Evidence**：保存實際驗收依據。
- **CURRENT**：在實際驗收成功後反映正式現況。

## 7. 關係

Blueprint 只保留對理解全局有用、且有來源支持的主要關係。

例如：
- part-of
- depends-on
- uses
- produces
- verifies
- triggers
- replaces
- supersedes
- related-to

特別注意：

depends-on ≠ affects。

Impact 必須由既有 Change / Impact / Evidence 能力判定。

## 8. 詳細內容導航規則

Blueprint 不複製大型規劃。

需要深入時：

Blueprint
→ 規劃／會議紀錄
→ 詳細設計
→ 實作
→ Verification
→ Evidence
→ 狀態更新

因此大型規劃可以持續增加深度，而 Blueprint 不必同步膨脹。

## 9. 防止 AI 誤判

Blueprint 出現一個名稱，不代表它已實作。

判定正式現況時，優先確認：
1. Status
2. CURRENT
3. Canonical Source / Definition
4. 必要時 Verification / Evidence

Blueprint 是導航來源，不是單獨的 CURRENT Source of Truth。

## 10. 更新條件

只有以下情況更新 Blueprint：

- 新增主要功能。
- 刪除主要功能。
- 主要功能狀態改變。
- 主要功能位置改變。
- 主要關係改變。
- 詳細規劃／紀錄入口改變。
- 發現地圖與正式現況不一致。

一般文件修改、單次問題、內部文字調整，不應直接修改 Blueprint。

## 11. 邊界

Blueprint 不保存：
- Skill 詳細 Definition。
- Registry 詳細資料。
- Verification 詳細規則。
- Evidence 詳細格式。
- Impact 計算。
- Runtime Trace。
- 完整 Repository Inventory。
- 完整 TODO。
- 自動架構修改。

## 12. 驗收狀態

Blueprint Governance 本身也遵守同一套階段語義：

【未】＝只有地圖上的功能線索／一句話描述與會議紀錄，尚未正式建立。
【驗】＝已有正式規劃，但 Blueprint Governance 的完整功能尚未全部建立，或尚未進入最後實際驗收前階段。
【代】＝Blueprint Governance 功能已全部建立，只剩最後實際驗收；此階段使用模擬驗收作為替代追蹤。
正式實際驗收成功後，移除「【代】」，並由正式狀態取代。

模擬驗收不是「功能已驗收」；它只證明在尚未進行實際運作前，流程與規則已經可以被預先檢查。


## 13. 狀態控制來源

所有正式 Skill／System 等工程資產的狀態語義，以《1-系統/工程資產狀態與驗收控制規格.md》為共同規格。

三個維度必須分開：
- State：目前正式可用／工作狀態。
- Acceptance Stage：【未】→【驗】→【代】→【已建立】。
- Lifecycle：正式生命週期。

例如「會議紀錄管理 Skill」不是 ACTIVE（代）這種單一狀態，而是：State=ACTIVE、Acceptance Stage=【代】、Lifecycle=Active。

會議紀錄自身的 OPEN → READY → CONVERTED → CLOSED 只屬於紀錄內容生命週期。

因此 Blueprint 可以統一顯示不同類型資產，而不把不同狀態系統混成一套。