# Agent Skill 語意路由系統

版本：v1.3
日期：2026-09-19
狀態：【正式規格；Control Plane 接入；自然運作 Evidence 持續累積】

## 1. 定位

Agent Skill 語意路由系統（Agent Skill Semantic Router）是獨立的輕量分流系統。

它不取代 Agent、Skill 或 AI Control Plane。

核心目的：

「在載入完整 Skill / System / Knowledge 之前，先以最低成本從使用者任務中辨識可用能力，將任務導向適合的 Agent Skill；無法明確匹配時立即回退一般 Agent 路徑。」

核心原則：

「只有當前置分流的預期成本低於它能避免的後續成本時才啟動 Router；先分流，再取 Context。」

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

## 4. 啟動條件

Router 不是每次任務都強制執行。

外部研究僅作設計依據，不把第三方數字直接變成本庫硬門檻。

因此本系統採條件式啟動：

- 候選 Skill 很少、邊界清楚、直接 Routing 成本低 → 可跳過 Semantic Router。
- 候選 Skill 增加、Context 成本升高、重複路由成本開始明顯 → 啟用 Semantic Router。
- Router 自身成本可能高於節省量 → 立即回退既有 Small Mode。

目前 repository 的 Skill 數量與實際 Context 成本尚未完成 FIELD，因此不設定固定數量門檻。

## 5. Router 最小輸入

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

## 6. 路由證據與漸進揭露

外部研究顯示，Skill metadata 不一定包含全部路由訊號；因此本系統採漸進揭露，而非假設 metadata 永遠足夠。

因此本系統不把「Metadata 足夠」當成真理，也不直接把完整 Skill 全部載入。採漸進揭露：

L0：Task / Observation
→ L1：Skill Metadata
→ L2：候選 Skill 的最小責任／Trigger 證據片段
→ L3：必要時進既有完整 Skill Routing

只有 L1 足以唯一命中時停止；L1 不足時，不得硬選，增加最小候選證據；仍不明確則交既有 Skill Routing / Agent。

## 7. Route 結果

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

## 8. 成本控制

Router 是「薄層」，不是第二個 Agent。

成本判斷必須比較：
Router Cost + 後續成本
vs.
既有 Routing Cost。

沒有 FIELD 證據前，不宣稱 Router 必然省 Token 或時間。

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

## 9. 分層

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

## 10. Routing 規則

1. 明確匹配唯一 Skill → 直接路由。
2. 多個候選 → 只取得必要 Metadata 進行最小消歧。
3. 無匹配 → 立即回退 Agent。
4. 不確定 → 不把推測當成 Skill 真值。
5. Skill 狀態不可用 → 不路由至該 Skill。
6. Router 不直接修改 Skill / System / Knowledge。
7. Router 只產生路由結果，不取代執行者。

## 11. 與 AI Control Plane 的關係

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

## 12. 失敗與回退

Router Failure 不等於 Task Failure。

可能結果：

- NO_MATCH → Agent fallback
- AMBIGUOUS → minimal disambiguation → Agent fallback
- Skill unavailable → Agent fallback
- Metadata insufficient → Control Plane minimal query
- Router error → Agent normal path

任何回退都應保留最小 Trace，供後續 FIELD 分析。

## 13. FIELD 運作紀錄

目前狀態：【待持續累積；不作為本輪架構阻塞條件】

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

只記錄自然運作中出現的 Routing / Context / Verification 結果；不為了驗證而人工製造 Failure。

Simulation 僅作設計檢查，不標記為 FIELD。

## 14. 不做

- 不建立第二個 Agent。
- 不建立第二個 Control Plane。
- 不把 Router 變成完整語意分析引擎。
- 不全庫預載 Skill。
- 不把 Router 當 Source of Truth。
- 不因 Router 存在而新增大量 State。
- 不預設固定 Token 節省比例。
- 不以 Simulation 結果宣稱實戰成本下降。

## 15. 外部方法比對

外部比對形成四項採用結論：

1. 保留「先分流、後載入」：外部 Tool / Semantic Routing 實作支持將能力發現與後續執行 Context 分離。
2. Router 必須條件式啟動：外部實作也存在小型能力集合可跳過額外 Router 的情境；但本庫不直接採用固定數量門檻。
3. 不假設 Metadata 永遠足夠：外部 Skill Routing 研究顯示完整 Skill 內容可能包含額外路由訊號，因此保留第二階段最小證據揭露。
4. 不把 Router 擴張成 Agent：外部 Semantic / Agent Routing 架構同樣將 routing、context 與 execution 分離。

採用結論：保留獨立 Semantic Router，但將其定位從「固定前置層」修正為「條件式成本閘門」；不提前導入 Vector DB、獨立 Router Server 或大型 Router LLM。

## 16. 完成條件

設計完成：

- Router 與 Agent / Skill / Control Plane 邊界明確。
- 先分流、後 Context 的流程成立。
- NO_MATCH / AMBIGUOUS 有回退路徑。
- Router 有成本控制。
- 不需要新增 Server / Graph DB / Vector DB。

實際效果由後續自然運作 Evidence 決定，不阻塞目前 Control Plane 接入。

---

核心理念：

「讓最上層只看懂『現在可能需要什麼能力』，而不是先讀懂整個系統；先找到 Skill，再讓 Control Plane 找資料。」



## 17. 建立後交接驗證

以「完全沒有本輪對話記憶，只取得 README + 本系統 + Agent Skill + Skill Routing + Query 規格」為條件進行推演。

驗證案例：

A. 明確單一責任
Task：要求執行已確認文件修改。
預期：可判斷 Execution 能力；若 Router 啟用，唯一命中後停止，不讀完整 Skill。

B. 多候選
Task：要求分析某問題並驗證結論。
預期：不得因「分析」單一詞直接選 Skill；至少進入 Capability / Candidate 比較。

C. 無匹配
Task：要求一個目前 Skill 未覆蓋的新型工作。
預期：NO_MATCH → Agent / Research，不自動建立 Skill。

D. Metadata 不足
Task：兩個 Skill Metadata 相似。
預期：AMBIGUOUS → 最小候選證據 → 仍不明確則既有 Skill Routing；不得硬選。

E. Router 不值得啟動
Task：目前候選 Skill 很少且既有 Small Mode 可直接判斷。
預期：跳過 Semantic Router，不為了形式完整增加額外成本。

F. Router 成本高於收益
預期：回退既有 Small Mode；不得為了維持 Router 使用率而強制啟動。

驗證通過條件：
- 能說明 Router 與 Skill Routing 不同。
- 能說明何時跳過 Router。
- 能說明 Metadata 不足時如何逐級揭露。
- 能正確回退 Agent / 既有 Routing。
- 不把 Simulation 結果寫成 FIELD。


## C-01 Control Plane Query Interface Alignment

C 不自行實作 Registry；Router 只消費 B 已定義的最小 Query Interface。

可使用：GET SKILL METADATA / GET SKILL STATE / GET ROUTING TERMS / GET REQUIRED CONTEXT POINTER / GET MINIMAL SKILL EVIDENCE。

最小 Query Result：EntityID / Scope / Authority / Depth / Result / Unknowns / Fallback / SourcePointer。

Router 不需要知道 Registry 儲存方式，也不得把 Query 結果當成 Skill Definition Source of Truth。

## C-02 Candidate Handling

UNIQUE → 必要 Context → Route。
MULTIPLE → 最小 Metadata → 最小 Evidence → 仍不明確則既有 Skill Routing / Agent。
NONE → STOP → Agent fallback。
INVALID → 排除；無有效候選則 NO_VALID_CANDIDATE。
UNKNOWN → 停止目前 scope，不把未知補成真值；必要時提高 Query depth。

Router 不得把 MULTIPLE 變成唯一答案，也不得因 NONE 自動建立 Skill。

## C-03 Runtime Boundary

Route 決定後：Load Skill Definition → Validate Input → Check Dependency → Execute → Stop Condition → Output。

Runtime 才可讀取完整 Skill Definition；Router 不預載完整 Definition。Runtime 不修改 Skill Definition、Registry 或 Query Contract。

## C-04 Verification / Evidence / Trace

Execution Output → Verification Rule → Verification Result → Evidence → Trace。

Verification Rule = 驗證方法；Evidence = 本次實際證據；Trace = 本次運作紀錄。Simulation 不得標記為 FIELD。

## C-05 Failure / Re-route

Failure 至少包含 Missing Input / Invalid Input / Dependency Failure / Execution Failure / Verification Failure / No Candidate / Ambiguous Candidate。

Failure → Classification / Diagnosis → 判斷是否可 Re-route → 可：重新 Query / Router；不可：STOP + 原因 + Evidence / Trace。禁止因 Failure 任意建立新 Skill。

## C-06 E2E Acceptance Target

至少驗證：正常 E2E、Skill Update、Skill Disable、Registry Rebuild、Dependency Failure、Verification Failure。以上目前均屬 DESIGN / STATIC TARGET；Natural FIELD 才能判定實際 Accuracy、Cost、Recovery 為 PASS。
