# Skill Control Plane｜交接 D：三工作包完成後最終驗收

狀態：【TEMP HANDOFF｜最終驗收完成後刪除】
日期：2026-09-19
工作包：D — Final Acceptance / Integration Audit
前置：A / B / C 三工作包均已完成施工並宣告各自 PASS
性質：驗收與進度一致性檢查，不負責重新施工 A / B / C

## 1. 工作目的

D 不是第四個施工工作包，而是 A / B / C 完成後的獨立驗收層。
核心問題：「三個工作包說自己完成，是否真的完成了原本規劃的系統？」

驗收必須重新以無記憶接手者視角進行，不得只接受 A/B/C 自己的完成宣告。

## 2. 啟動流程

1. 讀取 README.md。
2. 讀取 CURRENT Baseline。
3. 讀取目前施工交接包。
4. 讀取 A / B / C 的正式成果與驗收結果。
5. 讀取原始 Skill Control Plane 規劃與本階段完成條件。
6. 建立「原規劃 → 實際成果」逐項對照。
7. 盤點完成、未完成、變更、衝突、UNKNOWN。
8. 檢查正式文件與 Repository 實際狀態。

若資料不足，不得猜測；標記 UNKNOWN。

## 3. 第一層：進度一致性

逐項檢查至少：
- Skill Definition Contract
- Skill Boundary
- Skill Family / Mode
- Skill / Agent Boundary
- Skill / Workflow Boundary
- Version / Lifecycle
- Dependency
- Verification / Evidence
- Evolution
- Registry View
- Query Contract
- Candidate Filtering
- Query Stop
- Fallback
- Rebuild
- Change / Impact
- Semantic Router
- Runtime
- Verification
- Evidence / Trace
- Failure / Re-route

每項必須標記 PASS / FAIL / UNKNOWN，並提供實際文件路徑或測試證據。不得只寫「已完成」。

## 4. 第二層：功能驗收

F01 Skill 定義：給定新能力，能否固定判斷 Skill / Agent / Workflow / Mode / Family、拆分、合併、取代及 Definition。

F02 Registry：能否由 Source 產生 Registry View；Registry 是否只是 View / Query，而不是第二 Source of Truth。

F03 Query：給定 Capability、Trigger、I/O、Constraint、Dependency、Verification，能否取得合理 Candidate。

F04 Query Stop：Metadata → Candidate → 必要時 Definition，是否在足夠時停止，避免掃描完整 Skill 庫。

F05 Candidate Filtering：Disabled、Retired、Invalid Definition、Invalid Dependency、Verification-invalid 是否正確排除。

F06 No Candidate：沒有符合條件時，是否明確回報 No Candidate，而不是猜測。

F07 Multiple Candidate：多候選時，是否保留候選與必要 metadata，而非 Registry 偽造唯一答案。

F08 Runtime：Load Definition → Input Validation → Dependency Check → Execute → Stop → Output 是否完整。

F09 Verification：Output → Verification Rule → Result → Evidence → Trace 是否能區分。

F10 Failure / Re-route：Missing Input、Invalid Input、Dependency Failure、Execution Failure、Verification Failure、No Candidate、Ambiguous Candidate 是否正確 Stop / Re-route；不得產生錯誤成功，也不得任意創造新 Skill。

## 5. 第三層：E2E 驗收

E01 正常流程：Task → Agent → Semantic Router → Control Plane Query → Registry → Candidate → Definition → Runtime → Verification → Evidence / Trace。
E02 Skill Update：Definition 更新 → Registry 更新 → Router / Query 取得正確版本 → Runtime 使用正確 Definition。
E03 Skill Disable：Disable → 正常 Query → 不再成為正常 Candidate。
E04 Registry Rebuild：Registry 消失／失效 → Source → Rebuild → Query 恢復。
E05 Dependency Failure：依賴失敗 → 正確停止或依規則處理 → 不產生假成功。
E06 Verification Failure：Verification Fail → 正確記錄 Evidence / Trace → Stop 或 Re-route → 不宣告成功。

## 6. 第四層：權責邊界

確認：
- Agent ≠ Router
- Router ≠ Registry
- Registry ≠ Skill Definition
- Control Plane ≠ Source of Truth
- Skill ≠ Workflow
- Verification ≠ Evidence
- Evidence ≠ Trace
- Version ≠ Lifecycle ≠ State

若出現混合，記為 Boundary Failure。

## 7. 第五層：規劃漂移

必須回答：
1. 有沒有漏做原本規劃？
2. 有沒有多做原本禁止的功能？特別檢查大型 Ranking、Embedding、Graph DB、Autonomous Skill Evolution、第二套 Registry / Source of Truth、大型 Capability Registry。
3. 有沒有修改原規劃？若有，記錄原規劃、實際變更、原因、證據與影響。

變更不能只因「新設計比較好」就視為合理；必須有證據。

## 8. 第六層：最小 Context 與可重建性

檢查：
1. Router 是否先取得 Registry Metadata。
2. 是否只有必要時才載入 Definition。
3. 是否避免每次掃描完整 Skill 庫。
4. Query 是否有 Stop Condition。
5. Registry 是否為 Derived View。
6. Definition → Registry View 是否可重建。
7. Registry 損壞後能否由 Source Rebuild 並恢復 Query。

沒有實際證據，不得宣稱節省 Token，只能標記 UNKNOWN。

## 9. 第七層：Change / Version

至少測試：
Skill Definition Change → Version Change → Registry 更新 → Query / Router 行為更新 → Verification。

確認 Version、State、Lifecycle 不混淆；Deprecated / Retired 行為明確；Change 可追蹤；Impact 可查。

## 10. 問題分類

- Critical：阻止 Phase 1 DONE。
- Major：功能或接口缺失，必須修正。
- Minor：不阻塞核心功能，可進 Future Work。
- Drift：偏離原規劃，需要正式判定。
- UNKNOWN：證據不足，不得猜測。

D 發現問題時不得重新設計整個架構；應指向 A / B / C 負責工作包，建立 Change / Fix，修正後重新驗收受影響部分。

## 11. 最終驗收條件

只有全部成立才能宣布：
SKILL CONTROL PLANE PHASE 1 = ACCEPTED

1. A PASS。
2. B PASS。
3. C PASS。
4. 原規劃逐項對照完成。
5. F01～F10 核心功能 PASS。
6. E01～E06 E2E PASS。
7. Change PASS。
8. Disable PASS。
9. Rebuild PASS。
10. 權責邊界 PASS。
11. 沒有 Critical / Major 未解問題。
12. 剩餘 UNKNOWN 已列出且不阻塞 Phase 1。
13. 正式成果已寫入正式文件。
14. Repository 狀態與 CURRENT 一致。

## 12. 驗收輸出

必須輸出：
- 總結果：PASS / CONDITIONAL PASS / FAIL
- 規劃一致性：完全符合／合理變更／遺漏／額外增加／UNKNOWN，逐項列證據。
- F01～F10：PASS / FAIL / UNKNOWN
- E01～E06：PASS / FAIL / UNKNOWN
- 邊界驗收：逐項 PASS / FAIL
- 問題：Critical / Major / Minor / Drift / UNKNOWN
- Phase 1：ACCEPTED / NOT ACCEPTED
- 後續：阻塞問題修正；非阻塞問題進 Future Work；完成即停止擴張。

## 13. 最終清理

只有 A PASS + B PASS + C PASS + D ACCEPTED 才能清理暫存交接文件。

清理順序：
1. 確認正式成果已保存。
2. 確認 A/B/C 成果已被正式文件吸收。
3. 刪除 A、B、C、D 四個 TEMP HANDOFF。
4. 從檔案索引移除四個 TEMP 項目。
5. 重新讀取 Repository。
6. 搜尋四個檔名。
7. 確認不存在。
8. 確認正式成果仍完整存在。
9. 才宣布清理完成。

## 14. D 的明確終點

D 的終點不是提出更多改進。

D 的終點是：證明 A/B/C 已完成；證明實際系統與原規劃一致，或留下有證據的合理變更；證明核心功能與 E2E 可運作；確認沒有阻塞性問題；完成暫存交接文件清理。

達成後：SKILL CONTROL PLANE PHASE 1 = ACCEPTED。
停止本階段擴張。後續新增需求必須建立新的工作包或 Change。