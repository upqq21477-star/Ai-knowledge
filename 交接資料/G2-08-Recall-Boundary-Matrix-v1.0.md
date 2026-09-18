# G2-08 Recall Boundary Matrix

日期：2026-09-18
狀態：【G2-08 COMPLETE】
性質：Derived Recall / Context Safety Audit

## 一、目的

G2-08 的目的不是搬檔，而是先回答：一個沒有歷史記憶的 AI，在不同任務下，哪些 Repository 資料可以直接進入一般 CURRENT Recall，哪些必須按需載入，哪些只能作歷史／研究追溯，哪些必須隔離，哪些尚未判定。

## 二、正式邊界

| Boundary | 意義 | 預設 Recall |
|---|---|---|
| CURRENT | 目前有效工作依據 | 可直接載入 |
| RELEVANT EVIDENCE | 與目前任務直接相關的證據／決策 | 按任務載入 |
| HISTORY | 已退場但具有追溯價值 | 明確追溯才載入 |
| RESEARCH | 研究／外部比較／候選輸入 | 明確研究任務才載入 |
| DEPRECATED / RETIRED | 已被取代或停止使用 | 預設隔離 |
| UNKNOWN / REVIEW | 證據不足，尚未可靠判定 | 禁止當 CURRENT 使用 |

Recall Boundary 是使用邊界，不等於物理資料夾。同一路徑內可以存在不同 State；不能靠資料夾名稱取代 State。

## 三、CURRENT Recall

### 最小 CURRENT 工程 Recall

新 AI 若只要回答「現在在哪裡、下一步是什麼、不能做什麼」，優先讀：

1. README.md
2. 2-方案/完善/目前工程狀態快照-005.md
3. 規則.md
4. 待辦清單.md
5. 交接資料-v2.9.md（重大交接背景）
6. 交接資料/AI單人工作室全庫基線重建交接文件-G1完成_G2待續-v1.0.md（本次 G1/G2 Task State）

第 6 項只管理 G1/G2 Task State，不取代快照-005 的整體工程 State。

### CURRENT Support

按任務需要加入：目前狀態.md、1-系統/AI上下文與交接系統.md、2-方案/工程運作與持續改進方案-v1.8.md、AI單人工作室主系統資料基線重建規範-v1.0.md，以及具體任務所需的正式 0-知識／1-系統／2-方案文件。

## 四、RELEVANT EVIDENCE

Evidence 不應全部進一般 Context。只有與目前任務直接相關時才載入。

主要基線 Evidence：G2-01～G2-07 報告。它們是 Derived Evidence，不是整體工程 CURRENT Cursor。

## 五、HISTORY

以下資料保留追溯價值，但不得在一般工作中自動進入 Context：交接資料-v2.0～v2.8、快照-001～004、舊工程運作方案、已取代舊方案版本、歷史交接驗證、歷史變更紀錄、舊格式文件。

HISTORY 的目的不是無用，而是當前工作需要解釋「為什麼現在會是這樣」時才回頭載入。

## 六、RESEARCH

研究資料包括討論/研究會議記錄-001～006、紀錄/整體架構外部比對與合理性驗證紀錄-2026-09-18.md、參考資料研究與候選方向、藍圖／整體企劃候選版本。

研究資料不能因為結論合理就自動升格 CURRENT。

正確鏈：Research → Evidence → Candidate → Decision → Canonical Source → Implementation → Verification。

G2-07 已確認部分研究完成這條鏈，部分仍停在 Candidate / Partial Implementation / FIELD-PENDING。

## 七、DEPRECATED / RETIRED

此層目前以 State 隔離，不要求立即建立新的物理 Archive 目錄。

已明確具有歷史／取代性質的內容包括：舊 0-knowledge 已移至 舊資料/0-knowledge/、舊交接 v2.0～v2.8、舊快照 001～004、已被後續版本取代的方案文件。

HISTORICAL 與 DEPRECATED 不應混為一談：HISTORICAL 是保留追溯價值但不代表現在；DEPRECATED 是已有較新替代物；RETIRED 是明確停止使用。

沒有證據時，不得自行把 REVIEW 文件標成 DEPRECATED。

## 八、UNKNOWN / REVIEW

若文件沒有可靠來源、與 CURRENT 發生衝突但尚未查清、State 與後續 Evidence 不一致、不知道是否仍適用、只能靠檔名／路徑判斷，或研究結論尚未完成採用決策，則標為 UNKNOWN / REVIEW。

典型案例包括：能力蒸餾與系統重構方案-v1.1 的舊內部 State、部分舊知識文件在完成 Source Trace 前、無API v0.3 尚未被 CURRENT 明確吸收的候選內容、尚未完成自然 FIELD 的候選能力。

## 九、Recall 決策流程

任務 → CURRENT Recall → 是否需要證據？→ Relevant Evidence → 是否需要歷史？→ History Retrieval → 是否研究／候選問題？→ Research Retrieval。

若搜尋命中 UNKNOWN / REVIEW：停止當作事實 → Source Trace → 判定後再使用。

## 十、禁止的 Recall 行為

1. 禁止全庫平鋪 Recall。
2. 禁止用最新 Commit／修改時間直接判定 CURRENT。
3. 禁止用資料夾直接判定權威。
4. 禁止用版本號直接判定 State。
5. 禁止研究結果直接進 CURRENT。

## 十一、Recall 與無記憶交接

新 AI 第一輪 Recall 應得到：目前工程正常運作；四方案 A1～A12、B1～B16、C1～C18、D1～D20 已完成模擬／回歸；FIELD 待自然觸發；CURRENT 工程游標為快照-005；本次基線 Task 為 G2-08；不建立第五方案；不把歷史文件當 CURRENT；不直接 Migration；不人工製造 FIELD。

需要理解為什麼，再進入交接-v2.9 → G2-01～G2-07 Evidence；需要研究架構，再進 Research / Blueprint / Candidate。

核心原則：小 CURRENT Context；按需增加 Evidence；必要時才進 History / Research。

## 十二、Recall Safety 驗收

PASS 條件：
1. 新 AI 不讀歷史也能知道 CURRENT。
2. 新 AI 能知道歷史不是 CURRENT。
3. 搜尋命中舊文件不會自動採用。
4. 新 AI 知道研究不能直接改變正式架構。
5. 新 AI 能按需沿 Evidence → History / Research 追溯。
6. UNKNOWN / REVIEW 不會被當成已確認事實。
7. Migration 前仍保留 State / Source Trace / Recall 邊界。

目前判定：【PASS — 規則／文件結構級】。

依據：G2-04 CURRENT Authority Matrix、G2-05 Handoff Evolution Matrix、G2-06 State Evolution Matrix、G2-07 Research-to-Verification Traceability、主系統資料基線重建規範、全庫第一輪資產清冊。

但：【FIELD-PENDING】。尚未以長期自然工作流量測舊資料誤召回率。

## 十三、G2-08 最終判定

G2-08：PASS（Recall Boundary Established）。

已完成 Recall 層級、CURRENT 最小入口、Evidence 按需載入、History 明確追溯、Research 明確研究載入、Deprecated / Retired 隔離原則、Unknown / Review 安全閘、Recall 禁止行為與無記憶交接 Recall 驗收條件。

本輪沒有大規模搬檔、刪除、第五方案、Recall Engine、歷史改寫或人工 FIELD。

## 十四、下一步

G2-08 完成後，必須重新讀取主系統基線規範與交接文件中 G2-09 的實際定義；不得自行發明 G2-09。若 G2 尚未定義 G2-09，則停止並先修正基線交接工程順序，而不是自行擴張。