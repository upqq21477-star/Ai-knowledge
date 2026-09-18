
# AI 單人工作室整體系統企劃書
## 無 API 版本 v0.2

> 文件性質：未來整體規畫／企劃書
> 文件狀態：深度研究後候選版本／討論稿
> 適用環境：單人工作室、GPT／ChatGPT + GitHub、無 API
> 前版：AI單人工作室整體系統企劃書-無API版本-v0.1.md
> 重要界線：本文件不是現行四大方案之一，不取代現行工程架構，不代表已完成實作。

---

# 1. 核心結論

經過對目前 Repository、Git-backed AI memory、Claude Code、Cursor、Codex、ChatGPT + GitHub、Obsidian + MCP、NotebookLM 等方向的比對，本版作出一個重要修正：

> 無 API 版本不應繼續朝「完整 AI 管理平台」發展，而應收斂為「輕量、可攜式、可版本化的 AI 外部記憶與交接環境」。

最小核心：

~~~
使用者
  ↓
GPT
  │
  ├─ 讀入口
  ├─ 讀目前狀態
  ├─ 找相關資料
  ├─ 推理／工作
  ├─ 驗證
  └─ 保存成果
  ↓
GitHub
~~~

GitHub 保存長期真相；GPT 負責理解與推理；入口、索引、狀態文件負責降低重新理解成本。

---

# 2. 外部研究結論

## 2.1 Git-backed Markdown Memory 已經存在

已有工具直接採用 Git-backed Markdown 作為 AI memory 的 source of truth，資料可以人工編輯、grep、同步，資料庫只是可重建的 derived index，而且不要求 Vector Store 才能工作。另一類工具也使用 Git-synced Markdown knowledge base 管理跨 session、跨 Agent 的知識。這證明「Git + Markdown + AI memory」是已被實際採用的路線。citeturn2search6turn0search9

## 2.2 AI Coding Agent 已驗證 Repository Rules

Claude Code 使用 CLAUDE.md 作為專案記憶，並支援依目錄層級載入；Cursor 使用 Project Rules、AGENTS.md 等版本控制規則；Codex 使用 AGENTS.md 等 Repository instructions，並明確限制 Context 大小。共同方向都是：

> 少量、分層、可按需載入，而不是把全部歷史永久塞進模型 Context。citeturn2search3turn2search0turn2search4

## 2.3 ChatGPT + GitHub 已接近本系統的自然使用方式

OpenAI 現行 GitHub 整合可以按需檢索有權限的 Repository 內容，不要求使用者把整個 Repository 上傳到對話；官方也指出這種存取不是建立一份同步 GitHub index。citeturn3search0turn3search1

因此無 API 階段不需要自行建造一套重型 RAG 才能實現「AI 按需讀 Repository」。

## 2.4 Obsidian + MCP 類工具證明 Markdown + Search + AI 可行

現有工具已能直接讓 AI 讀寫 Markdown vault，並提供全文搜尋、metadata、backlinks、索引等能力。citeturn0search2turn0search7

但本系統不是單純筆記庫，而是知識、系統、方案、治理、狀態、交接的工程資料環境，因此不能直接照搬 Obsidian 架構。

---

# 3. 工具比對後的採用原則

| 工具／路線 | 值得採用 | 不直接採用 |
|---|---|---|
| Claude Code | 分層記憶、按需載入、Repository rules | coding-agent 專用架構 |
| Cursor | 小型 Rules、作用域、版本控制 | IDE 整體架構 |
| Codex | Context 上限、Repository instructions | 完整 runtime |
| NotebookLM | 來源範圍、以 source 為中心 | 作為工程治理核心 |
| Obsidian + MCP | Markdown、索引、人工可讀 | 提前建立完整 graph/server |
| Git-backed memory | Git + Markdown + derived index | 提前建立常駐 memory server |
| ChatGPT + GitHub | Repository 按需檢索 | 假設所有 AI 都有同等能力 |

核心共同點：

> 資料留在可攜式來源；AI 只在需要時取得相關 Context。

---

# 4. 對現有無 API 方案的重大修正

前版把：

- 圖書館
- 系統管理
- 觸發管理
- 事件管理
- 藍圖規劃
- 統御核心
- 翻譯／意圖層

描述得過於容易實體化。

本版規定：

> 「概念責任」不等於「必須建立獨立系統」。

例如「圖書館」可以只是一個目錄與索引責任，不需要一套圖書館軟體。

「Intent」可以只是 GPT 工作時的判斷方法，不需要大型 Intent Registry。

「統御」可以是工作原則，不需要常駐 Orchestrator。

這是為了防止：

> 治理系統本身開始產生大量治理文件。

---

# 5. 四層資料模型

無 API 版本只維持四個主要層級。

## 第一層：入口／狀態

回答：

> 現在是什麼狀態？

包含：

- 專案入口
- 當前狀態
- 核心規則
- 下一步
- 重要禁止事項

新 GPT 優先讀取。

## 第二層：能力

回答：

> 我們能做什麼？

包含：

- 系統
- 工作模式
- 方案索引
- 可用工具

只有實際使用、容易誤用或高風險能力才需要完整文件。

## 第三層：知識

回答：

> 需要知道什麼？

包含：

- 穩定知識
- 專案知識
- 研究結果
- 決策依據
- 外部證據

## 第四層：歷史

回答：

> 以前發生過什麼？

包含：

- 舊版本
- 測試
- 施工紀錄
- 舊決策
- 失敗案例

預設不進入工作 Context。

---

# 6. Context Loading Policy

新 GPT 不應一開始讀完整 Repository。

採用：

~~~
Level 0：入口
↓
Level 1：目前狀態
↓
Level 2：任務相關系統／方案
↓
Level 3：必要知識
↓
Level 4：證據／歷史
↓
Level 5：跨專案資料
~~~

原則：

> 除非有理由，不向下一層展開。

例如：

「方案四目前完成了嗎？」

只需要入口 + 目前狀態。

「方案四為什麼這樣設計？」

需要狀態 + 方案 + 相關決策。

「方案四是否符合業界方案？」

才需要 Repository + Web + 比較 + 反例。

---

# 7. 最小充分 Context

目標不是：

> 讓 GPT 讀越多越好。

而是：

> 讓 GPT 讀完成任務所需的最小充分資料。

因此：

~~~
Repository 很大
≠
每次 Context 很大
~~~

真正需要控制的是 Context Waste，而不是 Repository 文件總數。

---

# 8. 入口是第一級基礎設施

目前實際發生過入口引用漂移，因此入口穩定性必須成為無 API 版本的核心設計。

原則：

> 一個概念只保留一個 Canonical Location。

例如目前狀態只在一個正式位置定義，README、交接、方案文件只引用它。

不要讓：

~~~
README 一份
交接一份
規則一份
方案一份
目前狀態一份
~~~

同時維護同一個版本號。

---

# 9. CURRENT / PENDING / HISTORY

正式資料至少區分：

~~~
CURRENT
PENDING
HISTORY
DEPRECATED
~~~

含義：

- CURRENT：目前工作依據
- PENDING：尚未正式採用
- HISTORY：歷史，不作目前依據
- DEPRECATED：明確淘汰

新 GPT 預設：

~~~
CURRENT
+
必要 PENDING
~~~

只有追查原因、演化或失敗案例時才進入 HISTORY。

---

# 10. 知識原子化降級為「可獨立引用」

前版容易把原子化理解成「越碎越好」。

本版改成：

> 以可獨立理解、可獨立引用為目標，而不是以最短文字為目標。

一個知識單元可以是一段、一頁甚至完整文件，只要：

- 主題清楚
- 邊界清楚
- 狀態清楚
- 可以正確引用

就不需要為了原子化把 Repository 拆成大量碎片。

---

# 11. 知識生命週期

知識不是全部永久有效。

至少區分：

- 穩定定義
- 歷史事實
- 當前規則
- 時效性資料
- 專案決策
- 推論
- 未驗證假設

狀態可以：

~~~
ACTIVE
DEPRECATED
OBSOLETE
HISTORICAL
UNCERTAIN
CONTESTED
SUPERSEDED
~~~

過時資料不必刪除，因為歷史資料可以用於追溯與錯誤分析。

---

# 12. 圖書館重新定義

圖書館只需要完成三件事：

1. 知道有哪些資料。
2. 知道資料在哪裡。
3. 幫 GPT 找到可能相關資料。

第一階段可以只是：

~~~
知識/
系統/
方案/
目前狀態/
歷史/
入口
~~~

搭配一份短索引。

索引只需要：

~~~
ID
名稱
類型
用途
位置
狀態
關鍵詞
~~~

索引不是第二份知識庫。

---

# 13. 系統文件最小標準

系統只需要回答：

~~~
系統名稱
目的
何時使用
輸入
輸出
主要依賴
限制
驗證
~~~

如果一個系統兩三句即可說清楚，就不要為它建立十頁文件。

系統與知識的關係：

~~~
知識 = 知道什麼
系統 = 能做什麼
方案 = 如何解決問題
規則 = 必須遵守什麼
入口 = 到哪裡找
~~~

每種資料只回答自己的問題。

---

# 14. Intent 與 Trigger

無 API 沒有常駐 Listener。

因此：

~~~
Intent
=
GPT 對使用者目標的判斷
~~~

~~~
Trigger
=
遇到某種情況時應考慮某能力
~~~

不是自動執行器。

初期 Intent 只保留：

~~~
STATUS
LOOKUP
DISCUSS
RESEARCH
COMPARE
PLAN
CREATE
EDIT
VERIFY
EXECUTE
HANDOFF
~~~

實際誤判才增加。

這符合 Cursor 等工具「從實際重複錯誤逐步增加規則」的方向。citeturn2search2

---

# 15. 藍圖按任務規模啟動

### L0：直接回答

查單一資料或簡單問題。

### L1：查詢

需要定位 Repository 資料。

### L2：一般工作

需要簡單拆解。

### L3：研究／架構工作

Repository + Web + 比較 + 反例。

### L4：大型變更

完整藍圖 + 驗證 + 回歸 + 交接。

不是每個問題都啟動完整治理流程。

---

# 16. GitHub 的核心角色

GitHub 不只是儲存空間。

它同時提供：

- 長期保存
- 版本歷史
- Commit
- Diff
- Branch
- 權限
- 協作
- 可攜式檔案
- Repository archive
- 交接

GitHub 私有 Repository 可以限制存取；組織 Repository 還可使用 Read、Triage、Write、Maintain、Admin 等角色。citeturn1search0turn1search11

因此它很適合成為：

> AI 外部長期記憶 + 人工可讀工程資料。

---

# 17. 安全邊界

不能把：

> GitHub

理解成：

> 自動安全。

Private Repository 只是存取控制的一部分；仍需要強權限、MFA、定期審查等措施。citeturn1search6

本系統真正採用的是：

> 把資料集中在明確 Repository 邊界，並透過最小必要揭露降低不必要資料流動。

因此：

~~~
完整 Repository
↓
專案子集
↓
任務子集
↓
最小交接包
~~~

---

# 18. 交接包正式化

交接不等於把全部 Repository 丟給下一個 AI。

區分：

### Full Archive
完整備份。

### Project Package
單一專案。

### Task Package
單一任務。

### Handoff Package
讓下一個 AI 恢復工作所需的最小資料。

例如：

~~~
AI交接包/
├── 00-交接入口.md
├── 01-目前狀態.md
├── 02-核心規則.md
├── 03-系統索引.md
├── 04-目前方案.md
└── 05-必要知識/
~~~

GitHub API 本身也支援 Repository archive 下載，因此完整壓縮／攜帶是標準能力。citeturn1search12

---

# 19. AI 可攜性

正式長期資料應盡量使用：

- Markdown
- JSON／YAML metadata
- Git
- 普通檔案
- 明確 ID
- 明確狀態

避免核心記憶只存在：

- 某個 AI 的私人 Context
- 某家服務的 proprietary memory
- 不可重建的向量資料庫
- 單一 SaaS

這使：

~~~
GPT
Claude
Gemini
Codex
Cursor
其他 Agent
~~~

都可以使用相同的核心資料。

---

# 20. 399 份文件不等於過度工程化

Claude 的報告指出：

- 目前 Repository 約 399 份 Markdown。
- 2-方案／完善約 160 份。
- 58 項正式功能。
- FIELD 尚未形成。

這些是重要警訊，但：

> 文件總數本身不是失敗證據。

應區分：

~~~
399 files
≠
399 current files
≠
399 files loaded per task
≠
399 files maintained manually
~~~

真正應測量：

- Context Waste
- Retrieval Error
- Rework
- Maintenance Cost
- Handoff Success

如果 300 份是歷史資料，但新 GPT 每次只需要讀 3～8 份 CURRENT 文件，數量本身不是問題。

---

# 21. 160 份施工紀錄的處理

不要直接刪除。

流程：

~~~
施工紀錄
↓
標記歷史
↓
找出可重複規則
↓
蒸餾
↓
只有穩定規則進 CURRENT
~~~

不要：

~~~
160 份
↓
160 份摘要
↓
160 份摘要的摘要
~~~

否則只會增加資訊熵。

---

# 22. FIELD 的真正作用

目前 A1–D20 的模擬驗證仍有價值，但不能證明實際工作收益。

FIELD 應該很輕：

~~~
實際任務
↓
原本怎麼做
↓
哪裡卡住
↓
系統是否幫助
↓
是否節省 Context／時間
↓
是否產生新問題
~~~

不應為了 FIELD 製造假任務。

下一個自然的大型工作就是驗證機會。

---

# 23. 無 API 的核心成本

即使沒有 API 金錢成本，仍有：

~~~
Context
+
閱讀
+
搜尋
+
推理
+
等待
+
返工
+
治理
~~~

優化順序：

1. 減少重複閱讀。
2. 減少入口漂移。
3. 減少無關 Context。
4. 減少文件重複。
5. 減少不必要流程。
6. 最後才追求更複雜的搜尋演算法。

---

# 24. 目前不應建立

在沒有 FIELD 證據前，不建立：

1. 大型 Intent Registry
2. 自動 Event Router
3. Vector Database
4. Knowledge Graph
5. Agent Memory Server
6. Background Worker
7. Scheduler
8. 自動 Knowledge Distillation
9. 自動 Self-Healing
10. Multi-Agent 協調平台

不是因為這些技術沒有價值，而是：

> 尚未證明它們是目前瓶頸。

---

# 25. 無 API 最小可行架構

~~~
GitHub Repository
│
├── 00-入口
├── 目前狀態
├── 核心規則
├── 系統索引
├── 方案索引
├── 知識索引
├── 專案
└── 歷史
        │
        ↓
       GPT
        │
 ┌──────┼──────┐
 ↓      ↓      ↓
搜尋   推理   執行
        │
        ↓
      驗證
        │
        ↓
      GitHub
~~~

這是第一階段真正需要的核心。

---

# 26. API 升級關係

無 API：

~~~
GPT
+
GitHub
+
入口／索引／狀態
~~~

API：

~~~
GPT
+
GitHub
+
Client
+
Index
+
Context Engine
+
必要 Runtime
~~~

因此 API 不是重新設計資料。

而是：

> 把 FIELD 已證明值得自動化的人工工作交給程式。

例如：

無 API：
GPT 手動找資料。

API：
Client Search → GPT。

無 API：
GPT 手動檢查版本。

API：
Client 驗證。

無 API：
GPT 手動整理 Context。

API：
Context Builder。

---

# 27. 核心 KPI

不再使用「文件數量」作為主要 KPI。

### 交接時間
新 GPT 到可以正確工作的時間。

### Context Waste
讀取但沒有實際用途的內容比例。

### Retrieval Error
找錯 CURRENT、誤用 HISTORY 的次數。

### Rework
因知識庫錯誤造成的返工。

### Maintenance Cost
維護 AI 基礎設施所花時間。

### Handoff Success
新 GPT 是否能不依賴舊聊天繼續工作。

---

# 28. 成功判準

無 API 版本成功代表：

1. 新 GPT 能快速找到入口。
2. 能正確判斷 CURRENT。
3. 不會被 HISTORY 污染。
4. 能定位任務相關資料。
5. 不需要讀完整 Repository。
6. 不需要大量人工重新解釋。
7. 交接包可以跨 AI 使用。
8. 使用者維護成本沒有持續上升。
9. 真實工作效率沒有被治理系統拖慢。
10. API 未來可以在不改變資料語義的情況下接入。

---

# 29. 失敗判準

出現以下任一情況，就停止擴張並重新檢查：

- 新 GPT 必須讀大量文件才能工作。
- 同一資訊存在多個 CURRENT。
- README、交接、狀態文件互相矛盾。
- 規則文件比實際工作更複雜。
- 使用者花大量時間維護索引。
- 每次更新都要修改大量交叉引用。
- 新增治理系統比解決實際問題更常發生。
- 模擬測試很多，但真實工作沒有改善。

---

# 30. 後續工程順序

## 第一階段
驗證目前 Repository 是否能讓新 GPT 快速接手。

## 第二階段
找出真正 Context Waste、入口漂移與 Retrieval Error。

## 第三階段
只修正實際造成問題的結構。

## 第四階段
在自然工作中進行第一次 FIELD。

## 第五階段
從 FIELD 蒸餾真正有效的規則。

## 第六階段
正式決定哪些內容進入無 API 工程架構。

---

# 31. 最終原則

整套無 API 版本濃縮為：

> **GitHub 保存，GPT 理解；入口導航，狀態定錨；索引找路，歷史退後；實際痛點才增加系統。**

再進一步：

> **不要建立一個管理 AI 的巨大系統；建立一個 AI 可以長期理解、使用、驗證、交接的資料環境。**

---

# 32. 文件狀態

**【未來規畫／企劃書／無 API 版本 v0.2／深度研究後候選稿】**

本版主要修正：

- 降低「完整 AI 平台」傾向。
- 強化 GitHub 外部記憶定位。
- 強化入口與狀態的唯一真相。
- 導入分層、按需載入。
- 降低原子化知識的強制程度。
- 正式區分 CURRENT / PENDING / HISTORY。
- 正式區分 Full Archive / Project Package / Task Package / Handoff Package。
- 將 AI 可攜性列為核心非功能需求。
- 不以文件數量判斷過度工程化。
- 將 Context Waste、Retrieval Error、Rework、Maintenance Cost、Handoff Success 作為核心 KPI。
- FIELD 以自然工作為主，不製造假任務。
- 未經 FIELD 證明，不提前增加 Vector DB、Graph、Worker、Scheduler、Multi-Agent 等基礎設施。

本文件仍不是：

- 現行工程方案。
- 第五方案。
- 已完成架構。
- 已驗收功能。
- 立即實作規格。
