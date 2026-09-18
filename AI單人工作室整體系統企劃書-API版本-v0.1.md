
# AI 單人工作室整體系統企劃書
## API 版本 v0.2

> 文件性質：未來整體規畫／企劃書  
> 文件狀態：討論稿  
> 關係文件：AI單人工作室整體系統企劃書-無API版本-v0.1.md  
> 重要界線：本文件不是現行四大方案之一，不取代現行工程架構，不代表已完成實作。

---

# 1. 文件定位

本企劃書描述「取得電腦、API、較完整執行環境後」的 AI 單人工作室升級方向。

核心原則：

> **資料語義不變，執行方式升級；GitHub 不被 API 取代，API 只作為讀取、整理、驗證與執行的加速層。**

API 版本不是重新建立另一套知識庫，也不是一開始建立完整企業級 Agent 平台。

最重要的設計：

~~~
現有知識庫
    │
    │ GitHub = Canonical Source
    ↓
Client / API Layer
    │
    ├─ Index
    ├─ Search
    ├─ Cache
    ├─ Validation
    ├─ Context Assembly
    └─ 基礎運算
    │
    ↓
GPT / Model
    │
    ├─ 理解
    ├─ 推理
    ├─ 規劃
    └─ 必要時執行
    │
    ↓
GitHub
~~~

API 的第一價值不是「讓 AI 自動做更多事」，而是：

> **不要讓昂貴的模型去做可以由程式直接完成的資料處理。**

---

# 2. API 版本要解決的第一問題

無 API 階段最大的成本不一定是「做不到」，而可能是：

- GPT 每次重新搜尋大量文件。
- GPT 閱讀大量不相關內容。
- GPT 自己進行檔案分類。
- GPT 自己判斷版本。
- GPT 自己解析 metadata。
- GPT 重複處理沒有變更的資料。
- GPT 把基礎搜尋、整理、驗證也當成推理工作。

因此第一階段 API 化應優先處理：

~~~
資料取得
↓
資料過濾
↓
資料索引
↓
資料快取
↓
Context 組裝
↓
模型推理
~~~

而不是：

~~~
Multi-Agent
Event Bus
Scheduler
Worker Cluster
Graph DB
完整 Agent Runtime
~~~

---

# 3. 核心架構：GitHub + Client / API Layer

第一階段推薦架構：

~~~
                    使用者
                      │
                      ↓
              Client / AI Workspace
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
        Index       Search      Validation
          │           │           │
          └───────────┼───────────┘
                      ↓
               Context Builder
                      │
                      ↓
                 GPT / Model
                      │
                      ↓
               Result / Action
                      │
                      ↓
                   GitHub
~~~

其中：

### GitHub

負責：

- Canonical Source。
- 正式知識。
- 系統定義。
- 方案。
- 規則。
- 目前狀態。
- 交接資料。
- 重要證據。
- 版本歷史。

### Client / API Layer

負責：

- Repository 讀取。
- Index。
- Search。
- Metadata filter。
- Cache。
- 基礎解析。
- Schema validation。
- Context Assembly。
- 必要時呼叫模型 API。
- 必要時執行工具。

### GPT / Model

主要負責：

- 語意理解。
- Intent 判斷。
- 複雜推理。
- 規劃。
- 需要模型能力的內容生成。
- 高階判斷。

---

# 4. 最重要原則：API 是加速層，不是真相層

必須保持：

~~~
GitHub
  =
Canonical Truth

Client / API
  =
Derived / Operational Layer

GPT
  =
Reasoning Layer
~~~

因此：

- API 掛掉，GitHub 資料仍然存在。
- Index 損壞，可以重建。
- Cache 損壞，可以重新取得。
- Vector Store 損壞，可以重新建立。
- Runtime 損壞，不應摧毀正式知識。
- 換 GPT，不應失去知識。
- 換 Client，不應需要重建整個知識庫。

這是 API 版本最重要的容錯原則。

---

# 5. 不改目前資料設計

API 化原則：

> **先適配現有資料，而不是先要求現有資料配合 API。**

現有：

~~~
知識/
系統/
方案/
目前狀態/
交接/
歷史/
~~~

可以保持。

API Client 讀取後建立：

~~~
Repository
    ↓
Parser
    ↓
Metadata
    ↓
Index
    ↓
Search / Retrieval
~~~

因此 API 化不需要先重寫整個 Repository。

---

# 6. Context 壓縮是第一級核心能力

目前：

~~~
使用者問題
↓
GPT 搜尋 Repository
↓
讀大量 Markdown
↓
GPT 自己判斷相關內容
↓
推理
~~~

API 化：

~~~
使用者問題
↓
Client
↓
Index
↓
Metadata Filter
↓
Keyword / Semantic Search
↓
候選文件
↓
相關段落
↓
最小充分 Context
↓
GPT
~~~

例如：

~~~
399 份文件
↓
Index
↓
20 個候選
↓
5 個相關文件
↓
必要段落
↓
GPT
~~~

目標不是讓 GPT 讀更多。

目標是：

> **讓 GPT 只讀完成任務所需的正確資料。**

---

# 7. Token / Context 成本控制

API 版本應把 Token 視為資源。

成本不只包括 API 金錢成本，也包括：

- Context 長度。
- 模型推理量。
- Latency。
- 重複計算。
- Retrieval 次數。
- Embedding 次數。
- Tool Calls。

因此：

~~~
總成本
=
Model
+
Context
+
Retrieval
+
Embedding
+
Tool
+
Compute
+
Network
~~~

其中第一階段最值得降低的是：

> **Context Waste。**

---

# 8. 哪些工作不應交給大型模型

以下工作原則上應由 Client / Runtime 直接處理：

- 檔案是否存在。
- 檔案路徑。
- ID 查詢。
- 版本號比較。
- 狀態判斷。
- Metadata filter。
- Hash。
- 修改時間。
- JSON parsing。
- Schema validation。
- 重複檔案偵測。
- 索引更新。
- Cache 命中。
- 基本依賴檢查。
- 引用完整性檢查。
- 簡單統計。

模型主要處理：

- 語意。
- 意圖。
- 複雜判斷。
- 推理。
- 規劃。
- 生成。

原則：

> **Deterministic work → 程式；Semantic work → 模型。**

---

# 9. Retrieval 第一階段不必使用 Vector DB

第一版可以：

~~~
GitHub
↓
本地 / Client Index
↓
Keyword Search
↓
Metadata Filter
↓
GPT
~~~

只有當真實工作證明：

> Keyword Search 不足以找到需要的資料

才加入：

~~~
Embedding
↓
Semantic Search
↓
Hybrid Search
~~~

再有需要才考慮：

> Vector Database。

因此 Vector DB 不是 API 化的前置條件。

---

# 10. Hybrid Search

成熟後可以使用：

~~~
Keyword / BM25
+
Embedding / Semantic Search
+
Metadata Filter
+
Relationship
~~~

Keyword 適合：

- 專有名詞。
- ID。
- 文件名稱。
- 版本。
- 精確詞。

Semantic Search 適合：

- 同義表達。
- 自然語言。
- 使用者不知道正式名稱的情況。

Metadata 適合：

- 狀態。
- 類型。
- 專案。
- 版本。
- 時間。
- 適用範圍。

Relationship 適合：

- 系統依賴知識。
- 方案涉及系統。
- 知識取代舊知識。

---

# 11. Index 是派生資料

Index、Embedding、Vector Store 都不是正式知識。

~~~
GitHub Markdown / JSON
        ↓
Parser
        ↓
Index
        ↓
Embedding
        ↓
Vector Index
~~~

任何派生資料損壞都應可以：

~~~
刪除
↓
重新建立
↓
驗證
↓
恢復
~~~

因此：

> **不能因為 Index / Vector Store 損壞而失去 Knowledge。**

---

# 12. Index Lifecycle

自動索引至少需要：

~~~
建立
↓
更新
↓
驗證
↓
失效偵測
↓
重建
~~~

需要處理：

- 新增文件。
- 文件修改。
- 文件刪除。
- 版本更新。
- 狀態變更。
- Metadata 變更。
- 分類變更。

---

# 13. Cache

Cache 用於減少：

- 重複讀取。
- 重複解析。
- 重複搜尋。
- 重複 Embedding。
- API 成本。
- Token 使用。

但 Cache 必須保留：

- Source Reference。
- Source Version。
- Hash。
- TTL 或 invalidation 條件。

Cache 永遠不能取代 Canonical Source。

---

# 14. Context Assembly

這是 API 版本第一階段最重要的能力之一。

輸入：

~~~
Task
Intent
System
Plan
Constraints
State
~~~

輸出：

~~~
Context Package
~~~

目標：

> **最小充分上下文，而不是最大上下文。**

概念：

~~~json
{
  "task": {},
  "intent": {},
  "system": {},
  "plan": {},
  "knowledge": [],
  "constraints": [],
  "state": {},
  "evidence": [],
  "history": []
}
~~~

這只是概念模型，不是目前正式 Schema。

---

# 15. Context Cache

如果某份資料沒有變更，就不應每次重新處理。

例如：

~~~
文件
↓
Parse
↓
Metadata
↓
Summary
↓
Hash
~~~

下一次：

~~~
Hash 相同
↓
直接使用既有結果
~~~

只有：

~~~
Hash 改變
↓
重新解析
~~~

這可以降低大量重複 Token 與 Compute。

---

# 16. Retrieval Reranking

搜尋得到的內容只是 Candidate。

不能直接全部送給 GPT。

流程：

~~~
Candidate
↓
相關性
↓
Status Check
↓
Version Check
↓
Source Quality
↓
Conflict Check
↓
最小充分集合
↓
Context
~~~

---

# 17. System Registry

系統註冊表未來可以描述：

- System ID。
- Name。
- Purpose。
- Capability。
- Input。
- Output。
- Dependencies。
- Knowledge Dependencies。
- Plan。
- Trigger。
- Permission。
- Verification。
- Version。
- Status。
- Health。

Runtime 資訊與正式系統定義分離。

---

# 18. Capability Registry

API 化後可增加：

~~~
search_repository
read_file
write_file
search_web
run_test
run_python
call_model
generate_embedding
query_index
send_notification
~~~

每個 Capability 描述：

- Input。
- Output。
- Permission。
- Cost。
- Risk。
- Timeout。
- Verification。

---

# 19. Intent Router

Intent Router 可以逐步加入，但不應一開始就成為大型 AI 分流系統。

第一階段：

~~~
簡單規則
↓
必要時模型判斷
~~~

例如：

- STATUS。
- LOOKUP。
- EXPLAIN。
- DISCUSS。
- RESEARCH。
- COMPARE。
- PLAN。
- CREATE。
- EDIT。
- VERIFY。
- EXECUTE。
- HANDOFF。

只有低成本方法無法判斷時，才升級到較昂貴模型。

---

# 20. Model Routing

可以形成：

~~~
Cheap Signal
↓
Cheap Classifier
↓
Semantic Router
↓
必要時大型模型
~~~

例如：

- 檔案查詢 → Client。
- 精確搜尋 → Search。
- 簡單分類 → 小模型或規則。
- 一般整理 → 中型模型。
- 複雜推理 → 高階模型。
- 高風險決策 → 高階模型 + Verification + Human Gate。

---

# 21. Event / Trigger

API 版本後才有真正的自動觸發條件。

來源可能包括：

- User Message。
- GitHub Event。
- Webhook。
- Schedule。
- File Change。
- Test Failure。
- Health Alert。
- External Event。

Event：

> 發生了什麼？

Intent：

> 要完成什麼？

兩者不能混為一談。

---

# 22. Scheduler

Scheduler 只負責：

> 什麼時候觸發。

不負責：

> 應該做什麼。

因此：

~~~
Scheduler
↓
Event
↓
Router
↓
System
↓
Task
~~~

但 Scheduler 只有在真實需求出現後才建立。

---

# 23. Background Worker

長時間任務才需要 Worker。

例如：

- 大量 Index。
- 大量 Embedding。
- 大型測試。
- 批量研究。
- 長時間資料整理。

第一版 API 不預設建立 Worker Cluster。

---

# 24. Task Runtime

大型或長時間任務可以有 Task ID：

~~~
CREATED
↓
PLANNED
↓
RUNNING
↓
WAITING
↓
VERIFYING
↓
COMPLETED
~~~

異常：

~~~
FAILED
BLOCKED
CANCELLED
ROLLED_BACK
~~~

Task State 保存：

- 目標。
- 當前步驟。
- 已完成工作。
- 下一步。
- 失敗原因。
- 重試。
- 產出位置。
- 驗證狀態。

---

# 25. Agent Runtime / Harness

完整 Runtime 是後期能力，不是第一版 API 必備。

成熟後才加入：

- Context。
- Tool。
- State。
- Permission。
- Timeout。
- Retry。
- Memory。
- Verification。
- Failure Handling。
- Observability。
- Cost Control。

原則：

> **Runtime 是讓模型可靠工作的環境，不是另一個大腦。**

---

# 26. Tool Layer

工具需要標準化：

- Schema。
- Permission。
- Timeout。
- Error Format。
- Retry。
- Audit。

但第一階段只建立實際會反覆使用的工具。

---

# 27. 權限與安全

API 自動化後，權限至少區分：

~~~
READ
SEARCH
CREATE
UPDATE
DELETE
EXECUTE
ADMIN
~~~

高風險：

- 大量刪除。
- Repository 結構變更。
- 正式部署。
- 付費外部服務。
- 敏感資料操作。

應保留 Human Gate。

---

# 28. GitHub 的資料邊界與可攜式交接

GitHub 架構還有一個重要優勢：

> **正式資料可以維持在明確的 Repository 邊界內，交接可以採用人工選擇的最小資料集。**

完整 Repository 不等於每次都必須交給 AI。

可以產生：

~~~
完整 Repository
↓
專案子集
↓
任務子集
↓
最小交接包
~~~

例如：

~~~
AI交接包.zip
├── 00-交接入口.md
├── 01-目前狀態.md
├── 02-核心規則.md
├── 03-系統索引.md
├── 04-相關方案.md
└── 05-必要知識/
~~~

因此：

- GPT → Claude。
- Claude → GPT。
- AI A → AI B。
- 內部人員 → 其他內部人員。

都可以透過資料包完成。

API 不應破壞這種可攜性。

---

# 29. 最小必要揭露

未來 Client 可以根據任務只提供：

> 完成該任務所需的最小資料。

例如外部協作者只需要某一專案：

~~~
專案目標
+
目前版本
+
必要規則
+
必要知識
+
TODO
~~~

不需要取得整個 Repository。

這降低：

- Context 成本。
- 不必要資料暴露。
- 交接複雜度。
- AI 誤讀其他專案的機率。

GitHub 權限本身仍需正確配置；GitHub 並不等於天然安全。

---

# 30. Database / Vector Store 的位置

未來可以增加 Database，但責任必須分離。

### GitHub

Canonical durable artifacts：

- 知識。
- 系統。
- 方案。
- 規則。
- 架構。
- 交接。
- 正式證據。

### Database

Operational State：

- Task。
- Job。
- Queue。
- Runtime。
- Metrics。
- Cache Metadata。

### Vector Store

Derived Data：

- Embedding。
- Semantic Index。

三者不能互相取代。

---

# 31. Knowledge Graph

只有當 Reference / Relation 已經不足時才考慮 Graph Database。

第一階段：

- ID。
- Reference。
- Relation fields。

足夠。

不要因為「未來可能有關係圖」就提前建立 Graph DB。

---

# 32. Verification

驗證仍維持三層：

### 第一層：結果

輸出是否正確？

### 第二層：行為

系統是否按預期運作？

### 第三層：架構

是否造成：

- 重複。
- 衝突。
- 責任漂移。
- 依賴膨脹。
- Context 膨脹。
- 技術債。

---

# 33. Evaluation

需要逐步建立：

- Regression Cases。
- Behavioral Tests。
- Outcome Tests。
- Golden Cases。
- Failure Cases。
- Handoff Tests。

簡單任務可以 strict assertion。

複雜任務可以 outcome-based evaluation。

不能只依賴 AI 自評。

---

# 34. Trace / Observability

重要任務可以記錄：

~~~
Task
↓
Context
↓
Tool Calls
↓
Model
↓
Output
↓
Verification
↓
Result
~~~

觀察：

- 成功率。
- 失敗率。
- 耗時。
- Tool Error。
- Retry。
- Context 大小。
- Token。
- API Cost。
- Retrieval 命中。
- Verification 失敗。
- Human Intervention。

---

# 35. 自動交接

成熟 Runtime 可以產生：

- 完成事項。
- 未完成事項。
- 目前狀態。
- 重要決策。
- 修改檔案。
- 驗證結果。
- 待確認問題。
- 下一步。

但是：

> 自動產生不等於自動成為正式真相。

正式狀態仍由治理規則決定。

---

# 36. 自動研究

未來：

~~~
問題
↓
Research Planner
↓
Search
↓
Evidence
↓
Comparison
↓
Synthesis
↓
Draft
↓
Human Review
↓
Knowledge Candidate
~~~

研究結果與正式知識分離。

證據層級：

~~~
Primary Source
Secondary Source
Expert Analysis
Community Discussion
Model Inference
Unverified
~~~

---

# 37. Self-Healing 限制

可以自動：

- Retry。
- Re-index。
- Restart。
- Rollback。
- Re-run Test。

不能直接：

> AI 發現核心架構有問題 → 自動重寫核心架構。

核心架構仍進入：

~~~
Observation
↓
Analysis
↓
Proposal
↓
Human Confirmation
↓
Implementation
↓
Regression
~~~

---

# 38. 系統熵控制

API 會提高資料與操作產生速度。

因此需要觀察：

- 重複知識。
- 重複規則。
- 相似系統。
- Dead System。
- Dead Index。
- Stale Knowledge。
- Dependency Explosion。
- Context Explosion。

但：

> 偵測結果只是 Candidate，不是自動刪除命令。

這仍由方案四治理。

---

# 39. 與四方案的關係

四方案不變：

### 方案一
整體資料治理。

### 方案二
AI 知識管理。

### 方案三
知識與資料迭代演化。

### 方案四
能力蒸餾與系統重構。

API / Client / Harness 不構成第五方案。

它們是：

> **執行與加速基礎設施。**

---

# 40. API 升級順序重新調整

API 不再以「建立完整 Agent 平台」為起點。

推薦：

## Level 0
現有無 API 架構。

## Level 1
GitHub API + Client。

目標：穩定取得 Repository 資料。

## Level 2
Local / Client Index + Cache。

目標：避免重複讀取與解析。

## Level 3
Keyword Search + Metadata Filter。

目標：降低 GPT 搜尋成本。

## Level 4
Context Assembly。

目標：只提供最小充分 Context。

## Level 5
Verification / Validation。

目標：把部分檢查移出模型。

## Level 6
Embedding + Semantic / Hybrid Search。

只有 Keyword Search 已證明不足才建立。

## Level 7
Tool Execution。

目標：自動執行已經反覆出現的操作。

## Level 8
Observability / Cost Tracking。

目標：知道自動化是否真的有收益。

## Level 9
Task Runtime。

只有長時間任務成為實際瓶頸才建立。

## Level 10
Background Worker。

只有需要非同步長任務才建立。

## Level 11
Event / Scheduler。

只有存在穩定的自動觸發需求才建立。

## Level 12
Advanced Agent Runtime / Self-Improvement。

最後才考慮。

---

# 41. 每一級的升級條件

不是因為「技術上可以」就升級。

必須：

~~~
實際瓶頸
↓
重複發生
↓
成本可觀察
↓
自動化收益
>
維護成本
~~~

才升級。

因此：

> **真實 FIELD 是 API 升級的重要觸發器。**

---

# 42. 第一個真正值得自動化的環節

目前預期：

### 第一優先
Retrieval + Index + Context Assembly。

理由：

- 高頻。
- 重複。
- 直接消耗 Context。
- 容易量化。
- 不必改變核心資料結構。

### 第二優先
Verification。

### 第三優先
Repetitive Tool Execution。

### 最後
Background Event / Multi-Agent。

---

# 43. API 成本控制

每個 Task 可以有：

- Context Budget。
- Reasoning Budget。
- Tool Budget。
- Time Budget。
- Cost Budget。

超過時：

- 壓縮。
- 分批。
- 改用低成本模型。
- 延後。
- 要求人工決策。

核心目標：

> **把昂貴模型留給真正需要推理的地方。**

---

# 44. API 的主要風險

1. 自動化過度。
2. Retrieval 錯誤。
3. Index Drift。
4. Runtime State Drift。
5. Agent Loop。
6. Cost Explosion。
7. Permission Failure。
8. Silent Failure。
9. Context 污染。
10. API 基礎設施反過來成為新的治理負擔。

其中第 10 項是單人工作室最重要的風險之一。

---

# 45. 成功判準

API 版本成立後，應能證明：

1. GPT 不需要每次重新讀完整 Repository。
2. Client 可以可靠找到正確資料。
3. Context Assembly 明顯降低無關上下文。
4. Token / API 成本下降或產出效率提高。
5. Index 可以可靠重建。
6. Cache 不會取代 Canonical Source。
7. Tool 執行可以追蹤。
8. Verification 可以自動執行。
9. 失敗可以定位。
10. 高風險操作仍受控制。
11. GitHub 仍是長期資料來源。
12. Runtime 損壞不會摧毀核心知識。
13. 新 GPT 可以繼續接手。
14. API 系統本身沒有成為主要維護負擔。

---

# 46. 失敗判準

如果出現：

- 自動化比人工更慢。
- Retrieval 常常錯。
- Context 反而更大。
- Cache 產生錯誤真相。
- Index 無法可靠重建。
- Agent 不斷循環。
- Background Task 經常失敗。
- 成本無法解釋。
- Runtime 成為單點故障。
- GPT 無法理解 GitHub Canonical Data。
- API 開始取代資料治理。
- 使用者花更多時間維護 AI 基礎設施。

則停止擴張，回到無 API 核心架構檢查。

---

# 47. 無 API 與 API 的關係

~~~
無 API
=
人工執行同一套語義

API
=
程式自動執行已證明有效的部分
~~~

例如：

無 API：

~~~
GPT 手動搜尋知識
~~~

API：

~~~
Client Search
↓
必要資料
↓
GPT
~~~

無 API：

~~~
GPT 手動檢查版本
~~~

API：

~~~
Client / Runtime 直接檢查
~~~

無 API：

~~~
GPT 手動整理 Context
~~~

API：

~~~
Context Builder
↓
最小充分 Context
~~~

所以：

> **API 不是重新發明流程，而是把已經證明值得自動化的人工流程移交給程式。**

---

# 48. API 與資料安全的邊界

API 化不能被理解為「把所有資料送到 API」。

正確方向：

~~~
GitHub
↓
Client 權限判斷
↓
最小必要資料
↓
必要時模型
~~~

而不是：

~~~
整個 Repository
↓
全部上傳
↓
所有服務共享
~~~

因此：

- Repository 權限仍然重要。
- API Token 權限應最小化。
- 外部服務應按資料敏感度分級。
- 不必要資料不應送出。
- 交接應使用最小資料集。
- GitHub 不代表天然安全。

---

# 49. 最終成熟形態

成熟後可以形成：

~~~
                       使用者
                          │
                          ↓
                 Client / Workspace
                          │
             ┌────────────┼────────────┐
             ↓            ↓            ↓
           Index        Search      Validation
             │            │            │
             └────────────┼────────────┘
                          ↓
                   Context Engine
                          │
                          ↓
                    Intent / Plan
                          │
                          ↓
                     GPT / Models
                          │
                  ┌───────┼───────┐
                  ↓       ↓       ↓
                Tools   Runtime  Search
                  │       │       │
                  └───────┼───────┘
                          ↓
                     Verification
                          │
                          ↓
                    GitHub / Storage
                          │
             ┌────────────┴────────────┐
             ↓                         ↓
       Canonical Data             Derived Data
             │                         │
          GitHub                Index / Vector / Cache
~~~

注意：

> 這是成熟目標，不是第一天的實作要求。

---

# 50. 最終原則

整個 API 版本可以濃縮成十二條：

1. **GitHub 保存長期真相。**
2. **API 是加速層，不是真相層。**
3. **Client 優先處理資料，不要讓大型模型處理所有基礎工作。**
4. **Deterministic work 交給程式，Semantic work 交給模型。**
5. **最小充分 Context 優先於最大 Context。**
6. **Index、Embedding、Cache 都是派生資料。**
7. **任何派生資料都必須可以重建。**
8. **只有實際瓶頸才增加 API 能力。**
9. **先 Retrieval / Context，再 Runtime / Agent。**
10. **高風險操作保留 Human Gate。**
11. **API 不得破壞 GitHub 的可攜式交接能力。**
12. **如果 API 比人工更麻煩，就停止擴張。**

---

# 51. 文件狀態

目前狀態：

**【未來規畫／企劃書／API 版本 v0.2／討論稿】**

本次 v0.2 主要修正：

- 強化「GitHub = Canonical Source」。
- 新增 Client / API Layer 作為主要中介。
- 將 API 第一優先從「Agent Runtime」調整為「Index / Search / Cache / Context」。
- 強化 Token / Context 成本控制。
- 明確區分 Deterministic Work 與 Semantic Work。
- 降低第一階段對 Vector DB 的依賴。
- 增加 Context Cache。
- 增加最小必要揭露與可攜式交接。
- 將完整 Agent Runtime 延後。
- 將 API 升級路線重新排序。
- 將 FIELD 設為 API 升級的重要觸發條件。
- 明確保留無 API fallback。
- 明確區分資料安全邊界與 GitHub 本身的安全責任。

本文件仍不是：

- 現行工程方案。
- 第五方案。
- 已完成架構。
- 已驗收功能。
- 立即實作規格。

正式進入實作前仍應：

~~~
討論
↓
外部研究
↓
候選架構
↓
反例／壓力測試
↓
成本分析
↓
安全／權限分析
↓
確認
↓
正式設計
↓
實作
↓
驗證
↓
回歸
↓
交接
~~~

---

# 52. 與無 API 版本的最終關係

兩份文件長期並存：

~~~
AI單人工作室整體系統企劃書-無API版本-v0.1.md
AI單人工作室整體系統企劃書-API版本-v0.2.md
~~~

無 API 版本回答：

> 沒有 API 時，一個人如何建立可持續的 AI 工作環境？

API 版本回答：

> 有 API 與電腦執行環境後，如何在不破壞既有資料語義與交接能力的前提下，把已證明有效的人工流程逐步自動化？

共同目標：

> **讓一個人長期駕馭不斷增長的 AI 工作、知識、系統與專案，而不讓 AI 基礎設施本身變成新的負擔。**
