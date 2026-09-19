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
   └── Evidence
          ├── 狀態：已有正式 Evidence 能力／Control Plane 資料能力；不是因此宣告為獨立 Evidence System
          ├── 功能：保存、引用與追蹤驗證依據
          └── 詳細來源 → 1-系統/AI Control Plane.md、1-系統/Control Plane Registry 規格.md

## 4. 目前主要節點

| 節點 | 狀態 | 最小作用 | 詳細入口 |
|---|---|---|---|
| Skill Registry | 【已建立／正式接入】 | 提供 Skill 可查詢資訊 | 2-方案/完善/Skill Registry規劃基線-v1.0.md；1-系統/Control Plane Registry 規格.md |
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

## 6. 狀態語義

【已建立】＝有正式可確認的能力／規格。

【規劃中】＝已有規劃，但尚未宣告正式實作。

【未實作】＝明確規劃存在，但尚未形成可用正式能力。

【未獨立成立】＝能力可能存在，但沒有證據支持它應成為獨立主要節點／System。

【UNKNOWN】＝資料不足，不猜。

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

目前 Blueprint Governance 尚未形成獨立正式 Skill。

因此本規劃與地圖能力的未完成部分先採：

【Simulation Acceptance（代）】

待自然工作實際運作成功並有證據後，再移除「（代）」。

