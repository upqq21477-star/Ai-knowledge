# Context 管理 Skill（Context Management Skill） v1.1

版本：v1.1
日期：2026-09-19
狀態：【建立；待實際運作驗收】

## 1. 定位
決定目前任務需要載入哪些 Context，控制上下文邊界與成本。

## 2. Trigger
- 開始新任務。
- 任務跨文件／跨 Skill。
- 現有 Context 不足。
- Context 過大造成成本或失真風險。
- 發生上下文重置。
- 來源出現衝突。

## 3. 核心責任
- 判斷必要文件與資料。
- 控制載入範圍。
- 避免預載整個 repository。
- 衝突時回到現行入口與 Canonical Source。
- 重置後恢復必要狀態。

## 4. Input
Task Definition、工作狀態、Repository 入口、文件索引。

## 5. Output
Required Context
Context Boundary
Loaded Sources
Missing Context
Conflict Flags
Context Cost（L / M / H）

## 6. 路由
Context 不足 → Research / Knowledge。
來源衝突 → Evidence / Verification。
Context 過大 → 縮減載入範圍。
重置 → 重新讀取必要入口。

## 7. 邊界
Knowledge 管資料生命週期；Context 管現在載入什麼。

## 8. 失敗
不能確認 Canonical Source → UNKNOWN，不以舊文件猜測。

## 9. 成本
第一版使用 L / M / H，不追求虛假的精密 Token 數。

## 10. 來源
- `藍圖/Skill分類融合更新取代判斷問題紀錄-v1.0.md`
- `README.md`
- `1-系統/Agent Skill.md`

## 11. 驗收
文件建立：PASS
實際運作：PENDING

## 12. AI Control Plane 整合

Control Plane 提供 Entity / State / Dependency / Impact / Evidence / Provenance / Authority / Change metadata。
Context Skill 負責判斷本次任務需要哪些資料，不複製 Control Plane。

採 Progressive Retrieval：L0 現有 Context → L1 metadata → L2 直接關係 → L3 Evidence/Provenance → L4 Source → L5 History；足夠即停止。
