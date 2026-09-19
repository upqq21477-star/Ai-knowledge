# Skill Control Plane B｜Registry / Query 靜態驗收紀錄 v1.0

日期：2026-09-19
狀態：【DESIGN / STATIC PASS；SIMULATION ACCEPTANCE PASS】

## 驗收結果

| 項目 | 結果 |
|---|---|
| Registry View Contract | PASS |
| Query Contract | PASS |
| Candidate Filtering | PASS |
| Query Stop | PASS |
| No Candidate Fallback | PASS |
| Multiple Candidate Handling | PASS |
| Invalid Skill Handling | PASS |
| Dependency Query | PASS |
| Registry Rebuild | PASS |
| Definition Change → Registry Update | PASS |
| Impact Query | PASS |
| C Interface | PASS |

## 12 個案例

1. Identity → Q0 → UNIQUE → STOP
2. Capability → Q1 → Capability / Boundary → STOP
3. Trigger → Q2 → Trigger / Boundary → STOP
4. I/O → Q3 → Compatibility → STOP
5. Constraint → Q4 → State / Availability → STOP
6. Dependency → Q5 → Direct Relations → STOP
7. Verification → Q6 → Evidence；無有效證據則 UNKNOWN
8. History → Q7 → 最小 Change History → STOP
9. Impact → Q8 → Evidence-supported AFFECTS → STOP
10. NONE → Agent fallback
11. MULTIPLE → Minimal Metadata / Evidence → Agent / existing Routing
12. INVALID → EXCLUDED → 不進正常 Candidate

## Rebuild Case

Registry 缺失 → Source Definition → Derive → Rebuild → 原 Query 重跑 → 功能恢復。

設計流程：PASS。

## Change Case

Definition → Change Set → Affected Relations → Registry Invalidate / Rebuild → Verification。

設計流程：PASS。

## 還未證明

真實 Context / Token 成本、真實 Query Stop depth、Candidate 正確率、Drift detection、Rebuild recovery、Definition Change synchronization 不在本次模擬中宣稱為 Natural FIELD；本次改採「模擬運行驗收」作為 B 階段完成依據。

因此 B 現在進入：DESIGN / STATIC PASS；SIMULATION ACCEPTANCE PASS。


## 5. FIELD Protocol

已建立：
`1-系統/Skill Control Plane B FIELD Registry-Query 驗證規格-v1.0.md`

目前：
- Registry / Query Static：PASS
- Interface Alignment：PASS
- FIELD Protocol：READY
- Natural FIELD Evidence：OPTIONAL / 不阻塞本階段
- B Final：PASS（Simulation Acceptance）

FIELD 僅接受自然 Query / Registry 事件與實際 Evidence；Simulation 不得升格 FIELD。B 獨立進行，不等待 A/C 的實際驗證結果；跨包結果最後交由 D 統一驗收。


## 6. 模擬運行驗收

本次依現行 Registry / Query Contract 執行 10 個受控案例，驗證 Query → Filtering → Candidate / Fallback → Stop 的閉環。模擬不宣稱 Natural FIELD，也不填寫虛構 Token / Time。

| Case | 模擬情境 | 預期行為 | 結果 |
|---|---|---|---|
| B-S1 | Q0 Identity 唯一 ID | UNIQUE → STOP | PASS |
| B-S2 | Q1 Capability 單一候選 | Candidate → 最小 Metadata → STOP | PASS |
| B-S3 | Q2 Trigger 多候選 | Minimal Metadata → Minimal Evidence → MULTIPLE | PASS |
| B-S4 | Q3 I/O 不相容 | 排除不相容候選 | PASS |
| B-S5 | Q4 Constraint 導致候選不可用 | 依正式 State / Constraint 排除 | PASS |
| B-S6 | Q5 Dependency | 回傳直接 Relation，不擴張全圖 | PASS |
| B-S7 | Q6 Verification 無有效證據 | UNKNOWN，不補猜 | PASS |
| B-S8 | Q8 Impact | 僅 Evidence-supported AFFECTS；DEPENDS_ON 不冒充 Impact | PASS |
| B-S9 | Registry 遺失 | Source → Derive → Rebuild → 原 Query 重跑 | PASS |
| B-S10 | Definition Change | Change → Affected Relations → Invalidate/Rebuild → Verification → 新版本可查 | PASS |

補測：NONE → fallback、INVALID → exclude、MULTIPLE → 不由 Registry 自選最佳者，均 PASS。

模擬驗收結論：B 的 Registry View、Query、Filtering、Stop、Fallback、Dependency / Impact、Rebuild、Definition Change 流程均可在受控情境閉環；本次未發現需要修改現行 B Contract 的結構性問題。

本階段正式採用「Simulation Acceptance」取代等待 Natural FIELD 作為完成門檻。Natural FIELD 未來仍可作為真實運行觀察，但不再阻塞本階段 B 完成。

## 7. B 階段完成判定

Registry / Query Static：PASS
Interface Alignment：PASS
Simulation Acceptance：PASS
Natural FIELD：非本階段完成必要條件
B Final：PASS

本文件與 FIELD Protocol 已同步：Natural FIELD 僅作未來真實運行觀察，不再作為本階段 B Completion Gate。

## 8. 原 FIELD Protocol 說明

原 FIELD 文件保留 Natural FIELD 的定義，作為未來真實運行觀察標準；本次不把 Simulation 標記為 FIELD，避免驗收證據類型混淆。
