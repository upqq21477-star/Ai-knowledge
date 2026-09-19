# 遊戲開發附加 Skill 統御 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃基線；Simulation 待驗；Natural FIELD 待證】

## 1. 定位

本 Skill 是方案 A 的遊戲開發附加 Skill 統御能力。

方案 A 是目前遊戲開發工作區；開發期間不把遊戲能力再隔離成另一套獨立執行系統。中央系統提供完整 Agent、Control Plane、Runtime Closure、Skill Governance、Evidence、Verification、Evolution、Change 與其他通用能力；本 Skill 只負責遊戲領域能力的組織與使用邊界。

核心原則：

> 中央系統管理 AI 如何工作；方案 A 保存遊戲開發需要的 Skill 與資料；開發完成後才依實際 Evidence 進行精簡、抽取、封裝與回收。

## 2. 方案 A 內的遊戲能力

目前可納入的遊戲能力包括：

- Game Concept
- Game Model
- Game System Design
- Combat Calculation
- Attack Pattern
- Balance Analysis
- Progression
- Economy
- Level Design
- Game AI
- Simulation
- Playtest Analysis
- Game Verification
- Skill → Transformation
- Transformation → Code
- Runtime → Skill Reverse Trace

目前只建立已有需求與規劃的能力；不得因目錄存在而預先大量建立 Skill。

## 3. 與中央系統的關係

中央系統仍是唯一的：

- Agent
- Control Plane
- Runtime Closure
- Skill Governance
- State / Acceptance Authority
- Evidence / Verification Governance
- Evolution / Change Governance

方案 A 不建立第二套上述治理核心。

方案 A 的遊戲 Skill、資料、Game Model、Transformation、Code 與 Evidence 都屬方案 A 開發資產，除非經既有 Evolution / Verification 流程，不得自動升格為中央能力。

## 4. 開發期間的工作方式

啟動遊戲模式時：

1. 讀取方案 A。
2. 使用中央系統完整必要能力。
3. 方案 A 的遊戲資料與 Skill 作為遊戲專用 Context。
4. 依目前任務再選取必要資料，不要求每次載入所有遊戲內容。
5. 其他專案不載入。

這裡的「按需載入」是 Context 成本控制，不代表開發期間要把遊戲能力拆成獨立 Domain Runtime。

## 5. 方案 A 的分層

方案 A 採與主程式相同的資料分層概念，但目前只用於整理遊戲開發資產：

- 0-知識/：遊戲領域知識（有實際需求後建立）
- 1-系統/：遊戲專用 System / Skill / Game Model 規格
- 2-方案/：遊戲開發方案、Transformation 與實作規劃
- 3-軟體/：實際遊戲工具、程式或軟體資產（有實際需求後建立）
- 應用/：實際遊戲專案／應用資料（有實際需求後建立）

不預先建立空的大型目錄。

## 6. Skill 與 Game Model

Game Model 是遊戲內容與規則。

Skill 是操作 Game Model 的能力。

Transformation 是將已確認的能力／規則轉成特定實作環境的方式。

Code 是實體化結果。

Evidence 是驗證依據。

四者不得混為同一資產。

## 7. Skill → Transformation → Code

主要鏈：

Game Model
→ Skill
→ Transformation
→ Code
→ Test / Verification
→ Runtime Evidence

反向除錯：

Runtime
→ Evidence
→ Code
→ Transformation
→ Skill
→ Rule / Game Model
→ Diagnosis
→ Fix
→ Re-test

已驗證的 Transformation 可以在方案 A 後續開發中優先重用。

## 8. 開發期與完成後的不同

### 開發期

允許方案 A 保留完整遊戲開發能力與資料。

目的：

- 提高開發效率
- 保留真實使用 Evidence
- 避免過早判斷哪些能力最終需要保留
- 避免為了最終精簡而增加目前開發成本

### 完成後

才進行：

使用紀錄
→ Dependency Audit
→ 影響分析
→ Evidence 整理
→ KEEP / MERGE / COMPRESS / ARCHIVE / DELETE
→ 可重用能力抽取
→ 最終結構精簡

不得在開發尚未完成前，僅因「看起來可以共用」就提前大規模拆分。

## 9. 邊界

本 Skill 不負責：

- 建立第二個 Agent
- 建立第二個 Control Plane
- 建立第二個 CURRENT
- 建立第二個 Workpool
- 建立第二個 State Authority
- 自動把遊戲 Skill 升格中央
- 因為預想需求而大量建立遊戲 Skill
- 把 Code 當成唯一 Source of Truth

最高原則：

> 開發期間以完整能力支援遊戲開發；完成後才以 Evidence 進行精簡。
