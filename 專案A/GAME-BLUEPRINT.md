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