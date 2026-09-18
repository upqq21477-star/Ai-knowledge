# AI知識庫五層架構重構計畫書

## 一、計畫定位

本計畫針對現有 AI 知識庫架構進行整體重構。

目前架構主要由：

> Knowledge → System → Solution

組成。

實際運作後發現，現有架構缺少一個專門管理「問題類型與解法索引」的中間層，導致部分問題識別、System 路由與 Solution 選擇責任重疊。

本次重構新增：

> Project（專案／問題域）

並在最上層建立：

> Master Agent（總代理）

形成：

> Master Agent → Project → Solution → System → Knowledge

五層架構。

---

## 二、核心設計理念

每一層只負責自己應負責的事情。

| 層級 | 名稱 | 核心問題 | 主要責任 |
|---|---|---|---|
| L0 | Master Agent | 去哪裡？ | 判斷觸發並尋找 Project |
| L1 | Project | 哪一類問題？ | 管理問題索引與 Solution Mapping |
| L2 | Solution | 怎麼解？ | 調度解決方案 |
| L3 | System | 能做什麼？ | 提供可重複功能 |
| L4 | Knowledge | 依據什麼？ | 保存知識、原理、規則、證據 |

核心原則：

> Master Agent 不解決問題。
> Project 不執行問題。
> Solution 不保存基礎知識。
> System 不負責判斷整體任務。
> Knowledge 不負責調度。

---

## 三、標準資料流

```
使用者輸入
    ↓
Master Agent
    ↓
Trigger / 語意匹配
    ↓
Project
    ↓
Problem Index
    ↓
Solution Mapping
    ↓
Solution
    ↓
System
    ↓
Knowledge
    ↓
執行結果
    ↓
Solution 驗收
    ↓
輸出
```

簡化：

> 問題 → 專案 → 解法 → 能力 → 依據

---

## 四、Master Agent

### 定位

Master Agent 是整個知識庫的最高層入口。

它不負責解決問題。

唯一核心任務：

> 從使用者輸入判斷可能涉及哪些 Project。

### 觸發機制

每個 Project 提供自己的 Trigger Index。

例如搜尋專案：

```
搜尋
查找
找資料
研究
來源
GitHub
文獻
資料
工具
```

Master Agent：

```
Input
 ↓
Trigger Detection
 ↓
Project Matching
```

### 路由邊界

Master Agent 只負責：

> Trigger → Project

不直接負責：

> Trigger → Solution

避免總代理成為巨大萬能路由器。

---

## 五、Project 專案層

### 定位

Project 是：

> Problem Domain Manager

Project 只保存：

1. 問題索引
2. Solution Mapping

不保存完整 Knowledge、System 詳細功能或 Solution 完整流程。

### 最小結構

例如：

```
# 搜尋專案

P01 一般資訊搜尋 → S01
P02 研究資料搜尋 → S02
P03 GitHub／工具搜尋 → S03
P04 來源驗證 → S04
P05 歷史資料搜尋 → S05
P06 知識庫內搜尋 → S06
P07 缺失資訊搜尋 → S07
```

核心原則：

> 只保存索引，不重複知識。

---

## 六、Solution 方案層

Solution 是：

> 針對特定問題的解決方案與執行調度。

Project 找到問題後：

```
P03
 ↓
S03
```

Solution 可保存：

- 問題定義
- 執行目標
- System 調度順序
- 必要 Knowledge
- 執行條件
- 邊界
- 驗收條件
- 結果處理

不重新保存完整 Knowledge、System 詳細實作或其他 Project 索引。

---

## 七、System 系統層

System 是：

> 可重複使用的功能能力。

System 最小必要資訊：

```
Identity
Function
Dependencies
Knowledge Dependencies
Input
Output
Result Contract
```

其中：

> Function = 能做什麼  
> Dependencies = 需要什麼  
> Result Contract = 執行後產生什麼

System 可以調用 Knowledge，但不負責整體任務判斷。

---

## 八、Knowledge 知識層

Knowledge 是整個架構最底層的依據。

保存：

- 原理
- 事實
- 規則
- 證據
- 判斷依據
- 已驗證結論

核心原則：

> 知識保存知識，不負責調度。

Knowledge 是五層中相對最穩定的一層。

Project、Solution、System 的變動不應直接造成 Knowledge 改動；只有新的證據、研究或驗證改變原有知識時才更新。

---

## 九、五層責任邊界

```
Master Agent
只知道 Project

Project
只知道 Problem → Solution

Solution
知道如何調度 System

System
知道如何執行功能

Knowledge
提供執行依據
```

標準依賴方向：

```
Master Agent
    ↓
Project
    ↓
Solution
    ↓
System
    ↓
Knowledge
```

---

## 十、Context 隔離

本次重構的重要目的之一是降低 Context 成本。

不再讓 AI 每次讀取完整知識庫，而是逐級縮小：

```
完整知識庫
 ↓
Master Agent Context
 ↓
單一 Project
 ↓
單一 Problem
 ↓
單一 Solution
 ↓
必要 System
 ↓
必要 Knowledge
```

核心原則：

> 不是單純壓縮文字，而是壓縮需要被讀取的資訊範圍。

---

## 十一、搜尋專案範例

### Trigger

```
搜尋
查找
找資料
研究
來源
GitHub
文獻
工具
資料
```

### Problem Index

```
P01 一般資訊搜尋 → S01
P02 研究資料搜尋 → S02
P03 GitHub／工具搜尋 → S03
P04 來源驗證 → S04
P05 歷史資料搜尋 → S05
P06 知識庫內搜尋 → S06
P07 缺失資訊搜尋 → S07
```

Project 不需要知道 S01–S07 的完整內容，只負責 Mapping。

---

## 十二、重構原則

### 原則一：不重複語意

同一個語意只在真正需要它的層保存一次。

### 原則二：功能與問題分離

System 是功能。

Project 是問題索引。

Solution 是問題解法。

### 原則三：知識與調度分離

Knowledge 不負責決定執行順序。

### 原則四：上層極簡

越接近入口，Context 越小。

### 原則五：下層提供能力

越接近 Knowledge，資訊越完整。

### 原則六：先移動責任，再刪除

資訊仍然必要但屬於其他層時，先移到正確層，不直接刪除。

### 原則七：先 Mapping，再刪除

舊資料確認已由新層承接以前，不得直接刪除。

---

## 十三、重構流程

### Phase 0：建立新架構規範

正式建立：

Master Agent / Project / Solution / System / Knowledge

五層定義與責任邊界。

### Phase 1：盤點現有資產

盤點 Knowledge、System、Solution、交接文件、索引及其他核心資產。

建立：

> 現有文件 → 新架構位置

### Phase 2：建立 Project Index

從現有問題與 Solution 反向整理：

> 問題集合 → Problem Index → Project

### Phase 3：建立 Master Agent

建立：

> Trigger → Project

全域入口索引。

### Phase 4：重新整理 Solution

移除 Solution 中不屬於 Solution 的 Project 判斷、重複 System 與重複 Knowledge。

形成：

> Project → Solution → System → Knowledge

### Phase 5：System 瘦身

保留：

Identity / Function / Dependencies / Input / Output / Result Contract

### Phase 6：Knowledge 固化

確認知識、原理、規則、證據與判斷依據沒有被錯誤移入其他層。

### Phase 7：建立完整 Mapping

建立：

> Trigger → Project → Problem → Solution → System → Knowledge

完整路由圖。

---

## 十四、驗收指標

### 路由

- Input → Project
- Project → Problem
- Problem → Solution

### 功能

- Solution 是否能正常調用 System
- System 是否能取得必要 Knowledge

### 資料

- Knowledge 完整率
- 語意失真率
- 跨層污染率

### 成本

- Context 成本
- Token 成本
- 不必要文件讀取量

### 可靠性

- 路由正確率
- 功能完成率
- 結果正確率
- 零記憶交接成功率

---

## 十五、成功條件

重構成功不以文件數量減少為標準。

必須達成：

```
問題可以快速找到 Project
Project 可以找到正確 Solution
Solution 可以正常調度 System
System 可以取得必要 Knowledge
Knowledge 不因重構而遺失
Context 範圍下降
Token 成本下降
路由錯誤下降或至少不增加
功能完成率不下降
語意失真不增加
```

最終目標：

> 用最少的 Context，讓 AI 找到正確問題、正確方案、正確能力與正確知識。

---

## 十六、最終架構

```
                    ┌──────────────────┐
                    │   Master Agent   │
                    │ Trigger → Project│
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │     Project      │
                    │ Problem → Solution│
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │     Solution     │
                    │   問題解決與調度   │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │      System      │
                    │      功能能力      │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │    Knowledge     │
                    │   知識與依據      │
                    └──────────────────┘
```

### 最終責任公式

> Master Agent = 找專案  
> Project = 找問題／方案  
> Solution = 解決問題  
> System = 執行功能  
> Knowledge = 提供依據

核心原則：

> 上層負責選擇，下層負責能力。  
> 上層管理問題，下層保存依據。  
> 越上層越短，越下層越完整。  
> 任何資訊只保留在真正負責它的層。
