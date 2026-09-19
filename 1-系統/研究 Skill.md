# 研究 Skill（Research Skill） v1.4

版本：v1.5
日期：2026-09-19
狀態：【Control Plane 接入；正式 Definition；自然運作 Evidence 持續累積】

## 1. Definition
將需要研究的問題拆解、配置研究深度、搜尋與比較證據、形成可支持的候選方案，並依新證據動態升降研究深度。

## 2. Trigger
- 缺少完成任務所需資訊。
- 需要外部／歷史資料或多來源比較。
- 現有 Knowledge 不足以支持結論。
- 原因、範圍或解法不明。
- 涉及跨 Skill／跨系統影響。
- 涉及新 Skill、分層、融合、更新或取代候選。

已有充分可驗證資料時停止，不重複研究。

## 3. Input / Output
Input：Task Definition、Problem Definition、Triage、Research Conditions、必要 Context、Knowledge、既有 Skill / System。
Output：Research Problem、Problem Decomposition、Problem Map（D3）、Depth、Search Paths、Sources、Evidence Candidates、Comparison、Candidate Solutions、Unknowns、Verification Target。

## 4. Depth
D0：原因明確、局部、無外部資料需求。
D1：少量未知，可局部調查。
D2：原因不明、多候選方案、多來源比較。
D3：系統／架構級、高不確定性、跨 Skill、重複失敗或結構性問題。

深度可升級或降級；初始分級不是最終分級。

## 5. Research Procedure
Problem
→ Decomposition
→ Depth
→ Search / Compare
→ Evidence
→ Candidate Solutions
→ Verification Target
→ Escalate / Close

D2/D3 不對原始問題做單一搜尋；D3 必須保留研究問題地圖與反例／失敗模式。

## 6. Evidence Boundary
Search 結果不是自動 Evidence。
跨領域類比只能作候選參考。
單一來源不得自動視為充分。
證據不足 → UNKNOWN，不以合理性補空缺。

## 7. Skill Structure Boundary
涉及新 Skill 時：
Research D3 → 現有 Skill 盤點 → Responsibility / Boundary Analysis → Skill 分類判斷。
不得直接建立 Skill。

## 8. Cost / Stop
Context、Search、Execution、Verification 使用 L / M / H。
問題已被充分回答即停止；不為追求研究深度而無限延伸。

## 9. Routing
Task 不清 → Task Understanding。
需要載入資料 → Context Management。
需要證據判定 → Evidence / Verification。
確認結構變更 → Evolution。
實際修改 → Execution。
長期結構成本 → Distillation。
需要保存長期知識 → Knowledge Management。

## 10. Control Plane
可按需查詢 Entity / State / Dependency / Impact / Evidence / Provenance / Authority。
Control Plane 提供最小 metadata，不取代 Research Source。

## 11. Failure
搜尋不足、來源衝突或無法確認 → UNKNOWN / INSUFFICIENT。
研究過度膨脹 → 重新評估 Depth。
發現結構性問題 → 不以局部修補掩蓋。

## 12. Lifecycle
KEEP：研究責任穩定。
UPDATE：研究規則變更。
DEFER：證據不足。
ARCHIVE：責任退出現行結構。
