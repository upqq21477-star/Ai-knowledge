# Blueprint 功能地圖 v1.2

版本：v1.2
日期：2026-09-19
狀態：【Blueprint Map；最小可導航地圖】

## 1. 核心定位

Blueprint 是大型規劃與正式系統的地圖層。

它只讓 AI 先知道：
- 有哪些主要功能。
- 位於哪裡。
- 做什麼。
- 主要關係。
- 現在的最小 State / Acceptance。
- 詳細內容去哪裡找。

Blueprint 不取代 Registry、CURRENT、Verification、Evidence 或詳細規劃。

## 2. 核心流程

Skill Registry
    ↓
Blueprint
    ↓
Verification
    ↓
Evidence

這表示主要資訊／責任關係，不宣告四者都是同層級獨立 System。

## 3. 主要節點

| 節點 | State / Acceptance | 最小作用 | 詳細入口 |
|---|---|---|---|
| Skill Registry | ACTIVE | 提供 Skill 可查詢資訊 | 2-方案/完善/Skill Registry規劃基線-v1.0.md；1-系統/Control Plane Registry 規格.md |
| Blueprint Governance | ACTIVE / 【代】 | 維護 Blueprint 地圖與一致性 | 1-系統/Blueprint Governance Skill（代）.md |
| 會議紀錄管理 | ACTIVE / 【代】 | 管理會議紀錄保存與轉換 | 1-系統/會議紀錄管理 Skill（代）.md |
| Blueprint | 本地圖 | 顯示整體功能位置與關係 | 本文件 |
| Verification | 已有正式能力 | 驗證系統／Skill 是否符合條件 | 1-系統/證據驗證診斷 Skill.md |
| Evidence | 已有正式能力；非獨立 Evidence System | 保存／引用驗證依據 | 1-系統/AI Control Plane.md；1-系統/Control Plane Registry 規格.md |

## 4. 未實作功能

真正尚未實作的主要功能必須明確標記：

功能名稱【未實作】
- 功能：一句話最小說明
- 詳細規劃：XXX規劃.md

有規劃文件不等於已實作；已有相關能力也不等於已形成獨立 System。

## 5. State / Acceptance 最小語義

共同規則：
《1-系統/工程狀態與驗收最小規則.md》

State：
表示目前正式工作／可用狀態。

Acceptance：
- 【未】尚未開始建立。
- 【驗】建立／整合／修正中。
- 【代】功能完成、模擬 PASS、可運行，但尚缺自然工作 Evidence。
- 有足夠實際 Evidence → 移除【代】。
- 實際運行發現需要修正的問題 → 【驗】。

禁止把 State 與 Acceptance 合併成複合狀態字串。

Blueprint 只顯示，不建立第二套狀態規則。

## 6. 詳細內容導航

Blueprint
→ Planning / Meeting Record
→ 詳細設計
→ Implementation
→ Verification
→ Evidence
→ 更新正式狀態

Blueprint 不複製大型規劃。

## 7. 更新條件

只有以下情況更新 Blueprint：
- 新增／刪除主要功能。
- 主要功能 State / Acceptance 改變。
- 主要功能位置改變。
- 主要關係改變。
- 詳細規劃／紀錄入口改變。
- 發現地圖與正式現況不一致。

一般文字、格式、單次問題、普通文件新增不直接更新 Blueprint。

## 8. 關係

Blueprint 只記錄有來源支持且對理解全局有價值的主要關係：

part-of、depends-on、uses、produces、verifies、triggers、replaces、supersedes、related-to

depends-on ≠ affects。

Impact 仍由既有 Change / Impact / Evidence 能力判定。

## 9. 一致性

比較 Blueprint、CURRENT、Registry、正式 Definition / Source。

結果：
ALIGNED / DRIFT / CONFLICT / UNKNOWN

UNKNOWN 不等於 DRIFT。

## 10. 邊界

Blueprint 不保存：
- Skill 詳細 Definition
- Registry 詳細資料
- Verification 詳細規則
- Evidence 詳細格式
- Impact 計算
- Runtime Trace
- 完整 Repository Inventory
- 完整 TODO
- 自動架構修改

## 11. 模擬驗收【代】

A. 未建立功能 → 【未】。
B. 規劃／建立中 → 【驗】。
C. 全功能完成 → 模擬 PASS → 【代】。
D. Registry 新增 Skill → 只同步位置／主要關係。
E. 普通內部文字修改 → 不更新 Blueprint。
F. 主要位置改變 → 更新 Position / Relation。
G. Blueprint 與 CURRENT 不一致 → DRIFT / CONFLICT / UNKNOWN。
H. 【代】實際運行發現問題 → 【驗】。

模擬 PASS 不等於實際 Evidence。

## 12. 核心原則

> Blueprint 是地圖，不是詳細規格。
> Registry 管「它是什麼」；Blueprint 管「它在哪裡」。
> Verification 管「如何驗證」；Evidence 管「驗證依據」。
> CURRENT 管「現在正式是什麼」。
> State 管「目前正式狀態」；【代】只管「尚缺實際運行證據」。
> 不確定就 UNKNOWN，不猜。
