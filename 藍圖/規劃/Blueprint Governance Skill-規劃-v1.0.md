# Blueprint Governance Skill 規劃 v2.1

版本：v2.1
日期：2026-09-19
狀態：【代】；正式 Skill 已建立，尚待自然工作 Evidence
定位：維護 Blueprint 地圖與正式系統演化之間的對齊。

## 1. 核心定位

Blueprint 是整體系統的最小可導航地圖；Planning / Meeting Record 保存詳細設計；Registry 保存詳細物件資料；Verification / Evidence 保存驗證責任與依據。

Blueprint Governance 只負責主要功能、位置、主要關係、最小狀態／驗收標記、詳細入口與地圖層級一致性。

## 2. 責任分工

| 層 | 責任 |
|---|---|
| Skill Registry | Skill 身份、能力、觸發、依賴、I/O、版本等 |
| Blueprint | 主要功能位置、作用、關係、最小 State / Acceptance、深入入口 |
| Planning / Meeting Record | 尚未實作功能的詳細設計、討論、方案 |
| Verification | 判定功能是否符合條件 |
| Evidence | 實際驗證依據 |
| CURRENT | 現在正式工程狀態 |
| Handoff | 接手時恢復工作 |
| Problem Registry | 實際問題生命週期 |
| Evolution | 已確認變更的演化管理 |

## 3. Blueprint Node 最小模型

- Name
- Function Summary
- Position / Layer
- Relationship
- Source / Detail Pointer
- State（需要時）
- Acceptance（需要時）

不在 Blueprint 建立另一套 State / Lifecycle / Registry。

## 4. Acceptance

共同語義引用：
《1-系統/工程狀態與驗收最小規則.md》

- 【未】：尚未正式開始建立。
- 【驗】：建立、整合或修正中。
- 【代】：功能已完成、模擬驗收 PASS、可運行，但尚缺自然工作 Evidence。
- 足夠 Evidence：移除【代】。
- 發現需要修正的問題：回【驗】。

不再建立【已建立】作為額外 Acceptance 狀態。

## 5. State

State 表示目前正式工作／可用狀態。

Blueprint Governance 目前：
State = ACTIVE
Acceptance = 【代】

禁止 ACTIVE（代）或 ACTIVE【代】。

## 6. Mapping

Candidate
→ 判斷是否為主要功能
→ 查既有節點
→ Position
→ Relationship
→ State / Acceptance
→ Source Pointer
→ Consistency Check
→ 必要時更新 Blueprint

資料不足則 UNKNOWN，不猜測。

## 7. Update Trigger

T1 新增主要功能。
T2 主要功能 State / Acceptance 改變。
T3 主要功能位置改變。
T4 主要關係改變。
T5 詳細規劃／會議紀錄入口改變。
T6 發現 Blueprint Drift。
T7 重大架構變更。

拼字、格式、普通文件新增、單次問題、單次 Routing Failure、Provider 輸出波動通常不觸發。

## 8. 一致性

比較 Blueprint、CURRENT、Registry、正式 Definition / Source。

結果：
ALIGNED / DRIFT / CONFLICT / UNKNOWN

UNKNOWN 不等於 DRIFT。

## 9. Relationship

只記錄對整體地圖有價值且有來源支持的關係：

part-of、depends-on、uses、produces、verifies、triggers、replaces、supersedes、related-to

depends-on ≠ affects。

Impact 仍由既有 Change / Impact / Evidence 能力判定。

## 10. Verification / Evidence 邊界

Verification：如何判定功能成立。
Evidence：實際產生什麼依據。
Blueprint：功能在整體哪裡。

三者不互相取代。

## 11. Change / TODO 邊界

小型地圖修改直接更新。
主要功能新增、移除、位置重構才需要 Change Record。
重大跨 Skill / System 變更由既有 Evolution / Impact / Change 治理能力處理。

詳細工作仍由既有 TODO / Workpool / Planning 管理；Blueprint 不建立第二套 TODO。

## 12. 模擬驗收

A. 未建立功能 → 【未】。
B. 規劃／建立中 → 【驗】。
C. 全功能完成 → 模擬 PASS → 【代】。
D. Registry 新增 Skill → 只同步位置／主要關係。
E. 普通內部文字修改 → 不更新 Blueprint。
F. 主要位置改變 → 更新 Position / Relation。
G. Blueprint 與 CURRENT 不一致 → DRIFT / CONFLICT / UNKNOWN。
H. 【代】實際運行發現問題 → 【驗】。

模擬 PASS 不等於自然工作 Evidence。

## 13. 第一版完成條件

能維護 Blueprint Map；區分已實作與未實作；未實作節點具有最小功能說明與詳細來源；能讀取 Registry 而不取代 Registry；維持主要位置與關係；發現基本 Drift；UNKNOWN 不被猜成已知；不建立第二套 Registry、Impact 或 TODO System。

## 14. 明確不做

Blueprint Database、Blueprint Graph Database、Full Repository Graph、Automatic Architecture Refactoring、Automatic Skill Creation / Merge / Delete、Automatic Impact Engine、Automatic TODO Engine、Automatic Blueprint Rewrite。

## 15. 最高原則

> Blueprint 是地圖，不是詳細規格。
> Registry 管「它是什麼」；Blueprint 管「它在哪裡」。
> Verification 管「如何驗證」；Evidence 管「驗證產生什麼依據」。
> CURRENT 管「現在正式是什麼」。
> State 管「目前正式狀態」；【代】只管「尚缺實際運行證據」。
> 不確定就 UNKNOWN，不猜。
