# 會議紀錄管理 Skill

## Status

- State：ACTIVE
- Acceptance：【代】
- Lifecycle：依既有 Lifecycle 規格
- 模擬驗收：PASS
- 實際運行驗證：未完成
- 狀態／驗收共同規則：1-系統/工程狀態與驗收最小規則.md
- 來源企劃：藍圖/規劃/企劃/會議紀錄管理 Skill企劃-v1.0.md

## Responsibility

管理討論成果是否需要保存，以及應以哪一種過渡形式進入下一工程階段。

## Trigger

- 明確指令：會議紀錄
- 使用者要求保存目前討論中的決策、設計、未決事項並準備切換工作
- 需要把討論成果整理成下一階段可接續的工程記錄
- 「記一下／先記錄／簡短記錄」語意明確時觸發；歧義時先確認

## Non-trigger

一般摘要、單純問答、單一失敗診斷、無決策／設計／下一步的長內容，不自動建立會議紀錄。

## Input

目前討論上下文、保存意圖、已確認決策、未確認事項、排除事項、下一步。

## Output

- NO_RECORD
- MEETING_RECORD
- PLANNING
- HANDOFF
- EXISTING_UPDATE

## Delegation

- 內容壓縮：蒸餾 Skill
- 新 Skill 是否成立：Skill 分類判斷 Skill
- 結構變更：演化管理 Skill
- 檔案建立／修改／刪除：執行 Skill
- 結果確認：證據驗證診斷 Skill
- AI 交接：交接 Skill
- Context 載入與邊界：Context 管理 Skill

本 Skill 不建立第二套 Registry、Runtime 或 Source of Truth。

## Record minimum

日期、主題、目的／問題、已確認、未確認、依據、排除／暫緩、下一步、相關產物、狀態、清理條件。

## Record lifecycle

OPEN → READY → CONVERTED → CLOSED

DEFER、BLOCKED、SUPERSEDED 是輔助語義，不代表自動刪除。

## Cleanup

內容完整轉移、無未解決資訊且不再具有獨立長期價值後，才可交由執行流程清理。不得自動刪除唯一來源。

## Verification

模擬驗收最低條件：
- Trigger 正常。
- 責任邊界正常。
- I/O 正常。
- 委派正常。
- 無路由循環／責任衝突。
- 主要正常與失敗案例可處理。

本 Skill 目前 State=ACTIVE、Acceptance=【代】。自然工作 Evidence 足夠後才解除【代】。

## 邊界

本 Skill 的 OPEN → READY → CONVERTED → CLOSED 只描述「單筆會議紀錄內容」的處理生命週期。

它不是：
- Skill State
- Skill Acceptance
- 工程資產 Lifecycle
