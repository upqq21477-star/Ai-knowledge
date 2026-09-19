# Blueprint Governance Skill

版本：v1.1
日期：2026-09-19
State：ACTIVE
Acceptance：【代】
Lifecycle：依既有 Lifecycle 規格
定位：Blueprint 地圖維護與一致性判斷 Skill。

## 1. 核心責任

維護 Blueprint 最小可導航地圖：
- 主要功能。
- 功能位置。
- 主要關係。
- 最小狀態／驗收標記。
- 詳細規劃／會議紀錄入口。
- 地圖層級一致性。

不取代 Skill Registry、Planning、Verification、Evidence、CURRENT、Impact 或 TODO。

## 2. 觸發

- 新增主要功能。
- 主要功能狀態改變。
- 主要功能位置或主要關係改變。
- 詳細規劃／紀錄入口改變。
- 發現 Blueprint 與正式現況不一致。
- 重大架構變更需要同步地圖。

通常不因拼字、格式、普通文件新增、單次問題或單次 Routing Failure 觸發。

## 3. 核心流程

Candidate
→ 判斷是否為主要功能
→ 查既有節點
→ Position
→ Relationship
→ State / Acceptance
→ Source Pointer
→ Consistency Check
→ 必要時更新 Blueprint

資料不足時 UNKNOWN，不猜測。

## 4. Blueprint Node 最小資料

- Name
- Function Summary
- Position / Layer
- Relationship
- Source / Detail Pointer
- State（需要時）
- Acceptance（需要時）

Blueprint 不重建 Registry 的詳細資料。

## 5. Acceptance

本 Skill 遵守共同最小規則：

- 【未】：尚未正式開始建立。
- 【驗】：建立／整合／修正中。
- 【代】：功能已完成、模擬驗收 PASS、可運行，但尚缺自然工作 Evidence。
- 有足夠實際 Evidence：移除【代】。
- 實際運行發現需要修正的問題：回【驗】。

共同語義來源：
《1-系統/工程狀態與驗收最小規則.md》

## 6. State

本 Skill 目前：

State = ACTIVE
Acceptance = 【代】

State 與 Acceptance 必須分欄，不使用複合狀態字串。

## 7. 關係

可記錄：
part-of、depends-on、uses、produces、verifies、triggers、replaces、supersedes、related-to。

depends-on 不等於 affects。

Impact 仍由既有 Change / Impact / Evidence 能力判定。

## 8. 一致性

比較：
- Blueprint
- CURRENT
- Registry
- 正式 Definition / Source

結果：
ALIGNED / DRIFT / CONFLICT / UNKNOWN

UNKNOWN 不等於 DRIFT。

## 9. 邊界

不建立：
- Blueprint Database
- Graph Database
- Full Repository Graph
- Automatic Architecture Refactoring
- Automatic Skill Creation / Merge / Delete
- Automatic Impact Engine
- Automatic TODO Engine
- Automatic Blueprint Rewrite

## 10. 模擬驗收【代】

A. 新增未建立功能 → 能標記【未】並保留最小來源。
B. 已規劃但未完成 → 能標記【驗】。
C. 全功能完成 → 模擬 PASS 後標記【代】。
D. Registry 新增 Skill → Blueprint 只同步位置／主要關係。
E. 普通內部文字修改 → 不更新 Blueprint。
F. 主要位置改變 → 更新 Position / Relation。
G. Blueprint 與 CURRENT 不一致 → DRIFT / CONFLICT / UNKNOWN，不猜。
H. 【代】實際運行發現問題 → 回【驗】。

模擬 PASS 不等於實際 Evidence。

## 11. 正式來源

詳細規劃：
藍圖/規劃/Blueprint Governance Skill-規劃-v1.0.md

功能地圖：
藍圖/Blueprint功能地圖-v1.0.md
