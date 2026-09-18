# AI單人工作室全庫資產逐項清冊－第一輪

版本：v1.1
日期：2026-09-18
狀態：【G1 第三批完成；0-知識／1-系統／2-方案根目錄已取得 Repository recursive tree；逐文件狀態判定仍進行中】
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
| G1-096 | 藍圖/AI單人工作室未來藍圖待辦清單-v1.0.md | Planning / TODO | CURRENT候選 | KEEP | 未來藍圖，不是第五方案；2026-09-18移入藍圖/ |
| G1-097 | 藍圖/AI單人工作室未來藍圖規劃書-功能導向架構-v1.0.md | Planning / Architecture | CURRENT候選 | KEEP | 長期能力框架；2026-09-18移入藍圖/ |
| G1-098 | 藍圖/AI單人工作室功能導向藍圖地圖-既有資產完整Mapping-v1.0.md | Derived View / Mapping | CURRENT候選 | KEEP | 非 Canonical Source；2026-09-18移入藍圖/ |
| G1-099 | 藍圖/AI單人工作室功能導向藍圖交接入口-v1.0.md | Handoff / Entry | CURRENT候選 | KEEP | 未來藍圖入口；2026-09-18移入藍圖/ |
| G1-100 | 藍圖/藍圖交接資料-v1.0.md | Handoff / Blueprint State | CURRENT候選 | KEEP | 藍圖專用交接入口；不取代正式工程狀態 |

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

## 十一、G1 第二批：0-知識／1-系統 Repository 完整樹盤點

本批改用 GitHub Repository recursive tree 直接取得實際檔案集合，避免以搜尋結果推估目錄完整性。

### 11.1 0-知識：共 81 個 Markdown 資產

本批新增登錄 60 個未在第一批登錄的文件。因為「存在於 0-知識」本身不能證明 CURRENT，以下初始狀態統一採 REVIEW；後續再依 Canonical Source、交接鏈、實際引用、決策與驗證證據逐項確認。

| Asset ID | 路徑 | 類型 | 初步 State | Disposition |
|---|---|---|---|---|
| G1-110 | 0-知識/上下文/上下文成本.md | Knowledge | REVIEW | KEEP候選 |
| G1-111 | 0-知識/上下文/上下文管理原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-112 | 0-知識/上下文/上下文與資料載入介面原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-113 | 0-知識/上下文/人工智慧交接文件分工.md | Knowledge | REVIEW | KEEP候選 |
| G1-114 | 0-知識/上下文/模型能力補償.md | Knowledge | REVIEW | KEEP候選 |
| G1-115 | 0-知識/分類/分類原理.md | Knowledge | REVIEW | 已有第一批同名確認；本列不重複計數 |
| G1-116 | 0-知識/分類/分類維度.md | Knowledge | REVIEW | 已有第一批同類資產；不升格 |
| G1-117 | 0-知識/分類/分類與目錄.md | Knowledge | REVIEW | KEEP候選 |
| G1-118 | 0-知識/分類/核心資料類型與邊界.md | Knowledge | REVIEW | KEEP候選 |
| G1-119 | 0-知識/搜尋/候選資料整理與篩選.md | Knowledge | REVIEW | KEEP候選 |
| G1-120 | 0-知識/搜尋/搜尋原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-121 | 0-知識/搜尋/搜尋拆分.md | Knowledge | REVIEW | KEEP候選 |
| G1-122 | 0-知識/搜尋/搜尋擴展.md | Knowledge | REVIEW | KEEP候選 |
| G1-123 | 0-知識/搜尋/研究結果整合與綜合原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-124 | 0-知識/搜尋/研究過程與決策軌跡記錄原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-125 | 0-知識/搜尋/資料探索.md | Knowledge | REVIEW | KEEP候選 |
| G1-126 | 0-知識/搜尋/資訊適用性與情境匹配原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-127 | 0-知識/更新/AI模型更新檢查原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-128 | 0-知識/更新/區分目前狀態與設計歷史.md | Knowledge | REVIEW | KEEP候選 |
| G1-129 | 0-知識/更新/更新成本效益與停止判定.md | Knowledge | REVIEW | KEEP候選 |
| G1-130 | 0-知識/更新/更新觸發與變更偵測原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-131 | 0-知識/更新/更新頻率與審查週期原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-132 | 0-知識/更新/歷史與目前資料共存原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-133 | 0-知識/更新/版本與演化邊界.md | Knowledge | REVIEW | KEEP候選 |
| G1-134 | 0-知識/更新/目前狀態判定.md | Knowledge | REVIEW | KEEP候選 |
| G1-135 | 0-知識/更新/變更影響分析與影響範圍.md | Knowledge | REVIEW | KEEP候選 |
| G1-136 | 0-知識/更新/資料狀態模型.md | Knowledge | REVIEW | KEEP候選 |
| G1-137 | 0-知識/更新/重大變更與遷移安全原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-138 | 0-知識/比較/知識衝突判定.md | Knowledge | REVIEW | KEEP候選 |
| G1-139 | 0-知識/管理/共享能力與責任邊界原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-140 | 0-知識/管理/共同資料契約原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-141 | 0-知識/管理/共同資料最小描述原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-142 | 0-知識/管理/共同關係模型最小原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-143 | 0-知識/管理/工程狀態與交接紀錄時機規則-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-144 | 0-知識/管理/時間範圍與適用條件.md | Knowledge | REVIEW | KEEP候選 |
| G1-145 | 0-知識/管理/相容性與遷移最小原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-146 | 0-知識/管理/知識分類.md | Knowledge | REVIEW | KEEP候選 |
| G1-147 | 0-知識/管理/知識定義與邊界.md | Knowledge | REVIEW | KEEP候選 |
| G1-148 | 0-知識/管理/知識與系統的證據閉環原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-149 | 0-知識/管理/系統目錄分層與資料規模管理原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-150 | 0-知識/管理/系統目錄與系統登錄原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-151 | 0-知識/管理/系統穩定識別與引用原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-152 | 0-知識/管理/系統與方案完成度分層原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-153 | 0-知識/管理/舊能力重製判定原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-154 | 0-知識/管理/觸發條件管理與啟動保險原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-155 | 0-知識/管理/觸發條件管理與啟動保險原理.md | Knowledge | REVIEW | 版本／重疊待比較 |
| G1-156 | 0-知識/管理/觸發條件管理與系統路由原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-157 | 0-知識/管理/記憶定義與邊界.md | Knowledge | REVIEW | KEEP候選 |
| G1-158 | 0-知識/管理/變更影響分析最小原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-159 | 0-知識/管理/資料來源與使用追溯最小原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-160 | 0-知識/管理/資料版本相容性原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-161 | 0-知識/管理/資料狀態與生命週期原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-162 | 0-知識/管理/資料識別與引用原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-163 | 0-知識/管理/資料身份與唯一識別原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-164 | 0-知識/管理/資料關係類型與語義字典.md | Knowledge | REVIEW | KEEP候選 |
| G1-165 | 0-知識/管理/跨方案資料一致性原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-166 | 0-知識/系統/多方案交叉驗證原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-167 | 0-知識/系統/新舊系統獨立運行原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-168 | 0-知識/系統/系統依賴.md | Knowledge | REVIEW | KEEP候選 |
| G1-169 | 0-知識/系統/系統與方案介面原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-170 | 0-知識/系統/知識融合與能力蒸餾原理-v1.0.md | Knowledge | REVIEW | KEEP候選 |
| G1-171 | 0-知識/證據/來源主張證據追溯.md | Knowledge | REVIEW | KEEP候選 |
| G1-172 | 0-知識/證據/來源與證據.md | Knowledge | REVIEW | 已有第一批同類資產；不另升格 |
| G1-173 | 0-知識/證據/區分人工智慧輸出與知識真實性.md | Knowledge | REVIEW | KEEP候選 |
| G1-174 | 0-知識/證據/區分來源與知識.md | Knowledge | REVIEW | KEEP候選 |
| G1-175 | 0-知識/證據/資訊可信度與主張驗證原理.md | Knowledge | REVIEW | KEEP候選 |
| G1-176 | 0-知識/運作/AI知識庫基本運作循環.md | Knowledge | REVIEW | KEEP候選 |
| G1-177 | 0-知識/運作/實測結果回寫最小原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-178 | 0-知識/運作/小系統建立原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-179 | 0-知識/運作/後續工作觸發式順便驗證原則-v2.0.md | Knowledge | REVIEW | 版本／前身待比較 |
| G1-180 | 0-知識/運作/後續工作觸發式順便驗證原則.md | Knowledge | REVIEW | 版本／前身待比較 |
| G1-181 | 0-知識/運作/新方案建立前研究與確認原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-182 | 0-知識/運作/系統建立流程失效原因與防止提前建系統.md | Knowledge | REVIEW | KEEP候選 |
| G1-183 | 0-知識/運作/系統目錄與觸發條件分離原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-184 | 0-知識/運作/統御分支與系統歸屬管理原則.md | Knowledge | REVIEW | KEEP候選 |
| G1-185 | 0-知識/分類/廢棄/資料層級與分類-v1.0.md | Knowledge / Historical | HISTORICAL候選 | ARCHIVE候選 |

### 11.2 1-系統：共 61 個 Markdown 資產

本批以 Repository tree 為準。系統不因位於 1-系統即視為已啟用；版本並存、外部比對文件與研究文件尤其需要 REVIEW。

| Asset ID | 路徑 | 類型 | 初步 State | Disposition |
|---|---|---|---|---|
| G1-200 | 1-系統/AI上下文與交接系統.md | System | REVIEW | KEEP候選 |
| G1-201 | 1-系統/AI知識庫基本運作系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-202 | 1-系統/AI知識管理系統-v2.0.md | System | REVIEW | 版本／權威性待確認 |
| G1-203 | 1-系統/來源與證據-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-204 | 1-系統/來源與證據分析系統.md | System | REVIEW | KEEP候選 |
| G1-205 | 1-系統/共同對象與關係目錄系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-206 | 1-系統/分類與資料管理-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-207 | 1-系統/問題解決系統-v1.0.md | System | REVIEW | 與流程文件對照 |
| G1-208 | 1-系統/問題解決與新系統建立流程-v1.1.md | System / Process | REVIEW | KEEP候選 |
| G1-209 | 1-系統/實測結果回寫檢查小系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-210 | 1-系統/小系統建立與生命週期管理系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-211 | 1-系統/後續工作觸發式順便驗證系統-v1.0.md | System | REVIEW | 版本群待比較 |
| G1-212 | 1-系統/後續工作觸發式順便驗證系統-v1.1.md | System | REVIEW | 版本群待比較 |
| G1-213 | 1-系統/後續工作觸發式順便驗證系統-v1.2.md | System | REVIEW | 版本群待比較 |
| G1-214 | 1-系統/後續工作觸發式順便驗證系統-v2.0.md | System | REVIEW | 版本群待比較 |
| G1-215 | 1-系統/搜尋原理-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-216 | 1-系統/整體資料治理系統-v1.0.md | System | REVIEW | 與A方案責任對照 |
| G1-217 | 1-系統/新方案建立前研究與確認系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-218 | 1-系統/方案管理-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-219 | 1-系統/方案管理系統.md | System | REVIEW | KEEP候選 |
| G1-220 | 1-系統/方案紀錄模板.md | Template | REVIEW | KEEP候選 |
| G1-221 | 1-系統/更新影響分析與成本判斷系統.md | System | REVIEW | KEEP候選 |
| G1-222 | 1-系統/更新監控與觸發系統.md | System | REVIEW | KEEP候選 |
| G1-223 | 1-系統/知識外部比對系統.md | System | REVIEW | KEEP候選 |
| G1-224 | 1-系統/知識外部比對紀錄模板.md | Template | REVIEW | KEEP候選 |
| G1-225 | 1-系統/知識定義與邊界-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-226 | 1-系統/知識整合系統.md | System | REVIEW | KEEP候選 |
| G1-227 | 1-系統/知識更新原理-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-228 | 1-系統/知識更新與狀態管理系統.md | System | REVIEW | KEEP候選 |
| G1-229 | 1-系統/知識比較原理-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-230 | 1-系統/知識比較與衝突分析系統.md | System | REVIEW | KEEP候選 |
| G1-231 | 1-系統/知識衝突判定-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-232 | 1-系統/知識迭代與資料演化系統-v1.0.md | System | REVIEW | 與方案三對照 |
| G1-233 | 1-系統/知識重疊與資料演化檢查小系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-234 | 1-系統/研究問題與搜尋策略系統.md | System | REVIEW | KEEP候選 |
| G1-235 | 1-系統/研究結果整合系統.md | System | REVIEW | KEEP候選 |
| G1-236 | 1-系統/研究證據與採用判斷系統.md | System | REVIEW | KEEP候選 |
| G1-237 | 1-系統/系統管理統御分支-v1.0.md | System | REVIEW | 與統御方案對照 |
| G1-238 | 1-系統/系統管理統御分支系統-v1.0.md | System | REVIEW | 與上項關係待確認 |
| G1-239 | 1-系統/統御小系統協調管理系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-240 | 1-系統/統御方案系統-v1.0.md | System | REVIEW | KEEP候選 |
| G1-241 | 1-系統/觸發條件管理系統-v1.0.md | System | REVIEW | 與v1.1比較 |
| G1-242 | 1-系統/觸發條件管理系統-v1.1.md | System | REVIEW | 版本群待比較 |
| G1-243 | 1-系統/資料分類與組織系統.md | System | REVIEW | KEEP候選 |
| G1-244 | 1-系統/資料層級與分類-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-245 | 1-系統/資料探索-外部比對.md | Research / Evidence | HISTORICAL候選 | DISTILL候選 |
| G1-246 | 1-系統/資料探索與搜尋系統.md | System | REVIEW | KEEP候選 |

## 十二、第二批判定結論

本批最重要的結果不是把所有文件直接判成 KEEP，而是建立了實際資產集合：

- 0-知識：81 個 Markdown。
- 1-系統：61 個 Markdown。
- 合計：142 個 Markdown。
- Repository recursive tree 顯示未截斷（truncated=false）。

其中大量文件具有「版本並存、外部比對、歷史研究、候選系統、後續演化」特徵，因此目前只完成「存在性＋初步責任分類」，尚未完成「Canonical／State 最終判定」。

### 已發現的高優先比較群

1. 觸發條件：
   - 0-知識/管理/觸發條件管理原理.md
   - 0-知識/管理/觸發條件管理與啟動保險原理.md
   - 0-知識/管理/觸發條件管理與啟動保險原理-v1.0.md
   - 0-知識/管理/觸發條件管理與系統路由原理.md
   - 1-系統/觸發條件管理系統-v1.0.md
   - 1-系統/觸發條件管理系統-v1.1.md
   - 1-系統/更新監控與觸發系統.md

2. 後續工作／驗證：
   - 0-知識/運作/後續工作觸發式順便驗證原則.md
   - 0-知識/運作/後續工作觸發式順便驗證原則-v2.0.md
   - 1-系統/後續工作觸發式順便驗證系統-v1.0.md～v2.0.md

3. 問題解決：
   - 1-系統/問題解決系統-v1.0.md
   - 1-系統/問題解決與新系統建立流程-v1.1.md
   - 對應 2-方案／完善中的失效與驗證證據。

4. 統御：
   - 系統管理統御分支
   - 系統管理統御分支系統
   - 統御方案系統
   - 統御小系統協調管理系統
   - 對應 2-方案/統御/ 與相關研究。

5. 外部比對資料：
   多數不應直接進入 CURRENT Recall；應作為 Evidence / Research，後續再蒸餾有效結論。

## 十三、目前 G1 進度

| 批次 | 範圍 | 狀態 |
|---|---|---|
| 第一批 | 目前工程入口、部分知識、部分系統、方案、完善、根目錄藍圖 | 完成 |
| 第二批 | 0-知識／1-系統實際 Repository tree | 完成 |
| 第三批 | 2-方案 根目錄 | 待執行 |
| 第四批 | 2-方案/完善 | 待執行 |
| 第五批 | 討論／研究／會議／紀錄 | 待執行 |
| 第六批 | 根目錄其他企劃／模板／工具 | 待執行 |

## 十四、G1 第二批禁止事項

本批不做：

- 不把 142 個文件全部升格 CURRENT。
- 不因「知識」資料夾而認定內容正確。
- 不因「系統」資料夾而認定系統已啟用。
- 不因 v2.0／v2.1 名稱直接判定後繼關係。
- 不刪除外部比對文件。
- 不把歷史研究直接混入一般 Recall。
- 不在本批創建新的 A/B/C/D 功能。
- 不因資產數量增加而創建新的總方案。


## 十五、G1 第三批：2-方案 根目錄

本批取得 `2-方案/` 根目錄的實際 Markdown 資產，共 43 個。子目錄（例如 `2-方案/完善/`、`2-方案/統御/`）不包含在本批，避免與下一批責任分類混在一起。

其中已於前批登錄的文件不重複列為新資產；以下列出本批新增或需要重新確認的項目。

| Asset ID | 路徑 | 類型 | 初步 State | Disposition |
|---|---|---|---|---|
| G1-300 | 2-方案/AI知識管理方案-v2.0完整規劃.md | Solution / Planning | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-301 | 2-方案/AI知識管理方案-v2.0草案.md | Solution / Draft | REVIEW / DRAFT | ARCHIVE候選 |
| G1-302 | 2-方案/AI知識管理方案-重大更新研究.md | Research / Candidate | RESEARCH | RETAIN |
| G1-303 | 2-方案/三方案功能歸屬與治理權分析-第一版.md | Governance Research | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-304 | 2-方案/工程運作與持續改進方案-v1.0.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-305 | 2-方案/工程運作與持續改進方案-v1.1.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-306 | 2-方案/工程運作與持續改進方案-v1.2.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-307 | 2-方案/工程運作與持續改進方案-v1.3.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-308 | 2-方案/工程運作與持續改進方案-v1.4.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-309 | 2-方案/工程運作與持續改進方案-v1.5.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-310 | 2-方案/工程運作與持續改進方案-v1.6.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-311 | 2-方案/工程運作與持續改進方案-v1.7.md | Solution / Governance | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-312 | 2-方案/工程運作與持續改進方案-企劃-v1.0.md | Solution / Planning | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-313 | 2-方案/搜尋研究方案-v2.0.md | Solution | REVIEW | 版本關係待確認 |
| G1-314 | 2-方案/搜尋研究方案-功能系統盤點.md | Research / Inventory | REVIEW | RETAIN |
| G1-315 | 2-方案/搜尋研究方案-圖書館式知識管理外部研究-v1.0.md | Research / External | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-316 | 2-方案/方案規劃膨脹與幻覺稽核-第一輪.md | Audit / Evidence | HISTORICAL候選 | RETAIN |
| G1-317 | 2-方案/正確成立方案與系統方案-v1.0.md | Engineering Evidence | HISTORICAL候選 | RETAIN |
| G1-318 | 2-方案/正確成立方案與系統方案-v2.1.md | Engineering Evidence | HISTORICAL候選 | RETAIN |
| G1-319 | 2-方案/正確成立方案與系統方案-v2.2.md | Engineering Evidence | HISTORICAL候選 | RETAIN |
| G1-320 | 2-方案/正確成立方案與系統方案-v2.3.md | Engineering Evidence | HISTORICAL候選 | RETAIN |
| G1-321 | 2-方案/正確成立方案與系統方案-v2.4.md | Engineering Evidence | HISTORICAL候選 | RETAIN |
| G1-322 | 2-方案/知識迭代與資料治理方案-完整規劃.md | Solution / Planning | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-323 | 2-方案/變更與新知檢測方案.md | Solution | REVIEW | KEEP候選 |
| G1-324 | 2-方案/更新方案-建立與測試.md | Solution / Test | REVIEW | RETAIN |
| G1-325 | 2-方案/能力蒸餾與系統重構方案-v1.1.md | Solution | REVIEW / STATE-CONFLICT | 不處置，待溯源 |
| G1-326 | 2-方案/知識迭代與資料演化方案-v1.0.md | Solution / Predecessor | HISTORICAL候選 | RETAIN / EVIDENCE |
| G1-327 | 2-方案/知識迭代與能力蒸餾方案重製規劃-v1.0.md | Planning / Engineering Evidence | HISTORICAL候選 | RETAIN / EVIDENCE |

### 15.1 本批特別發現

1. `工程運作與持續改進方案-v1.8.md` 已在 G1-007 登錄為 CURRENT；v1.0～v1.7 應保留為歷史演化證據，不得與 v1.8 並列為目前工程入口。

2. `能力蒸餾與系統重構方案-v1.1.md` 仍維持 STATE-CONFLICT。不能因本次盤點而自行修正其內部狀態。

3. `AI知識管理方案-v2.0.md`、`知識與資料迭代演化方案-v2.0.md` 的檔名／內部版本漂移仍需個別確認，不能直接把 v2.0 改稱 v2.1。

4. `正確成立方案與系統方案` 存在 v1.0～v2.4 多代資料，應作為工程演化證據群處理，而非名稱合併。

### 15.2 G1 第三批結論

目前 `2-方案/` 根目錄的主要問題已從「不知道有哪些方案」進入「版本、責任、狀態與歷史演化需要逐項判定」。

下一步不能直接 Migration；應先處理：
`版本群 → 前後繼關係 → Canonical Source → State → Evidence → Disposition`。

## 十六、G1 目前進度總表

| 批次 | 範圍 | 狀態 |
|---|---|---|
| 第一批 | 目前工程入口、部分知識、部分系統、方案、完善、根目錄藍圖 | 完成 |
| 第二批 | 0-知識／1-系統 Repository tree | 完成 |
| 第三批 | 2-方案 根目錄 Repository tree | 完成 |
| 第四批 | 2-方案/完善 | 待執行 |
| 第五批 | 2-方案/統御及其他子目錄 | 待執行 |
| 第六批 | 討論／研究／會議／紀錄 | 待執行 |
| 第七批 | 根目錄其他企劃／模板／工具 | 待執行 |

G1 尚未完成，因此目前仍禁止大規模 Migration。
