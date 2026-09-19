# 研究 Skill（Research Skill） v1.3

版本：v1.2
日期：2026-09-19
狀態：【建立；已加入問題分級與研究深度控制；待實際運作驗收】

## 1. 定位
研究 Skill 不只是「搜尋與整理資訊」。
其責任是：將需要研究的問題拆解、建立研究問題地圖、選擇適當研究深度、搜尋與比較證據、形成可支持的解決方案，並在新證據出現時重新判斷研究深度。

核心原則：
問題越複雜，不代表一定要無限制深挖；應依問題規模、嚴重度、影響、不確定性、重複性與結構性配置處理成本。

## 2. Trigger
以下任一情況觸發：
- 缺少完成任務所需資訊。
- 需要確認外部／歷史資料。
- 需要多來源比較。
- 現有 Knowledge 不足以支持結論。
- 新資訊可能改變目前判斷。
- 發現問題但原因、範圍或解法不明。
- 問題可能涉及既有 Skill 的新增、分層、融合、更新、取代。
- 問題可能涉及系統結構或跨 Skill 影響。

若已有充分、可驗證資料，不重複搜尋。

## 3. 研究前：問題分級與處理深度
研究不是直接搜尋。

先判斷問題狀態，至少檢查：
- Scope：問題規模／範圍
- Severity：問題嚴重度
- Impact：影響範圍
- Uncertainty：不確定性
- Recurrence：是否重複發生
- Structurality：是否可能為結構性問題

注意：
「規模」與「嚴重度」不可視為同一維度。
大問題不一定需要深度研究；小問題也可能因高嚴重度而需要立即處理。

## 4. Research Depth
依問題評估選擇初始處理深度：

### D0：直接處理
適用：
- 原因明確
- 影響局部
- 不需要外部資料
- 無結構性疑慮

流程：
確認 → 執行 → 驗證。

### D1：快速調查
適用：
- 存在少量未知
- 範圍局部
- 可透過少量搜尋或局部診斷解決

流程：
問題理解 → 局部搜尋／調查 → 判斷 → 修正 → 驗證。

### D2：標準研究
適用：
- 原因不明
- 存在多個候選解法
- 需要外部資料
- 需要多來源比較

流程：
問題拆解 → 搜尋 → 比較 → 證據 → 解決方案 → 驗證。

### D3：深度／結構研究
適用：
- 系統級或架構級問題
- 高不確定性
- 跨 Skill／跨系統影響
- 重複失敗
- 明顯結構性問題
- 方案存在重大分歧

流程：
問題定義
→ 問題拆解
→ 研究問題地圖
→ 本系統現況
→ 外部研究
→ 同領域案例
→ 跨領域類比
→ 方案比較
→ 反例／失敗模式
→ 候選方案
→ 驗證
→ 決策

D0～D3 為目前研究模型，不視為最終固定分類。

## 5. 研究問題拆解
進入 D2／D3 時，不直接對原始問題做單一搜尋。

至少建立：
1. 核心研究問題
2. 子問題
3. 已知資訊
4. 未知資訊
5. 必須驗證的假設
6. 需要比較的方案
7. 可能的失敗模式

D3 必須形成「研究問題地圖（Research Problem Map）」。

## 6. 搜尋路徑
研究至少區分：

### Search
快速取得候選資料，不等同完整研究。

### Deep Research
多來源、交叉比較、方案分析。

### 同領域研究
搜尋相同或高度相近問題在原領域的處理方式。

### 跨領域類比
搜尋其他領域是否存在結構相同的問題及其解法。

跨領域類比只能作為候選證據／設計參考，不得直接視為本系統適用方案。

## 7. 方案形成
研究不能停在「找到資料」。

應完成：
資料 → 證據 → 方案 → 比較 → 支持程度 → 候選解法。

比較至少考慮：
- 是否解決原問題
- 適用範圍
- 複雜度
- Context Cost
- Execution Cost
- 維護成本
- 失敗模式
- 對既有架構的影響
- 驗證難度

研究輸出應指出「目前證據支持哪一方案／方向」，並清楚保留 UNKNOWN。

不得以「看起來合理」填補證據缺口。

## 8. 動態升級／降級
研究深度不是一次決定後永久固定。

研究過程中新證據出現時，重新評估：
- 問題是否比原先預期更大？
- 是否出現跨系統影響？
- 是否出現重複失敗？
- 不確定性是否提高？
- 是否發現結構性原因？

必要時：
D0 → D1 → D2 → D3。

反之，如果研究證明問題其實局部且原因明確，可降低處理深度。

因此：
「初始分級」≠「最終分級」。

## 9. 與其他 Skill 的邊界

Task Understanding：
理解任務與問題目標、限制、已知／未知。

Research：
拆解研究問題、配置研究深度、搜尋、比較、形成候選解法。

Context Management：
決定本次研究需要載入哪些 Context。

Evidence / Verification / Diagnosis：
判斷證據可信度、驗證結果、診斷失敗原因。

Knowledge Management：
保存經驗、已驗證知識、來源與生命週期資料。

Execution：
執行已確認的方案。

Evolution Management：
處理確認後的結構／規則／依賴變更。

Distillation：
只有在累積結構性證據後，才進行長期結構壓縮與重組。

## 10. Skill 建立屬於 D3 結構研究

「建立新 Skill」不是一般功能新增，而是系統責任邊界的結構性變更候選，因此預設以 D3 深度／結構研究處理。

除非研究證明只是既有 Skill 的內部功能、Mode、Workflow、Shared Capability、Provider / Tool 或 Reference，才可降級處理，不建立新 Skill。

標準流程：

D3 問題定義 → 問題拆解 → 研究問題地圖 → 現有 Skill 盤點 → Capability / Responsibility 分析 → Boundary Analysis → Skill 分類判斷 → 建立／融合／更新／取代／延後 → Execution → Verification → Feedback。

因此「建立 Skill」是 D3 研究的實際產出之一，不是研究完成後可直接跳過分類判斷的普通檔案建立。

## 11. Skill 新增／分層問題
當研究問題涉及：
- 新 Skill 是否應建立
- 現有 Skill 是否應分層
- 是否只是 Mode
- 是否只是 Workflow
- 是否只是 Shared Capability
- 是否只是 Provider / Tool
- 是否應融合、更新、取代

不得直接建立 Skill。

先進行問題拆解與研究深度判定，再比較既有 Skill 責任與候選責任。

必要時路由至：
Skill分類判斷 Skill

Skill 分類結果若確認需要結構變更，再交由：
演化管理 Skill → 執行 Skill → 證據驗證診斷 Skill

## 12. Input
- Task Definition
- Problem Definition
- Problem Triage 結果
- Research Conditions
- 必要 Context
- 既有 Knowledge
- 既有 Skill／System 文件

## 13. Output
最低輸出：
- Research Problem
- Problem Decomposition
- Problem Map
- Initial Depth
- Search / Research Paths
- Sources
- Evidence Candidates
- Comparison
- Candidate Solutions
- Recommended Direction（僅描述證據支持方向，不等同政治或價值判斷）
- Remaining Unknowns
- Final Depth / Escalation Record
- Verification Target

D3 必須保留完整研究鏈。

## 14. 路由
問題尚未理解 → Task Understanding。

需要 Context → Context Management。

需要研究 → Research。

研究完成，需要判斷證據 → Evidence / Verification。

研究發現失敗原因 → Evidence / Verification / Diagnosis。

研究結果涉及 Skill 新增／分層／融合／更新／取代 → Skill分類判斷。

研究結果確認需要系統結構變更 → Evolution Management。

需要實際修改 → Execution。

需要保存為長期知識 → Knowledge Management。

出現長期重複結構成本 → Distillation。

## 15. 失敗
- 搜尋不足不得以合理性補空缺。
- 找不到資料時標記 UNKNOWN。
- 單一來源不得自動視為充分證據。
- 跨領域類比不得直接視為本系統適用結論。
- 發現新問題不得默認升級成新 Skill。
- 研究過度膨脹時重新評估研究深度。
- 發現結構性問題時不得以局部修補掩蓋。

## 16. 成本控制
研究深度與成本一起評估：
- Context Cost：L / M / H
- Search Cost：L / M / H
- Execution Cost：L / M / H
- Verification Cost：L / M / H

原則：
不是「能研究多深就研究多深」，
而是「問題值得多少研究成本，就投入多少」。

## 17. 驗收
文件建立：PASS
問題分級模型：已建立
研究深度模型：已建立
動態升降級：已建立
實際運作：PENDING

## 18. 來源
- 藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md
- 1-系統/Agent Skill.md
- 外部研究：Task Decomposition、Skill Routing、Incident Triage、Research Query Decomposition 等相關研究與實務資料。
