# AI 單人工作室功能導向藍圖交接入口 v1.0

> 文件性質：【交接入口／Current Handoff View】
> 日期：2026-09-18
> Repository：upqq21477-star/Ai-knowledge
> 目的：讓沒有任何對話記憶的新 AI，在閱讀本入口後，能正確區分「目前工程狀態」與「未來功能導向藍圖」，並知道下一步應從哪裡讀取。
> 本文件不是第五方案，不新增工程責任；它只是既有資料的最小交接視圖。

---

## 一、這個專案是什麼

這是一套以 GPT／ChatGPT + GitHub 為核心的 AI 單人工作室外部記憶與工程治理環境。

GitHub 同時承擔：長期外部記憶、Canonical Source 保存、版本控制、證據與歷史追溯、AI 之間的 Handoff Boundary。

核心原則：

> 大記憶，小 Context；完整歷史，乾淨 CURRENT；完整能力，最小實體化。

目前仍是無 API 架構。不要因為閱讀未來藍圖，就假定 Vector DB、Agent Runtime、Event Bus、Scheduler、Worker、Multi-Agent Framework 或大型自動化 Orchestrator 已經存在。

## 二、目前正式工程架構

正式方案只有四個：
1. 方案一：整體資料治理
2. 方案二：AI 知識管理
3. 方案三：知識與資料迭代演化
4. 方案四：能力蒸餾與系統重構

正式功能清單：A1–A12、B1–B16、C1–C18、D1–D20。

目前四方案均已完成模擬／回歸驗收，進入正常工程運作。FIELD（Real-Work Validation）目前等待自然工作觸發，不人工製造 FIELD。

不要重新執行四方案總體驗收，也不要自行增加 A13、B17、C19、D21 等不存在的正式功能。

## 三、未來功能導向藍圖是什麼

「功能導向藍圖」不是第五方案，也不是目前已全部實體化的系統。

它回答長期問題：當 GPT、其他模型、工具與工作方法持續變強時，如何辨識哪些功能仍需要保留、哪些重疊、哪些可以部分取代、哪些應精簡、合併、重構或退役。

核心比較單位是 Capability（能力）。

Capability：可以被單獨描述、定位、測試、比較、觀察與替換的功能單位。

Provider 是目前提供該 Capability 的來源，例如 GPT／模型、System、Tool、Human。

Capability ≠ System ≠ Tool ≠ Software ≠ Provider。

## 四、最重要的關係語義

Knowledge、Capability、System、Plan、Task 不是強制線性 Pipeline。

不要理解成：Knowledge → Capability → System → Plan → Task。

正確理解是不同實體／責任之間存在多種關係：
- Knowledge：知道什麼，提供定義、證據、規則、歷史依據。
- Capability：能做什麼。
- System：如何把多項能力、資料與規則組合成可重複工作的結構。
- Plan：針對較大型問題如何安排解決方式。
- Task：目前要完成什麼。
- Provider：目前由誰提供某 Capability。

實際任務可以直接使用既有 Capability；也可以由 Plan 調度 System；Knowledge 可以作為支撐與依據。

## 五、四方案與 Capability 的關係

Capability 是跨方案的功能比較單位，不是第五方案。

目前已完成第一版實際 Mapping：A1–A12、B1–B16、C1–C18、D1–D20 均已映射到 Capability。

同一 Capability 可以由多個方案使用。例如 A11、C6、D13 都涉及 Impact Analysis，但三者的工程責任不因此合併成中央巨型 System。

> 共同 Capability ≠ 共同責任 ≠ 中央巨型系統。

## 六、目前 Mapping 的證據狀態

目前可直接由現行 Repository 證明：
- A1–A12：12/12
- B1–B16：16/16
- C1–C18：18/18
- D1–D20：20/20
- K01–K06：6/6
- S01–S10：10/10

目前沒有足夠現行權威來源可安全恢復：
- K07–K61：55 項
- S11–S37：27 項

禁止以編號、名稱或推測補造缺失內容。

## 七、Scenario Namespace 修復結果

S01–S10 已確認是方案三 Scenario。

功能導向藍圖正式使用：SCN-01～SCN-10。
S01～S10 僅保留為歷史來源識別。

其他 Namespace：Kxx=Knowledge、CAP-xxx=Capability、SYS-xxx=System、PLN-xxx=Plan、SCN-xxx=Scenario、EVD-xxx=Evidence、DEC-xxx=Decision。

S11–S37 尚未確認，不得自行指定 Namespace。

## 八、Capability ID 修復結果

原 Mapping 曾發生 CAP-55 ID 碰撞：K03 Trigger Registry 與 D20 Distillation Trigger。

目前正式修復：
- K03 → CAP-60 Trigger Registry
- D20 → CAP-61 Distillation Trigger

不得再次把兩者合併為 CAP-55。

## 九、目前最重要的工程邊界

功能導向藍圖目前是【未來規劃／長期藍圖】，不是【全部已實體化】。

Mapping 可以存在；Capability Matrix 可以作為 Derived View；Capability Registry、Graph Engine、自動 Orchestrator、Model Update 自動流程都不代表已經建立。

只有當實際工作出現重複瓶頸，才進入：實際使用 → Observation → 重複瓶頸 → 問題確認 → 候選方案 → 測試 → 驗證 → 建立／修改 → Regression → 正式採用。

## 十、模型更新時的未來流程

Model Update → Model Capability Profile → Capability Delta → 受影響 Capability → Provider 比較 → 反查 System / Plan / A/B/C/D → Scenario + Baseline + Test Corpus → Evaluation → Evidence → Decision → 必要時 Partial Replacement / Refactor → Regression → Cutover → Observation → Real-Work Validation → Distillation。

模型變強，不代表舊系統立即刪除。先比較、測試、取得 Evidence，再決定保留、精簡、部分取代、合併、重構、退役或移除。

## 十一、失敗處理原則

任何 Evolution／Replacement 失敗，不直接等於需要新增 System。

標準失敗閉環：Execution → Verification → Failure Classification → Diagnosis → Problem Confirmation → Solution Research → Fix Proposal → Implementation → Revalidation。

可能的失敗類型包括：資料不足、證據不足、資料衝突、Context 不足、Context 過量、Version / State 不適用、System Capability 不足、Plan 組合錯誤、Verification 不足。

## 十二、下一步

目前不要繼續擴充功能導向藍圖的抽象架構。

優先順序：
1. 維持四方案正常工程運作。
2. 回收 K07–K61 的歷史原始定義。
3. 回收 S11–S37 的歷史原始定義並確認真正 Namespace。
4. 保持現有 Mapping 作為 Derived View。
5. 等待自然模型更新、能力重疊或真實工作瓶頸。
6. 選擇實際案例進行第一次 Capability Evaluation。
7. 只有測試證明需要，才實體化新的 Registry、Graph、Automation 或其他系統。

## 十三、交接閱讀順序

L0：本文件。先理解目前狀態、邊界與禁止事項。

L1：閱讀「藍圖/AI單人工作室功能導向藍圖地圖-既有資產完整Mapping-v1.0.md」，查看 A/B/C/D Mapping、K/S 證據缺口、Capability 關係、Namespace 修復與模型更新路徑。

L2：閱讀「藍圖/AI單人工作室未來藍圖規劃書-功能導向架構-v1.0.md」，理解完整 Capability Lifecycle、Evaluation、Overlap、Migration、Distillation 與長期演化邏輯。

L3：需要施工或驗證時，再回讀四方案正式文件。不要因為看到未來藍圖就直接建立新系統。

## 十四、Memoryless Handoff 驗收標準

新 AI 讀完本入口、Mapping 與未來藍圖後，至少必須能回答：
1. 目前正式架構有幾個方案？四個。
2. 功能導向藍圖是不是第五方案？不是。
3. 四方案目前狀態？模擬／回歸完成，正常工程運作，FIELD 等自然觸發。
4. Capability 是什麼？功能比較與演化的基本單位。
5. Capability 是否等於 System？不等於。
6. Knowledge → Capability → System → Plan → Task 是否強制線性？不是。
7. K07–K61 能否自行補？不能。
8. S01–S10 是什麼？Scenario，正式藍圖語義使用 SCN-01～SCN-10。
9. K03 與 D20 是否可以共用 CAP-55？不可以；已修復為 CAP-60 與 CAP-61。
10. 是否應立即建立大型 Capability Registry / Graph Engine / Orchestrator？不應；先以實際瓶頸與測試證明需求。
11. 模型更新後是否立即刪除舊系統？不應；先比較與驗證。
12. 下一步最重要的是什麼？保持正常工程運作，回收缺失的歷史定義，等待自然實際案例。

## 十五、Canonical / Derived 邊界

本入口本身是【Derived Handoff View】，不是所有事實的唯一 Canonical Source。

真正責任仍由各自正式文件保存：四方案正式文件負責方案責任；Knowledge 原始文件負責 Knowledge 定義；Capability Mapping 負責目前 Mapping 視圖；Evidence / History 負責證據與歷史；Git Commit 負責版本控制與變更追溯。

若本入口與正式來源發生衝突，不能自行覆寫 Canonical Source；應回到來源文件進行驗證與修復。

## 十六、停止條件

本入口完成後，不再為了「交接看起來更完整」而無限增加交接層。

只有當實際 Memoryless Handoff 測試再次發現：新 AI 無法判斷目前狀態、無法找到 Canonical Source、對 Namespace 產生系統性誤解，或在實際工程操作中反覆犯同一類錯誤，才建立針對該問題的最小修正。

> 交接文件服務工程，不讓工程反過來服務文件。