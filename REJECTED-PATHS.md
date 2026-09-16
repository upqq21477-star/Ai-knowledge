# 歷史方案與目前不採用方向

> 這份文件只做歷史參考，**不是操作規則文件**，不應單獨作為目前架構決策依據。
>
> 必須區分：
> - **已否決**：目前已有充分理由認定不值得加入現行系統，除非出現新的具體反證，否則不要重新提出。
> - **暫緩**：目前證據不足，因此不實作、不正式化、不列為待辦；未來若實際痛點出現，可以重新評估。
>
> 目前狀態與 Gate 以 `HANDOFF.md` 為準；實際操作規則以 `RULES.md` 為準。

## 1. Knowledge Metadata / Knowledge ID — 已否決

曾提案為每份 Knowledge 建立正式編號（例如 K-CTX-001），並搭配 Specification Version、相容性欄位。否決：檔名本身已是唯一識別，多一層編號對單人使用沒有額外辨識價值，只增加維護欄位。

## 2. Evidence Source 分級（A/B/C/D）— 已否決

曾提案依來源可信度分級標註每份知識。否決：分級的目的是讓「他人」評估可信度；單人工作室只需要記得「自己驗證過」或「外部資料」，不需要正式量表。

## 3. Version History 表格 / Update Trigger Checklist — 已否決

曾提案每份文件維護版本歷史表格與更新觸發清單。否決：Git commit 歷史已完整涵蓋，另外維護表格是重複記錄，且會因疏於更新而失真。

## 4. Specification 版本化與 Migration 流程 — 已否決

曾提案先制定一份 Specification v0.1（22 個待定項目），並定義 Migration 分類（Compliant/Needs Update/Needs Rewrite/Needs Split）才能開始寫實際知識。否決：這是大型團隊用來約束多人協作的做法；單人不需要規範「別人」，而且這個流程本身會把「開始寫第一份知識」無限期擋在規劃階段之後。

## 5. Capability 概念與需求解析層 — 已否決

曾提案在 System 之上加一層 Capability（例如 Search / Retrieval / Verification），讓 Application 透過「需要什麼能力」尋找 System，而非直接瀏覽 System 清單。否決：System 的一句話用途本身已經是這個功能，另建分類系統是重複勞動，且容易演變成一套龐大的能力分類體系。

## 6. System 五階段狀態機 — 暫緩

曾提案 System 狀態分為 Draft / Prototype / Validated / Production / Deprecated 五階段。**目前不採用，也不建立相關狀態機。**暫緩原因：現階段規模太小，沒有證據顯示多階段狀態能降低實際維護成本；現行 System 仍維持 `草稿／已驗證` 的簡單表示。

這不是永久否決。若未來實際維護問題證明二態不足，才可重新評估更細的狀態模型。

## 7. 正式衝突處理流程 — 已否決

曾提案當兩份 Knowledge 出現矛盾時，走 Conflict → Identify → Check Conditions → Resolve → Record decision 的正式流程。否決：矛盾本質上是「適用條件不同」，這個條件本來就該寫在組合它們的 System 的「不適用情境」欄位裡，不需要獨立流程與紀錄格式。

## 8. Knowledge Graph / 中央 Dependency Database — 已否決

曾提案為所有 Knowledge 與 System 之間建立正式依賴關係圖，並用資料庫維護。否決：System 檔案本身已列出「組成的 Knowledge」，需要反查時直接用檔名做文字搜尋即可，維護一張圖或一個資料庫的成本遠大於它帶來的效益。

## 9. 自動化知識更新系統 / 自動 Cascade Update — 已否決

曾提案當外部資料更新時，自動觸發下游 Knowledge → System → Application 逐層更新或至少自動標記。否決：更新永遠只在「使用時」才檢查，且更新不自動連鎖到上層，每一層各自判斷是否受影響。全自動化在目前規模下沒有必要，且有錯誤傳播風險。

## 10. 4 級相關性分類（Required / Relevant / Potentially Relevant / Irrelevant）— 已否決

曾提案 Knowledge Discovery 時把候選知識分四級篩選。簡化為二選一（相關／不相關）。理由：對單人判斷來說，多一級分類只增加決策成本，沒有增加準確度。

## 11. 多層 Context Loading / 獨立 Index 系統 — 已否決

曾提案建立 Level 0-4 的 Context Loading 機制與獨立 Discovery 系統。否決：一份 INDEX.md（檔名＋一句話用途）搭配「先掃描、再深讀」的簡單原則已經足夠達到同樣的效果。

## 12. 預先建立 `_archive/` 資料夾結構 — 暫緩

曾提案一開始就建立 `_archive/knowledge/`、`_archive/systems/`、`_archive/applications/` 供未來封存舊版本使用。暫緩：`_archive/` 要防止的問題（AI 把舊版本誤認為現行版本）在檔案數量很少的現階段風險趨近於零；決定「淘汰當下才建立」，不預先蓋空資料夾。

## 13. 獨立 Runtime 程式模組 — 暫緩

曾提案將 Discovery / Selection / Loading / Composition / Validation 實作成 `runtime/` 資料夾底下的真正程式碼，作為整套系統的執行引擎。暫緩：目前連第一份 Knowledge 都還沒建立，優先讓 AI 依照 RULES.md 的文字流程手動執行；只有某個 System 被驗證有效、且手動執行成本已經高於寫程式成本時，才把該 System 實作成程式碼，避免「先蓋好引擎再找用途」。

## 14. GitHub 資料夾以功能分類 — 已否決

曾提案第一層資料夾直接用功能／類型分類。否決：第一層應該用架構層級（Knowledge/System/Application）區分「這是什麼角色」，功能分類（AI / 軟體 / 架構 / 資料）應該放在 Knowledge 資料夾內部的子分類，避免把「角色」和「領域」混在同一層，導致 AI 難以判斷抽象層級。

## 15. 其他目前暫緩的架構候選

以下方案目前沒有足夠實際證據，因此不實作、不正式化，也不是待辦事項：

- Atomic Knowledge
- Knowledge Aggregation
- PINNED / ACTIVE / DORMANT / RETIRED 等複雜內容狀態機
- Capability Lifecycle / Capability-Driven Pruning
- 大型自動化 Knowledge Pipeline
- 其他未來只有在實際痛點出現後才值得重新評估的架構

這些項目只有在 `HANDOFF.md` 定義的實際 Gate 被觸發後，才重新評估。
