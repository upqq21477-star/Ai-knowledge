# 會議紀錄管理 Skill（代）

## Status

- 狀態：ACTIVE（代）
- 模擬驗收：PASS
- 實際運行驗證：未完成
- 來源企劃：藍圖/規劃/企劃/會議紀錄管理 Skill企劃-v1.0.md

## Responsibility

管理討論成果是否需要保存，以及應以哪一種過渡形式進入下一工程階段。

## Trigger

- 明確指令：會議紀錄
- 使用者要求保存目前討論中的決策、設計、未決事項，並準備切換工作
- 使用者需要把討論成果整理成下一階段可接續的工程記錄
- 短語「記一下／先記錄／簡短記錄」語意明確時觸發；歧義時先確認

## Non-trigger

一般摘要、單純問答、單一失敗診斷、無決策／設計／下一步的長內容，不自動建立會議紀錄。

## Input

目前討論上下文、使用者保存意圖、已確認決策、未確認事項、排除事項、下一步。

## Output

- NO_RECORD
- MEETING_RECORD
- PLANNING
- HANDOFF（委派交接 Skill）
- EXISTING_UPDATE（委派演化／執行）

## Delegation

- 內容壓縮：蒸餾 Skill
- 新 Skill 是否成立：Skill分類判斷 Skill
- 結構變更：演化管理 Skill
- 檔案建立／修改／刪除：執行 Skill
- 結果確認：證據驗證診斷 Skill
- AI 交接：交接 Skill
- Context 載入與邊界：Context管理 Skill

本 Skill 不取代上述 Skill，也不自行建立第二套 Registry、Runtime 或 Source of Truth。

## Record minimum

日期、主題、目的／問題、已確認、未確認、依據、排除／暫緩、下一步、相關產物、狀態、清理條件。

## Lifecycle

OPEN → READY → CONVERTED → CLOSED

DEFER、BLOCKED、SUPERSEDED 為輔助狀態語義，不代表自動刪除。

## Cleanup

只有在內容已完整轉移、無未解決資訊且不再具有獨立長期價值時，才可交由執行流程清理。不得自動刪除唯一來源。

## Verification

模擬驗收最低條件：觸發正常、責任邊界正常、I/O 正常、委派正常、無路由循環／責任衝突、主要正常與失敗案例可處理。

本 Skill 已通過三輪模擬驗收，因此依《Skill 模擬驗收與代運行規則》進入正式運行，暫標「（代）」。
