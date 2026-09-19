# AI Control Plane 與整體改版施工清單 v1.0

日期：2026-09-19
狀態：【規劃完成；施工待開始】

## P0 Control Plane 設計 Gate
- [x] 核心責任
- [x] Registry 邊界
- [x] Query / Retrieval 深度
- [x] Observer / Trigger
- [x] Change / Reconciliation
- [x] Context 最小化
- [x] 與 CURRENT / Problem / Handoff / Monitoring 邊界
- [x] 完成 Gate
- [ ] 自然 FIELD 驗證

## P1 整體責任 Mapping
- [ ] Agent
- [ ] Skill
- [ ] Routing
- [ ] Context
- [ ] Problem
- [ ] Evidence
- [ ] Handoff
- [Monitoring]
- [ ] Evolution
- [ ] CURRENT / Workpool

輸出：
Control Plane ↔ 現有能力責任矩陣。

## P2 執行層重整
- [ ] Routing 只負責 Capability / Skill 選擇
- [ ] Control Plane 負責最小 Context 查詢
- [ ] Execute 產生最小 Trace
- [ ] Verify 產生 Evidence
- [ ] Change Set 統一跨文件修改

## P3 後台資料重整
- [ ] Entity
- [ ] State
- [ ] Dependency
- [ ] Impact
- [ ] Evidence
- [ ] Authority
- [ ] Provenance
- [ ] Lifecycle
- [ ] Capability
- [Trace]
- [ ] Drift / Reconciliation

## P4 FIELD 驗證
自然任務中觀察：
- Context 是否下降
- Routing 是否更穩定
- 是否減少跨文件同步遺漏
- Query 是否能在足夠深度停止
- Registry 是否可由 Source 重建
- Monitoring 額外成本是否可接受

## P5 改版 Gate
只有 FIELD 有證據後才：
KEEP / MERGE / COMPRESS / ARCHIVE / DEFER。

## P6 整體 Baseline
- [ ] 更新 CURRENT
- [ ] 更新 Handoff
- [ ] 更新 README
- [ ] 更新規則
- [ ] 更新 Workpool
- [ ] 更新 Index
- [ ] Memoryless Takeover Test

## 禁止
不因改版而重做四方案總驗收。
不因 Control Plane 而建立第五方案。
不以文件完成宣告能力完成。
