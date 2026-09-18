# AI單人工作室全庫資產逐項清冊－第一輪

版本：v1.0
日期：2026-09-18
狀態：【G1 第一批建立；非全庫完成】
上位文件：AI單人工作室全庫資產盤點-第一輪-v1.0.md

## 一、用途

本文件開始把「全庫資產盤點」從結構層推進到文件級。

第一輪不追求一次列完所有文件，而是先建立統一欄位、確認資產類型與狀態判定方式，並把目前已由 Repository 搜尋直接確認的重要資產登錄。

未列入本批的文件不代表不存在，也不代表低優先；後續持續補掃。

## 二、欄位規則

| 欄位 | 意義 |
|---|---|
| Asset ID | 暫時識別碼；未正式註冊前使用 G1-XXX |
| 路徑 | Repository 實際路徑 |
| 類型 | Knowledge / System / Solution / Evidence / Research / Test / Handoff / State / Template / History 等 |
| Filename Version | 檔名版本 |
| Internal Version | 文件內標示版本 |
| State | 文件目前明示或初步判定狀態 |
| Canonical | 是否可能成為該語義的權威來源 |
| Relation | 前身／後繼／支撐／證據／研究等 |
| Conflict | 是否存在版本或狀態衝突 |
| Disposition | 暫定 KEEP / REVIEW / DISTILL / ARCHIVE 等 |
| Evidence | 判定依據 |

規則：Filename Version ≠ Internal Version ≠ State ≠ Git Commit。

## 三、目前工程權威入口

| Asset ID | 路徑 | 類型 | State | Canonical | Disposition |
|---|---|---|---|---|---|
| G1-001 | README.md | Handoff / Entry | CURRENT | 是 | KEEP |
| G1-002 | 交接資料-v2.9.md | Handoff | CURRENT | 是 | KEEP |
| G1-003 | 2-方案/完善/目前工程狀態快照-005.md | State | CURRENT | 是 | KEEP |
| G1-004 | 目前狀態.md | State / Overview | CURRENT | 高階總覽 | KEEP |
| G1-005 | 規則.md | Rule | CURRENT | 是 | KEEP |
| G1-006 | 待辦清單.md | State / Task | CURRENT | 是 | KEEP |
| G1-007 | 2-方案/工程運作與持續改進方案-v1.8.md | Solution / Engineering Governance | CURRENT | 是 | KEEP |

## 四、知識資產第一批

| Asset ID | 路徑 | 類型 | State | 初步處置 | 備註 |
|---|---|---|---|---|---|
| G1-010 | 0-知識/管理/方案管理原理.md | Knowledge / Principle | REVIEW | KEEP候選 | 已確認為管理原理層 |
| G1-011 | 0-知識/管理/系統目錄與觸發管理原理.md | Knowledge / Principle | REVIEW | KEEP候選 | 與觸發／目錄責任相關 |
| G1-012 | 0-知識/管理/觸發條件管理原理.md | Knowledge / Principle | REVIEW | KEEP候選 | 需與觸發系統對照 |
| G1-013 | 0-知識/管理/以證據決定架構.md | Knowledge / Principle | REVIEW | KEEP候選 | 架構決策原理 |
| G1-014 | 0-知識/系統/系統與知識關係.md | Knowledge / Principle | REVIEW | KEEP候選 | 系統／知識邊界原理 |
| G1-015 | 0-知識/系統/方案責任與協作介面原理.md | Knowledge / Principle | REVIEW | KEEP候選 | 多方案責任關係 |
| G1-016 | 0-知識/搜尋/資訊需求建立.md | Knowledge / Search | REVIEW | KEEP候選 | 搜尋工作前置能力 |
| G1-017 | 0-知識/搜尋/問題理解與研究問題定義.md | Knowledge / Search | REVIEW | KEEP候選 | 研究問題形成 |
| G1-018 | 0-知識/搜尋/查詢策略建立.md | Knowledge / Search | REVIEW | KEEP候選 | 搜尋策略 |
| G1-019 | 0-知識/搜尋/研究結果採用判斷原理.md | Knowledge / Evidence | REVIEW | KEEP候選 | 研究結果採用判定 |
| G1-020 | 0-知識/比較/知識比較原理.md | Knowledge / Comparison | REVIEW | KEEP候選 | 比較責任 |
| G1-021 | 0-知識/更新/知識更新原理.md | Knowledge / Evolution | REVIEW | KEEP候選 | 更新責任 |

## 五、系統資產第一批

| Asset ID | 路徑 | 類型 | State | 初步處置 | 備註 |
|---|---|---|---|---|---|
| G1-030 | 1-系統/方案管理系統.md | System | REVIEW | KEEP候選 | 需與方案管理原理對照 |
| G1-031 | 1-系統/知識更新與狀態管理系統.md | System | REVIEW | KEEP候選 | 狀態管理核心候選 |
| G1-032 | 1-系統/知識整合系統.md | System | REVIEW | KEEP候選 | 知識整合 |
| G1-033 | 1-系統/知識外部比對系統.md | System | REVIEW | KEEP候選 | 外部比較能力 |
| G1-034 | 1-系統/資料探索-外部比對.md | Evidence / Research | HISTORICAL候選 | DISTILL候選 | 文件責任需確認 |
| G1-035 | 1-系統/搜尋原理-外部比對.md | Evidence / Research | HISTORICAL候選 | DISTILL候選 | 外部研究資料 |
| G1-036 | 1-系統/問題解決系統-v1.0.md | System | REVIEW | KEEP候選 | 版本需與其他問題解決文件比較 |
| G1-037 | 1-系統/觸發條件管理系統-v1.0.md | System | REVIEW | KEEP候選 | 存在多版本，不能單靠檔名判定 |
| G1-038 | 1-系統/AI上下文與交接系統.md | System | CURRENT候選 | REVIEW | 與目前交接入口鏈直接相關 |
| G1-039 | 1-系統/系統管理統御分支-v1.0.md | System | REVIEW | KEEP候選 | 統御責任候選 |

## 六、方案資產第一批

| Asset ID | 路徑 | 類型 | Filename Version | Internal Version | State | Disposition |
|---|---|---|---|---|---|---|
| G1-050 | 2-方案/AI知識管理方案.md | Solution | 無 | 文件內早期版本 | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-051 | 2-方案/AI知識管理方案-v2.0.md | Solution | v2.0 | v2.1 | REVIEW | 不直接升格 |
| G1-052 | 2-方案/AI知識管理方案-v2.0完整規劃.md | Solution / Planning | v2.0 | — | HISTORICAL / CANDIDATE | ARCHIVE / EVIDENCE |
| G1-053 | 2-方案/AI知識管理方案-v2.0草案.md | Solution / Draft | v2.0 | — | REVIEW / DRAFT | ARCHIVE候選 |
| G1-054 | 2-方案/AI知識管理方案-第一輪驗證.md | Evidence / Test | — | — | HISTORICAL / EVIDENCE | RETAIN |
| G1-055 | 2-方案/AI知識管理方案-重大更新研究.md | Research / Candidate | — | — | RESEARCH / CANDIDATE | RETAIN |
| G1-056 | 2-方案/知識與資料迭代演化方案-v2.0.md | Solution | v2.0 | v2.1 | REVIEW | 不直接升格 |
| G1-057 | 2-方案/知識迭代與資料演化方案-v1.0.md | Solution | v1.0 | — | HISTORICAL | RETAIN / EVIDENCE |
| G1-058 | 2-方案/能力蒸餾與系統重構方案-v1.0.md | Solution | v1.0 | — | HISTORICAL / PREDECESSOR | RETAIN / EVIDENCE |
| G1-059 | 2-方案/能力蒸餾與系統重構方案-v1.1.md | Solution | v1.1 | v1.1 | REVIEW / STATE-CONFLICT | 不處置 |
| G1-060 | 2-方案/搜尋研究方案.md | Solution | 無 | — | REVIEW | KEEP候選 |
| G1-061 | 2-方案/搜尋研究方案-系統成立性審查.md | Research / Review | — | — | EVIDENCE / REVIEW | RETAIN |
| G1-062 | 2-方案/搜尋研究方案-功能13-16知識盤點.md | Research / Inventory | — | — | REVIEW | RETAIN |
| G1-063 | 2-方案/整體系統更新方案.md | Solution | 無 | — | REVIEW | KEEP候選 |
| G1-064 | 2-方案/正確成立方案與系統方案-v2.0.md | Engineering Evidence | v2.0 | — | HISTORICAL | RETAIN / EVIDENCE |

## 七、完善／驗證資產第一批

| Asset ID | 路徑 | 類型 | State | Disposition |
|---|---|---|---|---|
| G1-070 | 2-方案/完善/方案四系統能力級真實蒸餾案例-001.md | Test / Evidence | REVIEW | 高優先檢查 |
| G1-071 | 2-方案/完善/方案三正常變更流程模擬驗證-001.md | Test / Evidence | HISTORICAL / EVIDENCE候選 | RETAIN |
| G1-072 | 2-方案/完善/四方案創建施工總規劃-v1.0.md | Engineering Evidence | HISTORICAL | RETAIN |
| G1-073 | 2-方案/完善/四方案逐項功能研究-017-D17至D20.md | Research / Evidence | HISTORICAL / EVIDENCE候選 | RETAIN |
| G1-074 | 2-方案/完善/方案四共同能力分析-001.md | Research / Capability Analysis | REVIEW | RETAIN |
| G1-075 | 2-方案/完善/候選系統能力既有能力重疊比對-v1.0.md | Comparison / Evidence | REVIEW | RETAIN |
| G1-076 | 2-方案/完善/跨 AI 交接模擬驗證-001.md | Test / Handoff | HISTORICAL / EVIDENCE候選 | RETAIN |
| G1-077 | 2-方案/完善/工程交接四情境失憶測試-001.md | Test / Handoff | HISTORICAL / EVIDENCE候選 | RETAIN |
| G1-078 | 2-方案/完善/目前工程狀態快照-001.md | State / History | HISTORICAL | ARCHIVE候選 |
| G1-079 | 2-方案/完善/目前工程狀態快照-002.md | State / History | HISTORICAL | ARCHIVE候選 |
| G1-080 | 2-方案/完善/目前工程狀態快照-003.md | State / History | HISTORICAL | ARCHIVE候選 |
| G1-081 | 2-方案/完善/目前工程狀態快照-004.md | State / History | HISTORICAL | ARCHIVE候選 |
| G1-082 | 2-方案/完善/目前工程狀態快照-005.md | State | CURRENT | KEEP | 唯一目前工程游標 |

## 八、根目錄企劃與藍圖資產

| Asset ID | 路徑 | 類型 | State | Disposition |
|---|---|---|---|---|
| G1-090 | AI單人工作室整體系統企劃書-無API版本-v0.1.md | Planning | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-091 | AI單人工作室整體系統企劃書-無API版本-v0.2.md | Planning | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-092 | AI單人工作室整體系統企劃書-無API版本-v0.3.md | Planning | REVIEW / HISTORY候選 | RETAIN |
| G1-093 | AI單人工作室整體系統企劃書-API版本-v0.1.md | Planning | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-094 | AI單人工作室主系統資料基線重建規範-v1.0.md | Rule / Engineering Spec | CURRENT候選 | KEEP |
| G1-095 | AI單人工作室全庫資產盤點-第一輪-v1.0.md | Inventory | CURRENT | KEEP | 本文件上位盤點 |
| G1-096 | AI單人工作室未來藍圖待辦清單-v1.0.md | Planning / TODO | CURRENT候選 | KEEP | 未來藍圖，不是第五方案 |
| G1-097 | AI單人工作室未來藍圖規劃書-功能導向架構-v1.0.md | Planning / Architecture | CURRENT候選 | KEEP | 長期能力框架 |
| G1-098 | AI單人工作室功能導向藍圖地圖-既有資產完整Mapping-v1.0.md | Derived View / Mapping | CURRENT候選 | KEEP | 非 Canonical Source |
| G1-099 | AI單人工作室功能導向藍圖交接入口-v1.0.md | Handoff / Entry | CURRENT候選 | KEEP | 未來藍圖入口 |

## 九、目前確定的判定

### 已可直接確認 CURRENT
- README.md
- 交接資料-v2.9.md
- 目前工程狀態快照-005.md
- 目前狀態.md
- 規則.md
- 待辦清單.md
- 工程運作與持續改進方案-v1.8.md

### 已確認存在但不可直接升格 CURRENT
- 能力蒸餾與系統重構方案-v1.1.md
- AI知識管理方案-v2.0.md
- 知識與資料迭代演化方案-v2.0.md
- 各類草案／研究／完整規劃文件

### 已確認屬歷史或證據價值較高
- 舊交接
- 舊快照
- 第一輪驗證
- 四方案創建施工總規劃
- 正確成立方案與系統方案
- 研究會議與外部比對資料

## 十、下一輪 G1

本文件目前只完成第一批。

下一批優先順序：
1. 0-知識 全量逐文件掃描
2. 1-系統 全量逐文件掃描
3. 2-方案 根目錄全量掃描
4. 2-方案/完善 文件責任分類
5. 討論／研究／會議資料
6. 根目錄其他企劃、模板與工具資料

完成 G1 前，不執行大規模 Migration。

## 十一、禁止推論

- 不因檔名新就判 CURRENT。
- 不因 Git Commit 新就判 CURRENT。
- 不因資料夾位於 0-知識／1-系統／2-方案就判定資產類型與狀態。
- 不因文件內容完整就判定正式。
- 不因歷史就判定無價值。
- 不因同名就 Merge。
- 不從未知 K07–K61／S11–S37 推導內容。
- 不從候選文件推導新的 A/B/C/D 功能。

本清冊是 Derived Inventory，不取代任何 Canonical Source。