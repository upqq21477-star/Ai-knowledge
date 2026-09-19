# AI 知識系統六層架構重構藍圖 v1.0

版本：v1.0
日期：2026-09-19
狀態：【規劃建立中】
定位：本文件定義 Ai-knowledge 下一階段的目標架構；不取代 CURRENT Baseline，不直接宣告既有文件已完成遷移。

## 1. 重構目的
將目前以大量 Markdown 文件承擔多種語義責任的結構，重新整理成可由 Agent 按需調用的分層架構。

核心目標：
1. 知識只保存小單位、可重用的事實或原理。
2. 系統只描述一項可重用功能，以及完成該功能需要組合哪些知識。
3. 專案只保存特定情境、啟動條件、可用範圍與邊界。
4. 方案升級為高階應用 Skill，負責一個大方向的系統組合與工作規則。
5. 協助 Skill 負責自然語言的語意拆解、確認與意圖結構化。
6. Agent Skill 負責任務規劃、分派、回收結果、重新規劃與結束。
7. Control Plane 作為橫向後台，管理 Entity、State、Dependency、Impact、Change、Evidence、Authority、Lifecycle、Capability、Trace，不變成新的資料層。

## 2. 目標架構
使用者
→ 協助 Skill
→ Agent Skill
→ Project Context
→ 方案 Skill
→ System
→ Knowledge

橫向控制：
Control Plane
├─ Registry / Query
├─ State / Authority / Lifecycle
├─ Dependency / Impact / Change
├─ Evidence / Provenance / Trace
└─ Context / Scope 控制

Project 是使用情境與邊界，不是更高階知識。
Skill 是 Agent 可路由、可載入、可執行的工作能力。
Control Plane 不是 Source of Truth；原始資產仍是內容真實來源。

## 3. 六個核心責任

### 3.1 Knowledge
回答：「這是什麼？」
允許：單一概念、單一事實、單一原理、小範圍可重用資訊、明確適用條件。
不允許：完整工作流程、專案專屬決策、Agent 調度、大型方案編排。
最低契約：Knowledge ID / 主張 / 適用條件 / 來源或形成依據。

### 3.2 System
回答：「如何完成一項功能？」
只保留：功能名稱、功能目的、輸入、需要的 Knowledge、最小處理邏輯、輸出、邊界。
System 不決定「什麼時候一定要啟動」；啟動條件由 Project / Skill 層決定。

### 3.3 Project
回答：「在哪個情境使用？」
保存：專案目標、啟動條件、可使用的 Skill / System、目前專案狀態、專案專屬規則、禁止跨入的邊界、專案資料 Scope。
Project 不複製通用 Knowledge / System；只引用它們。

### 3.4 方案 Skill
回答：「一個大方向的工作應如何組合？」
每個方案 Skill 至少定義：
name / description
trigger
input
context requirement
使用哪些 System
系統調用順序或條件
必要規則
output
verification target
stop / exit
failure / fallback

方案 Skill 可以組合其他 Skill，但不得把整個知識庫塞入 Skill。

### 3.5 協助 Skill
回答：「使用者真正想做什麼？」
主要責任：語意拆解、目標辨識、約束辨識、缺失條件辨識、不確定處提出確認、將自然語言轉成 Agent 可處理的 Intent Contract。
輸出至少包含：
Intent / Goal / Scope / Constraints / Unknowns / Expected Output / Verification Target。
協助 Skill 不負責最終任務規劃。

### 3.6 Agent Skill
回答：「現在做什麼、由誰做、下一步是什麼？」
主要責任：接收結構化 Intent、建立 Task、判斷 Project Scope、選擇方案 Skill、分派子任務、接收結果、判斷是否需要補充 Context、Replan / Retry / Fallback、驗證完成條件、回報使用者。
Agent 不作為知識庫，不應自行把未知內容補成事實。

## 4. Skill 共同契約
所有正式 Skill 都採相同最小介面：
Metadata → Trigger → Input → Context → Procedure / Composition → Output → Verification → Boundary → Stop / Exit → Failure / Fallback

Skill 可以使用 Markdown 作為描述格式；Markdown 是載體，不是 Skill 本身。
若採用實體 Agent Skills 形式，核心可逐步向 SKILL.md + references/ 的 progressive disclosure 模式靠攏。

## 5. Context 原則
不預載整個 repository。
運作採：最小必要 Context → 按需查詢 → 漸進載入 → 完成後釋放非必要 Context。
研究指出 Agent context 是有限資源，just-in-time retrieval 與 progressive disclosure 可避免大量低相關資訊同時進入模型。citeturn0search0turn0search1

## 6. Anti-Hallucination 原則
架構本身不保證零幻覺。
主要控制鏈：
Scope → 正確 Skill → 最小 Context → Source / Authority → Evidence → Verification → 不足即停止或要求補充。
禁止：缺失事實自動補完、把歷史資料當 CURRENT、把候選方案當正式方案、把 Simulation 當 FIELD、把 Skill 描述當實際運行證據。

## 7. Workspace / Project 隔離
通用 Knowledge / System / Skill 可以共享。
Project 只決定目前可讀取的 Scope。
Shared Capability + Project Scope = Current Working Context。
因此未來可切換 System Workspace、Game Project Workspace、其他 Project Workspace，而不需要複製整套治理邏輯。

## 8. 與現有 Control Plane 的關係
現有 AI Control Plane、Registry、Query、Routing、Runtime、Verification、Evidence、Trace 不推倒。
它們轉為這套新架構的運行後台。
核心鏈：
Task → Agent → Semantic / 協助解析 → Control Plane Query → Candidate Skill → Project Scope Check → Context Assembly → Runtime → Verification → Evidence / Trace → Agent Replan
Registry 仍是 Derived View，不取代 Source of Truth。

## 9. 目標資料流
自然語言 → 協助 Skill → Intent Contract → Agent → Project Scope → 方案 Skill → System → Knowledge → Result → Verification → Evidence → Agent → 回報 / 下一任務

## 10. 重構原則
不是「全部重新寫」。
採：分類 → 定責 → 建立新契約 → Mapping → 小批次遷移 → Re-read → Verification → 才移除舊責任。
既有文件在未完成遷移前仍保留。不得因新藍圖建立就把既有 CURRENT 資產標為完成。

## 11. 成功條件
第一階段不要求全部文件搬完。
只要求：
- 六層責任明確
- 每層契約可被另一個 AI 理解
- 至少一條完整運作鏈可模擬通過
- Project Scope 可以阻止不相關資料進入 Context
- Skill 可以按需載入
- Knowledge 不再承擔 Workflow
- System 不再承擔 Project 決策
- Agent 不再直接充當資料庫
- Control Plane 可以追蹤 Entity / Dependency / Evidence / Trace

## 12. 非目標
本階段不建立第二 CURRENT、第二 Workpool、第二套 Control Plane；不把所有 MD 改成 Skill；不把所有 Capability 建成 Skill；不立即建立 Large Mode；不大規模搬遷所有歷史文件；不以概念完整度宣告 FIELD PASS。

## 13. 外部設計參考
Agent Skills 公開設計採 Skill directory、SKILL.md、metadata-first 與 progressive disclosure；MCP 將 prompts、resources、tools 分成不同控制面。這些只作介面設計參考，不直接決定本 repository 的內部分類。citeturn0search1turn0search2
