# Agent Skill 語意路由系統

版本：v1.0
日期：2026-09-19
狀態：【正式建立；FIELD 驗證待進行】

## 1. 定位

Agent Skill 語意路由系統（Agent Skill Semantic Router）是獨立的輕量分流系統。

它不取代 Agent、Skill 或 AI Control Plane。

核心目的：

「在載入完整 Skill / System / Knowledge 之前，先以最低成本從使用者任務中辨識可用能力，將任務導向適合的 Agent Skill；無法明確匹配時立即回退一般 Agent 路徑。」

核心原則：

先分流，再取 Context。

## 2. 建立前檢查結論

既有 `1-系統/Agent Skill.md` 與 `1-系統/Skill分流運作規格.md` 已負責完整 Skill Routing：Task Understanding → Problem Triage → Required Capability → Candidate Skill → Skill Routing → Mode → Context。

本系統不取代上述流程，而是在其前面增加一個「低成本前置分流」：先判斷是否存在明確 Skill 候選；只有命中、歧義或需要進一步判斷時，才進入既有完整 Skill Routing。

因此兩者不是同一責任：
- Semantic Router：前置粗分流，目標是減少不必要的完整 Routing / Context 成本。
- Skill Routing：正式候選比較與最終路由。

既有 Agent Skill 保持為 Top-Level Orchestration Skill。

## 2. 系統邊界

Semantic Router：
Task → Observation / Task Features → Capability / Skill

Control Plane：
Capability / Skill → 必要 Context Query

Agent：
接受路由結果並負責執行與協調。

Skill：
執行被路由到的能力。

System：
提供 Skill 所需的穩定工作方法。

Knowledge：
提供必要基礎資訊。

因此 Router 不負責完整解題，也不負責決定全部 Context。

## 3. 核心流程

User Task
→ Semantic Router
→ Candidate Skill
→ Route Decision
→ Control Plane Query
→ 最小 Context
→ Agent / Skill Execute
→ Verify

若沒有足夠匹配：

User Task
→ Semantic Router
→ NO MATCH / AMBIGUOUS
→ Agent
→ Control Plane Query
→ 正常處理

## 4. Router 最小輸入

Router 原則上只觀察：

- Task text
- Observation Terms
- Task Type
- Capability hints
- 可用 Skill 的最小 Metadata

Skill Metadata 只需支援分流所需資訊，例如：

- Skill ID
- Capability
- Observation Terms / Trigger
- Input Type
- Output Type
- Required Context Query（僅指針）
- 狀態

不得為了路由而載入完整 Skill 文件。

## 5. Route 結果

Router 最小輸出：

- Route：MATCH / NO_MATCH / AMBIGUOUS
- Skill ID / Capability（若有）
- Confidence / Match basis（僅作路由依據，不是真值）
- Next Query pointer

若結果不明確，不得自行深度推理後硬選 Skill。

應：

AMBIGUOUS
→ 最小必要擴展
→ 仍不明確則交 Agent 處理

## 6. 成本控制

Router 是「薄層」，不是第二個 Agent。

禁止：

- 為路由讀完整 Skill。
- 為路由載入整套 System。
- 為路由預載 Knowledge。
- 每次全庫搜尋所有文件。
- 為了選 Skill 進行完整解題。
- 建立獨立大型推理循環。

目標：

在增加極少量 Router 成本的前提下，減少後續 Context 載入與重複推理。

目前僅建立成本假設，尚未宣稱實測節省比例。

## 7. 分層

L0：Observation
只判斷「這是什麼類型的工作？」

L1：Capability / Skill Routing
判斷「是否存在可直接處理的能力？」

L2：Control Plane Query
判斷「這個能力需要哪些最小 Context？」

L3：Skill Execution
執行工作。

L4：Verification
驗證結果。

一般任務應盡可能停留在最低必要層級。

## 8. Routing 規則

1. 明確匹配唯一 Skill → 直接路由。
2. 多個候選 → 只取得必要 Metadata 進行最小消歧。
3. 無匹配 → 立即回退 Agent。
4. 不確定 → 不把推測當成 Skill 真值。
5. Skill 狀態不可用 → 不路由至該 Skill。
6. Router 不直接修改 Skill / System / Knowledge。
7. Router 只產生路由結果，不取代執行者。

## 9. 與 AI Control Plane 的關係

兩者為相鄰但不同的系統：

Semantic Router：
「誰來做？」

Control Plane：
「做它需要知道什麼？」

因此正式流程為：

Task
→ Semantic Router
→ Capability / Skill
→ Control Plane Query
→ 最小 Context
→ Execute

Control Plane 可提供 Router 所需的最小 Skill Metadata，但不得因此把 Registry 全部載入 Context。

## 10. 失敗與回退

Router Failure 不等於 Task Failure。

可能結果：

- NO_MATCH → Agent fallback
- AMBIGUOUS → minimal disambiguation → Agent fallback
- Skill unavailable → Agent fallback
- Metadata insufficient → Control Plane minimal query
- Router error → Agent normal path

任何回退都應保留最小 Trace，供後續 FIELD 分析。

## 11. FIELD 驗證

目前狀態：【未驗收】

自然工作中觀察：

- Route 正確率
- NO_MATCH fallback
- AMBIGUOUS 比例
- 誤分流
- Context 載入量
- Token 成本
- 執行時間
- Verification 結果
- Human Intervention
- Router 本身額外成本

對照：

A：現有 Agent / Routing
B：Semantic Router → Agent / Skill

禁止人工製造 Failure。

Simulation 可驗證流程，但不能取代 FIELD。

## 12. 不做

- 不建立第二個 Agent。
- 不建立第二個 Control Plane。
- 不把 Router 變成完整語意分析引擎。
- 不全庫預載 Skill。
- 不把 Router 當 Source of Truth。
- 不因 Router 存在而新增大量 State。
- 不預設固定 Token 節省比例。
- 不以 Simulation 結果宣稱實戰成本下降。

## 13. 外部方法比對

外部 Agent / Skill Routing 實作普遍採用「路由層先於完整能力載入」的方向；例如 Tool Router 將能力發現與執行分離，以避免整個能力目錄進入 Agent Context。citeturn0search1 vLLM Semantic Router 也將語意路由定位為 LLM / Agent 前的決策層。citeturn0search7 近期 Skill Routing 研究則顯示，大規模 Skill 庫的選擇本身是獨立問題，但不同研究對「只用 metadata 是否足夠」存在明顯差異；因此本系統不預設 metadata 一定足夠，將透過 FIELD 驗證決定是否需要第二階段資訊。citeturn0academia23turn0academia22

採用結論：保留「先分流、後載入」原則；不提前導入向量資料庫、獨立 Router Server 或大型模型 Router。

## 14. 完成條件

設計完成：

- Router 與 Agent / Skill / Control Plane 邊界明確。
- 先分流、後 Context 的流程成立。
- NO_MATCH / AMBIGUOUS 有回退路徑。
- Router 有成本控制。
- 不需要新增 Server / Graph DB / Vector DB。

實戰完成仍需 Natural FIELD 證據。

---

核心理念：

「讓最上層只看懂『現在可能需要什麼能力』，而不是先讀懂整個系統；先找到 Skill，再讓 Control Plane 找資料。」

