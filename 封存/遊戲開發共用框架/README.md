# 遊戲開發共用框架封存

狀態：【ARCHIVE-REUSABLE；不啟用】

## 目的

保存在 Project A 開發過程中確認具有跨遊戲重用價值的「遊戲開發框架」，供未來 Project B、Project C 等遊戲專案直接套用。

本封存不是第二套 Agent、Control Plane、Runtime、CURRENT 或 Workpool，也不在日常執行時自動載入。

## 分層原則

### 共用框架

處理「如何開發遊戲」：

- Game Model 最小契約
- Core Loop 設計方法
- Game System / Rule / State / Flow 建模
- L1 / L2 / L3 驗證
- System Integration Validation
- Game Rule → Game Model → Skill → Transformation → Code → Verification
- Runtime → Evidence → Code → Transformation → Skill → Rule / Game Model 反向追蹤
- 遊戲開發共通 Skill 的治理、驗證與最小記錄方式

### 專案專屬

處理「這個遊戲是什麼」：

- 戰鬥
- 敵人
- 武器
- 數值
- 地圖
- 關卡
- 經濟
- 技能效果
- 劇情
- 美術／音效規格
- 實際 Game Data
- 專案專屬測試與 Playtest

專屬內容不得因為存在於某一遊戲而自動進入本封存。

## 套用方式

新遊戲專案啟動：

中央遊戲開發共用框架封存
→ 選擇適用版本
→ 建立新專案的遊戲開發框架基線
→ 再加入該遊戲專屬設計

因此 Project B 不需要重新建立 Project A 已驗證的共通框架。

## 更新方式

共通框架修正時：

正式共通框架變更
→ 更新中央封存版本
→ 新專案使用最新版本
→ 已開發專案依相容性／影響分析決定是否升級

不得把專案專屬資料反向整包同步到中央。

## 目前來源

本封存由 Project A 遊戲開發規劃蒸餾而來。

目前僅建立封存結構與邊界；尚未宣稱其中所有能力都已完成 Natural FIELD。

只有經 Project A 實際使用、Verification 與 Evidence 支持的共通內容，才可升格為正式可重用框架。

## 重要原則

「一次建立、跨遊戲重用；共通框架更新集中管理；專屬遊戲設計留在各自專案。」



## 可重用性分類

本框架不把所有「可能重用」的內容視為同一類，採三種語義分類：

### Common｜共通

預期跨多數遊戲都適用的開發方法或最小契約，例如 Game Model 最小契約、Core Loop 基本建模與驗證、Rule / State / Transition / Output 基本語義、L1 / L2 / L3 驗證邊界，以及 Rule → Model → Skill → Transformation → Code → Verification 追蹤方法。

Common 代表可作為共通基線，不代表永遠正確，也不代表不需要版本管理。

### Variant｜可變／條件共用

已具有重用價值，但只適用某些遊戲類型或設計條件，例如 RPG Progression、Turn-based Combat、Economy、Dialogue、特定 AI 行為模式。

Variant 不應硬塞進所有遊戲的基線。使用專案必須確認適用與不適用條件。

### Project-specific｜專案專屬

只服務單一遊戲的設計、規則、數值或內容，例如特殊戰鬥規則、特定敵人、特定地圖、專案數值、劇情、專案專屬 Game Data。

Project-specific 預設不升格中央框架。

目前不建立 Common / Variant / Project-specific 三套大型 Registry；這只是分類語義，實際資料仍依需求存放。

## 「可重用」不等於「已證明可重用」

任何內容在 Project A 中成功一次，都只能證明「Project A 可用」，不能直接證明「跨遊戲可重用」。

正式升格流程：

Project 使用 → Evidence → Verification → Generalization → Cross-project applicability 判定 → 蒸餾共通部分 → ARCHIVE-REUSABLE

至少確認：
1. 確實有實際使用。
2. 有可追溯 Evidence / Verification。
3. 不依賴 Project A 的專屬規則才能成立。
4. 可以用清楚的 Input / Output / Preconditions 表達。
5. 已知道適用與不適用情境。
6. 升格後不會把 Project A 專屬設計帶入共通框架。

若不足，留在原專案，不強制抽取。

## 可重用資產最小履歷

進入中央共用框架的能力，至少保留：

- Asset / Capability ID
- 分類：Common / Variant
- Source Project
- Source Evidence / Verification
- Purpose
- Applicability
- Non-applicability
- Version
- Dependency
- Last Validated
- Promotion Reason

這不是大型 Registry；可先以文件段落或最小記錄存在。

## 框架版本綁定

每個使用中央共用框架的遊戲專案，都應知道自己基於哪個框架版本。

最低語義：

Project Framework Baseline = Common Framework Version + Project-specific additions + Project-specific overrides（若有）

新專案預設使用最新正式版本。

既有專案不得自動覆蓋；框架升級必須經 Change Signal → Compatibility / Impact Analysis → Upgrade / Stay / Migrate → Verification。

## Core Loop 是一級驗證對象

Game-BLUEPRINT 應把 Core Loop 視為一級設計對象：

Core Loop → System → Mechanic → State → Player Decision → Feedback → Next Loop

驗證時至少回答：玩家每輪做什麼、做決策需要哪些資訊、系統如何回饋、回饋如何影響下一輪，以及是否存在能破壞核心循環的重要系統交互。

Core Loop 驗證屬 L2，不取代 L1 規則驗證或 L3 Runtime 驗證。

## 不建立的東西

目前不建立 Game Framework Registry、Feature Registry、Variant Registry、Game Project Factory、全自動 Migration、全自動 Framework Sync、大型 Game Knowledge Graph、全自動 Game Code Generator。

只有當多專案實際使用後，維護或檢索成本成為瓶頸，才重新評估。

## 當前狀態

【ARCHIVE-REUSABLE；不啟用】

此文件定義的是共用框架邊界與升格規則，不宣稱框架內每一項能力都已完成 Natural FIELD。

Project A 是第一個驗證專案：Project A proves → Central distills → Project B validates reuse → 再決定是否擴大共用框架。
