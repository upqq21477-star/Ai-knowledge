# AI Control Plane 與整體改版藍圖 v1.0

日期：2026-09-19
狀態：【正式規劃基線】
定位：在既有 CURRENT Baseline 之上，先完成 AI Control Plane 的設計收束，再以 Control Plane 作為後台控制層，重整整體 AI 工作室架構。

## 1. 改版目標

本輪不是增加更多獨立系統，而是把現有 Agent、Skill、Routing、Context、Evidence、Problem、Handoff、Monitoring、Evolution 等能力，收束到明確的控制平面之下。

核心分工：

資產層：
Rules → Knowledge / Memory → System → Plan → Software / Tool → Application

AI 執行層：
Agent → Task Understanding → Context → Skill Selection → Execute → Verify → Replan

Control Plane：
Observe → Registry / Query → Route / Context Control → Execute Trace → Verify → Change / Impact → Reconcile

Control Plane 是後台管理與控制層，不是新的資產層，也不取代 CURRENT Authority。

## 2. Control Plane 的核心責任

Control Plane 只管理「需要被知道、被查詢、被比較、被追蹤，但不應全部進入目前 Context」的後台資訊。

核心 Entity：
Entity / State / Dependency / Impact / Change / Evidence / Provenance / Authority / Lifecycle / Capability / Trace / Drift / Recovery。

核心工作：
1. 定位目前工作涉及哪些資產。
2. 只查必要 metadata。
3. 按需展開 Dependency / Impact。
4. 發生異常時提升 Evidence / Source 深度。
5. 為跨文件修改形成 Change Set。
6. 驗證修改後狀態。
7. 保留可恢復的最小證據。
8. 發現 Drift 時提出 Reconciliation Proposal。

## 3. 控制流程

Task
→ Task Understanding
→ Control Plane Query
→ 最小 Context
→ Skill Selection
→ Execute
→ Trace
→ Verify
→ Evidence
→ 若有異常：Problem / Impact
→ 若需修改：Change Set
→ Verification
→ Registry Reconcile
→ CURRENT / Historical 更新
→ Close

一般任務不應經過完整後台流程；只在需要時展開。

## 4. 分層查詢

L0：現有 Context
L1：Entity metadata / State / Authority
L2：直接 Dependency / Impact
L3：Evidence / Provenance / Problem
L4：原始文件
L5：History / 大型重構資料

停止規則：
目前層已足以回答任務 → 停止。
不得為「完整」而繼續載入。

## 5. Observer

Observer 是控制面觀察器，不是常駐全庫掃描器。

Observe
→ Detect
→ Compare
→ Diagnose
→ Propose

Trigger 優先來自：
目前任務、變更事件、Verification Failure、Problem、Drift、自然工作。

一般工作不主動全庫掃描。

## 6. Registry 邊界

Registry 保存 metadata、relationship、evidence pointer，不複製原文。

Source of Truth：
正式文件／實際 Evidence／Problem Registry／Git History 等依既有 Authority 規則判定。

任何 Registry、Index、Cache、Graph 都必須能由 Source 重建。

## 7. Change / Reconciliation

Desired State
→ Observed State
→ Diff
→ Impact
→ Proposal
→ USER CONFIRM（高風險）
→ Change
→ Verification
→ Reconcile

跨文件修改一律以 Change Set 為完成單位。

「單檔修改成功」不等於施工完成。

## 8. 與現有系統的重新定位

Agent：執行入口與協調者。
Skill：可重用能力模組。
System：穩定工作方法。
Plan：大型問題的工作安排。
Control Plane：後台狀態、關係、查詢、影響與變更控制。
Problem Registry：問題生命週期真實入口。
Handoff：跨 AI 的最小恢復資料。
Monitoring：低成本觀察訊號，不是第二套 Control Plane。
CURRENT Baseline：唯一目前工程狀態權威。

## 9. 整體改版後的責任邊界

不再讓 Skill 自行承擔：
- 全庫狀態管理
- 全庫 Dependency 維護
- CURRENT 判定
- 歷史狀態管理
- 跨文件 Change 組織
- 全庫 Context 預載

上述責任移至 Control Plane。

Skill 只回答：
「這個任務需要什麼能力，以及如何執行這項能力。」

## 10. Routing 改版

Routing 不再直接決定「讀多少資料」。

Routing：
Task → Capability / Skill

Control Plane：
Task / Capability → 最小必要 Context

因此：
上層只需要識別觀察詞／任務類型；
Control Plane 再按需分發必要查詢。

目的：
降低 Context 載入與重複推理。

## 11. Context 改版

Context 不再等同「目前對話內容 + 大量知識」。

改為：
Base Context
+ Task Context
+ Query Result
+ Execution Result
+ Verification Result

Query Result 僅保留必要內容與 Source pointer。

## 12. Monitoring 定位

「啟動監控」維持為可取消的輕量 Observer。

五輪冷啟動規則、低風險輕量檢查、SUSPECT / FAIL 才升級深度等既有規則保留。

Monitoring 不得變成常駐全庫分析。

若自然 FIELD 證明成本高於收益：
降低頻率／降低深度／停止。

## 13. Control Plane 完成 Gate

設計完成必須證明：
- Entity / State / Dependency / Impact / Change / Evidence / Authority / Trace 均有明確責任。
- Query 有明確深度與停止規則。
- Registry 不取代 Source。
- Derived data 可重建。
- Change Set 有完整完成條件。
- 高風險修改有確認邊界。
- 無記憶 AI 能理解控制面與 CURRENT 的差異。
- 不需要新增 Server / Graph DB / Vector DB 才能成立。

實際能力仍需 FIELD 驗證，不得把「規格完成」寫成「實戰完成」。

## 14. 整體改版施工順序

Phase A：Control Plane 規劃收束
→ Phase B：現有系統責任重新 Mapping
→ Phase C：Agent / Routing / Context 接口重整
→ Phase D：Problem / Evidence / Handoff / Monitoring 接口重整
→ Phase E：最小 FIELD 驗證
→ Phase F：依 Evidence 修正
→ Phase G：整體 Baseline 更新
→ Phase H：Large Mode 決策

禁止直接刪除舊系統。
先 Mapping → 驗證 → 再 Merge / Compress / Archive。

## 15. 本輪明確不做

- 不建立第五治理方案。
- 不建立第二 CURRENT。
- 不建立第二 Workpool。
- 不提前建立 Graph DB。
- 不建立常駐 Server。
- 不把所有 Registry 預載。
- 不把所有歷史放入 Context。
- 不因 Control Plane 存在就新增大量 State。
- 不人工製造 FIELD Failure。
- 不以 Simulation 代替 FIELD。

最高原則：

「Control Plane 管理資訊如何被找到與控制；資產層管理資訊本身；Agent 管理 AI 如何執行。」

