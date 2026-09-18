# AI 單人工作室整體系統企劃書
## API 版本 v0.1

> 文件性質：未來整體規畫／企劃書  
> 文件狀態：討論稿  
> 關係文件：AI單人工作室整體系統企劃書-無API版本-v0.1.md  
> 重要界線：本文件不是現行四大方案之一，不取代現行工程架構，不代表已完成實作。

---

# 1. 文件定位

本企劃書描述「取得電腦、API、較完整執行環境後」的 AI 單人工作室升級方向。

它不是要推翻無 API 版本，而是把無 API 版本已確立的資料語義、責任邊界與工程原則，逐步自動化。

核心原則：

> 資料語義穩定，執行能力升級。

因此 API 版本與無 API 版本不是兩套互相競爭的系統，而是：

```
同一套核心資料與治理語義
              │
       ┌──────┴──────┐
       ↓             ↓
    無 API          API
 GPT + GitHub     GPT + Runtime
```

API 版本增加的是「自動化能力」，不是重新定義「什麼是知識、系統、方案、狀態與證據」。

---

# 2. API 版本的核心目標

API 版本主要解決無 API 階段的人工瓶頸：

- 人工搜尋。
- 人工建立索引。
- 人工整理 Context。
- 人工執行重複操作。
- 人工觸發固定任務。
- 人工等待背景工作。
- 人工進行大量重複驗證。
- GPT 每次重新取得相同資料。
- 多工具之間的資料傳遞。
- 長時間任務無法持續。

因此 API 版本不是單純：

> 「GPT 加一個 API。」

而是逐步形成：

> AI Runtime／AI Harness。

---

# 3. 核心架構

成熟方向：

```
                         使用者
                           │
                           ↓
                 Interaction Layer
                           │
                           ↓
                    Intent Router
                           │
                           ↓
                    Control Plane
                           │
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
 Knowledge Library   System Registry    Plan Registry
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ↓
                  Context Assembly
                           │
                           ↓
                       Planner
                           │
                           ↓
                    Agent Runtime
                           │
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
          Tools          Search         External
                                       Services
            └──────────────┼──────────────┘
                           ↓
                     Verification
                           │
                           ↓
                 Evidence / Observability
                           │
                           ↓
                    GitHub / Storage
                           │
                           ↓
                       Evolution
```

這是一個目標架構，不代表第一天全部建立。

---

# 4. API 版本仍然遵守「大架構、小運行」

API 增加自動化後，最大的風險反而是：

> 自動化把原本不存在的複雜度全部帶進來。

因此 API 版本仍然遵守：

- 最小充分上下文。
- 最小有效複雜度。
- 需求驅動自動化。
- 可觀測。
- 可驗證。
- 可回滾。
- 人工可以介入。
- 核心資料可以脫離 Runtime 使用。

---

# 5. API 版本新增的主要能力

可以分為：

## 5.1 Retrieval

自動搜尋知識。

## 5.2 Context Assembly

自動組裝任務需要的最小充分上下文。

## 5.3 Tool Execution

讓 GPT 呼叫外部工具。

## 5.4 Runtime

管理任務狀態與執行。

## 5.5 Background Worker

處理長時間工作。

## 5.6 Event System

接收事件並觸發工作。

## 5.7 Scheduler

執行定時任務。

## 5.8 Verification

自動檢查結果。

## 5.9 Observability

記錄執行軌跡、成本、錯誤與效能。

## 5.10 Evolution

根據實際使用資料發現系統問題。

---

# 6. API 不應直接成為核心依賴

一個重要原則：

> Repository 中的核心資料必須能在沒有 Runtime 的情況下被理解。

例如：

- 知識不能只能由 API Database 讀懂。
- 系統定義不能只存在程式碼。
- 方案不能只存在 Agent Prompt。
- 重要決策不能只存在 Vector DB。
- 交接不能依賴某個常駐 Agent。

GitHub 仍應保存 canonical source。

API 系統是：

> 執行層與加速層。

---

# 7. 知識庫自動化

無 API：

```
GPT
↓
GitHub Search
↓
GPT 判斷
```

API：

```
使用者任務
↓
Intent
↓
Query Generation
↓
Keyword Search
+
Semantic Search
+
Metadata Filter
↓
Reranking
↓
Evidence Check
↓
Context Assembly
```

---

# 8. Hybrid Search

不應只使用 Vector Search。

建議：

```
Keyword / BM25
+
Embedding / Semantic Search
+
Metadata Filter
+
Relationship Graph
```

原因：

### Keyword Search

適合：

- 專有名詞。
- ID。
- 文件名稱。
- 精確詞。
- 版本號。

### Semantic Search

適合：

- 同義表達。
- 自然語言。
- 使用者沒有使用正式名稱的情況。

### Metadata Filter

適合：

- 狀態。
- 類型。
- 版本。
- 時間。
- 專案。
- 適用範圍。

### Relationship

適合：

- 某系統依賴哪些知識。
- 某方案涉及哪些系統。
- 某知識取代哪些舊知識。

---

# 9. Embedding

Embedding 的用途是：

> 把語義相近內容映射到可搜尋的向量空間。

但不能把 Embedding 當成知識本體。

Vector Index 屬於：

> 派生資料 Derived Data。

Canonical source 仍然是原始知識。

因此：

```
Markdown / JSON
       ↓
Embedding
       ↓
Vector Index
```

如果 Vector Index 損壞：

```
重新建立
↓
恢復
```

不能因為 Vector DB 壞掉就失去知識。

---

# 10. Index Lifecycle

任何自動索引都需要：

```
建立
↓
更新
↓
驗證
↓
失效偵測
↓
重建
```

不能假設索引永遠正確。

需要處理：

- 文件刪除。
- 文件修改。
- 版本更新。
- 狀態變更。
- 分類變更。
- Metadata 變更。

---

# 11. Reranking

初次搜尋得到的是：

> Candidate Set。

不能直接全部送進 GPT。

應：

```
候選
↓
相關性排序
↓
狀態檢查
↓
來源品質
↓
衝突檢查
↓
最小充分集合
```

這可以降低 Context 污染。

---

# 12. Context Assembly

這是 API 版本最重要的能力之一。

目標不是：

> 找到最多資料。

而是：

> 找到完成任務所需的最少正確資料。

輸入：

```
Task
Intent
System
Plan
Constraints
```

輸出：

```
Context Package
```

可以包含：

- 必要知識。
- 系統定義。
- 方案規則。
- 當前狀態。
- 相關證據。
- 必要歷史。

---

# 13. Context Package

未來可標準化為：

```json
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
```

這不是最終 Schema，只是概念模型。

---

# 14. System Registry

系統註冊表可以從 Markdown 索引逐步演化為：

```
System ID
Name
Purpose
Capabilities
Inputs
Outputs
Dependencies
Knowledge Dependencies
Plan
Triggers
Permissions
Verification
Version
Status
Health
Owner
Runtime
```

其中：

> Runtime metadata 不應污染系統本體定義。

---

# 15. Capability Registry

API 版本可以增加：

> 「現在到底能做什麼？」

例如：

```
search_repository
search_web
read_file
write_file
create_issue
run_test
run_python
call_model
generate_embedding
query_vector
send_notification
```

每個 Capability 可以描述：

- 名稱。
- 功能。
- 輸入。
- 輸出。
- 權限。
- 成本。
- 風險。
- Timeout。
- 驗證方式。

---

# 16. Trigger System

API 版本的 Trigger 不再只是關鍵詞表。

可以接收：

```
User Message
GitHub Event
Webhook
Schedule
File Change
Test Failure
System Health Alert
External Event
```

然後轉換成：

```
Event
↓
Intent / Event Classification
↓
Policy
↓
System
↓
Task
```

---

# 17. Event Schema

所有自動觸發事件應盡量標準化。

概念：

```json
{
  "event_id": "...",
  "event_type": "...",
  "source": "...",
  "timestamp": "...",
  "payload": {},
  "priority": "...",
  "correlation_id": "..."
}
```

這可以讓不同來源的事件進入同一套控制流程。

---

# 18. Event 與 Intent 必須分開

兩者不是同一件事。

Event：

> 發生了什麼？

Intent：

> 這個事件／訊息想要完成什麼？

例如：

```
Event:
GitHub file changed

Intent:
重新建立知識索引
```

另一例：

```
Event:
使用者說「建立新的知識」

Intent:
CREATE_KNOWLEDGE
```

---

# 19. Scheduler

Scheduler 適合：

- 每日整理。
- 定期驗證。
- 索引健康檢查。
- 研究更新。
- 備份。
- 報告。

但：

> Scheduler 只負責「什麼時候觸發」，不負責「應該做什麼」。

所以：

```
Scheduler
↓
Event
↓
Router
↓
System
```

---

# 20. Background Worker

長時間任務不應佔住主要對話。

例如：

- 大量文件索引。
- Embedding。
- 大型測試。
- 批量研究。
- 長時間資料整理。

流程：

```
GPT 建立 Task
↓
Queue
↓
Worker
↓
執行
↓
保存結果
↓
通知
```

---

# 21. Task Runtime

每一個大型工作應有 Task ID。

例如：

```
TASK-2026-001
```

狀態：

```
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
```

異常：

```
FAILED
BLOCKED
CANCELLED
ROLLED_BACK
```

---

# 22. Task State

Task State 不等於知識。

它保存：

- 任務目標。
- 當前步驟。
- 已完成工作。
- 下一步。
- 失敗原因。
- 重試次數。
- 產出位置。
- 驗證狀態。

這使長時間工作可以恢復。

---

# 23. Agent Runtime

Agent Runtime 負責：

- 任務上下文。
- Tool 調用。
- 狀態。
- 權限。
- Timeout。
- Retry。
- Memory。
- Verification。
- Failure handling。

它不是另一個「大腦」。

模型仍是推理核心。

Runtime 是：

> 讓模型可靠工作的環境。

---

# 24. Harness

成熟 API 版本應逐步形成 Harness。

Harness 管理：

- 任務規格。
- Context。
- Tools。
- 權限。
- 狀態。
- 記憶。
- 驗證。
- Observability。
- 失敗歸因。
- 成本。
- 介入。

核心概念：

```
Model capability
+
Harness
+
Environment
=
實際 Agent 能力
```

---

# 25. Tool Layer

工具應標準化。

例如：

```
Repository Tool
Search Tool
Web Tool
File Tool
Code Tool
Database Tool
Notification Tool
Model Tool
Test Tool
```

每個 Tool 應具備：

- Schema。
- Permission。
- Timeout。
- Error format。
- Retry policy。
- Audit log。

---

# 26. 權限

API 自動化後，權限會成為重要問題。

至少區分：

```
READ
SEARCH
CREATE
UPDATE
DELETE
EXECUTE
ADMIN
```

高風險操作應要求額外條件。

例如：

- 大量刪除。
- Repository 結構變更。
- 正式部署。
- 外部服務付費。
- 敏感資料操作。

---

# 27. 人工介入

AI 自動化不是「完全不需要人」。

應保留 Human Gate。

例如：

```
低風險
→ 自動

中風險
→ AI 執行 + 驗證

高風險
→ AI 提案 → 人確認 → 執行
```

人力應集中在：

> 高價值、高風險、不可逆決策。

---

# 28. Verification Pipeline

API 版本應把驗證從「最後人工檢查」變成流程的一部分。

```
Execute
↓
Result Validation
↓
Behavior Validation
↓
Regression
↓
Architecture Check
↓
Evidence
```

---

# 29. 三層驗證

仍維持三層：

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

# 30. Evaluation

不能只依賴一次 AI 自評。

應建立：

- Regression Cases。
- Behavioral Tests。
- Outcome Tests。
- Golden Cases。
- Failure Cases。
- Handoff Tests。

簡單任務可用嚴格 assertion。

複雜任務可使用 outcome-based evaluation。

---

# 31. Episode / Trace

每個重要 Agent Task 可以產生：

```
Task
↓
Context
↓
Tool Calls
↓
Model Decisions
↓
Outputs
↓
Verification
↓
Final Result
```

形成 Trace。

用途：

- Debug。
- 成本分析。
- 品質分析。
- 回歸。
- 系統改善。
- Failure Attribution。

---

# 32. Observability

至少觀察：

- 任務成功率。
- 任務失敗率。
- 平均耗時。
- Tool 錯誤。
- Retry 次數。
- Context 大小。
- Token 使用。
- API 成本。
- Retrieval 命中率。
- Retrieval 錯誤率。
- Verification 失敗率。
- Human Intervention Rate。

---

# 33. 成本模型

API 版本開始出現真實金錢成本。

因此需要：

```
Cost
=
Model
+
Embedding
+
Search
+
Storage
+
Compute
+
Network
```

任務應能知道：

> 「這次工作花了多少資源？」

---

# 34. Token Budget

不能因為 API 可以大量呼叫，就無限制把資料送給模型。

每個任務可以有：

```
Context Budget
Reasoning Budget
Tool Budget
Time Budget
Cost Budget
```

超過限制：

- 壓縮。
- 分批。
- 降低模型。
- 延後。
- 要求人工決策。

---

# 35. Model Routing

未來不應所有事情都使用最大模型。

例如：

```
簡單分類
→ 小模型

一般整理
→ 中型模型

複雜推理
→ 高階模型

高風險決策
→ 高階模型 + 驗證 + Human Gate
```

因此 Intent Router 同時可以成為：

> Model Router。

---

# 36. Cascade Architecture

理想流程：

```
Cheap Signal
↓
Cheap Classifier
↓
Semantic Router
↓
必要時大型推理
```

只有不確定或高價值任務才使用昂貴模型。

---

# 37. Memory Architecture

API 版本可以建立分層記憶：

```
Working Memory
Short-term Task State
Long-term Knowledge
Project Memory
Historical Memory
Derived Index
```

其中：

> Memory 與 Knowledge 不完全相同。

Memory 保存：

> 發生過什麼、目前進度是什麼。

Knowledge 保存：

> 可重複使用的理解。

---

# 38. GitHub 與 Database

API 版本可以增加 Database，但不能讓 Database 自動取代 GitHub。

建議：

### GitHub

Canonical durable artifacts：

- 知識。
- 系統定義。
- 方案。
- 規則。
- 架構。
- 交接。
- 重要證據。

### Database

Operational state：

- Task。
- Job。
- Queue。
- Runtime。
- Metrics。
- Cache。
- Index metadata。

### Vector Store

Derived retrieval data：

- Embeddings。
- Vector index。
- Semantic retrieval metadata。

三者責任分開。

---

# 39. Cache

Cache 可以降低：

- API 成本。
- Retrieval 成本。
- 重複計算。

但 Cache 必須有：

- TTL。
- Version。
- Invalidation。
- Source reference。

不能把 Cache 當成永久真相。

---

# 40. Knowledge Graph

當系統規模變大，可以增加關係圖：

```
Knowledge
↓
depends_on
↓
System
↓
part_of
↓
Plan
↓
triggered_by
↓
Event
```

但不應一開始就建立複雜 Graph Database。

先從：

- ID。
- Reference。
- Relation fields。

開始。

---

# 41. 自動索引

未來 GitHub 文件變更可以觸發：

```
File Changed
↓
Parse
↓
Metadata
↓
Embedding
↓
Index Update
↓
Validation
```

如果索引失敗：

```
Index Failure
↓
Alert
↓
Retry
↓
Fallback
```

不能默默失敗。

---

# 42. 自動交接

成熟 Runtime 可以在重要任務結束時自動產生：

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

正式狀態仍需要治理規則。

---

# 43. 自動研究

未來可以建立：

```
問題
↓
Research Planner
↓
Search
↓
Source Collection
↓
Evidence Extraction
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
```

研究結果與正式知識仍應分離。

---

# 44. 外部資料的證據層級

研究資料可以區分：

```
Primary Source
Secondary Source
Expert Analysis
Community Discussion
Model Inference
Unverified
```

避免：

> 搜到的東西全部視為事實。

---

# 45. 自動化不能取代治理

API 可以自動：

- 搜尋。
- 索引。
- 執行。
- 測試。
- 產生報告。

但是不能因此自動決定：

> 「這一定應該成為正式架構。」

正式採用仍需要：

```
證據
+
反例
+
風險
+
相容性
+
使用者決策
```

---

# 46. 事件驅動架構

成熟版本可能：

```
GitHub
  │
  ├── File Change
  ├── PR
  └── Issue
        ↓
      Event Bus
        ↓
    Event Router
        ↓
      Policy
        ↓
      Task
        ↓
     Worker
```

但這應在確定有大量背景任務後再建立。

---

# 47. Self-Healing 的限制

未來可以自動：

- Retry。
- Re-index。
- Restart Worker。
- Rollback。
- Re-run Test。

但不應直接：

> AI 發現架構有問題 → 自動重寫核心架構。

高風險演化仍應進入治理流程。

---

# 48. Self-Improvement

系統可以從實際資料找出：

- 常見失敗。
- 常見誤觸發。
- 常見搜尋失敗。
- Context 過大。
- 重複研究。
- Tool 錯誤。
- Verification 失敗。

然後形成：

```
Observation
↓
Problem Candidate
↓
Analysis
↓
Improvement Proposal
↓
Human Confirmation
↓
Implementation
↓
Regression
```

這比讓 AI 自己無限制改自己安全。

---

# 49. 系統熵控制

API 版本會讓資料產生速度大幅提高。

因此 Plan 4 的重要性反而提高。

可能需要自動偵測：

- 相似系統。
- 重複知識。
- 重複規則。
- Dead Systems。
- Dead Index。
- Stale Knowledge。
- Dependency Explosion。
- Context Explosion。

但自動偵測的結果仍然只是：

> Candidate。

不是自動刪除。

---

# 50. AI Harness 與四方案

四方案與 Harness 可以形成互補：

### 方案一

治理資料語義。

### 方案二

治理 AI 如何使用知識與能力。

### 方案三

治理知識與資料如何演化。

### 方案四

治理能力如何蒸餾與重構。

### Harness

提供：

- Runtime。
- Tools。
- Context。
- State。
- Verification。
- Observability。

因此 Harness 不是第五方案。

它是：

> 讓四方案可以在實際 AI Runtime 中運作的執行環境。

---

# 51. AI-Native SDLC

API 版本可以借鑑 AI-native software engineering：

```
Goal
↓
Specification
↓
Context
↓
Implementation
↓
Tests
↓
Evaluation
↓
Review
↓
Merge
↓
Observation
↓
Evolution
```

但不能照搬大型公司的組織流程。

單人工作室需要更低摩擦。

---

# 52. 人類角色重新定位

AI 能力提高後，使用者不應成為：

> 每一步都手動批准的操作員。

更合理的是：

```
方向
↓
規則
↓
高風險決策
↓
例外
↓
重大架構
```

AI 負責：

```
搜尋
整理
執行
測試
監控
報告
```

---

# 53. Human Bandwidth

長期瓶頸可能從：

> AI 能不能做？

變成：

> 人能不能審完 AI 做出的所有東西？

因此系統應優先提高：

- 自動驗證。
- Evidence。
- Trace。
- Regression。
- Metrics。
- Failure Classification。

讓使用者看到：

> 哪裡需要我決定。

而不是：

> 所有細節都丟給我。

---

# 54. API 升級順序

不建議一次全部建立。

建議：

## Level 1

API + GitHub。

## Level 2

Repository 自動搜尋。

## Level 3

Metadata / Index。

## Level 4

Embedding + Hybrid Search。

## Level 5

Context Assembly。

## Level 6

Tool Runtime。

## Level 7

Verification。

## Level 8

Observability。

## Level 9

Background Worker。

## Level 10

Event / Scheduler。

## Level 11

Advanced Agent Runtime。

## Level 12

自動演化輔助。

---

# 55. 每一級的升級條件

不是時間到了就升級。

必須存在：

```
實際瓶頸
↓
重複出現
↓
成本可量化
↓
自動化收益
>
維護成本
```

才進入下一級。

---

# 56. API 版本的最低可行形態

取得 API 後，第一版不需要：

- Multi-Agent。
- Event Bus。
- Scheduler。
- Vector DB。
- Graph DB。
- Worker Cluster。

最小形態：

```
GPT API
+
GitHub API
+
簡單 Task Runtime
+
簡單 Search
+
基本 Verification
```

先證明自動化有價值。

---

# 57. 第一個真正值得自動化的環節

優先候選通常是：

> Retrieval + Context Assembly。

原因：

它會反覆發生，而且直接影響 GPT 工作效率。

第二層：

> Verification。

第三層：

> Repetitive Tool Execution。

最後才是：

> Background Event System / Multi-Agent。

---

# 58. API 版本的風險

主要風險：

### 1. 自動化過度

系統比工作還複雜。

### 2. Retrieval 錯誤

AI 得到錯誤上下文。

### 3. Index Drift

索引與原始資料不一致。

### 4. Runtime State Drift

執行狀態與 Repository 不一致。

### 5. Agent Loop

AI 不斷重試卻沒有實質進展。

### 6. Cost Explosion

任務數量增加造成 API 成本暴增。

### 7. Permission Failure

AI 執行不該執行的操作。

### 8. Silent Failure

背景任務失敗但沒有人知道。

---

# 59. API 版本的安全原則

任何自動化都應：

```
可觀測
+
可限制
+
可停止
+
可回滾
+
可追蹤
```

高風險任務再加：

```
Human Gate
```

---

# 60. 成功判準

API 版本成立後，應能證明：

1. GPT 不需要每次重新讀完整 Repository。
2. Retrieval 可以找到正確資料。
3. Context Assembly 能降低無關上下文。
4. Tool 執行可追蹤。
5. 長任務可以恢復。
6. Verification 可以自動執行。
7. 失敗可以定位。
8. API 成本可以觀察。
9. Human Gate 可以控制高風險操作。
10. GitHub 仍然可以作為長期資料來源。
11. Runtime 損壞不會摧毀核心知識。
12. 新 GPT 可以繼續接手。

---

# 61. 失敗判準

如果出現：

- 自動化比人工更慢。
- Retrieval 常常錯。
- Context 反而更大。
- Agent 不斷循環。
- Background Task 經常失敗。
- 成本無法解釋。
- Runtime 變成新的單點故障。
- GPT 無法理解 GitHub 上的 canonical data。
- API 系統開始取代資料治理。
- 使用者花更多時間維護 AI 基礎設施。

則應停止擴張，回到無 API 核心架構重新檢查。

---

# 62. 無 API 與 API 的關係

最重要的兼容關係：

```
無 API
=
人工執行同一套語義

API
=
自動執行同一套語義
```

例如：

無 API：

```
GPT 手動搜尋知識
```

API：

```
Retrieval Service 搜尋知識
```

無 API：

```
GPT 手動判斷任務
```

API：

```
Intent Router 協助判斷
```

無 API：

```
GPT 手動驗證
```

API：

```
Evaluation Pipeline 自動驗證
```

因此 API 不是重新發明流程。

---

# 63. 最終成熟形態

理想狀態：

```
                  使用者
                     │
                     ↓
              Interaction Layer
                     │
                     ↓
                Intent Router
                     │
                     ↓
                Control Plane
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   Knowledge      Systems       Plans
    Library       Registry      Registry
        │            │            │
        └────────────┼────────────┘
                     ↓
               Context Engine
                     │
                     ↓
                  Planner
                     │
                     ↓
                Agent Runtime
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
        Tools     Search      Models
          │          │          │
          └──────────┼──────────┘
                     ↓
                Verification
                     │
                     ↓
             Observability
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
       GitHub                Runtime DB
       Canonical             Operational
          │                     │
          └──────────┬──────────┘
                     ↓
                  Evolution
```

---

# 64. 最終原則

整個 API 版本可以濃縮成十條：

1. GitHub 保存長期真相。
2. Database 保存運行狀態。
3. Vector Store 保存派生索引。
4. GPT 負責理解與推理。
5. Runtime 負責讓 GPT 可靠執行。
6. Retrieval 負責找到正確上下文。
7. Verification 負責確認結果。
8. Observability 負責知道系統發生什麼。
9. Governance 負責決定什麼可以改。
10. Human 負責方向與高價值決策。

---

# 65. 文件狀態

目前狀態：

**【未來規畫／企劃書／API 版本／討論稿】**

本文件不是：

- 現行工程方案。
- 第五方案。
- 已完成架構。
- 已驗收功能。
- 立即實作規格。

正式進入實作前仍應：

```
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
```

---

# 66. 與無 API 版本的最終關係

兩份文件應長期並存：

```
AI單人工作室整體系統企劃書-無API版本.md
AI單人工作室整體系統企劃書-API版本.md
```

無 API 版本回答：

> 「沒有 API 時，一個人如何建立可持續的 AI 工作環境？」

API 版本回答：

> 「有 API 與電腦執行環境後，如何把已證明有效的人工流程逐步自動化？」

兩者共同回答：

> 「如何讓一個人長期駕馭不斷增長的 AI 工作、知識、系統與專案，而不讓 AI 基礎設施本身變成新的負擔？」

