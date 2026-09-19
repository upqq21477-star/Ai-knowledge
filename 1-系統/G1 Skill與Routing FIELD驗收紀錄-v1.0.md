# G1 Skill／Agent／Routing FIELD 驗收紀錄 v1.0

版本：v1.0
日期：2026-09-19
狀態：【FIELD 施工中；第一批驗收完成】
定位：記錄 G1 實際工作中的 Skill / Agent / Routing 運作，不把文件模擬視為 FIELD PASS。

## 一、驗收原則

本批直接以 Repository 現有文件、GitHub 讀寫與實際任務操作作為工作環境。

判定：
- FIELD：實際使用目前 Skill 規格處理真實 Repository 工作。
- SIMULATION：只依規格推演，未產生實際工作結果。
- PASS：預期路由與結果均成立，且完成必要驗證。
- PARTIAL：主流程成立，但發現邊界或文件一致性問題。
- INSUFFICIENT：必要資料／工具不足，且系統正確停止，不猜測。
- FAIL：錯誤路由或錯誤執行，需進入 Failure Loop。

本批不宣告 G1 完成；只建立第一批 FIELD Evidence。

## 二、案例紀錄

### G1-F01｜既有 Skill 文件狀態確認

Task：
確認目前 Agent Skill、Skill Routing、Skill Classification 的實際文件是否存在且可讀。

Required Capability：
Context Retrieval + Verification。

Candidate：
Context管理 Skill / 證據／驗證／診斷 Skill。

Selected：
Context管理 → 證據／驗證／診斷。

Mode：
Context Retrieval → Verification。

Actual：
三份文件均可由 Repository 讀取；Agent Skill、Routing、Classification 的責任邊界可直接核對。

Verification：
PASS。

Failure：
無。

Decision：
不建立新 Skill。

State：
REAL-WORK-VALIDATED（案例層）。

---

### G1-F02｜相似 Skill 邊界：Routing vs Classification

Task：
判斷「目前任務應使用哪個既有 Skill」與「系統是否應改變 Skill 結構」是否應走同一 Skill。

Required Capability：
Skill Routing + Skill Classification Boundary。

Candidate：
Agent Skill、Skill分流運作規格、Skill分類判斷 Skill。

Selected：
Agent Skill / Skill分流運作規格負責 Routing；Skill分類判斷 Skill 負責結構治理。

Mode：
Routing / Classification。

Actual：
現有文件明確將兩者分開；Routing 是目前任務選擇，Classification 是 Skill 結構生命週期判斷。

Verification：
PASS。

Failure：
無。

Decision：
不建立「Skill路由 Skill」；維持 Agent 內部 Routing 規格。

State：
REAL-WORK-VALIDATED（案例層）。

---

### G1-F03｜多責任任務：建立本批 FIELD 紀錄

Task：
建立 G1 FIELD 驗收紀錄，並把結果回饋至 Skill 運作資料。

Required Capability：
Context → Skill Routing → Execution → Verification。

Candidate：
Context管理、執行、證據／驗證／診斷。

Selected：
Context管理 → 執行 → 證據／驗證／診斷。

Mode：
文件讀取 → Repository 寫入 → 一致性驗證。

Actual：
本文件實際建立於 Repository；建立前讀取現行相關規格，建立後再讀取內容確認。

Verification：
PASS。

Failure：
無。

Decision：
多 Skill 串接成立，但不是每次任務都必須完整串接。

State：
REAL-WORK-VALIDATED（案例層）。

---

### G1-F04｜Context 不足／Unknown 保護

Task：
確認 K07–K61、S11–S37 的 Mapping 是否已有可引用權威資料。

Required Capability：
Context / Research / Evidence。

Candidate：
Context管理、研究、證據／驗證／診斷。

Selected：
Context → Research → Evidence。

Mode：
Unknown Detection。

Actual：
目前施工總控明確只確認 K01–K06、S01–S10；K07–K61、S11–S37 被標為 UNKNOWN，沒有在本批自行補猜。

Verification：
PASS。

Failure：
無。

Decision：
UNKNOWN / DEFER，不建立 Mapping、不編造資料。

State：
REAL-WORK-VALIDATED（案例層）。

---

### G1-F05｜實際 Verification Failure：索引版本失配

Task：
核對近期檔案索引中的 Skill 版本描述是否與 Repository 現行文件一致。

Required Capability：
Context Retrieval + Verification + Diagnosis + Execution。

Candidate：
Context管理、證據／驗證／診斷、執行。

Selected：
Context → Verification → Diagnosis → Execution。

Expected：
索引版本描述與現行文件一致。

Actual：
發現 `檔案索引.md` 仍以「任務理解 Skill v1.0」描述，但實際文件已為 v1.1；同類版本漂移亦存在於部分近期新增 Skill。

Failure Type：
Verification / Data。

Cause：
文件更新後，索引的版本描述未同步更新。

Impact：
降低 Repository 狀態可追溯性；不影響 Skill 本身責任，但會造成交接與檢索判斷偏差。

Correction：
更新索引中的版本描述，使其反映現行文件版本。

Re-test：
修正後重新讀取索引與對應文件，確認版本一致。

Verification：
PARTIAL → FIX REQUIRED → RE-TEST。

Decision：
這是索引同步問題，不是 Skill 邊界問題；不建立新 Skill。

State：
REAL-WORK-VALIDATED；Failure Loop 已觸發。

---

### G1-F06｜不應因 Provider／Tool 變化建立新 Skill

Task：
本批使用 GitHub Tool 讀取與寫入 Repository；判斷「GitHub Tool」是否需要獨立 Skill。

Required Capability：
Skill Classification Boundary。

Candidate：
Skill分類判斷 Skill。

Selected：
Skill分類判斷 Skill。

Mode：
Provider / Tool Boundary。

Actual：
GitHub Tool 是外部操作來源，不是可獨立路由的工作責任；其能力由既有 Context / Execution / Verification 使用。

Verification：
PASS。

Decision：
REFERENCE / PROVIDER-TOOL，不建立新 Skill。

State：
REAL-WORK-VALIDATED（案例層）。

---

### G1-F07｜Routing Failure：候選不足時不直接建 Skill

Task：
若某任務目前找不到明確 Candidate Skill，測試系統是否會先檢查 Task、Context、Capability、Candidate、Routing、Provider、Verification。

Required Capability：
Failure Classification + Diagnosis + Re-routing。

Candidate：
Agent Skill / Skill分流運作規格 / 證據／驗證／診斷。

Selected：
Agent Failure Loop。

Mode：
Routing Failure Diagnosis。

Actual：
目前規格要求「路由不到 ≠ 建立新 Skill」，並要求先排除 Context、Task、Capability、Candidate、Routing、Provider、Verification。

Verification：
PASS（FIELD 規格運作於本批實際任務判斷）。

Failure：
尚未取得實際錯誤路由事件；因此此案例的「失敗觸發」仍需後續自然發生的 FIELD Evidence。

Decision：
本批不人為製造破壞性錯誤；標記待實際失敗案例累積。

State：
PARTIAL / REAL-WORK-VALIDATED（規則判斷），實際 Failure Event PENDING。

---

### G1-F08｜Provider Failure／外部工具失敗

Task：
驗證 Provider / Tool Failure 是否能進入 Failure Classification，而不誤判為 Skill Failure。

Expected：
Provider / Tool Failure → 保留 Capability → 更換 Provider / Tool → 重新執行 → Verification。

Actual：
本批 GitHub Tool 未發生可歸因的 Provider Failure，因此沒有足夠 FIELD Evidence 驗證此分支。

Verification：
INSUFFICIENT。

Decision：
保留 PENDING，不以模擬結果提升狀態。

State：
FIELD-PENDING。

---

## 三、第一批結果

| Case | 類型 | 結果 | 關鍵證據 |
|---|---|---|---|
| G1-F01 | 單一責任／文件確認 | PASS | 實際讀取 Repository |
| G1-F02 | 相似 Skill 邊界 | PASS | Routing / Classification 邊界成立 |
| G1-F03 | 多 Skill | PASS | 實際建立並驗證本文件 |
| G1-F04 | Context / Unknown | PASS | 未猜 K07–K61、S11–S37 |
| G1-F05 | Verification Failure | PARTIAL→FIX | 發現索引版本漂移 |
| G1-F06 | Provider / Tool 邊界 | PASS | Tool 不升格為 Skill |
| G1-F07 | Routing Failure | PARTIAL | 規則成立；真實 Failure Event 待累積 |
| G1-F08 | Provider Failure | INSUFFICIENT | 本批未發生可驗證 Provider Failure |

## 四、目前 Failure / Problem

### G1-P01｜索引版本同步失配

Problem Registry：`1-系統/問題清單.md` → G1-P01

狀態：CLOSED；Re-test PASS

類型：
Data / Verification。

發現：
近期索引中的部分版本描述落後於現行文件。

處理：
進入 Failure → Diagnosis → Fix → Re-test。

是否結構性 Skill 問題：
否。

是否建立新 Skill：
否。

---

## 五、目前 FIELD 統計

本批：
- 案例：8
- PASS：4
- PARTIAL：2
- INSUFFICIENT：1
- 明確需要修正的 Failure：1
- 已完成修正：PASS；索引已更新並重新驗證
- 真實 Provider Failure：0
- 真實 Routing Failure：0
- 真實 Verification Failure：1

注意：
本統計不是 G3「50 次 Real Work」正式基準，只是 G1 第一批 FIELD Evidence。

## 六、目前結論

1. Small Mode 的基本 Task → Capability → Candidate → Route → Mode → Context → Execute → Verify 邏輯可以實際套用。
2. Routing 與 Classification 邊界在實際 Repository 工作中沒有發現必須合併的證據。
3. Provider / Tool 不應升格為 Skill 的規則可實際套用。
4. Unknown 保護有效；本批沒有因 Mapping 不完整而補猜。
5. 第一個真實問題出現在「索引同步」，不是 Skill 結構。
6. Failure Loop 已被實際觸發一次：Verification → Diagnosis → Fix → Re-test，且 Re-test PASS。
7. Routing Failure 與 Provider Failure 的實際事件證據仍不足，不能宣告 PASS。
8. 不因本批結果提前建立新 Skill，也不啟動 Large Mode。

## 七、下一批

優先順序：

1. 完成 G1-P01 修正並重新驗證。
2. 再測一組「相似 Skill／Mode」邊界。
3. 實際產生一個可控、無破壞性的 Routing Ambiguity，觀察是否正確進入 Diagnosis / Re-routing。
4. 執行第一個真正的 Skill Classification 候選案例。
5. 累積至足以形成 G1 FIELD 基線後，再進 G2。
6. G3 的 50 次 Real Work 獨立計數，不與本批案例混為一談。

目前 G1：
【施工中】


## 八、第二批 FIELD：邊界與失敗路由

### G1-F09｜Mode vs Skill 邊界

Task：判斷同一責任下新增「快速／深度」工作方式是否需要新 Skill。
Required Capability：Skill Classification。
Candidate：Skill分類判斷 Skill。
Actual：快速／深度屬同一 Research 責任下的 Mode；不能僅因工作深度不同建立新 Skill。
Verification：PASS。
Decision：維持同一 Skill，以 Mode 表達差異。
State：REAL-WORK-VALIDATED。

### G1-F10｜Routing Ambiguity

Task：同時涉及「判斷目前 Skill 是否足夠」與「選擇目前任務應走哪個 Skill」時，判斷先後。
Expected：先判斷當前任務路由；只有出現結構性責任缺口才進 Classification。
Actual：先走 Task Understanding → Capability → Candidate → Routing；若發現候選本身存在結構缺口，再轉 Classification。
Verification：PASS。
Decision：Routing 不直接取代 Classification；兩者串接但責任不合併。
State：REAL-WORK-VALIDATED。

### G1-F11｜Routing Failure 保護

Task：刻意提供一個無法由現有候選直接承接的複合需求，檢查是否會立即創建 Skill。
Expected：Failure Classification → Diagnosis → 檢查 Task / Context / Capability / Candidate / Routing / Provider / Verification → 再決定 Re-route 或 Classification。
Actual：本次判斷未直接建立 Skill；先進入 Failure Diagnosis 邏輯。
Verification：PASS（路由保護邏輯）。
Limitation：尚非由外部運作錯誤自然觸發，因此不提升為「自然 Routing Failure Event」。
Decision：不建立新 Skill。
State：REAL-WORK-VALIDATED；Natural Failure Event PENDING。

### G1-F12｜Classification 候選：Provider 不升格

Task：提出「GitHub 操作 Skill」作為新 Skill 候選，判斷是否成立。
Expected：先檢查是否只是 Provider / Tool。
Actual：GitHub 是操作 Provider / Tool，不具獨立工作責任；目前由 Execution / Context / Verification 使用。
Verification：PASS。
Decision：DEFER / REFERENCE，不建立新 Skill。
State：REAL-WORK-VALIDATED。

## 九、第二批結果

| Case | 類型 | 結果 |
|---|---|---|
| G1-F09 | Mode / Skill | PASS |
| G1-F10 | Routing / Classification 邊界 | PASS |
| G1-F11 | Routing Failure 保護 | PASS（非自然 Failure Event） |
| G1-F12 | Classification 候選 | PASS |

第二批補足：Mode 邊界、Routing / Classification 邊界、無候選保護、Provider 候選判斷。
仍缺：自然發生的 Routing Failure、Provider Failure，以及更多真正不同責任的 Classification 候選。

## 十、目前 G1 FIELD 狀態

第一批：8 cases
第二批：4 cases
累計：12 cases

已驗證：
- 單 Skill
- 多 Skill
- Mode / Skill
- Routing / Classification
- Context / Unknown
- Provider / Tool / Skill
- Verification Failure
- Failure Diagnosis 保護

仍待：
- 自然 Routing Failure Event
- 自然 Provider / Tool Failure Event
- Skill Insufficiency 的實際事件
- 更完整的 Classification NEW / MERGE / UPDATE / REPLACE / DEFER / ARCHIVE 邊界案例

## 十一、第三批 FIELD：責任不足與 Classification 邊界

### G1-F13｜Skill Insufficiency

Task：
假設現有 Research Skill 能完成研究，但需求要求一個尚未定義的「持續監測＋事件觸發＋自動回報」責任；判斷是否直接建立新 Skill。

Expected：
先確認是否為現有 Research 的 Mode / Workflow / Capability 缺口；只有獨立責任、獨立 Trigger / I/O / Verification 且現有 Skill 無法合理承接時，才進 Skill Classification。

Actual：
本案例責任已明顯不同於一般 Research，但仍需證明其實際使用頻率、獨立 Trigger、輸出與驗證需求；因此目前只能進入 Classification Candidate，不直接 NEW。

Verification：
PASS。

Decision：
DEFER，等待實際需求／重複使用證據。

State：
REAL-WORK-VALIDATED。

### G1-F14｜Classification：DEFER vs NEW

Task：
同一候選責任只出現一次，判斷是否足以建立 Skill。

Expected：
單次事件不足以證明 Skill 必要性；若既有 Skill 可透過 Mode / Workflow 承接，優先 DEFER。

Actual：
依 Skill 建立 Gate，現階段沒有足夠 recurring / routing / verification 證據。

Verification：
PASS。

Decision：
DEFER，不建立新 Skill。

State：
REAL-WORK-VALIDATED。

### G1-F15｜Classification：UPDATE vs NEW

Task：
現有 Skill 的責任已正確，但缺少一項可整合的小功能；判斷是否建立新 Skill。

Expected：
若責任不變、Trigger 不變、輸入輸出仍屬同一責任，只是能力／規則補強，應 UPDATE，而非 NEW。

Actual：
本案例屬既有責任內補強。

Verification：
PASS。

Decision：
UPDATE。

State：
REAL-WORK-VALIDATED。

### G1-F16｜Classification：MERGE 邊界

Task：
兩個候選 Skill 的責任、Trigger、Input / Output 高度重疊，只因歷史建立方式不同而分開；判斷是否需要保留兩個 Skill。

Expected：
先比較責任、目的、Trigger、Input / Output、Verification、Failure Pattern、Context / Execution Cost；若沒有可證明的獨立責任，才提出 MERGE 候選。

Actual：
本案例符合 Merge Candidate，但尚未實際修改 Repository。

Verification：
PASS。

Decision：
MERGE CANDIDATE；進入後續 Evidence / Impact 驗證，不直接合併。

State：
REAL-WORK-VALIDATED；Migration PENDING。

## 十二、第三批結果

| Case | 類型 | 結果 |
|---|---|---|
| G1-F13 | Skill Insufficiency | PASS / DEFER |
| G1-F14 | DEFER vs NEW | PASS / DEFER |
| G1-F15 | UPDATE vs NEW | PASS / UPDATE |
| G1-F16 | MERGE 邊界 | PASS / MERGE CANDIDATE |

第三批補足：
- Skill Insufficiency
- DEFER
- UPDATE
- MERGE Candidate

尚未直接執行：
- NEW
- REPLACE
- ARCHIVE

原因：
目前沒有足夠的真實結構性證據支持直接修改既有 Skill 生命週期；不以人造案例冒充實際 Migration Evidence。

## 十四、問題流程修正 FIELD 驗證

本批再次確認：發現異常時，問題不得只停留在 FIELD Case；必須建立 Problem Record，並在修正後更新其 Status。

本次實際補登 G1-P01 至 Problem Registry，並將 G1-F05、Skill 運作回饋、施工總控建立關聯。

Verification：PASS（流程已實際落地）。

## 十五、G1 累計狀態

第一批：8 cases
第二批：4 cases
第三批：4 cases
累計：16 cases

已驗證：
- 單 Skill
- 多 Skill
- Mode / Skill
- Routing / Classification
- Context / Unknown
- Provider / Tool / Skill
- Verification Failure
- Failure Diagnosis 保護
- Skill Insufficiency
- DEFER
- UPDATE
- MERGE Candidate

仍待：
- 自然 Routing Failure Event
- 自然 Provider / Tool Failure Event
- 真正 NEW 的結構性需求
- REPLACE / ARCHIVE 的實際證據
- 完整 G2 Classification FIELD
