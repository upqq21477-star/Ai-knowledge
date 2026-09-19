# Blueprint Governance Skill

版本：v1.0
日期：2026-09-19
State：ACTIVE
Acceptance Stage：【代】
Lifecycle：Active
狀態控制依據：1-系統/工程資產狀態與驗收控制規格.md
定位：Blueprint 地圖維護與一致性判斷 Skill。

## 1. 核心責任

維護 Blueprint 最小可導航地圖，負責：
- 主要功能是否應進入 Blueprint。
- 功能在整體架構中的位置。
- 主要關係。
- 工作階段狀態。
- 詳細規劃／會議紀錄入口。
- Blueprint 與正式現況的地圖層級一致性。

不取代 Skill Registry、Planning、Verification、Evidence、CURRENT、Impact 或 TODO。

## 2. 觸發

以下情況觸發：
- 新增主要功能。
- 主要功能狀態改變。
- 主要功能位置或主要關係改變。
- 詳細規劃／會議紀錄入口改變。
- 發現 Blueprint 與正式現況不一致。
- 重大架構變更需要同步地圖。

以下通常不觸發：
- 拼字／格式修改。
- 普通文件新增。
- 單次問題。
- 單次 Routing Failure。
- Provider 輸出波動。
- 尚未形成結構性證據的想法。

## 3. 輸入

- Blueprint 現況。
- Skill Registry 資訊。
- Planning / Meeting Record。
- CURRENT。
- 正式 Definition / Canonical Source。
- 必要時 Verification / Evidence。
- Change / Evolution 資訊。

## 4. 核心流程

Candidate
→ 判斷是否為主要功能
→ 查既有節點
→ Position
→ Relationship
→ Status
→ Source Pointer
→ Consistency Check
→ 必要時更新 Blueprint

資料不足時標記 UNKNOWN，不自行猜測。

## 5. Blueprint Node 最小資料

- Name
- Status
- Function Summary
- Position / Layer
- Relationship
- Source / Detail Pointer
- Acceptance Stage

Blueprint 只保存理解全局所需的最小資訊。

## 6. Acceptance Stage

### 【未】

只有 Blueprint 上的一句功能描述與會議紀錄／規劃線索，連第一次正式建立都尚未開始。

### 【驗】

已有正式規劃，但功能尚未全部完成，或尚未進入最後實際驗收階段。

### 【代】

所有規劃功能已完成，Skill／System 已具備完整功能，只剩最後實際驗收。

「代」表示實際驗收尚未發生，因此先以模擬驗收追蹤；不代表正式驗收已通過。

### 【已建立】

實際運行取得足夠 Evidence 後，Acceptance Stage 由【代】轉為【已建立】。State / Lifecycle 仍由各自正式規則管理。

Acceptance Stage 流程：

【未】 → 【驗】 → 【代】 → 【已建立】

注意：Acceptance Stage ≠ State ≠ Lifecycle。Blueprint 不自行創造新的 State。

【代】實際驗收失敗 → 【驗】。

## 7. 狀態責任

- Blueprint Governance：標記、同步、維護地圖。
- Planning / Meeting Record：建立與維護正式規劃。
- Skill / System 實作者：建立、整合、修正並完成功能。
- Verification：負責最後實際驗收。
- Evidence：保存驗收依據。
- CURRENT：反映正式工程現況；不得被 Acceptance Stage 單獨取代。

Blueprint Governance 不代替實作者建立功能，也不代替 Verification 做正式驗收。

## 8. 關係

可記錄：
- part-of
- depends-on
- uses
- produces
- verifies
- triggers
- replaces
- supersedes
- related-to

depends-on 不等於 affects。

Impact 仍由既有 Change / Impact / Evidence 能力判定。

## 9. 一致性檢查

比較：
- Blueprint
- CURRENT
- Registry
- 正式文件

只檢查地圖層級：
- 節點
- 狀態
- 位置
- 主要關係
- 詳細來源

結果：
- ALIGNED
- DRIFT
- CONFLICT
- UNKNOWN

UNKNOWN 不等於 DRIFT。

## 10. 輸出

Mapping：
- Item
- Position
- Relationship
- Status

Source：
- Detail Document
- Meeting Record
- Canonical Source

Decision：
- No Change
- Add Node
- Update Node
- Update Relation
- Mark Planned
- Mark Unknown

必要時 Follow-up：
- Planning TODO
- Verification
- Evidence
- Change Record

## 11. 邊界

不建立：
- Blueprint Database
- Blueprint Graph Database
- Full Repository Graph
- Automatic Architecture Refactoring
- Automatic Skill Creation / Merge / Delete
- Automatic Impact Engine
- Automatic TODO Engine
- Automatic Blueprint Rewrite

## 12. 模擬驗收【代】

目前以模擬驗收代替尚未發生的實際運作驗收。

至少檢查：

A. 新增未建立功能
→ 能標記【未】，保留一句功能描述與詳細來源。

B. 已有規劃但功能未完成
→ 能標記【驗】，不得誤標為完成。

C. 功能全部完成、只剩實際驗收
→ 能轉為【代】並進行模擬驗收。

D. Registry 新增 Skill
→ 詳細資料留在 Registry，Blueprint 只同步位置與主要關係。

E. 內部文字修改
→ 不因普通文字變更更新 Blueprint。

F. 主要功能位置改變
→ 更新 Position / Relation，必要時建立 Change Record。

G. Blueprint 與 CURRENT 不一致
→ 標記 DRIFT / CONFLICT / UNKNOWN，不自行猜測。

H. 【代】實際驗收失敗
→ 退回【驗】，進入 Problem / Evidence 流程。

模擬驗收 PASS 不等於實際運行 Evidence；它只支持進入【代】並准入運行。

## 13. 正式來源

詳細規劃：
藍圖/規劃/Blueprint Governance Skill-規劃-v1.0.md

功能地圖：
藍圖/Blueprint功能地圖-v1.0.md
