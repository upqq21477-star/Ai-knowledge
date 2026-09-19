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

