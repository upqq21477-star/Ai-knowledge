# Blueprint Governance Skill 規劃 v2.0

版本：v2.0
日期：2026-09-19
狀態：【重新規劃；尚未建立正式 Skill】
定位：維護 Blueprint 地圖與正式系統演化之間的對齊。

## 1. 核心定位
Blueprint 是整體系統的最小可導航地圖；Planning / Meeting Record 保存詳細設計；Registry 保存詳細物件資料；Verification / Evidence 保存驗證責任與依據。

Blueprint Governance 只負責：主要功能是否進入 Blueprint、應放在哪裡、主要關係、實作狀態、詳細規劃入口，以及地圖層級的一致性。

> Blueprint 是地圖；Blueprint Governance 是地圖維護與一致性判斷能力。

## 2. 深度研究結論
Structurizr / C4 支持同一架構模型提供不同視圖，而不是每張圖都成為獨立資料庫。
Backstage Catalog 使用 Entity + Relation 建立可導航的高階模型，並用 System / Domain 組織大量元件；這支持本專案採 Map / Source 分層，而不是把所有詳細資料複製進 Blueprint。
關係必須有語義；depends-on 不等於 affects。本專案既有 Impact 能力仍負責影響判定。

## 3. 責任分工
| 層 | 責任 |
|---|---|
| Skill Registry | Skill 身份、能力、觸發、依賴、I/O、版本等 |
| Blueprint | 主要功能位置、作用、關係、狀態、深入入口 |
| Planning / Meeting Record | 尚未實作功能的詳細設計、討論、方案 |
| Verification | 如何判定功能是否符合條件 |
| Evidence | 實際驗證產生的依據 |
| CURRENT | 現在正式工程狀態 |
| Handoff | 接手時恢復工作 |
| Problem Registry | 實際問題生命週期 |
| Evolution | 已確認變更的演化管理 |

## 4. Blueprint Node 最小模型
- Name
- Status
- Function Summary
- Position / Layer
- Relationship
- Source / Detail Pointer
- Acceptance Stage

## 5. 狀態生命週期與責任

本 Skill 使用三個階段標記，避免把「有規劃」、「功能未完成」與「只剩實際驗收」混為一談。

### 【未】
定義：Blueprint 只有一句功能描述，以及對應的會議紀錄／規劃線索；連第一次正式建立都尚未開始。

責任：
- Blueprint Governance：維持地圖標記與來源。
- Planning / Meeting Record：決定是否形成正式規劃。
- 尚未進入正式實作責任。

### 【驗】
定義：已有正式規劃，但功能尚未全部完成，或尚未走到最後實際驗收階段。即使目前沒有實際功能，只要已經有正式規劃並進入建立準備，就不再使用【未】。

責任：
- Planning / Meeting Record：提供可執行規格。
- Skill / System 實作者：負責建立、整合、修正功能。
- Blueprint Governance：同步目前階段。
- Verification：可定義驗收條件，但此時不宣告實際驗收完成。

### 【代】
定義：規劃中的功能全部已完成，Skill／System 已具備完整功能，只剩最後的實際驗收。

「代」的意思是：在實際驗收尚未發生前，以模擬驗收代替實際驗收來追蹤，不代表已經通過正式驗收。

責任：
- Skill / System 實作者：確認所有規劃功能已完成並提交驗收。
- Verification：負責最後實際驗收。
- Evidence：保存驗收證據。
- Blueprint Governance：將狀態記為【代】，並在實際驗收後移除「【代】」。

### 狀態轉移

【未】
  ↓ 正式規劃建立／進入建立階段
【驗】
  ↓ 全部功能完成，只剩實際驗收
【代】
  ↓ 實際驗收成功
【已建立】

若【驗】階段發現規劃變更，不應直接跳成【代】；先完成必要修改。
若【代】實際驗收失敗，退回【驗】並進入 Problem / Evidence 流程。

### 核心責任原則

> Blueprint Governance 負責「標記與同步」；
> Planning 負責「規劃」；
> Skill / System 實作者負責「建立與完成」；
> Verification 負責「實際驗收」；
> Evidence 負責「留下證據」；
> CURRENT 負責「反映正式現況」。

## 6. Blueprint Mapping
Candidate → 判斷是否為主要功能 → 查既有節點 → Position → Relationship → Status → Source Pointer → 必要時更新 Blueprint。
資料不足則 UNKNOWN，不猜測。

## 7. 不應成為 Blueprint Node
單一文件、單一 Tool、Provider、普通資料、單次 Task、單次 Problem、普通 TODO、內部實作步驟、尚無穩定責任的概念、只有名稱沒有功能證據的候選項。

## 8. Update Trigger
T1 新增主要功能。
T2 主要功能狀態改變。
T3 主要功能位置改變。
T4 主要關係改變。
T5 詳細規劃／會議紀錄入口改變。
T6 發現 Blueprint Drift。
T7 重大架構變更。

## 9. 不應啟動
拼字修正、格式整理、普通文件新增、單次失敗、單次 Routing Failure、Provider 輸出波動、尚未形成結構性證據的想法、純歷史資料整理。
若最後改變主要功能、關係或正式狀態，才重新進入 Trigger。

## 10. Consistency Check
比較 Blueprint、CURRENT、Registry、正式文件，只檢查地圖層級：節點、狀態、位置、主要關係、詳細來源。
結果：ALIGNED / DRIFT / CONFLICT / UNKNOWN。
UNKNOWN 不等於 DRIFT。

## 11. Relationship 最小集合
part-of、depends-on、uses、produces、verifies、triggers、replaces、supersedes、related-to。
只記錄對理解整體地圖有價值且有來源支持的關係。

## 12. Impact 邊界
Blueprint 可以指出 A depends-on B，但不能因此直接寫 A affects B。
Impact 仍由既有 Change / Impact / Evidence 能力判定。

## 13. Verification / Evidence 邊界
Verification：如何判定功能成立。
Evidence：實際產生什麼依據。
Blueprint：功能在整體哪裡。
三者分開。若尚未獨立成為 Blueprint 功能，地圖只標狀態並提供詳細來源。

## 14. 最小輸出
Mapping：Item / Position / Relationship / Status。
Source：Detail Document / Meeting Record / Canonical Source。
Decision：No Change / Add Node / Update Node / Update Relation / Mark Planned / Mark Unknown。
Follow-up：只有需要時才產生 Planning TODO / Verification / Evidence / Change Record。

## 15. Change Record 邊界
小型地圖修改直接更新。
主要功能新增、移除、位置重構才建立簡短 Change Record。
跨 System / Skill 的重大架構變更由既有 Evolution / Impact / Change 治理能力處理；Blueprint Governance 只同步地圖。

## 16. TODO 邊界
Blueprint 只指出主要節點尚未完成；詳細工作仍由現有 Workpool / Todo / Planning 文件管理。
Blueprint TODO 不成為第二套任務系統。

## 17. 核心流程
Skill Registry → Blueprint Mapping → Blueprint。
Blueprint → Planning / Meeting Record → 詳細設計 → Implementation → Verification → Evidence → Blueprint Status 更新。

## 18. 驗收方式

### 18.1 模擬驗收與三階段標記

未完成實際運作前，不把「模擬驗收」寫成正式驗收通過。

- 【未】：只有 Blueprint 線索／一句話功能與會議紀錄，尚未正式建立。
- 【驗】：已有正式規劃，但功能尚未完成，或尚未達到最後驗收前狀態。
- 【代】：全部功能已完成，只剩實際驗收；此時可以先做模擬驗收並持續追蹤。
- 【已建立】：實際驗收完成且有 Evidence 支持。

### 18.2 模擬驗收的責任

模擬驗收由 Blueprint Governance 負責地圖層級的預先檢查；它不能取代 Verification 的正式實際驗收。

### 18.3 失敗處理

若模擬驗收發現缺陷，回到對應規劃／實作責任，不得把【代】視為完成。
若實際驗收失敗，Verification 產生問題／證據，狀態由【代】退回【驗】，直到再次達成「全部功能完成、只剩實際驗收」。

## 19. 最小模擬案例
Case A：新增未實作 Verification → 有狀態、功能說明、詳細來源，不誤標完成。
Case B：Registry 新增 Skill → Registry 保存詳細資料，Blueprint 只保存位置與關係。
Case C：內部文字修改 → 不更新 Blueprint。
Case D：主要功能換位置 → 更新 Position / Relation，必要時 Change Record。
Case E：規劃尚未實作 → 保留節點、標記未實作、指向規劃文件。
Case F：Blueprint 與 CURRENT 不一致 → 標記 DRIFT / CONFLICT，不自行猜測。

## 20. 第一版完成條件
能維護 Blueprint Map；區分已實作與未實作；未實作節點具有最小功能說明與詳細來源；能讀取 Registry 而不取代 Registry；維持主要位置與關係；發現基本 Drift；UNKNOWN 不被猜成已知；不建立第二套 Registry、Impact 或 TODO System。

## 21. 明確不做
Blueprint Database、Blueprint Graph Database、Full Repository Graph、Automatic Architecture Refactoring、Automatic Skill Creation / Merge / Delete、Automatic Impact Engine、Automatic TODO Engine、Automatic Blueprint Rewrite。

理由：目前已存在 Control Plane、Registry、Impact、Evolution、CURRENT 等相關責任；只有自然工作 Evidence 證明存在缺口時才重新評估。

## 22. 最高原則
> Blueprint 是地圖，不是詳細規格。
> 規劃內容可以很龐大，但不能全部塞進地圖。
> 詳細內容交給 Planning / Meeting Record；地圖必須告訴 AI 去哪裡找。
> 未實作功能必須明確標記，並附最小功能說明與詳細來源。
> Registry 管「它是什麼」；Blueprint 管「它在哪裡」。
> Verification 管「如何驗證」；Evidence 管「驗證產生什麼依據」。
> CURRENT 管「現在正式是什麼」。
> 不確定就 UNKNOWN，不猜。
> Blueprint 提供全局方向，Planning 保存深度，Evidence 決定是否可以把規劃變成正式現況。