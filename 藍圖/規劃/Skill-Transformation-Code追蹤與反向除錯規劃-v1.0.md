# Skill → Transformation → Code 追蹤與反向除錯規劃 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃中；已建立概念基線，尚未施工／尚未 FIELD 驗證】

## 1. 目的

建立一條可追蹤的遊戲實作鏈：

Game Model
→ Skill
→ Transformation
→ Code
→ Test / Verification
→ Runtime Evidence

並建立反向路徑：

Runtime Bug
→ Evidence
→ Code
→ Transformation
→ Skill
→ Rule / Game Model
→ Diagnosis
→ Fix
→ Re-test

目標不是讓 AI 每次重新生成程式，而是累積已驗證的 Skill → Transformation 實作模式，降低程式漂移、Context 成本與除錯範圍。

## 2. 核心概念

### Skill
描述「要完成什麼能力」。

例：
Damage Calculation

### Transformation
描述「該能力在特定實作環境如何轉換」。

例：
Damage = max(Attack - Defense, 0)
→ Unity / C# implementation pattern

### Code
特定遊戲、引擎、語言、版本下的實際實作。

### Evidence
證明 Transformation / Code 是否正確的測試、模擬、實際運作結果。

四者不可混為一談。

## 3. 最小資料關係

最小追蹤單位至少需要能表達：

- Transformation ID
- Skill ID / Version
- Game Model / Rule reference
- Implementation Target（語言／引擎／平台）
- Transformation Pattern
- Code Reference
- Test / Verification Reference
- Evidence Status
- Version
- Dependency / Impact
- Provenance
- Last Validated

實際欄位仍需後續研究與最小化，不提前建立大型 Registry。

## 4. Context / Token 原則

中央可以保存大量 Transformation Records，但執行時不得全部載入 Context。

採：

Need
→ Capability / Skill Discovery
→ Transformation Search
→ 僅載入相關 Record
→ Execute

因此：

「資料庫很大」不等於「Context 很大」。

Transformation Library 應可被索引／查詢；只有目前任務相關內容進入 Context。

## 5. 程式漂移控制

第一次建立並驗證成功的 Transformation，可以成為後續同類實作的優先 Pattern。

後續遇到相同 Skill：

Existing Validated Transformation
→ 優先重用
→ 不重新自由生成
→ 若環境不同，選擇相容 Transformation
→ 若無適用 Transformation，才產生候選新實作
→ 驗證後再決定是否收錄

「固定」的是經驗證的轉換規則與介面，不是要求所有語言／引擎使用同一段文字程式碼。

## 6. 反向除錯

Bug 不直接等同 Code Bug。

應依序判斷：

Runtime
→ Code
→ Transformation
→ Skill
→ Game Rule
→ Game Model / Design

可能結果包括：

- Code implementation defect
- Transformation defect
- Skill execution defect
- Rule defect
- Game Design defect
- External / Engine / Provider defect

只有定位證據足夠時才進入對應修正層。

## 7. 雙向 Traceability

正向：

Game Model
→ Skill
→ Transformation
→ Code
→ Test
→ Runtime

反向：

Runtime
→ Evidence
→ Code
→ Transformation
→ Skill
→ Rule / Model

變更影響：

Skill / Rule 修改
→ 受影響 Transformation
→ 受影響 Code
→ 受影響 Test
→ Re-verification

## 8. 與現有 Ai-knowledge 的關係

本規劃不是新的資料層，也不是立即新增一組 Game Skill。

它是既有：

Agent
→ Task Understanding
→ Context
→ Skill Selection
→ Execute
→ Verify

以及：

Control Plane / Runtime Closure / Evidence / Evolution / Change

在遊戲實體化階段的延伸。

Game Skill 仍必須經既有 Skill Classification / Evolution / Verification 邏輯判定，不因本規劃自動建立大量 Skill。

## 9. 與多專案架構的關係

中央系統保存可重用的：

- 通用 Skill
- 通用 Transformation Pattern
- 驗證經驗
- 實作接口／契約

遊戲專案保存：

- Game Model
- Game-specific Skill
- Project-specific Transformation
- Actual Code
- Project Evidence

中央成果不能因單一專案使用就自動升格為通用能力。

專案成果若具跨專案重用價值：

Project Evidence
→ Proposal
→ Research / Evaluation
→ Generalization
→ Central Adoption

## 10. 目前不提前建立

暫不建立：

- 大型 Code Transformation Registry
- 自動 Code Generator
- 完整 Code ↔ Model 雙向同步平台
- 自動 Bug-to-Skill 診斷平台
- 全專案 AST / Graph 基礎設施

原因：目前只有設計需求與架構推論，尚無 Natural FIELD 證據證明需要大型基礎設施。

## 11. 後續驗證

先以一個極小案例驗證：

Skill：
Damage Calculation

Model：
Damage = max(Attack - Defense, 0)

Transformation：
固定語言／引擎 Pattern

Code：
實際函式

Verification：
正常、邊界、錯誤案例

Runtime：
故意觀察實際錯誤

Reverse Trace：
Runtime → Code → Transformation → Skill → Rule

確認是否能在不讀取整片遊戲 Code 的情況下縮小問題範圍。

## 12. 成功判準

不是「AI 產生更多 Code」。

而是：

1. 相同 Skill 能重用已驗證 Transformation。
2. 不需要每次重新創作相同實作。
3. Transformation 查詢不造成不必要 Context 膨脹。
4. Skill / Transformation / Code / Evidence 可互相追蹤。
5. Runtime Bug 可以反向縮小到合理的設計／實作層。
6. 修正後可以重新驗證並更新版本。
7. 無法證明時保持 UNKNOWN / INSUFFICIENT，不猜測。

最高原則：

> Skill 定義能力，Transformation 定義實作轉換，Code 是實體化結果，Evidence 決定它是否可信。


## 13. 附加 Skill 統御

本規劃納入「遊戲開發附加 Skill 統御」管理範圍，但不因此將 Transformation、Code Trace 等全部內容自動建立為 Skill。

附加 Skill 層與中央 Core System 分離，採按需載入；Project-specific Skill 保持專案範圍。詳見：
`附加技能/遊戲開發/附加Skill統御.md`。
