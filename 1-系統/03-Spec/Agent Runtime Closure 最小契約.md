# Agent Runtime Closure 最小契約 v1.0

版本：v1.0
日期：2026-09-19
狀態：【正式規格；Simulation 可驗；Natural FIELD 待證】

## 1. 定位

本文件把既有 Agent、Semantic Router、Control Plane、Skill Definition、Context、Execution、Verification 與 Problem / Evidence 串成最小 Runtime Contract。

它不是新的 Agent、Router、Registry、Skill 或大型 Runtime 系統。

目的：
> 補上「知道要選哪個 Skill」與「實際如何啟動、執行、驗證、失敗後如何恢復」之間的最小契約。

## 2. 完整最小鏈

Task
→ Task Understanding
→ Trigger
→ Capability
→ Candidate
→ Route
→ Invocation Contract
→ Context
→ Execute
→ Verify
→ Final / Stop

失敗時：

Failure
→ Classify
→ Diagnosis
→ Retry / Re-route / Fallback / Stop
→ Verify
→ Final / Stop

## 3. Trigger Contract

Trigger 不直接等於 Skill。

Trigger 必須至少回答：

- Trigger Source：Task / Failure / Change / Natural Work / User
- Trigger Condition：為何現在需要某能力
- Required Capability：需要完成什麼責任
- Candidate Scope：可考慮哪些既有 Skill
- Exclusion：哪些 Skill 不應被選
- Confidence / Ambiguity：是否足以直接路由

若 Trigger 不足以區分 Candidate：
→ 回 Task Understanding / Context
→ 不得猜測 Skill。

## 4. Routing Contract

Routing 輸出：

- Candidate Skills
- Selected Skill
- Route Reason
- Required Context
- Verification Target
- Mode
- Fallback Class

Routing 結果：
- UNIQUE：可進 Invocation
- MULTIPLE / AMBIGUOUS：補 Context 或重新分流
- NONE：回 Capability / Research / User Required
- INVALID：停止並記錄原因

Router 只負責選擇，不執行 Skill。

## 5. Invocation Contract

每次正式啟動 Skill 前，必須形成最小 Invocation：

- Invocation ID
- Task
- Trigger
- Selected Skill
- Mode
- Required Context
- Input
- Constraints
- Expected Output
- Verification Target
- Stop / Failure Boundary

Invocation 必須通過：
1. Skill 存在且可用。
2. Input Preconditions 滿足。
3. Required Context 可取得。
4. Skill Dependency 可取得或有明確 fallback。
5. Verification Target 可定義。

任一必要條件不滿足：
→ 不進 Execute。
→ 進 Failure Classification / Context / Fallback / Stop。

## 6. Execution Contract

Execute 只能處理 Invocation 已授權的 Responsibility。

不得在 Execution 中自行：
- 改變 Skill Responsibility。
- 建立新 Skill。
- 修改 Source of Truth。
- 把 Failure 當成成功。
- 跳過 Verification。

需要改變結構：
→ 回 Evolution / Change 流程。

## 7. Verification Contract

Verification 必須回答：

- Expected：原本要完成什麼？
- Actual：實際完成什麼？
- Evidence：證據在哪？
- Result：PASS / FAIL / INSUFFICIENT
- Scope：哪些部分已驗證？
- Next Action：失敗後往哪裡走？

PASS：
→ Final。

FAIL：
→ Failure Diagnosis。

INSUFFICIENT：
→ Context / Research / User Required，不得假裝 PASS。

## 8. Failure / Recovery Contract

Failure 類型最小集合：

- MISSING_INPUT
- INVALID_INPUT
- CONTEXT_INSUFFICIENT
- DEPENDENCY_FAILURE
- PROVIDER_TOOL_FAILURE
- ROUTING_FAILURE
- NO_CANDIDATE
- AMBIGUOUS_CANDIDATE
- EXECUTION_FAILURE
- VERIFICATION_FAILURE
- LIMIT_REACHED
- USER_REQUIRED

Recovery 順序不是固定重試，而是依 Failure Type 判定：

Transient：
→ bounded Retry

Context / Routing：
→ Context 補充或 Re-route

Provider / Tool：
→ Fallback Provider / Tool 或 degraded mode

Skill Insufficient：
→ Diagnosis → Classification；不得直接 NEW

Verification Failure：
→ Diagnosis → Fix / Re-route → Re-execute → Verify

Limit Reached：
→ Stop / Degraded Result

User Required：
→ Stop 並等待使用者

Recovery 失敗後：
→ Final FAILED / INSUFFICIENT + Evidence / Trace。

## 9. Fallback Contract

Critical path 的 fallback 最小層級：

Primary
→ Alternative
→ Degraded Mode
→ Stop / User Required

Fallback 必須標示：
- Why primary failed
- Which fallback activated
- Capability impact
- Whether output quality is degraded
- Verification requirement

不得靜默降級。

## 10. Runtime Receipt

每次 Agent / Skill 執行至少產生可追溯的最小 Receipt：

- Invocation ID
- Task
- Trigger
- Route
- Selected Skill
- Mode
- Context Source
- Input Validation
- Execution Result
- Verification Result
- Failure / Re-route
- Final Result
- Stop Reason

Receipt 的目的不是建立大型 Log 系統，而是讓後續可以回答：

「為什麼啟動這個 Skill？」
「用了什麼 Context？」
「做了什麼？」
「怎麼知道完成？」
「如果失敗，怎麼恢復？」
「為什麼最後停止？」

目前若自然運行無法取得完整 Receipt：
狀態 = FIELD PENDING。
不得用 Simulation 宣稱 Natural FIELD PASS。

## 11. Agent-Level Boundary

每次任務必須有最小邊界：

- Retry Budget
- Re-route Budget
- Maximum Skill Chain Depth
- Context Expansion Budget
- Research Depth / Iteration Limit
- Cost / Token Observation
- Stop Reason

這些不是固定永久數字。

Small Mode 先採「有界但可調」原則；實際數值由自然工作 Evidence 再校準。

任何一項達到上限：
→ Stop / Degraded / User Required。

不得無限：
Retry → Re-route → Research → Context Expansion。

## 12. Multi-Skill Composition

多 Skill 只有在第一個 Skill 的 Output 是下一個 Skill 的必要 Input 時才形成 Composition。

最小鏈：

Skill A
→ Validated Output
→ Skill B Input
→ Execute
→ Verify

每個 Skill 必須保留自己的：
- Responsibility
- Input / Output
- Verification
- Failure Boundary

Agent 負責組合，不把 Composition 本身自動升格為 Skill。

若中間結果未驗證：
→ 不直接傳給下一 Skill 作為已確認事實。

## 13. Stop Contract

Final Stop 必須屬於：

- PASS
- INSUFFICIENT
- FAILED
- USER_REQUIRED
- LIMIT

Stop 必須有 Stop Reason。

PASS 不等於「模型覺得差不多」。
必須有 Verification Evidence。

INSUFFICIENT 不得轉寫成 PASS。

FAILED 不得產生假成功結果。

USER_REQUIRED 不得由 Agent 自行替使用者做決策。

## 14. Natural FIELD 邊界

目前本契約可做：
- Static Check
- Simulation Acceptance

但以下仍必須靠自然工作驗證：
- 真實 Trigger → Route Accuracy
- 真實 Invocation
- 真實 Failure Classification
- 真實 Fallback / Re-route
- 真實 Receipt 完整度
- 真實 Retry / Chain / Cost 邊界
- 真實 Multi-Skill Composition
- Agent E2E 自然成功率

因此本文件狀態保持：
【正式規格；Simulation 可驗；Natural FIELD 待證】

## 15. 最小 Acceptance

Simulation 必須至少覆蓋：

S01 正常 UNIQUE → Invocation → Execute → Verify → PASS
S02 AMBIGUOUS → Context → Re-route
S03 NO_CANDIDATE → Capability / Research / Stop
S04 Missing Input → Stop / Context
S05 Provider Failure → Fallback
S06 Execution Failure → Diagnosis → Re-route / Retry
S07 Verification Failure → Diagnosis → Re-execute → Verify
S08 Retry Budget → LIMIT
S09 Chain Depth → LIMIT
S10 User Required → Stop
S11 Multi-Skill → A Output → Verify → B Input
S12 Receipt → 可回答 Trigger / Route / Skill / Context / Execution / Verification / Final / Stop

Simulation PASS 不代表 Natural FIELD PASS。

## 16. Governance Boundary

Agent：
任務決策、編排、重新分流、停止。

Semantic Router：
Candidate / Route。

Control Plane Query：
提供 Derived Metadata / Relationship / State。

Skill Definition：
Skill Responsibility 與正式契約。

Context：
提供本次執行必要資料。

Execution：
執行已確認 Responsibility。

Verification：
判定結果。

Problem / Evidence：
保存失敗與證據。

Workpool：
保存後續工作。

不得讓其中任一層吞掉其他層的責任。

## 17. 研究後的設計判斷

目前不新增：
- 大型 Runtime Engine
- 大型 Observability System
- Capability Registry
- Capability Graph
- 新 Orchestrator
- 新 Recovery Skill

先以本最小契約把既有元件接閉。

只有自然 FIELD 證明契約仍不足，才增加下一層能力。

