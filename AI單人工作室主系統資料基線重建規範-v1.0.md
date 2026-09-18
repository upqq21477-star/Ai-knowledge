# AI 單人工作室主系統資料基線重建規範 v1.0

> 文件定位：未來藍圖 P0.5 前置工程規範。
>
> 文件目的：在大量 Mapping、Scenario、Evaluation 之前，將目前因規格演化而混雜的新舊資料重新建立可判定、可追溯、可供 AI 正確 Recall 的主系統基線。
>
> 本文件不是第五套正式方案，不新增 A/B/C/D 功能。

---

# 一、問題定義

目前 Repository 內存在不同時期形成的：

- 舊規格
- 新規格
- 草稿
- 研究資料
- 歷史決策
- 不同版本格式
- 重複內容
- 已被後續規格取代的內容
- 仍具有部分有效資訊的舊文件

這是規格尚未凍結期間的正常歷史結果。

目前不能直接把「文件存在」視為「目前有效」。

真正要解決的是：

> 讓主系統只暴露目前應被 AI 使用的有效資料，同時完整保留歷史資料的追溯能力。

---

# 二、最高原則

## 1. 不直接刪除歷史資料

舊資料先分類、再處置。

除非已確認沒有任何保存價值，否則優先：

- 保留
- 蒸餾
- 重製
- 移入歷史
- 移入備份

而不是直接刪除。

## 2. 主系統與歷史資料必須分離

主系統：

> CURRENT 工作依據。

歷史／備份：

> 曾經存在、可追溯，但不應在一般工作中被當成 CURRENT。

## 3. 狀態優先於路徑

資料是否有效，不由檔案放在哪裡決定。

路徑是承載位置；State 才是生命週期語意。

Git Commit 是變更證據，不取代 State 或 Version。

## 4. 不因整理而重新發明規格

本次工作只執行已確立的規格。

如果發現真正的規格缺口：

> 記錄為規格問題，不在清理過程中自行創造新規則。

## 5. 蒸餾不是摘要

蒸餾的目的不是單純縮短文件，而是：

> 從舊資料中保留仍有效的語意、決策、證據、限制與可用知識，並遷移到目前規格。

---

# 三、資料狀態

統一使用以下判定：

| State | 定義 | 一般工作是否可直接使用 |
|---|---|---|
| CURRENT | 目前有效且可作為工作依據 | 是 |
| REVIEW | 正在確認或尚未完成判定 | 否 |
| DEPRECATED | 已被較新內容取代 | 否 |
| RETIRED | 已停止使用 | 否 |
| HISTORICAL | 歷史有效資料，保留追溯價值 | 否 |
| UNKNOWN | 目前證據不足，無法可靠判定 | 否 |

注意：

> REVIEW、DEPRECATED、RETIRED、HISTORICAL、UNKNOWN 不代表「資料不存在」。

它們代表：

> 不應在沒有額外判定的情況下進入一般 CURRENT Context。

---

# 四、處置類型

每份舊資料必須最終得到一個主要處置：

| Disposition | 用途 |
|---|---|
| KEEP | 原資料仍有效，直接保留 |
| UPDATE | 小幅修正後成為 CURRENT |
| DISTILL | 抽取有效內容後重製 |
| MERGE | 與其他資料合併 |
| SPLIT | 拆成不同責任的資料 |
| ARCHIVE | 移入歷史／備份 |
| RETIRE | 明確停止使用 |
| DELETE | 確認無保存價值後移除 |

原則：

> DELETE 是最後處置，不是預設處置。

---

# 五、資料判定流程

每份舊資料依序判定：

~~~text
原始資料
  ↓
Identity
  ↓
來源／時間／版本
  ↓
目前規格比對
  ↓
是否仍有效？
  ├─ YES
  │   ↓
  │  是否格式仍適用？
  │   ├─ YES → KEEP
  │   └─ NO  → UPDATE / DISTILL
  │
  └─ NO
      ↓
     是否具有歷史／證據價值？
      ├─ YES → ARCHIVE / HISTORICAL
      └─ NO  → RETIRE / DELETE
~~~

若無法判定：

~~~text
UNKNOWN
  ↓
不得猜測
  ↓
進入 REVIEW
~~~

---

# 六、舊資料盤點

正式清理前，先建立 Inventory。

最低欄位：

| 欄位 | 說明 |
|---|---|
| Source Path | 原始路徑 |
| Identity | 資料身份 |
| Name | 文件名稱 |
| Type | 文件類型 |
| Topic | 主題 |
| Version | 已知版本 |
| State | 判定狀態 |
| Canonical Source | 是否有正式來源 |
| Current Counterpart | 是否存在目前對應 |
| Conflict | 是否存在衝突 |
| Duplicate | 是否重複 |
| Valid Content | 是否仍有有效內容 |
| Distillation Needed | 是否需要蒸餾 |
| Disposition | 最終處置 |
| Evidence | 判定依據 |
| Notes | 備註 |

盤點階段不得直接搬移大量檔案。

---

# 七、判定優先級

判定舊資料時，優先使用：

1. 已確認的 Canonical Source
2. 已驗收的正式方案文件
3. 已確認的正式責任整合文件
4. 已確認的規格／管理原則
5. 有明確 Evidence 的後續決策
6. 歷史討論與研究資料
7. 無法確認來源的草稿

高層級來源與低層級來源衝突時：

> 不直接融合兩者；回到 Canonical Source 判定。

---

# 八、新舊規格衝突處理

發現：

~~~text
舊規格 A
vs
CURRENT 規格 B
~~~

先確認：

- B 是否已正式確認
- A 是否仍有特殊適用範圍
- A 是否包含 B 沒有的有效資訊
- 是否存在不同時間／不同 Scope
- 是否只是格式不同而非語意衝突

處置：

~~~text
A 與 B 等價
→ 合併

A 部分仍有效
→ DISTILL

A 已被 B 取代
→ ARCHIVE / DEPRECATED

A 是否有效無法判定
→ REVIEW / UNKNOWN
~~~

禁止：

> 為了讓資料看起來整齊，直接把衝突內容人工「平均融合」。

---

# 九、蒸餾工具的正式角色

蒸餾工具在本次工程中負責：

- 舊格式 → 新格式
- 重複文件 → 結構化合併
- 新舊混合 → 拆分有效與歷史內容
- 長期討論 → 提取已確認決策
- 舊方案 → 提取仍有效的原理
- 舊資料 → 形成 CURRENT 所需最小有效內容

蒸餾後必須保留：

- 原始來源
- 判定依據
- 重要決策
- 限制條件
- 被取代資訊的歷史關係

不能只留下「結論摘要」而丟失可追溯性。

---

# 十、主系統／歷史／備份邊界

推薦邏輯：

~~~text
主系統
├── CURRENT
├── 正式規格
├── 有效知識
├── 有效能力
├── 有效 Scenario
└── 必要 Evidence / Decision

歷史與備份
├── DEPRECATED
├── RETIRED
├── HISTORICAL
├── 舊格式
├── 舊版本
├── 原始研究
└── UNKNOWN / REVIEW
~~~

實際 Repository 路徑可依既有架構決定。

本文件不強迫現在立即建立特定資料夾名稱。

---

# 十一、Context Hygiene

一般 AI 工作 Recall 的預設範圍：

~~~text
CURRENT
  ↓
相關已驗證 Capability
  ↓
相關 Evidence / Decision
  ↓
必要歷史
  ↓
外部資料
~~~

不得無差別把：

- DEPRECATED
- RETIRED
- HISTORICAL
- UNKNOWN
- 舊草稿

與 CURRENT 一起送入一般工作 Context。

需要歷史時：

> 明確提出 Historical Retrieval，再載入相關歷史資料。

---

# 十二、Migration 驗證

資料搬移完成後，至少驗證五件事：

## 1. 完整性

重要 CURRENT 資料沒有遺失。

## 2. 語意保真

蒸餾後沒有改變原始決策、限制或規格含義。

## 3. 狀態正確

已取代資料不再被標示為 CURRENT。

## 4. Recall 隔離

一般工作不會無差別召回歷史／廢棄資料。

## 5. 無記憶交接

以沒有本次歷史對話記憶的 AI，只提供主系統入口與 CURRENT 資料，應能理解：

- 目前系統是什麼
- 哪些規格有效
- 哪些資料不能直接使用
- 目前工程狀態
- 下一步工作

這是本次資料基線重建的重要驗收。

---

# 十三、清理執行順序

~~~text
Phase A
規則確認
    ↓
Phase B
全 Repository 盤點
    ↓
Phase C
建立 Inventory
    ↓
Phase D
Canonical Source 對照
    ↓
Phase E
CURRENT 候選確認
    ↓
Phase F
蒸餾／重製
    ↓
Phase G
舊資料分類
    ↓
Phase H
移入歷史／備份
    ↓
Phase I
建立 CURRENT Baseline
    ↓
Phase J
Recall / Context 驗證
    ↓
Phase K
Git Commit 固化
~~~

不得直接：

~~~text
看到舊檔
→ 覺得沒用
→ 移走／刪除
~~~

---

# 十四、與方案四的關係

本次資料基線重建會使用方案四已建立的：

- 蒸餾
- 重構
- 重疊分析
- 責任分析
- 取代
- 合併
- 拆分
- 保留
- 淘汰

但本次工作本身不是新增 D21。

它是：

> 將已存在的能力正式用於 Repository 歷史資料遷移。

---

# 十五、與未來藍圖的關係

本文件是：

> 未來藍圖 P0.5 的執行規範。

位置：

~~~text
P0 核心規格
 ↓
P0 AI 工作管理
 ↓
P0.5 主系統資料基線重建
 ↓
P1 Mapping
 ↓
P1 Scenario / Test / Evaluation
~~~

原因：

> 沒有乾淨的 CURRENT Baseline，就無法可靠判斷後續 Mapping 到底是在 Mapping「目前系統」，還是在 Mapping「歷史混合物」。

---

# 十六、禁止事項

1. 不直接刪除未判定資料。
2. 不把最新檔案自動視為 CURRENT。
3. 不把 Git Commit 當成 State。
4. 不把 Version 當成 State。
5. 不因路徑不同就推定語意不同。
6. 不因名稱相似就直接合併。
7. 不因名稱不同就直接視為不同能力。
8. 不把歷史資料直接混入一般 Context。
9. 不在清理過程中自行創造新的正式規格。
10. 不因追求「乾淨」而犧牲可追溯性。
11. 不為了完成清理而製造假的 CURRENT。
12. 不在 Inventory 尚未完成前進行大規模搬移。

---

# 十七、完成條件

P0.5 不以「所有舊檔案都移走」作為完成標準。

真正完成條件：

- 舊資料已盤點
- CURRENT 已可辨識
- 舊資料狀態已可判定或標記 UNKNOWN
- 有效內容已完成必要蒸餾
- 歷史資料仍可追溯
- 一般 Recall 不會無差別混入歷史資料
- 主系統形成明確 CURRENT Baseline
- Git Commit 固化此次基線
- 無記憶 AI 可以只依主系統理解目前狀態

最終目標：

> **不是讓 Repository 看起來乾淨，而是讓 AI 在工作時得到正確、最小、可追溯的有效 Context。**
