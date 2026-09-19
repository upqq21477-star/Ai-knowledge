# Control Plane Registry 規格

版本：v1.0
日期：2026-09-19

## 1 Entity
欄位：
ID / Type / Name / Path / State / Authority / Version / Source / Updated / Confidence

Type：
Rule / Knowledge / Memory / System / Skill / Plan / Application / Problem / Evidence / FIELD / Change / Handoff / CURRENT / Document / Tool / Model / Provider / Runtime / Capability

## 2 State
第一版採既有需求可證明的狀態：
CURRENT / HISTORICAL / PENDING / DEFERRED / CLOSED / UNKNOWN / ACTIVE / INACTIVE

不得因 Registry 建立而自動新增 PINNED / DORMANT / RETIRED 等複雜狀態。

## 3 Relation
第一版：
DEPENDS_ON / USES / REFERENCES / DERIVED_FROM / VERIFIED_BY / SUMMARIZES / SUPERSEDES / AFFECTS / PART_OF / PRODUCES / CONSUMES

欄位：
Source / Relation / Target / Evidence / Confidence / Updated

## 4 Impact
欄位：
Change / Source Entity / Affected Entity / Reason / Evidence / Confidence / Verification

Impact 與 Dependency 分開。

## 5 Change
欄位：
Change ID / Reason / Source Problem / Affected Set / Before / After / Verification / Status / Date

跨文件修改必須以 Change Set 為單位。

## 6 Evidence
欄位：
Evidence ID / Type / Source / Target / Result / Date / Confidence / Related Problem / Related Change

Evidence Type：
FIELD / SIMULATION / REAL_WORK / VERIFICATION / RESEARCH / EXTERNAL_SOURCE / HUMAN_DECISION

Simulation 不等於 FIELD。

## 7 Provenance
描述資料形成來源：
Source → Event → Analysis → Decision → Change → Verification

## 8 Authority
Authority：
CURRENT / PRIMARY / DERIVED / SUMMARY / REFERENCE / HISTORICAL

權威高於摘要；摘要不得覆寫 Authority。

## 9 Lifecycle
Created → Tested → FIELD → Active → Updated → Superseded → Historical

Lifecycle 描述演變，不取代 State。

## 10 Capability
描述 Model / Provider / Tool / Skill 能力。
Provider、Tool、Model 不自動等於 Skill。

## 11 Trace
Trace ID / Task / Routing / Context / Skill / Tool / Result / Verification / Date

只保存具有長期診斷價值的最小摘要。

## 12 Registry 原則
Registry 是 metadata / relationship layer，不複製原始文件全文。
所有 Registry 項目應能回指 Source。
衍生 Index / Graph / Cache 必須可重建。
