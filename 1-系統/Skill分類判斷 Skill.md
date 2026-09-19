# Skill 分類判斷 Skill（Skill Classification & Lifecycle Judge） v1.1

版本：v1.0
日期：2026-09-19
狀態：【建立；待實際運作驗收】
定位：Skill 治理層；判斷新能力、新 Skill 或既有 Skill 變更應如何處理。

## 1. 核心責任

當出現新能力、新工具、新 Provider、新 Mode、新 Skill 候選或既有 Skill 失效／重疊時，判斷：

KEEP / MERGE / UPDATE / REPLACE / REFERENCE / DEFER / ARCHIVE

本 Skill 不直接執行變更；決策確認後交給 Evolution Management，再由 Execution 執行。

## 2. Trigger

Skill 建立、分層、融合、更新、取代等結構變更候選，預設視為 D3 結構研究輸入；本 Skill 不得因「只是新增檔案」而跳過研究與邊界判斷。

以下任一情況觸發：

- 出現新的 Skill 候選。
- 新增能力可能與既有 Skill 重疊。
- 新 Provider / Tool / Model 被提出為 Skill。
- 既有 Skill 出現責任膨脹、重複或失效。
- Failure Pattern 顯示 Skill 邊界可能錯誤。
- Actual Usage 顯示 Skill 長期未使用或使用方式改變。
- 需要融合、更新、取代或封存 Skill。

一般工作任務若沒有 Skill 結構變更，不啟動本 Skill。

## 3. 判斷順序

若候選尚未經 Research D3：先回 Research Skill 完成問題拆解、研究問題地圖、既有 Skill 盤點與證據比較；本 Skill 接收研究結果後進行正式分類。

N
→ 定義責任
→ Input / Output
→ Trigger
→ 實際使用
→ 反查既有 Skill
→ 比較責任是否相同
→ 判斷 Provider / Tool / Mode / Shared Capability / Reference
→ 判斷是否形成獨立責任
→ 決定處置

## 4. 分類規則

Capability：要完成什麼。
Provider：誰提供能力。
Tool：如何進行外部操作。
Mode：同一責任下的不同運作方式。
Skill：可重複、可獨立路由的工作責任。
Reference / Rule / Knowledge：提供依據，但本身不是工作責任。

新 Provider、Tool、Model、名稱或方法本身，不足以建立新 Skill。

## 5. 比較欄位

至少比較：

Purpose
Trigger
Input
Output
Responsibility
Mode
Dependency
Context Cost
Execution Cost
Verification
Actual Usage
Overlap
Migration Cost
Failure Pattern
Long-term Maintenance Cost

缺資料不得猜測，標記 UNKNOWN。

## 6. 處置

建立新 Skill 的必要條件：
- 已完成 D3 結構研究，或有明確證據證明可直接判定。
- 存在獨立 Responsibility。
- 有獨立 Trigger 或明確獨立路由需求。
- Input / Output 可明確定義。
- 與既有 Skill 無法以 Mode / Workflow / Shared Capability 合理承接。
- 分離後的 Context、Routing、Execution、Maintenance 成本具合理性。

若上述條件不足，不直接建立，優先 MERGE / UPDATE / DEFER。



KEEP：形成獨立責任且與既有 Skill 不重疊。
MERGE：責任相近，可由既有 Skill + Mode 承接。
UPDATE：既有 Skill 責任仍正確，但規則需要改進。
REPLACE：新方案完整承接舊責任，且已有足夠替代證據。
REFERENCE：不是工作責任，只需保留為 Rule / Knowledge / Reference。
DEFER：證據不足，不做永久結構變更。
ARCHIVE：退出現行工作結構，但保留歷史。

## 7. Unknown / Evidence 規則

不能因「看起來更好」而 REPLACE。
不能因「功能很多」而拆成多個 Skill。
不能因「文件不同」而視為不同責任。
不能因「Provider 不同」而建立新 Skill。
不能因一次失敗就改變 Skill 邊界。

證據不足 → DEFER。
重複失敗且有結構性證據 → UPDATE / MERGE / REPLACE 評估。

## 8. Output

每次判斷至少輸出：

Candidate
Existing Match
Responsibility Comparison
Classification
Action
Reason
Unknowns
Dependencies
Migration Needed
Verification Target

## 9. 與其他 Skill 的路由

新能力／Skill 候選
→ 本 Skill

需要實際修改結構
→ Evolution Management
→ Execution
→ Evidence / Verification

只是一般工作
→ 不進入本 Skill。

若發現長期重複、責任漂移或結構性成本
→ Distillation 評估。

## 10. 驗收

文件建立：PASS
規則定義：PASS
實際運作：PENDING
多案例分類：PENDING
50 次實際任務測試：PENDING
