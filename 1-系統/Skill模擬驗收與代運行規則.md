# Skill 模擬驗收與代運行規則 v1.1

## 目的

將「建立完成後必須等待實際驗收才能運行」改為「模擬驗收通過即可准入運行」，同時保留實際運行驗證的獨立證據價值。

核心原則：**模擬驗收決定能否上線運行；實際運行決定是否解除「【代】」標記。**

## 1. 責任分工

| 責任 | 主責 | 工作 |
|---|---|---|
| 任務理解／意圖 | Task Understanding | 確認驗收目標與範圍 |
| 模擬驗收 | 證據／驗證／診斷 Skill | 執行模擬情境、判定 PASS / FAIL / INSUFFICIENT |
| Skill 是否應建立 | Skill 分類判斷 Skill | NEW / KEEP / MERGE / UPDATE / REPLACE / DEFER 等 |
| 結構如何改 | 演化管理 Skill | Change Scope / Impact / Migration |
| 實際建立／修改 | 執行 Skill | 寫入正式 Skill Definition 與相關文件 |
| 正式路由／編排 | Agent / Semantic Router / Control Plane | 將 PASS 的 Skill 納入可運行路徑 |
| 實際運行觀察 | Skill運作回饋紀錄／自然工作 Observation | 記錄真實使用結果與異常 |
| 問題修正 | 證據／驗證／診斷 + 分類 + 演化 + 執行 | FAIL 時形成問題、修正並重新驗證 |

任何單一 Skill 不得自行宣告自己已通過驗收、自己修改正式架構或自行解除「【代】」。

## 2. 正式規則

1. Skill 完成 Definition、Trigger、Boundary、I/O、Delegation 與驗收條件後，進行模擬驗收。
2. 模擬驗收 PASS，即取得「正式運行准入」，建立／標記為正式 Skill。
3. 尚未有實際運行驗證時，加註「（代）」。
4. 「（代）」不是未完成、DEFER 或候選；它代表「可正式運行，但實際運行證據尚未成立」。
5. 實際運行不得被人工製造來只為解除「（代）」；應由正常工作自然產生，或只有在確有正當測試需求時依一般測試流程產生。
6. 實際運行取得足夠、可追溯且代表性的正常結果後，才可取消「（代）」。
7. 實際運行出現異常時，保留「（代）」或重新加回，並進入問題／診斷／演化流程。
8. 單次異常不自動撤銷 Skill；依 Failure Pattern 與 Verification 結果判斷。



## 2A. 與工程資產狀態控制的關係

本文件只負責「模擬驗收 → 准入運行 → 自然運行 Evidence → 解除【代】」這一段。

工程資產的完整狀態模型由：
`1-系統/工程資產狀態與驗收控制規格.md`
統一管理。

因此：

- Acceptance Stage：【未】→【驗】→【代】→【已建立】
- State：ACTIVE / INACTIVE / PENDING / ... 
- Lifecycle：Created → Verified → FIELD → Active → ...

三者分開。

本文件中的「（代）」歷史語義統一改稱「【代】」，並作為 Acceptance Stage 使用；不得把它與 ACTIVE 組合成單一狀態字串，例如 `ACTIVE（代）`。

會議紀錄 Skill 的 OPEN → READY → CONVERTED → CLOSED 屬於「會議紀錄內容生命週期」，不屬於本文件的工程資產 State / Lifecycle。

## 3. 狀態流程

企劃候選 → 模擬驗收 → PASS → 正式 Skill（代）→ 自然／實際運行 Observation →

- NORMAL：累積足夠證據 → 取消「（代）」
- ABNORMAL：問題流程 → 修正 → 再模擬驗收 → 繼續（代）運行
- INCONCLUSIVE：保留（代）

模擬驗收 FAIL：不得進入正式運行。

## 4. 「（代）」語義

「（代）」是運行成熟度／實際證據標記，不是 Skill 類型，也不是第二套生命週期。

它只回答：**是否已取得足夠實際運行證據？**

- 否 → 保留「（代）」
- 是 → 取消「（代）」
- 實際異常 → 保留或重新標記，並追蹤修正

## 5. 驗收最低條件

至少模擬確認：

1. Trigger 正常。
2. Responsibility Boundary 正常。
3. Input / Output 正常。
4. Delegation / 協作正常。
5. 無 Routing Loop 或責任衝突。
6. 正常案例與主要失敗案例可處理。
7. Stop / Unknown / Insufficient 條件正常。

這些條件 PASS 後即可准入正式運行，但不得把 Simulation PASS 寫成 FIELD PASS。

## 6. 實際運行解除條件

「（代）」解除不採單一固定次數，而採證據充分性：

- 涵蓋主要 Trigger / 使用情境；
- 有可追溯的實際 Operation / Observation；
- 無尚未處理的關鍵異常；
- 結果足以支持「目前運作正常」的判定；
- Verification / Feedback 已回寫。

若證據不足，維持「（代）」。

## 7. 與 Control Plane 的關係

- Skill Definition 仍是 Source of Truth。
- Registry 仍是 Derived View。
- Simulation PASS 是 Runtime Admission Gate，不是 Natural Evidence。
- Natural / Actual Operation 是成熟度驗證來源。
- 不建立第二 Registry。
- 不讓 Registry 取代 Definition。

## 8. 適用範圍

本規則適用於新 Skill、既有 Skill 更新後的驗收，以及需要先取得可運行資格的系統／方案施工階段。

對方案整體而言，模擬驗收 PASS 可以進入正常工程運行，但**不得宣稱方案整體已完成實戰驗證**。

## 9. 本次決策

2026-09-19 起，所有尚未完成的「前置實際驗收／等待實際案例才能准入」改為先做模擬驗收。模擬 PASS 即准入運行並標註「（代）」；後續實際運行只負責驗證成熟度並解除標記。

歷史文件中的舊 FIELD-PENDING、實際驗收待觸發等狀態不追溯改寫，避免破壞歷史證據；新規則自本版本起適用。
