# RULES

> 本文件只規定「怎麼做」，不含設計理由。設計歷程與理由見交接文件 HANDOFF.md（目前暫置於 repository 根目錄，供開發階段參考；非正式操作規則，不在本文件重複其內容）。

## 1. 層級定義

- **Rules**（本文件）：定義系統怎麼運作，不存知識本身
- **Knowledge**：可跨場景重用的基本原理；不含專案決策；不預先建立彼此關係
- **System**：由兩份以上 Knowledge 組合而成、且已經實際重複使用過的方法／模型
- **Application**：組裝 System／Knowledge 解決具體需求的實際工具或方案

三條界線：Rules 不存知識本身／Knowledge 不預先建立關係也不含專案決策／每層更新互不強制連動（見第 7 節）。

## 2. Discovery 順序

優先序：INDEX → 判斷相關 → 深讀相關項目 → 必要時查最新資料。不要一次載入整個 repository。

- 建立 Application：優先掃描 `1-systems/INDEX.md`；System 涵蓋不到的部分，才往下查 `0-knowledge/INDEX.md`
- 建立 System：掃描 `0-knowledge/INDEX.md`
- 新專案／新場景開始：掃描 `0-knowledge/`、`1-systems/` 兩份 INDEX，判斷相關／不相關（二選一，不做多級分類）

## 3. AI 可讀性格式規則

> 背景：部分 AI（尤其是純網頁抓取工具）無法瀏覽 GitHub 的資料夾樹狀頁面（`/tree/xxx`），只能跟隨頁面中已經存在的明確連結。為了讓這類 AI 也能從 README.md 一路點進任何一份 Knowledge／System／Application，不需要使用者一個個貼網址，全系統的跨檔案／跨層引用一律使用 Markdown 相對路徑連結格式，不可只寫純文字檔名或路徑。

- **README.md 的 AI Entry Point**：對 RULES.md 與三份 INDEX.md 的引用，一律用連結，例如 `[0-knowledge/INDEX.md](./0-knowledge/INDEX.md)`
- **各層 INDEX.md 的「檔名」欄位**：一律用連結包住檔名，例如 `| [xxx.md](xxx.md) | 一句話用途 |`，不可只寫 `xxx.md` 純文字
- **System 的「組成的 Knowledge」欄位**：一律用連結，例如 `- [xxx.md](../0-knowledge/xxx.md)`
- **資料夾型 Application 的入口檔案連結**：沿用第 6 節既有規則——一律連結入口檔案，不可連結資料夾路徑本身

這條規則不需要額外工具或驗證機制，寫的時候養成習慣即可：GitHub 會在渲染頁面時，把相對路徑連結自動解析成完整網址，讓網頁抓取工具能直接跟隨，不需要瀏覽資料夾。

## 4. Knowledge 格式

檔名：`kebab-case.md`，放在 `0-knowledge/`。

```markdown
# [名稱]

> 一句話：解決什麼問題、什麼情境會用到、什麼情況不需要
> （這句話同時要放進 INDEX.md）

## 核心原理

## 適用情境

## 不適用情境

## 實務方法／注意事項

## 參考資料

## 我的補充
（個人經驗，需與上面的外部知識明確分開）
```

**類型標註（選填，只有補償型知識需要）**：

```
> 類型：模型能力補償
> 此知識為彌補當時模型限制而寫（例如：容易幻覺、易超出範圍作答）；
> 模型不再有此限制時，此知識應視為淘汰，而非被推翻。
```

**自包含原則**：可以引用其他 Knowledge（例如「詳見 [xxx.md](xxx.md)」），但不可以要求先讀懂別份才能理解本份。

**什麼不算 Knowledge**：單一專案的特殊設定、一次性 bug 或修法、只對某情境有效的決定、未驗證的原始資料——這些留在該 Application 自己的文件裡。

## 5. System 格式

檔名：`kebab-case.md`，放在 `1-systems/`。

**建立門檻**：至少兩份 Knowledge 已經被同一類問題**實際重複組合使用過一次以上**才能建立；「未來可能用到」不算數。

```markdown
# [名稱]

> 一句話：這個組合解決什麼類型的問題
> （這句話同時要放進 INDEX.md）

## 組成的 Knowledge
- [Knowledge A](../0-knowledge/knowledge-a.md)
- [Knowledge B](../0-knowledge/knowledge-b.md)

## 輸入／輸出／流程（選填，複雜組合才需要）

## 狀態
草稿 ／ 已驗證

## 適用情境

## 不適用情境
（Knowledge 之間如有衝突或但書，寫在這裡；不需要獨立的衝突處理流程）

## 參考資料／我的補充
```

「組成的 Knowledge」欄位即反查機制：某份 Knowledge 修改後，用檔名到 `1-systems/` 搜尋即可找出受影響的 System，不需要額外的 Dependency Database 或 Registry。

## 6. Application 格式

放在 `2-applications/`，可以是單一 `.md` 檔或一個資料夾。

**資料夾型 Application 必須有明確入口檔案**（例如 `README.md`）：`2-applications/INDEX.md` 一律連結入口檔案，不可連結資料夾路徑本身（資料夾路徑無法被單檔連結存取）。若資料夾內尚無明確入口檔案，應先建立後才登記進 INDEX.md。

```markdown
# [名稱]

## 目的

## 用到的 System／Knowledge

## 本專案特有的決策

## 狀態
草稿 ／ 已驗證
```

判斷子機制（搜尋、管理、分層等）是否該獨立成 System：這個子機制是否已經／即將被另一個不同的 Application 重複需要？否則一律留在該 Application 內部當自己的實作細節，不必抽象化。

**Application 與程式碼的關係**：若 Application 是「這套知識系統工具本身」要調度自己建立的 System（例如工具自己的搜尋、比對功能），對應實作留在本 repository；若是外部專案（例如某個軟體、遊戲），程式碼放在該專案自己的 repository，這裡只記錄「這個專案怎麼使用哪些 System／Knowledge」。

**工具自我調用的建立門檻**：不要預先把搜尋、比對等功能寫成程式。只有當某個 System 已經被手動使用驗證有效、且手動執行的成本已經高過寫程式的成本時，才把它實作成程式碼。

## 7. 更新規則

三層各自獨立判斷，互不強制連動：

**Rules**：只有「整套系統運作方式本身有問題」時才修改，低頻。

**Knowledge**：
- 不更新：新資訊只是補充、核心結論沒變、新工具出現但原理沒變
- 更新：原本有錯誤／新證據改變核心結論／實際使用發現重大限制
- 淘汰（不是更新，是整份不再需要）：標註「模型能力補償」，且目前使用的模型已不再出現當初要補償的限制——判斷時機是下次真的要用到它的時候，不排程稽核

**System**：
- 不更新：底層 Knowledge 只是小幅補充，沒影響組合邏輯
- 更新：底層 Knowledge 核心結論改變且確實影響此組合／實際使用發現明顯更好的組合方式

**連動範圍**：Knowledge 更新不自動要求 System 更新；System 更新不自動要求 Application 更新。每一層只在自己需要維護、重新檢查、或發現問題時，才回頭看上一層是否有更新。

## 8. Latest Check

只在問題具時效性時才查最新資料（例如：API／函式庫版本、模型能力變化），不做排程性的全面更新。

## 9. Feedback 分層

使用後的新發現，依性質歸類：
- 只對這次有用 → 留在該 Application 自己的文件
- 新的組合方式，可能被不同場景重複用到 → 走第 5 節，新增／更新 System
- 新的基本原理，可能被不同場景重複用到 → 走第 4 節，新增／更新 Knowledge

## 10. 檔案與棄用

- 檔名一律穩定，不加版本後綴（`v1`／`final`／`old`）；版本交給 Git 處理
- 淘汰一份 Knowledge／System：若不需要保留設計脈絡，直接刪除即可；若脈絡有參考價值，在淘汰的當下才建立 `_archive/` 資料夾並移入，不預先建立空的 archive 結構
- 如果 `_archive/` 存在，其內容一律不得被視為目前有效資料

## 11. 明確排除的機制

以下都不是核心機制，只是「未來如果真的痛了才考慮」的工具：

- Knowledge ID 編號系統
- 正式 Evidence Source 分級（A/B/C/D）
- Version History 表格、Update Trigger checklist
- Specification 版本化與 Migration 流程
- Capability 分類系統／正式需求解析層
- 五階段以上的 System 狀態機
- 正式衝突處理流程（Conflict → Identify → Resolve 這種獨立 pipeline）
- 多層 Context Loading／獨立索引系統（INDEX.md 已足夠）
- 自動化知識更新系統
- 中央 Knowledge Usage Table／Dependency Registry
- 預先建立的 `_archive/` 資料夾結構
- 檔名內嵌類別碼／版本碼（例如 `0-1-2.3-xxx.md`）——類別靠 INDEX.md 一句話用途即可判斷，版本交給 Git，草稿／已驗證狀態靠 System／Application 既有欄位

## 12. 新機制加入前的判斷

任何要加入這套系統的新功能，先問一句：

> 它是否直接降低下一次重新研究問題的成本？

沒有 → 不加。有 → 先評估能不能用更簡單的方式做到，優先用 Markdown + Git + INDEX，而不是資料庫、圖譜、儀表板或治理流程。
