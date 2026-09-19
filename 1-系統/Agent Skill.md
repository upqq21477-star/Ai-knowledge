# Agent Skill v1.4

版本：v1.4
日期：2026-09-19
狀態：【Control Plane 接入；正式運作基線】
定位：最上層 Orchestration Skill（Agent as Top-Level Skill）

## 1. Definition
Agent 負責任務級決策與編排，不直接承擔各專業 Skill 的工作責任。

核心鏈：
Task → Understand → Triage → Capability → Candidate → Route → Mode → Context → Execute → Verify

## 2. Responsibility Boundary
Agent：決策、編排、失敗後重新分流。
Skill：可重複、可獨立路由的工作責任。
Provider / Tool：能力來源／外部操作。
Knowledge：可引用資料。
Application：實際工作場景。

Agent 不把 Provider、Tool、Mode、單次 Workflow 或失敗事件升格為 Skill。

## 3. Trigger
- 新任務。
- 現有任務邊界改變。
- Skill 執行失敗，需要重新分流。
- Context 重置後需要恢復。
- 使用者要求停止／改變工作目標。

## 4. Input / Output
Input：User Task、CURRENT、必要 Context、可用 Skill metadata。
Output：Task Definition、Selected Route、Execution Result、Verification Result 或明確 Stop Status。

## 5. Routing
Small Mode 先依：
Responsibility → Trigger → Input / Output → Context → Verification

候選衝突時再比較：
Failure Pattern → Dependency → Cost → Actual Usage

Skill Routing 與 Skill Classification 分離：
- Routing：選哪個既有 Skill。
- Classification：Skill 結構是否需要改變。

## 6. Failure
Failure → Classification → Diagnosis → Fix / Re-route → Execute → Verify。
不得因 Routing Failure 直接建立新 Skill。

## 7. Control Plane
正式鏈：
Task → Agent → Semantic Router → Control Plane Query → Candidate → Skill Definition → Runtime → Verification → Evidence / Trace

Control Plane 提供 metadata / relationship / state，不取代 Skill Definition 或其他 Source of Truth。

## 8. 停止
PASS / INSUFFICIENT / FAILED / USER_REQUIRED / LIMIT。
完成後停止本次任務，不因 Agent 保持可用而持續執行。

## 9. Governance
涉及 Skill 結構變更：
Research / Classification → Evolution → Execution → Verification。
Agent 不可無證據永久新增、刪除或取代 Skill。

## 10. Context
不預載整個 Repository；只取得本次任務所需 metadata 與 Source。
