# 交接 Skill（Handoff Skill）v1.1

版本：v1.1
日期：2026-09-19
狀態：【FIELD 驗收 PASS；Memoryless Homepage-only PASS】
定位：負責將目前工作狀態壓縮成可由無既有對話記憶的 AI 恢復與繼續執行的最小充分交接 Context。

## 1. 核心責任

交接不是單純複製歷史。
本 Skill 負責：
- 凍結目前工作游標。
- 區分 CURRENT / Historical / Deferred / Unknown。
- 整理已完成、未完成、問題、決策、禁止事項與下一步。
- 指定下一次 AI 的入口與讀取順序。
- 移除不必要歷史 Context，保留恢復工作所需資訊。
- 驗證無記憶 AI 能否依交接資料恢復正確工作。

## 2. Trigger

- Context 即將重置。
- 更換 AI / Model。
- 工作跨對話延續。
- 使用者要求交接。
- 目前任務已形成可暫停施工的穩定節點。
- 長 Context 已不足以可靠繼續。

## 3. Input

- Repository 現行入口。
- CURRENT Baseline / CURRENT State。
- 施工總控。
- Problem Registry。
- 相關 Skill / System 狀態。
- 目前 FIELD / Real Work 證據。
- 未完成工作與下一施工游標。

## 4. Output

最小充分 Handoff Package：
- 工作目的
- CURRENT State
- 已完成
- 未完成
- 已關閉問題
- OPEN / DEFER / ACCEPTED RISK
- 目前施工游標
- 下一步
- 必讀入口
- 禁止事項
- Unknown
- 驗證方式

## 5. 核心流程

盤點 CURRENT
→ 區分 Historical / Current / Deferred / Unknown
→ 整理問題狀態
→ 固定下一施工游標
→ 建立 Handoff Package
→ 最小化 Context
→ Memoryless Takeover Test
→ 發現缺口
→ 修正交接資料
→ Re-test
→ HANDOFF READY

## 6. 邊界

Context管理 Skill：
決定「下一個任務需要載入哪些 Context」。

交接 Skill：
負責「把目前工作狀態轉換成下一個 AI 可以恢復的交接包」。

Agent Skill：
負責「拿到交接包後如何恢復並分流工作」。

三者不合併。

## 7. 交接狀態

HANDOFF-DRAFT：正在整理。
HANDOFF-READY：內容完成，但尚未通過無記憶驗收。
HANDOFF-VALIDATED：無記憶 AI 可正確恢復。
HANDOFF-STALE：Repository 狀態變更後交接包未同步。

## 8. 驗收

至少驗證：
1. 無既有對話記憶的 AI 能找到正確入口。
2. 能理解目前目標。
3. 能辨識 CURRENT 與 Historical。
4. 能辨識已 CLOSED 與尚未完成問題。
5. 不會把 DEFER / UNKNOWN 當成已完成。
6. 能找到下一施工動作。
7. 不會重做已完成工作。
8. 不會提前執行 Large Mode 或其他被暫緩事項。
9. 能依 Agent / Skill Routing 進入正確工作。
10. 執行後能繼續更新 Problem Registry 與施工總控。

文件建立 ≠ 交接驗收。

## 9. AI Control Plane 整合

交接可按需查詢 CURRENT / Authority / State / Relevant Entity / Evidence / Recovery Data。
不要求完整載入 Registry；Control Plane 只提供恢復所需 metadata，Source 文件仍為權威。
