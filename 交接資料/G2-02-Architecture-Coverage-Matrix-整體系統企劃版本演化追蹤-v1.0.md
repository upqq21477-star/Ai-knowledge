# G2-02 Architecture Coverage Matrix：整體系統企劃版本演化追蹤

日期：2026-09-18
狀態：【G2-02 COMPLETE】
工程：AI 單人工作室主系統資料基線重建
Repository：upqq21477-star/Ai-knowledge

## 一、任務目的

本文件追蹤：

API v0.1
→ 無 API v0.1
→ 無 API v0.2
→ 無 API v0.3（檔名雖如此，文件內標題仍為 v0.2，後段另有「v0.3 修訂核心」）
→ 現行工程架構

目的不是選出「最新文件」，而是確認每一階段提出了什麼、哪些內容被後續吸收、哪些只是候選設計，以及哪些內容目前不能升格為 CURRENT。

本文件是 Derived Architecture Evidence，不是 Canonical Source。

## 二、實際文件狀態

| 階段 | Repository 文件 | 文件內狀態 | 本次判定 |
|---|---|---|---|
| API v0.1 | AI單人工作室整體系統企劃書-API版本-v0.1.md | 文件內標示 API 版本 v0.2；未來整體規畫／討論稿 | 歷史／候選架構研究 |
| 無 API v0.1 | AI單人工作室整體系統企劃書-無API版本-v0.1.md | 討論稿、未來規畫 | 歷史／候選架構研究 |
| 無 API v0.2 | AI單人工作室整體系統企劃書-無API版本-v0.2.md | 深度研究後候選版本／討論稿 | 歷史／候選架構研究 |
| 無 API v0.3 | AI單人工作室整體系統企劃書-無API版本-v0.3.md | 檔名 v0.3，但文件標題／前段仍標 v0.2，後段加入 v0.3 修訂核心 | 歷史／候選架構研究 |
| 現行工程 | 交接資料-v2.9.md、快照-005 等 | 正式工程運作；FIELD 待自然觸發 | CURRENT 工程狀態 |

重要：企劃書系列本身沒有證據可以直接取代現行工程狀態文件。

## 三、版本演化

### API v0.1

核心思想：

GitHub = Canonical Source / 長期資料中心

API / Client = 讀取、Index、Search、Cache、Validation、Context Assembly 等加速層

GPT = 語意理解、推理、規劃

主要提出：
- Index
- Search
- Cache
- Context Assembly
- Validation
- Capability Registry
- Intent Router
- Model Routing
- Event / Trigger
- Scheduler
- Worker
- Task Runtime
- Agent Runtime
- Tool Layer
- Permission
- Observability
- Evaluation

但文件同時明確規定 API 不是資料真相層，且完整 Runtime、Vector DB、Scheduler、Worker 等不應在第一版全部建立。

判定：形成「未來 API 升級方向」，不是目前已實作系統。

### 無 API v0.1

核心修正：

「今天就能工作的完整無 API 基礎架構，未來取得 API 後逐步自動化。」

主要形成：
- GitHub 作為長期資料與版本中心
- GPT 作為主要理解／推理核心
- 知識、系統、方案分層
- Library / 圖書館
- Intent
- Trigger
- Response Contract
- 統御核心
- Verification
- Evidence
- Artifact
- Current / History
- Handoff
- Context Control

重要原則：
「大架構，小運行」
「最小充分上下文」
「需求驅動自動化」

判定：完整概念模型，但仍屬未來規畫。

### 無 API v0.2

經外部工具與方法研究後，方向明顯收斂。

核心修正：
- 不再朝完整 AI 管理平台發展。
- 收斂為輕量、可攜式、可版本化的 AI 外部記憶與交接環境。
- 四層資料模型：入口／狀態、能力、知識、歷史。
- 強化 Current / History 分離。
- 強化唯一目前狀態入口。
- 知識原子化由「越小越好」降級為「可獨立引用」。
- Handoff Package 正式化。
- Context Loading Policy 形成。
- 以交接時間、Context Waste、Retrieval Error、Rework、Maintenance Cost、Handoff Success 作為 KPI。
- 不因技術可能性提前建立大型基礎設施。

判定：比 v0.1 更接近目前工程治理方向，但仍是候選企劃。

### 無 API v0.3

注意：Repository 檔名為 v0.3，但文件前段標題仍為「無 API 版本 v0.2」，後段另加入「v0.3 修訂核心」。因此不能把檔名直接視為完整版本真相。

v0.3 修訂核心進一步提出：
- 「完整概念模型 + 最小實體化 + 持續蒸餾」
- CURRENT 與 ARCHIVE 分離
- 歷史完整保留，但預設不進 Context
- 分離「資料本體／資料狀態／Context 載入層級」
- Canonical Source 唯一真相原則
- 大記憶、小 Context
- 完整能力、最小實體化
- 新系統必須經過實際使用 → Observation → 重複瓶頸 → 方案 → 壓力測試 → 確認 → 建立 → 回歸
- 無 API 階段暫不建立 Vector DB、Embedding Server、常駐 Memory Server、Agent Runtime、Event Bus、Scheduler、Worker、Multi-Agent Framework、大型 Intent Registry、Trigger Engine、Orchestrator
- 下一階段優先蒸餾，而不是繼續增加架構文件

判定：是目前「未來架構候選」中最成熟的版本，但仍不能直接標成 CURRENT。

## 四、Architecture Coverage Matrix

| 架構能力／概念 | API v0.1 | 無API v0.1 | 無API v0.2 | 無API v0.3修訂 | 現行工程是否已有對應 | CURRENT 判定 |
|---|---|---|---|---|---|---|
| GitHub 作為長期外部記憶 | ✓ | ✓ | ✓ | ✓ | ✓ | CURRENT |
| GitHub / Canonical Source 邊界 | ✓ | ✓ | ✓ | ✓強化 | ✓ | CURRENT 原則 |
| 知識／系統／方案分離 | ✓ | ✓ | ✓ | ✓ | ✓ | CURRENT |
| 目前狀態單一入口 | 部分 | ✓ | ✓強化 | ✓ | ✓ 快照-005 | CURRENT |
| CURRENT / HISTORY 分離 | ✓ | ✓ | ✓強化 | ✓強化 | ✓ | CURRENT |
| PENDING / 候選狀態 | 部分 | ✓ | ✓ | ✓ | ✓ 在治理流程中 | CURRENT 原則 |
| Archive / 歷史隔離 | ✓ | ✓ | ✓ | ✓強化 | ✓ 已開始實體化 | CURRENT 原則／施工中 |
| Handoff / Memoryless Handoff | ✓ | ✓ | ✓ | ✓ | ✓，已完成兩次回歸 | CURRENT 能力 |
| 最小充分 Context | ✓ | ✓ | ✓ | ✓強化 | ✓ | CURRENT 原則 |
| Library / Discovery | ✓ | ✓ | ✓ | ✓ | 有相關索引／入口能力 | CURRENT 候選／部分實體化 |
| No-API Retrieval | — | ✓ | ✓ | ✓ | GitHub + 搜尋 + 入口鏈 | CURRENT 工作方式 |
| API Retrieval | ✓ | 未使用 | 未使用 | 未使用 | 無證據 | 未建立 |
| Vector DB / Embedding | ✓候選 | 不建議 | 不建議 | 明確暫不建立 | 無 | NOT CURRENT |
| Agent Runtime | ✓後期候選 | 不建議 | 不建議 | 明確暫不建立 | 無 | NOT CURRENT |
| Event Bus / Scheduler / Worker | ✓後期候選 | 不建議 | 不建議 | 明確暫不建立 | 無 | NOT CURRENT |
| Multi-Agent Framework | ✓後期候選 | 不建議 | 不建議 | 明確暫不建立 | 無 | NOT CURRENT |
| Capability 導向架構 | ✓部分概念 | ✓部分 | ✓能力層 | ✓正式強化 | 四方案中已有能力蒸餾與能力 ID | CURRENT 原則／藍圖能力 |
| Capability Registry | ✓候選 | 概念 | 候選 | 未完成實體化 | 有 K/CAP Mapping，但非完整 Registry | CANDIDATE |
| Verification | ✓ | ✓ | ✓ | ✓ | 四方案與回歸已有 | CURRENT 能力 |
| Evidence / Provenance | ✓ | ✓ | ✓強化 | ✓ | 有 Evidence／研究／紀錄層 | CURRENT 能力／持續完善 |
| Artifact | ✓ | ✓ | ✓ | ✓ | Repository 文件即持久 Artifact | CURRENT 原則 |
| Context Loading Policy | ✓ | ✓ | ✓ | ✓強化 | 已有入口→狀態→任務相關資料流程 | CURRENT 原則 |
| Intent Router | ✓候選 | 概念 | 概念 | 保留但不實體化 | 無獨立 Router 證據 | CANDIDATE |
| Trigger Registry / Trigger | ✓ | ✓ | ✓ | ✓ | CAP-60 Trigger Registry 已確認 | CURRENT 能力 |
| Task Runtime | ✓後期 | 不建議 | 不建議 | 不建議 | 無 | NOT CURRENT |
| Observability / Cost Tracking | ✓ | KPI 概念 | KPI | KPI | 尚無完整 Runtime | CANDIDATE |
| 自動交接 | ✓ | Handoff | Package | Handoff / Recovery | 目前以文件式交接實現 | CURRENT 能力；自動化 NOT CURRENT |
| 自動研究 | ✓後期 | 概念 | 不作前置 | 不作前置 | 研究流程由人工/GPT 執行 | CURRENT 工作流程，非 Runtime |
| Self-Healing | ✓受限 | 受限 | 受限 | 受限 | Rollback / 驗證原則存在 | 原則 CURRENT，Runtime NOT CURRENT |
| FIELD 驅動升級 | ✓ | ✓ | ✓ | ✓強化 | FIELD 待自然觸發 | CURRENT 原則 |

## 五、最重要的演化結論

### 1. API v0.1 不是 CURRENT

它提供未來自動化的完整能力地圖，但大量能力是「未來可以建立」而不是「目前已建立」。

不能因為 API 版本功能最完整，就把它視為正式架構。

### 2. 無 API v0.1 是概念母體

它第一次把：
- Knowledge
- System
- Plan
- Library
- Intent
- Trigger
- Governance
- Verification
- Evidence
- Handoff
- Context

放入同一個整體模型。

### 3. v0.2 的主要價值是「反膨脹」

v0.2 開始明確限制：
「概念責任」不等於「必須建立獨立系統」。

這是後續 v0.3 與目前工程的重要轉折。

### 4. v0.3 的主要價值是「蒸餾 + 狀態 + Context 三維分離」

最重要的不是增加功能，而是停止把所有概念實體化。

形成：
資料本體
＋
資料狀態
＋
Context 載入層級

三者分離。

### 5. 現行工程並不是直接等於 v0.3

這是本次 G2-02 最重要的 State 判定。

現行工程有自己的 CURRENT 權威鏈：

README
→ 交接資料-v2.9
→ 快照-005
→ 目前狀態
→ 規則
→ 待辦
→ 工程運作與持續改進方案

而四方案 A1–A12、B1–B16、C1–C18、D1–D20 已完成模擬／回歸。

v0.3 是未來架構候選與蒸餾方向，不是現行工程狀態替代品。

## 六、目前 Architecture Coverage 的邊界

已確認的 CURRENT：
- GitHub 外部記憶與版本邊界
- Knowledge / System / Plan 分離
- Current State
- Current / History 分離
- Handoff
- Context 控制
- Verification
- Evidence
- 四方案治理
- FIELD 驅動升級原則
- Trigger Registry 等已正式確認能力

候選／待實體化：
- 完整 Capability Registry
- 完整 Library System
- Intent Router
- Observability / Cost Tracking
- 自動化 Handoff
- API Layer
- Embedding / Hybrid Retrieval

明確 NOT CURRENT：
- Vector Database
- 常駐 Memory Server
- Agent Runtime
- Event Bus
- Scheduler
- Worker
- Multi-Agent Framework
- 大型 Orchestrator

## 七、對後續 G2 的影響

G2-02 已完成「版本演化追蹤 + Architecture Coverage」。

下一步不能直接把 v0.3 全部實體化。

應進入：

**G2-03：追蹤「能力蒸餾與系統重構方案-v1.1」與 D1～D20、回歸結果、快照-005 的 State 關係。**

核心問題：

> v1.1 內部舊 State 是否與後續 D1～D20 完成證據衝突？

必須建立：
- Document State
- Execution State
- Verification Evidence
- Current State
四者的對照。

