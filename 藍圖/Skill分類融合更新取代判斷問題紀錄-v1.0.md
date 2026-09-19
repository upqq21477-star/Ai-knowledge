# Skill分類、融合、更新與取代判斷問題紀錄 v1.0

版本：v1.0
日期：2026-09-19
狀態：【流程紀錄／候選知識；尚非正式 Skill】
用途：保存本次功能盤點、蒸餾、Skill 化、反向驗證過程中遇到的問題與解法，未來用於建立「新 Skill 應分類、融合、更新、取代或保留」的判斷 Skill。

## 一、核心目的
新能力出現時，不直接新增 Skill。先判斷：是否已有相同能力、是否只是新 Provider、是否只是新 Mode、是否應融合、更新、取代、拆分，或其實只應成為 Reference / Rule / Shared Capability。

## 二、本次實際問題與解決方案

### P01 過早建立新架構
問題：直接建立 Master Agent → Project → Solution → System → Knowledge 五層架構。
原因：未先盤點成熟 Agent / Skill / Tool / Knowledge 類型。
解決：先做既有解法審查，再比較自建架構。
規則：若現有能力已能承接，不新增架構。

### P02 功能數量被誤當成 Skill 數量
問題：66 個 A/B/C/D 功能容易直接變成大量 Skill。
原因：以歷史功能邊界代替實際責任邊界。
解決：去除方案、版本、編號後按真正責任聚合。
規則：66 功能不等於 66 Skill。

### P03 一對一 Mapping 導致重複
問題：A11、C6、D13 都是 Impact，若各自建立會重複。
解決：聚合為共同 Impact Capability，但保留不同使用情境與責任。
規則：先判斷共同能力與責任差異，再決定融合程度。

### P04 Search 與 Research 混合
問題：快速查找與完整研究成本不同。
解決：同一 Research Skill 內保留 Search / Deep Research Mode 的候選。
規則：模式差異不自動產生新 Skill。

### P05 Evidence 與 Verification 混淆
問題：兩者都使用證據與判定，但目的不同。
解決：同一 Skill 內分 Evidence Mode 與 Verification Mode。
規則：共享資料結構與判斷機制時可合併 Skill、保留 Mode。

### P06 Verification 與 Problem Diagnosis 混淆
問題：Verification 回答是否正確；Diagnosis 回答為何錯。
解決：目前先保持責任分開，後續以真實案例驗證是否可融合。
規則：判斷結果與找原因原則上先分責任。

### P07 Context 與 Knowledge 混淆
問題：兩者都處理資料。
解決：Knowledge 管理資料生命週期；Context 管理目前任務應載入什麼。
規則：資料生命週期不等於任務上下文。

### P08 Execution 與 Decision 混淆
問題：容易把決定改什麼與實際修改混在一起。
解決：Evolution 負責判斷與候選；Execution 負責執行已確認動作。
規則：Decision 與 Execution 不因流程連續而自動融合。

### P09 Change 與 Distillation 層級混淆
問題：局部修正與長期結構重構可能使用相似分析。
解決：Change 處理一般演化；Distillation 處理長期、重複、重疊、責任漂移與結構性成本。
規則：不是問題很大就 Distillation，必須有結構性證據。

### P10 Impact / Migration 不應固定啟動
問題：固定經過會增加 Token 與執行成本。
解決：改成條件式能力，只有相容性、依賴或結構變動時啟動。
規則：Skill 路由必須允許條件式跳過。

### P11 Mapping 被誤認為 Canonical Source
問題：Mapping 表可能變成第二套真實資料庫。
解決：Mapping 定位為 Derived View；原始責任文件與 Canonical Data 才是來源。
規則：聚合表必須標示是否為 Derived View。

### P12 未確認 K07–K61、S11–S37 被自行補猜
問題：為了完整而推測缺失內容。
解決：只保留目前直接驗證的 K01–K06、S01–S10；未知保持待回收。
規則：缺資料標記 UNKNOWN，不得用合理性推測原始內容。

### P13 S Namespace 碰撞
問題：S01–S10 已是 Scenario，不能同時假定 S 為 System Namespace。
解決：Scenario 改用 SCN-01…，原 S01–S10 保留為歷史識別。
規則：Namespace 必須具有唯一語義。

### P14 Simulation PASS 被誤認為 Field PASS
問題：61/61 PASS 只是模擬驗收。
解決：分離 SIMULATION-PASSED 與 FIELD-PENDING。
規則：測試結果必須帶驗證層級。

### P15 Provider 與 Capability 混淆
問題：GPT、Repository、System、Tool 都可能提供同一能力。
解決：Capability 是要完成什麼；Provider 是誰提供；Skill 是如何組織可重用工作；Tool 是外部操作。
規則：Provider 改變不等於 Capability 消失。

### P16 新 Skill 過度依賴名稱
問題：新工具、新模型、新方法容易直接產生新 Skill。
解決：先判斷是新能力、既有能力的新 Provider、既有 Skill 的新 Mode、Reference、Rule 或 Tool。
規則：只有新增獨立責任才考慮新 Skill。

## 三、反向驗證結果
原 11 個候選 Skill：Task Understanding、Search、Research、Evidence / Verification、Context Management、Knowledge Management、Execution、Problem Diagnosis、Change Management、Impact / Migration、Distillation。
S01–S10：PASS。
I01–I08：PASS。
功能覆蓋：PASS；必要功能遺失：0；重大路由錯誤：0。

## 四、目前 8 Skill 壓縮候選
1. Task Understanding
2. Research（含 Search / Deep Research Mode）
3. Context Management
4. Evidence / Verification / Diagnosis（需保留 Mode 邊界）
5. Knowledge Management
6. Execution
7. Evolution Management（融合 Change + Impact / Migration）
8. Distillation
狀態：候選，尚未定案。

## 五、未來 Skill 分類判斷器的決策順序
N → 定義責任 → 確認 Input / Output → 確認 Trigger → 確認實際使用 → 反查既有 Skill → 判斷是否已有相同責任 → 判斷 Provider / Mode / Update / Duplicate → 判斷是否只是 Shared Capability / Reference → 判斷是否形成獨立責任 → 決定處置。

## 六、可能處置
KEEP：保留獨立 Skill。
MERGE：融合進既有 Skill。
UPDATE：更新既有 Skill。
REPLACE：由新 Skill 取代舊 Skill。
REFERENCE：只保存為規則、知識或參考。
DEFER：證據不足，暫不處理。
ARCHIVE：退出目前工作結構但保留歷史。

## 七、判斷依據
不得只依名稱、文件相似度、功能數量、主觀偏好或模型覺得較新來決定。
至少比較：Purpose、Trigger、Input、Output、Responsibility、Mode、Dependency、Context Cost、Execution Cost、Verification、Actual Usage、Overlap、Migration Cost、Failure Pattern、Long-term Maintenance Cost。

## 八、目前狀態
功能盤點：PASS。
66 功能去重：PASS。
Capability 聚合：PASS。
S01–S10 反向重建：PASS。
I01–I08 反向重建：PASS。
11 Skill 初版：驗證通過。
8 Skill 壓縮候選：已建立。
8 Skill 最終驗證：PENDING。
實際 Skill 執行測試：PENDING。
真實工作驗證：PENDING。
Skill 分類判斷器：未正式建立。

下一階段：用真實工作案例驗證 8 Skill 候選，不再增加架構。