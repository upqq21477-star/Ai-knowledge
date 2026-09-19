# Control Plane Query 規格

版本：v1.1
日期：2026-09-19

## 目的
以最低 Context 成本取得完成任務所需的最小後台資訊。

## Semantic Router 前置查詢

Semantic Router 不直接讀完整 Skill。

需要時只查：

GET CAPABILITY METADATA
GET SKILL METADATA
GET SKILL STATE
GET ROUTING TERMS
GET REQUIRED CONTEXT POINTER

目的：
確認「是否存在可用能力」，而非取得執行所需完整資料。

標準順序：

Task
→ Semantic Router
→ Capability / Skill
→ Control Plane Query
→ 最小 Context
→ Execute

## Router 查詢停止規則

1. 找到唯一且可用的 Skill → 停止路由查詢。
2. 多候選 → 只增加必要 Metadata。
3. 無候選 → STOP，回退 Agent。
4. 仍不明確 → STOP，回退 Agent 或要求最小必要澄清。
5. 不得為了提高「完整性」而讀取完整 Skill / System / Knowledge。

## 基本查詢
GET ENTITY
GET STATE
GET DEPENDENCIES
GET IMPACT
GET EVIDENCE
GET PROVENANCE
GET CHANGE
GET TRACE
GET AUTHORITY
GET LIFECYCLE
GET CAPABILITY
GET CAPABILITY METADATA
GET SKILL METADATA
GET ROUTING TERMS
GET REQUIRED CONTEXT POINTER

## 任務查詢
修改 X：
X → State → Authority → Dependency → Impact → Evidence → Open Problems → Related Change → Affected Set

交接：
CURRENT → Authority → State → Relevant Entity → Evidence → Recovery Data

問題：
Problem → Root Cause → Dependency → State → Impact → Evidence → Change

## Retrieval 深度
L0：現有 Context
L1：Entity metadata
L2：直接 Dependency / Impact
L3：Evidence / Provenance
L4：Source
L5：History

足夠即停止。

## Traversal
預設只查直接關係。
只有直接結果不足時才增加深度。
限制：
- depth
- breadth
- entity count
- evidence count
- history depth

## Context 最小化
不得因存在 Registry 就自動載入 Registry。
Query 結果只返回：
必要 Entity
必要關係
必要證據
必要 Source 指針

Router 階段尤其禁止返回完整 Skill / System / Knowledge。

## Cache
Search / Graph / Query Result 可快取。
Cache 非 Source of Truth。
Cache 可刪除、重建。

## Drift Query
優先檢查：
目前任務涉及的 Entity
最近修改的文件
已知 Problem
最近 Verification
而非每次全庫掃描。

## Rebuild Query
Registry 不完整：
→ 找 Source
→ 找 Git History
→ 重建 metadata
→ 驗證
→ 更新 Registry

## 成本原則
Router：
最低成本 Metadata 查詢。

一般工作：
L0-L1。

關係問題：
L2。

異常／驗證：
L3-L4。

歷史研究／大型重構：
L5。

## 禁止
- 不全庫預載。
- 不把完整 Graph 放入 Context。
- 不把所有 History 放入 Context。
- 不因查詢便利而複製全文。
- 不為 Semantic Router 載入完整 Skill / System / Knowledge。
