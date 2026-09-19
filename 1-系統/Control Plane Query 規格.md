# Control Plane Query 規格

版本：v1.0
日期：2026-09-19

## 目的
以最低 Context 成本取得完成任務所需的最小後台資訊。

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
一般工作：L0-L1。
關係問題：L2。
異常／驗證：L3-L4。
歷史研究／大型重構：L5。

## 禁止
- 不全庫預載。
- 不把完整 Graph 放入 Context。
- 不把所有 History 放入 Context。
- 不因查詢便利而複製全文。
