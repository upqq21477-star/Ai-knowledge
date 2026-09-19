# AI 知識系統六層架構第一階段施工計畫 v1.0

版本：v1.0
日期：2026-09-19
狀態：【施工規劃】

## 1. 第一階段目標
不是一次完成全庫重構。第一階段只建立「新架構可運作的骨架」，並用一個 Project 做端到端模擬。

## 2. Phase 0｜凍結邊界
規則：
- 不改 CURRENT Baseline 的工程游標。
- 不取代現有 Skill Control Plane。
- 不大規模移動舊檔案。
- 不宣告既有資產已完成新分類。
- 新架構文件本身屬 Blueprint / Planning。

完成條件：新舊架構可以同時存在，且沒有兩個 CURRENT。

## 3. Phase 1｜建立六層契約
建立：
1. Knowledge Contract
2. System Contract
3. Project Contract
4. Plan Skill Contract
5. 協助 Skill Contract
6. Agent Skill Contract

驗收：
- 每層能回答負責什麼／不負責什麼。
- 每層有最小 Input / Output。
- 層與層之間不存在循環責任。

## 4. Phase 2｜既有資產分類
對目前主要資產進行 Mapping：
0-知識/
1-系統/
2-方案/
專案A/
藍圖/
以及 root Governance。

輸出：
Asset → Responsibility → Target Layer → Action → Evidence → Status。
第一輪允許 UNKNOWN，不允許猜測。

## 5. Phase 3｜建立最小運作鏈
選擇一個低風險、非遊戲內容的工作情境：
User → 協助 Skill → Agent → Project Scope → 方案 Skill → System → Knowledge → Verification → Evidence → Agent 回報。
此階段以 Simulation Acceptance 為主，標記「（代）」。

## 6. Phase 4｜接入 Control Plane
將運作鏈映射到既有：
Semantic Router → Control Plane Query → Registry → Candidate → Runtime → Verification → Evidence → Trace。
不新增第二套 Registry。

## 7. Phase 5｜Project A Scope 實驗
至少測：
A. 正常任務
B. 缺少條件
C. 跨 Project 資料污染
D. Skill 找不到
E. System 找不到
F. Knowledge 不足
G. Verification 失敗
H. Replan

通過條件：錯誤情況不能靠模型自行補資料繼續假裝完成。

## 8. Phase 6｜再決定是否遷移
只有前五階段穩定後，才開始：
分類 → SPLIT / MERGE / WRAP / REFINE → 引用掃描 → 小批次實體搬遷 → Re-read → Verification → Evidence → 下一批。
如果新架構在實驗中沒有優於舊架構，停止大規模遷移並重新研究。

## 9. 第一階段成功指標
不以建立多少文件衡量。
主要觀察：
- Context token 是否下降
- Skill 選擇是否更準
- Project Scope 是否更乾淨
- 缺失資訊是否能被正確暴露
- Verification 是否更容易
- 舊文件互相衝突是否減少
- 新 AI 是否能從最小入口恢復正確結構

## 10. Acceptance
- 設計驗收：可立即進行。
- 模擬驗收：可作為目前通過依據，標記「（代）」。
- Natural FIELD：待自然工作產生 Evidence。
- 實體大搬遷：等待前述 Evidence。
這與目前 repository 的「Simulation 不等於 FIELD」規則一致。

## 11. 停止條件
出現以下任一情況，停止擴張並回到研究／問題流程：
- 新舊責任無法清楚區分
- Project Scope 仍會大量污染
- Skill 數量快速膨脹但責任沒有獨立性
- System 開始重新變成大型說明書
- Knowledge 開始承擔 Workflow
- Agent 開始直接承擔領域知識
- Control Plane 出現第二套 Source of Truth
- Context 成本沒有下降且複雜度上升

## 12. 第一階段終點
第一階段不是「全庫完成」。
終點是：
一條可理解、可路由、可按需載入、可驗證、可回報的六層工作鏈，在 Project Scope 內成功運作。
完成後才決定是否進入全庫遷移。
