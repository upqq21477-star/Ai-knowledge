# Blueprint 功能地圖 v1.0

版本：v1.0
日期：2026-09-19
狀態：【Blueprint Map；最小可導航地圖】

## 核心流程
Skill Registry
    │ 提供 Skill 資訊
    ↓
Blueprint
    │ 顯示整體位置、功能與關係
    ↓
Verification
    │ 驗證結果
    ↓
Evidence

## 深入導航
Blueprint
 ├── Skill Registry
 │      └── 詳細規格 → 2-方案/完善/Skill Registry規劃基線-v1.0.md
 ├── Verification【未獨立成為 Blueprint 功能節點】
 │      ├── 功能：驗證系統／Skill 是否符合既定條件
 │      └── 詳細規格 → 1-系統/證據驗證診斷 Skill.md
 └── Evidence【未獨立成為 Blueprint 功能節點】
        ├── 功能：保存、引用與追蹤驗證依據
        └── 詳細規格／既有責任 → 1-系統/證據驗證診斷 Skill.md

## 節點規則
| 節點 | 狀態 | 最小作用 | 詳細入口 |
|---|---|---|---|
| Skill Registry | 【已建立／Control Plane 接入】 | 提供 Skill 可查詢資訊 | 2-方案/完善/Skill Registry規劃基線-v1.0.md |
| Blueprint | 【本地圖】 | 顯示整體功能位置與關係 | 本文件 |
| Verification | 【未獨立成為 Blueprint 功能節點】 | 驗證結果是否符合條件 | 1-系統/證據驗證診斷 Skill.md |
| Evidence | 【未獨立成為 Blueprint 功能節點】 | 保存／引用驗證依據 | 1-系統/證據驗證診斷 Skill.md |

## 防錯規則
Blueprint 中出現名稱，不代表功能已實作。必須查看 Status、Source、CURRENT，必要時查看 Verification / Evidence。
未實作功能至少保留：名稱、狀態、最小功能說明、詳細規劃／會議紀錄名稱。

## 邊界
Blueprint 不保存 Skill 詳細 Definition、Registry 詳細資料、Verification 詳細規則、Evidence 詳細格式、Impact 計算、Runtime Trace 或完整 Repository Inventory。

## 更新
只有新增／刪除主要功能、主要狀態改變、主要位置或關係改變、詳細來源入口改變、或發現正式狀態不一致時更新。
