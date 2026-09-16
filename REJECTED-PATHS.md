# 歷史方案與目前不採用方向

> 這份文件只做歷史參考，**不是操作規則文件**，不應單獨作為目前架構決策依據。
>
> 目前狀態與重新評估條件以 `HANDOFF.md` 為準；實際操作規則以 `RULES.md` 為準。

本次重新整理後，尤其要注意：部分舊方案之所以被提出，是因為當時把「某些 AI 無法直接瀏覽 GitHub 資料夾」當成設計限制。現在這個假設已不再成立，因此相關 Discovery workaround 不應繼續保留為現行架構。

## 1. Knowledge Metadata / Knowledge ID — 已否決

曾提案為每份 Knowledge 建立正式編號，例如 K-CTX-001，並搭配 Specification Version、相容性欄位。否決：檔名已足以識別文件，額外編號只增加維護成本。

## 2. Evidence Source 分級（A/B/C/D）— 已否決

曾提案建立正式來源可信度分級。否決：目前是單人工作室，不需要用治理量表取代實際驗證與來源記錄。

## 3. Version History 表格 / Update Trigger Checklist — 已否決

曾提案在每份文件內維護版本歷史與更新清單。否決：Git 已經保存版本歷史，額外表格容易失真。

## 4. Specification 版本化與 Migration 流程 — 已否決

曾提案先完成大型 Specification，再逐份把舊內容 Migration 到規格。否決：會把真正建立 Knowledge 的工作延後，且不符合單人工作室的低維護原則。

## 5. Capability 概念與需求解析層 — 已否決

曾提案在 System 之上增加 Capability 層，讓 Application 透過能力分類尋找 System。否決：目前 System 的用途描述已足夠，不需要另一套分類治理。

## 6. System 五階段狀態機 — 暫緩

曾提案 Draft / Prototype / Validated / Production / Deprecated 五階段。暫緩：目前沒有證據顯示多階段狀態能降低維護成本。現階段維持簡單狀態即可。

## 7. 正式衝突處理流程 — 已否決

曾提案 Conflict → Identify → Check Conditions → Resolve → Record 的獨立流程。否決：多數衝突其實是適用條件不同，應直接在相關 Knowledge／System 中寫清楚，而不是再建立治理流程。

## 8. Knowledge Graph / 中央 Dependency Database — 已否決

曾提案用圖譜或資料庫保存 Knowledge 與 System 關係。否決：目前規模不需要。文件中的直接引用與 GitHub 搜尋已足夠；若未來真的不足，再由實際痛點觸發。

## 9. 自動化知識更新 / 自動 Cascade Update — 已否決

曾提案外部資料更新後自動觸發 Knowledge → System → Application。否決：不同層級是否受影響應由實際使用判斷，自動傳播會增加錯誤擴散風險。

## 10. 4 級相關性分類 — 已否決

曾提案 Required / Relevant / Potentially Relevant / Irrelevant 四級 Discovery。否決：目前只需要判斷相關或不相關即可。

## 11. 多層 Context Loading / 獨立 Index 系統 — **舊方案失效，不再採用**

曾提案建立 Level 0–4 Context Loading 與 INDEX Discovery，主要目的是補償當時認為 AI 無法直接進入 GitHub 子資料夾的限制。

現在已確認本系統使用的 GitHub 讀取能力可以直接取得目錄與子目錄文件，因此：

- INDEX 不再是 AI Discovery 的必要層。
- 不再要求 AI 只能透過 INDEX 尋找文件。
- 不再因為資料夾可讀性建立額外導航機制。
- 現有空 INDEX 可以刪除。

這不是「INDEX 永遠沒有用」，而是：**它不能再被當成架構必要條件。**未來若內容規模真的讓檔案定位變慢，再重新評估最小的 Retrieval 解法。

## 12. 預先建立 `_archive/` 資料夾結構 — 暫緩

只有真的需要保存淘汰內容時才建立 `_archive/`。不預先建立空結構。

## 13. 獨立 Runtime 程式模組 — 暫緩

曾提案建立 Discovery / Selection / Loading / Composition / Validation 的 runtime。暫緩：目前沒有足夠實際使用證據證明程式化值得其維護成本。先手動使用，等手動成本真的超過實作成本再考慮。

## 14. GitHub 第一層資料夾以功能分類 — 已否決

第一層仍以 Knowledge / System / Application 的抽象角色分類，不把 AI、軟體、架構、資料等領域直接混在第一層。

## 15. Atomic Knowledge — 暫緩

目前沒有證據證明需要把 Knowledge 再拆成原子單位。只有實際重疊與維護成本出現時才重新評估。

## 16. Knowledge Aggregation — 暫緩

目前沒有證據證明需要建立額外的聚合層。不要為了預測未來規模而先建立。

## 17. 複雜內容狀態機 — 暫緩

PINNED / ACTIVE / DORMANT / RETIRED 等狀態目前不需要。若未來內容生命週期真的造成維護問題，再重新評估。

## 18. Capability Lifecycle / Capability-Driven Pruning — 暫緩

目前只在需要時簡單標註模型能力補償，不建立 Registry、Audit 或自動淘汰機制。

## 19. 大型自動化 Knowledge Pipeline — 暫緩

沒有實際規模與重複工作量以前，不建立大型自動化流水線。

## 20. 判斷歷史方案的共同原則

任何舊方案未來若被重新提出，都必須先回答：

1. 現在真的發生了當初要解決的問題嗎？
2. 這個問題已經造成可觀的工作成本嗎？
3. 有沒有更簡單的解法？
4. 最小解法是否已經實際驗證不足？

如果沒有，維持不採用。

> **歷史方案不是待辦事項；只有實際痛點才會把它重新變成候選方案。**
