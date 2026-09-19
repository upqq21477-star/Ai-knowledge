# Project A 遊戲開發藍圖

狀態：【正式規劃入口；遊戲內容依實際專案建立】

## 1. 文件責任
本文件只負責 Project A 的「遊戲本體開發路線」。
中央負責 AI Studio 整體工程藍圖、Agent / Control Plane / Runtime / Governance、唯一 CURRENT、唯一 Workpool，以及中央遊戲開發共用框架封存。
Project A 負責本遊戲的 Game Concept、Core Loop、Game Model、Game Systems、Rules、State / Data / Flow、Simulation / Verification，以及實際遊戲設計與實作。

## 2. 遊戲開發主線
Game Concept → Core Loop → Game Model → Game Systems → Relationships → Rules → State → Data → Flow → Simulation → Verification → Physicalization → Runtime Evidence → Playtest → 修正／再驗證

## 3. Game Model 最小契約
每個可執行的核心遊戲模型，至少說明 Input → State → Rules → Transition → Output，並定義 Invariant、Termination；需要時再加入 Entity / Data / Action / Event / Dependency。

## 4. 驗證分層
L1：邏輯／規則正確性。
L2：遊戲設計／Core Loop／系統交互合理性。
L3：實際引擎／平台／Runtime 實作正確性。
L1 PASS 不代表 L2 PASS；L2 PASS 不代表 L3 PASS。

## 5. 系統整合
除單一系統驗證外，對實際存在且重要的交互執行 System Integration Validation，例如 Combat × Progression、Economy × Progression、Level × AI、Resource × Core Loop。不預先建立完整矩陣。

## 6. 設計與實作追蹤
共通框架採用：Game Rule → Game Model → Skill → Transformation → Code → Test / Verification → Runtime Evidence。
反向除錯：Runtime → Evidence → Code → Transformation → Skill → Rule / Game Model → Diagnosis → Fix → Re-test。
詳細追蹤規格位於：專案A/2-方案/Skill-Transformation-Code追蹤與反向除錯規劃-v1.0.md

## 7. 專案專屬內容
以下屬 Project A 本體，不預設進中央共用框架：實際戰鬥設計、敵人與 AI、武器／技能、數值與平衡、地圖與關卡、經濟、劇情、美術／音效規格、實際 Game Data、專案專屬測試與 Playtest。

## 8. 共用框架
Project A 在實際開發中若驗證出具有跨遊戲價值的能力，依 Evidence → Verification → 蒸餾共通部分 → 中央遊戲開發共用框架封存。
中央封存：封存/遊戲開發共用框架/
狀態：【ARCHIVE-REUSABLE；不啟用】。
Project B 等新遊戲可直接套用已驗證的共通框架，不重新建立相同能力。

## 9. 開發完成後
使用紀錄 → Dependency Audit → 影響分析 → Evidence 整理 → KEEP / MERGE / COMPRESS / ARCHIVE / DELETE → 共通能力抽取 → 更新中央遊戲開發共用框架 → Project A 最終精簡。

## 10. 原則
「如何開發遊戲」與「這個遊戲是什麼」分離。
共通框架集中管理；遊戲專屬設計留在 Project A。
開發期不為了最終結構過早拆分；先實際工作、取得證據，再決定哪些能力跨遊戲重用。

## 11. 共用框架分類

Project A 的遊戲開發資產採三種語義：
- **Common**：跨遊戲可重用的開發方法與最小契約。
- **Variant**：只在部分遊戲類型／條件下適用的可重用能力。
- **Project-specific**：本遊戲的規則、數值、內容與資料。

這是分類語義，不建立三套大型 Registry。

## 12. Core Loop 一級驗證

Core Loop 不只是藍圖章節，而是遊戲設計的核心驗證對象：

Core Loop → System → Mechanic → State → Player Decision → Feedback → Next Loop

L2 驗證時確認核心循環是否成立，以及重要系統交互是否破壞核心循環。L1 仍負責規則／邏輯；L3 仍負責引擎／平台／Runtime。

## 13. 共用框架升格 Gate

Project A 中任何候選共用能力：

使用 → Evidence → Verification → Generalization → Cross-project applicability → 蒸餾 → Central Archive

「在 Project A 能工作」只能證明 Project A 可用，不足以直接證明跨遊戲可重用。

升格前至少確認：有實際使用證據、有 Verification、不依賴 A 的專屬規則、有清楚 Input / Output / Preconditions、已知 Applicability / Non-applicability、蒸餾後不夾帶 A 專屬設計。不足時留在 Project A。

## 14. 框架履歷與版本綁定

進入中央封存的共用能力，保留最小履歷：Asset / Capability ID、Common / Variant、Source Project、Source Evidence / Verification、Purpose、Applicability、Non-applicability、Version、Dependency、Last Validated、Promotion Reason。

Project A 使用中央框架時記錄：Common Framework Version + Project-specific additions + Project-specific overrides（若有）。目前框架尚未建立正式版本號，因此不假設一個不存在的版本。

新專案使用最新正式版本；既有專案不自動覆蓋，升級需經 Compatibility / Impact Analysis → Upgrade / Stay / Migrate → Verification。

## 15. 遊戲開發框架的邊界

目前不建立 Game Framework Registry、Feature Registry、Variant Registry、Game Project Factory、大型 Game Knowledge Graph、全自動 Framework Sync、全自動 Migration、全自動 Code Generator。

這些只有在多專案實際使用後，維護成本或檢索成本成為瓶頸，才重新評估。

## 16. Project A 的驗證角色

Project A 是第一個真實驗證專案：Project A proves → Central distills → Project B validates reuse → 再決定是否擴大中央共用框架。

因此目前優先工作不是繼續增加框架，而是讓 Project A 真正使用、留下 Evidence，並觀察 Common / Variant / Project-specific 的邊界是否穩定。
