# Agent／Skill 類架構快速對照測試版

## 目的

不再先假設五層架構具有獨創性。

本測試用同一批任務，快速比較：

A：目前五層外置架構
> Master Agent → Project → Solution → System → Knowledge

B：業界常見 Agent／Skill 類架構的最小抽象
> Agent → Skill → Tool → Knowledge

C：扁平 GitHub 文件架構
> User → 文件搜尋 → 執行

B 只做「概念級對照」，不是宣稱已實際呼叫 OpenAI／Anthropic 原生 runtime。

## 一、測試原則

1. 三組使用完全相同的任務。
2. 不比較模型智力；只比較架構造成的差異。
3. 不把既有產品宣稱的功能當成測試結果。
4. Token 只做估算，若沒有實際 API 計量，不宣稱為真實 Token。
5. 每次失敗都記錄「錯在哪一層」。
6. 先做小樣本快速篩選，再決定是否進行 50／100 次正式測試。

## 二、三組架構

### A 五層架構

User
→ Master Agent
→ Project
→ Problem
→ Solution
→ System
→ Knowledge
→ Acceptance
→ Output

優點假設：
- 問題域先縮小 Context。
- Project 負責 Problem → Solution。
- Solution 負責調度。
- System 負責功能。
- Knowledge 提供依據。

待驗證：
- 多一層 Project 是否真的降低錯誤。
- 額外路由是否抵消 Context 節省。
- 與 Agent／Skill 類架構相比是否仍有必要。

### B Agent／Skill 類最小架構

User
→ Agent
→ Skill
→ Tool
→ Knowledge
→ Output

優點假設：
- Agent 負責任務理解與編排。
- Skill 提供可重複工作能力。
- Tool 執行具體操作。
- Knowledge 提供資料與依據。

待驗證：
- 是否需要 Project 這個中間層。
- Agent／Skill 自動發現是否能取代 Problem Index。
- 是否能維持低 Context。

### C 扁平文件架構

User
→ GitHub／文件搜尋
→ 直接讀取相關文件
→ 執行
→ Output

用途：
- 測量「分層本身」到底帶來多少收益。

## 三、快速測試任務

先做 15 題，每題三組各執行一次，共 45 次。

T01 一般資訊搜尋
T02 研究資料搜尋
T03 GitHub 工具搜尋
T04 來源驗證
T05 找不到資料時的處理
T06 已知資料的快速定位
T07 複合問題拆分
T08 多個 System／Skill 組合
T09 跨領域問題
T10 需要引用證據的回答
T11 需要修改既有文件
T12 新 AI 零記憶接手
T13 Context 過大時的資訊裁剪
T14 發現既有規則衝突
T15 任務完成後驗收

## 四、記錄欄位

每次記錄：

| 欄位 | 說明 |
|---|---|
| Task | 任務編號 |
| Route | 路由是否正確 |
| Context | 是否讀取不必要內容 |
| Function | 是否完成需要的功能 |
| Grounding | 是否有依據 |
| Distortion | 是否發生語意失真 |
| Handoff | 零記憶是否能接手 |
| Acceptance | 是否正確判定完成 |
| Cost | Context／Token 估算 |
| Error Layer | 失敗發生在哪一層 |
| Notes | 原因 |

## 五、核心比較指標

### 1. 正確率

成功任務 ÷ 總任務。

### 2. 路由錯誤率

錯誤路由 ÷ 總任務。

### 3. Context 成本

完成任務實際需要讀取的文件量。

若無 Token 計量，以：
- 字元數
- Markdown 行數
- 估算 Token

三者之一記錄，並標記「估算」。

### 4. 功能完成率

完成要求功能 ÷ 總任務。

### 5. 語意失真率

輸出與任務／來源語意不一致的比例。

### 6. 零記憶交接率

拿掉歷史對話後，僅依外部資料完成任務的比例。

### 7. 驗收正確率

完成與未完成的判定是否正確。

## 六、錯誤分類

A／B／C 任一組出錯時，先歸類：

R = Routing
C = Context
S = Semantic
F = Function
G = Grounding
H = Handoff
A = Acceptance

同一錯誤可有主因與次因：

> 主因：R；次因：C

## 七、快速判定門檻

15 題快速測試後，不直接宣布誰較好。

只回答：

1. A 是否明顯增加不必要路由？
2. A 是否明顯降低 Context？
3. B 是否已自然涵蓋 A 的主要功能？
4. C 是否其實足夠？
5. 哪些功能是 A 特有的？
6. 哪些功能 B 已成熟提供？
7. 哪些功能三組都做得到？
8. 哪些差異值得進入 50／100 次正式測試？

## 八、重要限制

本測試不是產品 Benchmark。

若沒有直接使用 OpenAI／Anthropic 等產品的實際 runtime，不得寫成：
> 「A 比 OpenAI Agent 好」
或
> 「A 比 Claude Skill 好」。

只能寫：
> 「A 與 Agent／Skill 類架構的概念模型比較結果」。

正式競品測試必須另外取得相同條件的實際 runtime。

## 九、測試後決策

若 B 已涵蓋 A 的主要功能，且 A 沒有顯著 Context／交接優勢：

> 停止擴張 A，改研究如何把現有 Knowledge／Solution 遷移到成熟 Agent／Skill 架構。

若 A 在「手機端、跨模型、GitHub 外部記憶、低 Context、零記憶交接」出現可重現優勢：

> 保留 A，但重新定位為「外置、模型無關的 Agent／Skill 架構研究」。

若 C 已接近 A／B：

> 優先保留最簡單方案，不增加額外分層。

## 十、啟動方式

測試開始時只輸入：

> 啟動快速對照測試

然後依序執行 T01～T15。

第一輪完成後，再決定是否擴大至 50／100 次。
