# G2-04 CURRENT State Authority Matrix

日期：2026-09-18
狀態：【G2-04 COMPLETE】
用途：確認 Repository 中哪些文件可以作為 CURRENT 入口、哪些只是高階總覽／交接背景／工作池／候選藍圖／歷史證據，避免多份文件競爭目前狀態。

## 一、Authority 判定原則
目前工程狀態只認 `2-方案/完善/目前工程狀態快照-005.md` 為唯一工程游標。
其他文件可以引用、摘要或提供背景，但不得自行覆蓋快照-005。
歷史文件即使內容仍然正確，也不因存在而自動成為 CURRENT。
Version、Git Commit、文件存在、文件內「狀態」欄位都不能單獨決定 CURRENT。

## 二、CURRENT Authority Matrix
| 文件 | Authority Scope | CURRENT？ | 用途 | 判定 |
|---|---|---:|---|---|
| README.md | 入口導航 | 是（導航層） | 告訴 AI 往哪裡讀 | KEEP |
| 2-方案/完善/目前工程狀態快照-005.md | 目前工程游標 | 是 | 現在在哪裡、工程下一步、禁止事項 | PRIMARY CURRENT |
| 目前狀態.md | 專案／架構高階總覽 | 否（不作工程游標） | 穩定高階定位與架構 | CURRENT SUPPORT |
| 規則.md | 操作規則 | 是（規則 Authority） | 怎麼做、衝突如何處理 | CURRENT RULE AUTHORITY |
| 待辦清單.md | 工作池 | 否（不取代工程游標） | 未完成工作、自然觸發項目 | CURRENT WORKPOOL |
| 交接資料-v2.9.md | 交接背景 | 否（不取代快照） | 重大決策、接手邊界、交接背景 | CURRENT HANDOFF SUPPORT |
| 交接資料/AI單人工作室全庫基線重建交接文件-G1完成_G2待續-v1.0.md | 基線重建 Task State | 否（只管理本次 G 任務） | G1/G2 游標與基線工程狀態 | CURRENT TASK AUTHORITY |
| 1-系統/AI上下文與交接系統.md | 交接系統規則／流程 | 否（不取代快照） | Context、交接、恢復流程 | CURRENT SUPPORT |
| 藍圖/AI單人工作室功能導向藍圖交接入口-v1.0.md | 未來藍圖交接視圖 | 否 | 說明未來能力與目前邊界 | BLUEPRINT / DERIVED |
| AI單人工作室整體系統企劃書-無API版本-v0.3.md | 候選整體架構 | 否 | 未來架構研究與候選設計 | CANDIDATE / HISTORY |
| 2-方案/能力蒸餾與系統重構方案-v1.1.md | 方案設計歷史狀態 | 否 | 設計依據與歷史決策 | HISTORICAL |
| 2-方案/工程運作與持續改進方案-v1.7.md | 舊工程運作版本 | 否 | 歷史演化證據；內含快照-004引用 | HISTORICAL / SUPERSEDED |
| 2-方案/工程運作與持續改進方案-v1.6.md | 舊工程運作版本 | 否 | 歷史演化證據；內含更早入口 | HISTORICAL |
| 目前工程狀態快照-001～004 | 舊工程游標 | 否 | 歷史工程狀態與演化證據 | HISTORICAL |
| 交接資料-v2.0～v2.8 | 舊交接游標 | 否 | 歷史交接與問題修正證據 | HISTORICAL |

## 三、最小 CURRENT Recall
一個完全沒有歷史記憶的新 AI，若只是要回答「現在工程在哪裡、下一步做什麼、不能做什麼」，最小必要入口為：

1. README.md
2. 2-方案/完善/目前工程狀態快照-005.md
3. 規則.md
4. 待辦清單.md

需要理解重大決策與交接背景時，再讀 `交接資料-v2.9.md`。
本次基線重建工作則額外讀 `交接資料/AI單人工作室全庫基線重建交接文件-G1完成_G2待續-v1.0.md`。

## 四、目前狀態交叉檢查
目前多個 CURRENT-support 文件在核心工程狀態上互相一致：
- 四方案模擬／回歸完成。
- 正常工程運作。
- FIELD 待自然觸發。
- 不建立第二套工程 CURRENT。
- 不把歷史文件升格為目前狀態。

因此目前沒有發現兩份「工程游標」同時競爭的 CURRENT split-brain。

但發現歷史文件仍可能被搜尋直接讀到，尤其是：
- 工程運作 v1.7 仍引用快照-004。
- 能力蒸餾 v1.1 仍記錄其當時的待驗收狀態。
- 舊快照 001～004 本身仍保存舊游標。

這些不是目前入口衝突；它們是 Retrieval Risk。

## 五、Retrieval Risk 與處理方式
目前不全面修改歷史文件。

原因：
1. 歷史文件具 Evidence Value。
2. 修改歷史文件可能破壞時間線。
3. CURRENT Authority 已由 README、快照-005、規則、待辦、v2.9 建立。
4. 基線重建目前優先是辨識 State，而不是無差別清洗所有舊文件。

因此採用：
`CURRENT Authority 明確化` + `Historical 保留` + `Archive / Migration 後續處理`。

## 六、G2-04 結論
G2-04 完成。

目前 Repository 沒有證據顯示存在兩個同等權威的 CURRENT 工程游標。
真正的問題已從「CURRENT 不存在」轉變為「CURRENT 已存在，但歷史文件仍可能被檢索到並誤讀」。

因此下一階段不能再單純增加入口文件。
應開始檢查：哪些歷史／候選內容會被新 AI 誤認為 CURRENT，以及是否需要透過 Archive、標記、索引或 Recall 驗證降低誤讀率。

## 七、下一步
G2-05：建立 State Evolution Matrix。

目標：把主要文件的「設計 → 執行 → 驗證 → CURRENT → HISTORY」演化鏈串起來，確認目前 CURRENT 的形成依據與歷史退場位置。