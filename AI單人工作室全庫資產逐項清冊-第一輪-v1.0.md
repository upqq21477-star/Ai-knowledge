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

本批以 Repository recursive tree 確認 0-知識 共 81 個 Markdown 資產；其中部分已在第一批登錄，因此本節不再以「新增數量」作為完整性指標。因為「存在於 0-知識」本身不能證明 CURRENT，以下初始狀態統一採 REVIEW；後續再依 Canonical Source、交接鏈、實際引用、決策與驗證證據逐項確認。

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


## 十七、G1 第四批：2-方案/完善 Repository 全量資產盤點

本批改用 GitHub Contents API 直接取得 2-方案/完善/ 實際文件集合，共 **160 個 Markdown 文件**。本批不以搜尋結果估算目錄完整性。

其中已有 G1-070～G1-082 等前批資產者視為「既有資產重新稽核」，不重複建立 Asset ID；其餘文件以下新增登錄。這一批仍是文件級初判，不是最終 Canonical／State 判定。

### 17.1 新增文件逐項登錄

| Asset ID | 路徑 | 類型 | 初步 State | 初步處置／備註 |
|---|---|---|---|---|
| G1-400 | 2-方案/完善/AI知識庫基本運作系統-v1.0最小實測-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-401 | 2-方案/完善/AI知識管理方案-v2.1完善草案.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-402 | 2-方案/完善/三方案協作驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-403 | 2-方案/完善/三方案問題發現與舊搜尋方案解法驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-404 | 2-方案/完善/三方案問題解法實測結果-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-405 | 2-方案/完善/三方案第二輪真實案例檢驗-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-406 | 2-方案/完善/三方案跨系統長流程壓力測試-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-407 | 2-方案/完善/交接失憶模擬測試-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-408 | 2-方案/完善/兩方案重製交叉驗證案例-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-409 | 2-方案/完善/共同對象與關係目錄系統-最小實作驗收-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-410 | 2-方案/完善/功能到系統能力映射第一版-v1.0.md | Derived View / Mapping | REVIEW | 非Canonical Source |
| G1-411 | 2-方案/完善/問題處理-功能清單批次錯置-A13至A16未定義-v1.0.md | Engineering Evidence / Review | REVIEW | 需逐文件讀取後判定 |
| G1-412 | 2-方案/完善/問題處理-實際驗證延後機制-研究與候選解法-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-413 | 2-方案/完善/問題處理-無記憶交接測試發現現行入口引用漂移-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-414 | 2-方案/完善/問題處理-無記憶交接測試發現現行入口引用漂移-研究與候選解法-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-415 | 2-方案/完善/問題處理-第二次無記憶交接測試-完整現行入口鏈回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-416 | 2-方案/完善/問題處理-第二次無記憶交接測試發現現行規則仍引用-v2.7-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-417 | 2-方案/完善/問題處理與回報流程-錯誤發現案例整合驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-418 | 2-方案/完善/問題解決-功能清單批次錯置-回歸模擬驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-419 | 2-方案/完善/問題解決-功能清單批次錯置-研究與候選解法-v1.0.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-420 | 2-方案/完善/問題解決-問題解決系統未被實際啟動案例-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-421 | 2-方案/完善/問題解決-新系統建立流程入口失效案例-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-422 | 2-方案/完善/問題解決-施工階段誤跳至⑨之最小守門能力驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-423 | 2-方案/完善/問題解決-統御異常偵測與問題解決路由第三輪案例驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-424 | 2-方案/完善/問題解決-統御異常偵測與問題解決路由第二輪案例驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-425 | 2-方案/完善/問題解決與新系統建立流程-搜尋研究方案加入實測-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-426 | 2-方案/完善/四方案功能拆解第一版-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-427 | 2-方案/完善/四方案逐項功能研究-001-A1至A4.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-428 | 2-方案/完善/四方案逐項功能研究-002-A5至A8.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-429 | 2-方案/完善/四方案逐項功能研究-003-A9至A12.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-430 | 2-方案/完善/四方案逐項功能研究-004-B1至B4.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-431 | 2-方案/完善/四方案逐項功能研究-005-B5至B8-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-432 | 2-方案/完善/四方案逐項功能研究-005-B5至B8.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-433 | 2-方案/完善/四方案逐項功能研究-006-B9至B12-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-434 | 2-方案/完善/四方案逐項功能研究-006-B9至B12.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-435 | 2-方案/完善/四方案逐項功能研究-007-B13至B16-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-436 | 2-方案/完善/四方案逐項功能研究-007-B13至B16.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-437 | 2-方案/完善/四方案逐項功能研究-008-C1至C4-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-438 | 2-方案/完善/四方案逐項功能研究-008-C1至C4.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-439 | 2-方案/完善/四方案逐項功能研究-009-C5至C8-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-440 | 2-方案/完善/四方案逐項功能研究-009-C5至C8.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-441 | 2-方案/完善/四方案逐項功能研究-010-C9至C12-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-442 | 2-方案/完善/四方案逐項功能研究-010-C9至C12.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-443 | 2-方案/完善/四方案逐項功能研究-011-C13至C16-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-444 | 2-方案/完善/四方案逐項功能研究-011-C13至C16.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-445 | 2-方案/完善/四方案逐項功能研究-012-C17至C18-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-446 | 2-方案/完善/四方案逐項功能研究-012-C17至C18.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-447 | 2-方案/完善/四方案逐項功能研究-013-D1至D4-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-448 | 2-方案/完善/四方案逐項功能研究-013-D1至D4.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-449 | 2-方案/完善/四方案逐項功能研究-014-D5至D8-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-450 | 2-方案/完善/四方案逐項功能研究-014-D5至D8.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-451 | 2-方案/完善/四方案逐項功能研究-016-D13至D16-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-452 | 2-方案/完善/四方案逐項功能研究-016-D13至D16.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-453 | 2-方案/完善/四方案逐項功能研究-017-D17至D20-模擬實作驗收.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-454 | 2-方案/完善/實測結果回寫檢查小系統-最小實測-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-455 | 2-方案/完善/實測結果回寫檢查小系統-第二輪自然施工模擬-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-456 | 2-方案/完善/實際驗證待觸發標記清冊-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-457 | 2-方案/完善/實際驗證待觸發機制-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-458 | 2-方案/完善/實際驗證待觸發機制-模擬實作驗收-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-459 | 2-方案/完善/實際驗證觀察與待觸發機制-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-460 | 2-方案/完善/工程紀錄時機與交接同步-新基準-001.md | Engineering Evidence / Review | REVIEW | 需逐文件讀取後判定 |
| G1-461 | 2-方案/完善/工程紀錄時機與交接同步-自然工作驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-462 | 2-方案/完善/工程紀錄時機與交接同步狀態-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-463 | 2-方案/完善/工程紀錄時機與交接同步規劃-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-464 | 2-方案/完善/工程紀錄時機與交接同步規劃-交接摘要-001.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-465 | 2-方案/完善/工程紀錄時機與交接同步規劃-待辦狀態-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-466 | 2-方案/完善/工程紀錄時機與交接同步規劃-驗證前狀態-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-467 | 2-方案/完善/工程紀錄時機與交接同步驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-468 | 2-方案/完善/工程運作批次來源驗證-B13至B16批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-469 | 2-方案/完善/工程運作批次來源驗證-B9至B12批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-470 | 2-方案/完善/工程運作批次來源驗證-C13至C16批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-471 | 2-方案/完善/工程運作批次來源驗證-C17至C18批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-472 | 2-方案/完善/工程運作批次來源驗證-C1至C4批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-473 | 2-方案/完善/工程運作批次來源驗證-C5至C8批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-474 | 2-方案/完善/工程運作批次來源驗證-C9至C12批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-475 | 2-方案/完善/工程運作批次來源驗證-D17至D20批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-476 | 2-方案/完善/工程運作批次來源驗證-D1至D4批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-477 | 2-方案/完善/工程運作批次來源驗證-D1至D4批次檢查-修正-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-478 | 2-方案/完善/工程運作批次來源驗證-D5至D8批次檢查-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-479 | 2-方案/完善/工程運作批次來源驗證-迭代修正方案-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-480 | 2-方案/完善/工程運作自然工作驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-481 | 2-方案/完善/工程運作與持續改進方案-最小實作驗收-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-482 | 2-方案/完善/待辦-本輪交接發現事項-v1.0.md | Engineering Evidence / Review | REVIEW | 需逐文件讀取後判定 |
| G1-483 | 2-方案/完善/後續工作觸發式順便驗證-外部方法比對記錄-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-484 | 2-方案/完善/搜尋研究方案-v2.0加入後新系統穩定性驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-485 | 2-方案/完善/整體系統更新方案-自然案例驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-486 | 2-方案/完善/整體系統更新方案-重大變更遷移演練-001.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-487 | 2-方案/完善/整體資料治理方案-v1.1完善草案.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-488 | 2-方案/完善/新系統與三方案對接穩定性及資料格式檢驗-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-489 | 2-方案/完善/方案一-A1至A12正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-490 | 2-方案/完善/方案一整體責任統整-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-491 | 2-方案/完善/方案一整體責任統整-模擬實作驗收-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-492 | 2-方案/完善/方案三-C13至C16正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-493 | 2-方案/完善/方案三-C13至C16正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-494 | 2-方案/完善/方案三-C17至C18正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-495 | 2-方案/完善/方案三-C17至C18正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-496 | 2-方案/完善/方案三-C1至C4正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-497 | 2-方案/完善/方案三-C1至C4正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-498 | 2-方案/完善/方案三-C5至C8正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-499 | 2-方案/完善/方案三-C5至C8正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-500 | 2-方案/完善/方案三-C9至C12正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-501 | 2-方案/完善/方案三-C9至C12正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-502 | 2-方案/完善/方案三整體責任統整-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-503 | 2-方案/完善/方案三整體責任統整-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-504 | 2-方案/完善/方案三整體責任統整-模擬實作驗收-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-505 | 2-方案/完善/方案三整體驗收後最小實作與工程運作驗證方案-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-506 | 2-方案/完善/方案三最小實作驗收模擬-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-507 | 2-方案/完善/方案三變更失敗修正閉環模擬驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-508 | 2-方案/完善/方案二-B13至B16正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-509 | 2-方案/完善/方案二-B13至B16正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-510 | 2-方案/完善/方案二-B1至B8正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-511 | 2-方案/完善/方案二-B1至B8正式責任整合-模擬回歸驗收-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-512 | 2-方案/完善/方案二-B9至B12正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-513 | 2-方案/完善/方案二-B9至B12正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-514 | 2-方案/完善/方案二任務理解與Context責任鏈模擬驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-515 | 2-方案/完善/方案二功能既有能力映射-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-516 | 2-方案/完善/方案二失敗修正閉環模擬驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-517 | 2-方案/完善/方案二最小實作驗收模擬-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-518 | 2-方案/完善/方案二變更接口模擬驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-519 | 2-方案/完善/方案四-D13至D16正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-520 | 2-方案/完善/方案四-D13至D16正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-521 | 2-方案/完善/方案四-D17至D20正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-522 | 2-方案/完善/方案四-D17至D20正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-523 | 2-方案/完善/方案四-D1至D4正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-524 | 2-方案/完善/方案四-D1至D4正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-525 | 2-方案/完善/方案四-D5至D8正式責任整合-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-526 | 2-方案/完善/方案四-D5至D8正式責任整合-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-527 | 2-方案/完善/方案四共同能力影響分析-001.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-528 | 2-方案/完善/方案四整體責任統整-模擬回歸驗證-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-529 | 2-方案/完善/方案四整體責任統整-模擬實作驗收-v1.0.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-530 | 2-方案/完善/方案四蒸餾邊界與失敗修正模擬驗證-001.md | Test / Evidence | HISTORICAL候選 | 保留驗證證據，需判定後續基準是否已吸收 |
| G1-531 | 2-方案/完善/方案規劃與施工入口標記模板-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-532 | 2-方案/完善/施工主線-①至⑪-v1.0.md | Engineering Evidence / Review | REVIEW | 需逐文件讀取後判定 |
| G1-533 | 2-方案/完善/施工順序修正-知識書先於共同規格細化-v1.0.md | Engineering Spec | REVIEW | 需確認是否已併入正式方案 |
| G1-534 | 2-方案/完善/正確成立方案與系統-功能盤點與外部研究-v1.0.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-535 | 2-方案/完善/正確成立方案與系統-功能盤點與外部研究-v1.1.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-536 | 2-方案/完善/正確成立方案與系統方案-v1.0-外部比對與失效分析-001.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |
| G1-537 | 2-方案/完善/正確成立方案與系統方案-v2.0-重建狀態-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-538 | 2-方案/完善/目前工程狀態快照恢復驗證-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-539 | 2-方案/完善/目前狀態來源責任重整-施工前影響分析-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-540 | 2-方案/完善/目前狀態來源責任重整-第二輪失去記憶交接驗證-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-541 | 2-方案/完善/目前狀態來源責任重整狀態-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-542 | 2-方案/完善/目前狀態來源責任重整規劃-v1.0.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-543 | 2-方案/完善/目前狀態與工程狀態快照責任分工分析-001.md | State / Evidence | REVIEW | 需依時間軸與內容判定 |
| G1-544 | 2-方案/完善/知識迭代與資料演化方案-v1.1完善草案.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-545 | 2-方案/完善/統御方案-提前建立缺陷標記-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-546 | 2-方案/完善/能力蒸餾與系統重構方案-閉環補強規格-v1.0.md | Solution / Planning | REVIEW | 需與正式方案及後續整合文件比對 |
| G1-547 | 2-方案/完善/變更影響與遷移能力整合盤點-v1.0.md | Research / Analysis | REVIEW | 研究／分析證據，不直接進CURRENT Recall |

### 17.2 第四批高優先關係群

1. 方案四正式責任整合與舊方案文件的狀態差異：能力蒸餾與系統重構方案-v1.1、閉環補強規格、D1～D4／D5～D8／D13～D16／D17～D20 正式責任整合，以及方案四整體責任統整回歸。

2. 能力映射／共同能力候選：功能到系統能力映射、候選系統能力既有能力重疊比對、共同對象與關係目錄系統最小實作驗收、變更影響與遷移能力整合盤點。這些不得直接升格為正式系統。

3. 三方案／跨系統驗證證據群：三方案協作驗證、三方案問題發現與舊搜尋方案解法驗證、三方案問題解法實測、三方案第二輪真實案例檢驗、三方案跨系統長流程壓力測試，以及失憶交接／狀態責任重整驗證。主要價值是 Evidence／Test Corpus，不因 PASS 自動成為 CURRENT 規格。

4. 目前工程入口歷史鏈：快照-001～004 為歷史證據；快照-005 為 CURRENT 唯一工程游標；快照恢復驗證與來源責任重整驗證屬 Evidence。

### 17.3 第四批判定

本批確認 2-方案/完善/ 不是單純「完善文件夾」，而是 Repository 中最大的工程證據、驗證、責任整合與狀態演化資料層之一。因此不能整批 Archive，也不能整批放入 CURRENT Recall。

後續應按：正式責任整合 → 驗證證據 → 研究／候選 → 歷史狀態 → 派生 Mapping，逐項處理，而不是按資料夾一次搬遷。

### 17.4 方案四 v1.1 狀態衝突追溯結果

目前已取得足夠證據把原先的「未知衝突」縮小為「後續正式整合已發生，但 v1.1 文件內 State 未同步」的高可信候選：

- v1.1 文件自身仍標示「整體重整完成；待最小流程驗收；真實系統能力案例待執行」。
- 後續正式文件已完成 D1～D20 分批正式責任整合。
- 後續驗收已完成 D17～D20 模擬回歸，並有 D1～D20 整體模擬／回歸結果。
- 現行交接／快照已明確記錄 D1～D20 模擬／回歸完成，FIELD 待自然觸發。
- 因此不應再把 v1.1 的舊 State 當作目前方案四狀態；但仍保留 v1.1 作為歷史演化來源，直到確認其內容是否全部被後續文件吸收。

這是狀態追溯結果，不是對舊文件做內容改寫。

## 十八、G1 目前進度修正

| 批次 | 範圍 | 狀態 |
|---|---|---|
| 第一批 | 目前工程入口、部分知識、部分系統、方案、完善、根目錄藍圖 | 完成 |
| 第二批 | 0-知識／1-系統 Repository tree | 完成；存在性完成，最終狀態仍需逐項審查 |
| 第三批 | 2-方案 根目錄 Repository tree | 完成；存在性完成，最終狀態仍需逐項審查 |
| 第四批 | 2-方案/完善 Repository tree + 高優先證據追溯 | 完成；逐文件初判完成，最終 State/Canonical 尚未全部定案 |
| 第五批 | 2-方案/統御及其他子目錄 | 待執行 |
| 第六批 | 討論／研究／會議／紀錄 | 待執行 |
| 第七批 | 根目錄其他企劃／模板／工具 | 待執行 |

G1 仍未完成，因此仍禁止大規模 Migration。

## 十九、G1 第五批：2-方案/統御 Repository 全量盤點

本批直接讀取 Repository tree，確認 `2-方案/統御/` 共 **9 個 Markdown 資產**；`2-方案/廢棄/` 目前只有 `.gitkeep`，沒有實際方案文件，因此不建立文件級 Asset ID。

### 19.1 統御分支九項資產

| Asset ID | 路徑 | 類型 | 初步 State | 初步處置／備註 |
|---|---|---|---|---|
| G1-550 | `2-方案/統御/統御分支候選方案-既有能力比對與功能裁減-v1.0.md` | Candidate Solution / Comparison | REVIEW | 重要的能力去重證據；尚非正式方案 |
| G1-551 | `2-方案/統御/統御分支方案-v1.0.md` | Candidate Solution | HISTORICAL候選 | v1.0 架構版本；已被 v1.1 進一步收斂 |
| G1-552 | `2-方案/統御/統御分支方案-v1.1.md` | Candidate Solution | REVIEW / CANDIDATE | 架構已調整，但文件自己明確寫「建立中、待最終比對與實際驗證」 |
| G1-553 | `2-方案/統御/統御分支方案-功能需求分析-v1.0.md` | Requirements Analysis | HISTORICAL候選 | 功能候選較寬；已由 v1.1 收斂 |
| G1-554 | `2-方案/統御/統御分支方案-功能需求分析-v1.1.md` | Requirements Analysis | REVIEW / CANDIDATE | 已完成觸發功能收斂，仍待既有能力最終比對與自然案例驗證 |
| G1-555 | `2-方案/統御/統御分支方案-架構與施工規劃-v1.0.md` | Architecture / Construction Plan | HISTORICAL候選 | v1.0 架構版本；已由 v1.1 調整 |
| G1-556 | `2-方案/統御/統御分支方案-架構與施工規劃-v1.1.md` | Architecture / Construction Plan | REVIEW / CANDIDATE | 已完成架構調整與功能收斂，仍未完成自然工作驗證 |
| G1-557 | `2-方案/統御/統御方案狀態標記-v1.0.md` | State / Governance Evidence | CURRENT CANDIDATE / HIGH-PRIORITY | 明確規定「統御 ≠ 已確認方案 ≠ 已成立方案」；此文件對當前狀態判定具有高價值，但不能視為正式方案規格 |
| G1-558 | `2-方案/統御/統御系統狀態總表-v1.0.md` | State Index / Derived View | REVIEW / HISTORICAL-CANDIDATE | 明確標示統御本身為候選；其中部分系統狀態與目前快照可能已過時，需後續逐項重建 |

### 19.2 第五批核心判定

本批得到的最重要結論是：**「統御」目前不是第五方案，也不是現行四方案之外的正式方案。**

現有統御文件是一組在 2026-09-17 形成的候選架構、功能分析、施工規劃、狀態標記與狀態索引。其自身文件已經明確要求：重新按照問題／目的 → 既有能力盤點 → 外部研究 → 比較 → 漏洞 → 反方案檢查 → 候選架構 → 討論 → 修正 → 確認 → 建立的 Gate 處理。

因此不能因為文件位於 `2-方案/統御/` 就將它判定為「正式方案」。

### 19.3 與既有系統的重疊問題

統御候選目前最值得保留的不是「新增更多中央控制能力」，而是它對既有責任重疊的發現：

- `1-系統/觸發條件管理系統-v1.0/v1.1` 已存在 Trigger Registry 能力。
- `1-系統/系統管理統御分支-v1.0` 已存在系統身份、目錄、狀態與方案路由相關責任。
- 因此候選統御的主要問題已轉化為「既有能力整合／缺口補強」，而不是直接建立第二套系統。

候選 v1.1 進一步將其收斂為：

`System Catalog + Activation Safety / Trigger Registry`

並明確排除中央事件匯流排、完整 Rule Engine、Workflow Engine、中央問題解決器、最佳方案選擇器等擴張方向。

### 19.4 目前處置

- 統御 v1.0：保留為歷史演化證據。
- 統御 v1.1：保留為候選架構，不能升格 CURRENT 正式方案。
- 功能需求 v1.0：保留作為需求演化證據。
- 功能需求 v1.1：保留作為收斂後候選需求。
- 架構施工 v1.0：保留作為前一版架構證據。
- 架構施工 v1.1：保留作為目前候選架構證據。
- 狀態標記：作為判定「統御尚未成立」的重要證據。
- 狀態總表：視為 Derived State View，後續需與 CURRENT 基線重新對齊。

本批不搬移、不刪除、不建立統御正式方案、不建立新的統御系統。

## 二十、G1 第五批後的進度

| 批次 | 範圍 | 狀態 |
|---|---|---|
| 第一批 | 目前工程入口、部分知識、部分系統、方案、根目錄藍圖 | 完成 |
| 第二批 | 0-知識／1-系統 Repository tree | 完成 |
| 第三批 | 2-方案 根目錄 Repository tree | 完成 |
| 第四批 | 2-方案/完善 Repository tree + 高優先證據追溯 | 完成 |
| 第五批 | 2-方案/統御 + 廢棄目錄檢查 | 完成 |
| 第六批 | 討論／研究／會議／紀錄 | 待執行 |
| 第七批 | 根目錄其他企劃／模板／工具 | 待執行 |

G1 仍未完成，Migration 仍然禁止。

## 二十一、G1 第六批：討論／研究／會議／紀錄

本批以 Repository recursive tree 實際盤點根目錄 `討論/` 與 `紀錄/`，共發現 **12 個文件項目**；其中 `討論/README.md` 為目錄說明，不列入工程資產逐項清冊，因此本批新增 **11 個實質資產**。

### 21.1 文件級初步判定

| Asset ID | 路徑 | 類型 | 初步 State | 初步處置／備註 |
|---|---|---|---|---|
| G1-650 | `紀錄/整體架構外部比對與合理性驗證紀錄-2026-09-18.md` | External Research / Architecture Validation | CURRENT EVIDENCE / HIGH-PRIORITY | 已完成外部比對並形成「核心架構通過、進入實體化與實際驗證」的研究證據；不是取代正式架構的 Canonical Source。 |
| G1-651 | `紀錄/新內容未問題化處理失效-2026-09-17.md` | Failure Record / Process Evidence | CURRENT EVIDENCE / HIGH-PRIORITY | 已確認失效並納入流程修正；應作為 Problem Intake Gate 的反向測試案例。 |
| G1-652 | `紀錄/方案四完善-2026-09-17.md` | Engineering Change Record | HISTORICAL / EVIDENCE | 保留方案四 v1.0 → 閉環補強 → 後續正式整合的演化證據，不應當成目前方案四 State。 |
| G1-653 | `紀錄/統御方案建立錯誤-2026-09-17.md` | Failure Record / Governance Evidence | CURRENT EVIDENCE / HIGH-PRIORITY | 已記錄實際施工順序失效；與目前統御候選不得混為正式方案。 |
| G1-654 | `紀錄/舊模式重疊能力重製映射-v1.0.md` | Derived Mapping / Refactoring Evidence | REVIEW / FUTURE INPUT | 明確聲明不是新方案／新系統規格；供未來整體重製作為輸入，不能直接升格架構。 |
| G1-655 | `討論/研究會議記錄-001-研究架構啟動與第一階段結果.md` | Research Meeting / External Evidence | RESEARCH / CANDIDATE INPUT | 研究層第一階段；應提取有效外部證據與結論，不直接進 CURRENT Recall。 |
| G1-656 | `討論/研究會議記錄-002-AI決策與控制層初步研究.md` | Research Meeting / Architecture Research | RESEARCH / CANDIDATE INPUT | 研究決策／控制層責任；研究結論需與現行方案及系統逐項對照。 |
| G1-657 | `討論/研究會議記錄-003-品質與可信度層初步研究.md` | Research Meeting / Evidence Research | RESEARCH / CANDIDATE INPUT | 包含 Evidence／Provenance 等方向；可作未來 Evidence 架構研究輸入，不等於已正式導入完整框架。 |
| G1-658 | `討論/研究會議記錄-004-時間與上下文層初步研究.md` | Research Meeting / Context Research | RESEARCH / CANDIDATE INPUT | Current/History、Handoff、Context Control、No-API Retrieval 等研究；與現行交接與基線重建高度相關，但仍標示研究中。 |
| G1-659 | `討論/研究會議記錄-005-決策治理層研究.md` | Research Meeting / Decision Governance | RESEARCH / CANDIDATE INPUT | 提出 Evidence→Proposal→Decision→Implementation→Verification 分離，以及 Adoption Gate；研究結論不能自行改變正式架構。 |
| G1-660 | `討論/研究會議記錄-006-長期演化層研究.md` | Research Meeting / Lifecycle Research | RESEARCH / CANDIDATE INPUT | 研究 System/Knowledge Lifecycle 與長期 System Entropy；可作未來藍圖輸入，不直接等同正式新增能力。 |

### 21.2 第六批的核心判定

這一批證明「討論／研究／紀錄」不能被簡單視為低價值歷史資料。

其中至少存在三種完全不同的資產：

1. **失效證據（Failure Evidence）**：例如新內容未問題化、統御方案建立錯誤。這些不是 Current 規則本身，但對驗證規則是否真正約束 AI 行動具有高價值。
2. **研究／外部證據（Research Evidence）**：研究會議與外部架構比對，應保留 provenance，必要時再將已確認結論蒸餾進正式 Canonical Source。
3. **工程演化紀錄（Engineering Change Record）**：例如方案四完善紀錄，用來解釋正式方案如何從舊版本演化，不能直接當成目前 State。

因此「History 不等於無用」；真正要做的是：**隔離其 Recall 權重，同時保留其證據價值。**

### 21.3 研究 → 採用的治理邊界

第 005 號研究紀錄提出的：

`Evidence → Proposal → Decision → Implementation → Verification`

與本次基線重建的 Source Priority、State、Evidence 分離高度一致，但目前仍屬研究結論，不能因研究文件存在就自行升格為新的正式治理規則。

同樣地，第 006 號對 System Entropy 的分析很有價值，尤其把長期腐化拆成 Semantic／State／Structural／Decision／Context／Historical 六類；目前應保留為研究資產，而不是現在立即建立六套新系統。

### 21.4 第六批處置原則

- 不把研究會議直接放進 CURRENT 規格層。
- 不刪除失效案例。
- 不因外部研究「支持」某方向就直接採用。
- 若未來正式採用，必須建立從 Evidence → Decision → Canonical Source 的可追溯鏈。
- Failure Record 應進入後續自然工作／回歸驗證的候選案例庫。
- 舊模式 Mapping 應作為未來重製輸入，不作為目前架構權威。

## 二十二、G1 第六批後進度

| 批次 | 範圍 | 狀態 |
|---|---|---|
| 第一批 | 目前工程入口、部分知識、部分系統、方案、根目錄藍圖 | 完成 |
| 第二批 | 0-知識／1-系統 Repository tree | 完成 |
| 第三批 | 2-方案 根目錄 Repository tree | 完成 |
| 第四批 | 2-方案/完善 Repository tree + 高優先證據追溯 | 完成 |
| 第五批 | 2-方案/統御 + 廢棄目錄檢查 | 完成 |
| 第六批 | 討論／研究／會議／紀錄 | 完成；11 個實質資產完成初判 |
| 第七批 | 根目錄其他企劃／模板／工具 | 待執行 |

G1 尚未完成，Migration 仍禁止。

## 二十三、G1 第七批：根目錄其他企劃／交接／待辦／參考／索引

本批依 Repository recursive tree 實際列出的剩餘 41 個 Markdown 資產進行初步分類。重點不是立即處置，而是先把「舊交接、早期整體企劃、待辦、參考資料、索引、英文舊目錄」從 CURRENT 與歷史混雜狀態中識別出來。

| Asset ID | 路徑 | 類型 | 初步 State | 初步處置／備註 |
|---|---|---|---|---|
| G1-700 | 0-knowledge/上下文成本.md | Knowledge / Legacy naming | REVIEW | 與 0-知識 語系目錄重疊，先確認是否舊副本；不可因路徑直接判定廢棄。 |
| G1-701 | 0-knowledge/人工智慧交接文件分工.md | Knowledge / Handoff | REVIEW | 與現行交接鏈相關，需與目前交接資料及交接規則比對。 |
| G1-702 | 0-knowledge/以證據決定架構.md | Knowledge / Architecture Principle | REVIEW | 可能是重要原則來源，需確認是否已被正式規則吸收。 |
| G1-703 | 0-knowledge/區分人工智慧輸出與知識真實性.md | Knowledge / Epistemic Principle | REVIEW | 與 Evidence / Knowledge truth boundary 相關，需追溯 Canonical Source。 |
| G1-704 | 0-knowledge/區分來源與知識.md | Knowledge / Source Principle | REVIEW | 與來源、知識及 Evidence 邊界相關，需追溯。 |
| G1-705 | 0-knowledge/區分目前狀態與設計歷史.md | Knowledge / State Principle | REVIEW | 與 Current / History 分離直接相關，需與基線規範比對。 |
| G1-706 | 0-knowledge/模型能力補償.md | Knowledge / AI Limitation | REVIEW | 可能是歷史設計原則；需確認目前適用性。 |
| G1-707 | 0-knowledge/知識分類.md | Knowledge / Classification | REVIEW | 可能與目前分類模型重疊；禁止直接以檔名判定權威。 |
| G1-708 | 0-knowledge/知識定義與邊界.md | Knowledge / Definition | REVIEW | 可能是知識層 Canonical 候選，需與 0-知識 正式文件比對。 |
| G1-709 | AI單人工作室主系統資料基線重建規範-v1.0.md | Governance / Baseline Specification | CURRENT / HIGH-PRIORITY | 本輪基線重建的正式規範；不得與一般歷史規劃混同。 |
| G1-710 | AI單人工作室四方案舊版本盤點報告-第一輪-v1.0.md | Audit / Historical Evidence | REVIEW / EVIDENCE | 四方案歷史版本盤點證據；不是新的正式方案。 |
| G1-711 | AI單人工作室整體系統企劃書-API版本-v0.1.md | Planning / Historical Architecture | HISTORICAL / EVIDENCE | API 版本早期整體企劃；與目前 No-API 約束存在歷史差異，保留演化證據。 |
| G1-712 | AI單人工作室整體系統企劃書-無API版本-v0.1.md | Planning / Architecture Candidate | HISTORICAL / EVIDENCE | 早期 No-API 架構企劃；需與 v0.2/v0.3 及現行架構比對。 |
| G1-713 | AI單人工作室整體系統企劃書-無API版本-v0.2.md | Planning / Architecture Candidate | HISTORICAL / EVIDENCE | 架構演化版本；不得直接取代現行正式工程入口。 |
| G1-714 | AI單人工作室整體系統企劃書-無API版本-v0.3.md | Planning / Architecture Candidate | REVIEW / PRE-CURRENT CANDIDATE | 較新的整體企劃候選；必須與現行正式鏈及 2026-09-18 外部比對紀錄確認關係後才可判定。 |
| G1-715 | AI單人工作室舊交接與工程快照比對報告-第一輪-v1.0.md | Audit / Handoff Evidence | HISTORICAL / EVIDENCE | 用於舊交接與快照比對；不可取代目前快照-005。 |
| G1-716 | 三方案角色與狀態澄清-v1.0.md | Governance / Clarification | HISTORICAL / EVIDENCE | 三方案演化中的角色與 State 澄清證據；需避免與四方案現況混淆。 |
| G1-717 | 交接修復記錄-v1.0.md | Handoff Repair Evidence | HISTORICAL / EVIDENCE | 保存交接失效與修復過程；與目前交接入口形成歷史證據鏈。 |
| G1-718 | 交接資料-v2.0.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-719 | 交接資料-v2.1.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-720 | 交接資料-v2.2.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-721 | 交接資料-v2.3.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-722 | 交接資料-v2.4.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-723 | 交接資料-v2.5.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-724 | 交接資料-v2.6.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-725 | 交接資料-v2.7.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-726 | 交接資料-v2.8.md | Handoff / Historical | HISTORICAL | 舊交接版本，保留歷史，不作 Current。 |
| G1-727 | 交接資料.md | Handoff / Historical | HISTORICAL | 最早交接文件；保留演化證據。 |
| G1-728 | 交接驗證-無記憶AI題詞與模擬-v1.0.md | Handoff Validation | HISTORICAL / EVIDENCE | 無記憶交接驗證證據；應保留測試結果。 |
| G1-729 | 交接驗證-無記憶AI題詞與模擬-v2.0.md | Handoff Validation | HISTORICAL / EVIDENCE | 較新版無記憶交接驗證證據；與目前 8/8 PASS 結論需追溯。 |
| G1-730 | 參考資料/目標守恆治理引擎_企劃書.md | Reference / Candidate | HISTORICAL / RESEARCH | 外部／候選治理方向；不得直接作為正式系統。 |
| G1-731 | 參考資料/重構治理系統研究與設計建議.md | Reference / Research | RESEARCH / CANDIDATE INPUT | 治理／重構研究資料；需與統御候選及舊模式 Mapping 交叉。 |
| G1-732 | 待辦/交接待辦與統御能力檢驗-v1.0.md | TODO / Validation | REVIEW / ACTIVE CANDIDATE | 待辦與能力檢驗資料；需與目前 FIELD 自然觸發狀態比對。 |
| G1-733 | 待辦/待辦工作記憶與施工順序-v1.0.md | TODO / Workflow | REVIEW | 可能保存施工順序原則；需與目前待辦清單及規則比對。 |
| G1-734 | 待辦/架構整合後續工作-v1.0.md | TODO / Integration Plan | REVIEW | 後續整合規劃；不得直接視為 CURRENT。 |
| G1-735 | 待辦清單-v2.0.md | TODO / Historical | HISTORICAL | 舊待辦版本，保留演化證據。 |
| G1-736 | 待辦清單-v2.1.md | TODO / Historical | HISTORICAL | 舊待辦版本，保留演化證據。 |
| G1-737 | 更新紀錄/2026-09.md | Change Log | HISTORICAL / EVIDENCE | 變更時間線；屬證據，不是 Current State。 |
| G1-738 | 檔案索引.md | Index / Derived View | CURRENT / DERIVED | 全庫定位索引；屬 Derived View，不取代 Canonical Source。 |
| G1-739 | 歷史方案與不採用方向.md | Historical Decision Index | CURRENT / DERIVED | 歷史方案／不採用方向索引；應隔離於一般 Current Recall。 |
| G1-740 | 說明.md | Repository Guide | REVIEW / ENTRY CANDIDATE | 需確認與 README、交接入口的責任邊界；不可自動升格第二入口。 |

### 23.1 第七批重要發現

**一、Repository 存在舊的 `0-knowledge/` 英文目錄。**

目前不能直接把它判定為廢棄，也不能把其中內容當成第二套 CURRENT 知識層。這是本輪發現的高優先級結構問題之一。下一階段必須逐項比對 `0-knowledge/` 與 `0-知識/`，判斷是舊版、複製、不同時期內容，還是仍有唯一有效內容。

**二、早期整體企劃存在 API → No-API 的架構演化鏈。**

因此不能用檔名「最新」直接選擇 v0.3。需要把 v0.1 → v0.2 → v0.3 與目前正式工程入口、2026-09-18 外部比對紀錄一起追溯，確認哪些內容已被吸收、哪些被淘汰、哪些仍是候選。

**三、舊交接文件數量很多，但目前正式入口仍只有 v2.9。**

本批不會因舊交接文件存在而建立第二個 Current Entry。舊交接的價值是歷史演化與交接失效證據。

**四、待辦不是狀態本身。**

舊待辦可以說明當時下一步，但不能直接覆蓋現在的 `快照-005`。State 必須以目前正式工程狀態鏈判定。

**五、索引與權威來源分離。**

`檔案索引.md` 是 Derived View。即使索引指出某文件位置，也不能因此提高該文件的權威等級。

### 23.2 G1 七批完成後的判定

G1 的「逐項盤點」階段已完成第一輪全庫覆蓋；但這不等於基線重建完成。

下一階段應停止繼續增加盤點表，轉入 **G2：跨資產衝突、版本漂移、Canonical Source、State 與 Recall 邊界重建**。

G2 第一優先應處理：

1. `0-knowledge/` ↔ `0-知識/` 重疊與唯一性。
2. `AI單人工作室整體系統企劃書` v0.1／v0.2／v0.3 ↔ CURRENT 架構關係。
3. `能力蒸餾與系統重構方案-v1.1` 的 State Conflict。
4. `AI知識管理方案-v2.0` 與內部 v2.1 的版本漂移。
5. `知識與資料迭代演化方案-v2.0` 與內部 v2.1 的版本漂移。
6. 舊交接／舊快照與目前 v2.9／快照-005 的覆蓋關係。
7. 研究／Evidence 是否已被正式 Canonical Source 吸收。

在上述問題完成前，**不得進行大規模 Migration、Delete、Merge 或 Rename。**
