# RULES

> 本文件只規定「怎麼做」。目前狀態、設計背景、歷史決策與本次架構重新整理原因見 `HANDOFF.md`。**本文件是正式操作規則的最高權威。**

## 1. 層級定義

- **Rules**：定義系統怎麼運作，不存知識本身。
- **Knowledge**：可跨場景重用的基本原理、知識、判斷或方法；應能獨立理解，不含單一專案決策。
- **System**：由多份 Knowledge 組合而成，且已在實際工作中證明具有重複使用價值的方法／模型。
- **Application**：針對具體需求，組裝 Knowledge／System 形成的實際應用。

核心界線：Rules 不存知識本身；Knowledge 不預先建立固定關係；Application 可以包含專案特有決策；各層更新不自動強制連動。

## 2. Repository Discovery

**GitHub repository 的實際檔案樹是 Source of Truth。**

AI 可以直接讀取資料夾內的文件，因此不得把 INDEX、README 連結或其他人工維護的目錄視為唯一發現機制。

Discovery 原則：

```text
實際 repository 檔案樹
        ↓
判斷任務需要哪些資料夾／文件
        ↓
直接讀取相關文件
        ↓
必要時擴大閱讀範圍
```

兩種情況要區分：

- **任務導向閱讀**：只讀取與當前問題相關的文件，降低 Context 成本。
- **完整稽核／交接**：可以遞迴讀取 repository 內全部相關文字文件，不能因為文件位於子資料夾就假設無法讀取。

不要求每次任務都讀完整 repository；也不允許因為省 Context 而把未閱讀的內容當成不存在。

## 3. 文件引用

跨文件引用仍應使用 Markdown 相對路徑，例如：

```markdown
[Knowledge A](../0-knowledge/knowledge-a.md)
```

這是為了提高 GitHub 可讀性與人工導航便利，不是因為 AI 無法讀取資料夾。

不要求建立額外索引、Registry 或 Discovery 系統來補足資料夾存取能力。

## 4. Knowledge 格式

檔名：`kebab-case.md`，放在 `0-knowledge/`。

```markdown
# [名稱]

> 一句話：解決什麼問題、什麼情境會用到、什麼情況不需要

## 核心原理

## 適用情境

## 不適用情境

## 實務方法／注意事項

## 參考資料

## 我的補充
```

**自包含原則**：可以引用其他 Knowledge，但本份文件不能要求先讀懂其他文件才能理解核心內容。

**不算 Knowledge**：單一專案特殊設定、一次性 bug／修法、只對單一情境有效的決定、未驗證的原始資料。這些留在對應 Application 或研究資料中。

**模型能力補償**：若某份 Knowledge 的主要存在理由是補償當時模型能力限制，可以簡單標註「模型能力補償」。模型能力改善後，在實際使用到該知識時再判斷是否淘汰，不建立預先的生命週期系統。

## 5. System 格式

檔名：`kebab-case.md`，放在 `1-systems/`。

**建立門檻**：至少兩份 Knowledge 已經在同一類問題中實際重複組合使用，並證明這個組合值得保存。單純「可能一起使用」不算。

```markdown
# [名稱]

> 一句話：這個組合解決什麼類型的問題

## 組成的 Knowledge
- [Knowledge A](../0-knowledge/knowledge-a.md)
- [Knowledge B](../0-knowledge/knowledge-b.md)

## 輸入／輸出／流程（複雜組合才需要）

## 狀態
草稿／已驗證

## 適用情境

## 不適用情境

## 參考資料／我的補充
```

System 本身列出組成的 Knowledge，即可作為基本反查線索。現階段不建立 Dependency Database、Knowledge Graph 或 Registry。

## 6. Application 格式

放在 `2-applications/`，可以是單一 `.md` 或資料夾。

```markdown
# [名稱]

## 目的

## 用到的 System／Knowledge

## 本專案特有的決策

## 狀態
草稿／已驗證
```

資料夾型 Application 若需要讓人或 AI 快速進入，應有清楚的入口文件，例如 `README.md`。這是內容組織原則，不代表 AI 無法讀取資料夾。

只有當某個 Application 的子機制已經在不同 Application 中重複需要，才評估是否抽成 System；不要預先抽象化。

## 7. 更新規則

三層各自獨立判斷，互不強制連動。

**Rules**：只有整套系統運作方式本身出現問題時才修改，低頻。

**Knowledge**：
- 不更新：新資訊只是補充，核心結論沒有改變。
- 更新：原本有錯誤、新證據改變核心結論、或實際使用發現重大限制。
- 淘汰：若是模型能力補償，且實際使用時已確認原問題不存在，可以整份淘汰。

**System**：
- 不更新：底層 Knowledge 小幅補充且組合邏輯不受影響。
- 更新：底層 Knowledge 核心結論改變並影響組合，或實際使用發現更好的組合方式。

**Application**：依具體專案實際需求更新。

Knowledge 更新不自動要求 System 更新；System 更新不自動要求 Application 更新。只有實際需要維護或重新使用時才檢查上一層。

## 8. Latest Check

只有問題具有時效性時才查最新資料，例如 API／函式庫版本、模型能力、平台規格。不要排程式全面更新。

## 9. Feedback 分層

使用後的新發現依性質處理：

- 只對這次有用 → 留在該 Application。
- 新的可重複組合方式 → 評估建立／更新 System。
- 新的可跨場景基本原理 → 評估建立／更新 Knowledge。
- 發現整套系統本身的運作方式有問題 → 評估修改 Rules。

## 10. 檔案與淘汰

- 檔名保持穩定，不加入 `v1`、`final`、`old` 等版本後綴；版本交給 Git。
- 淘汰文件時，如果不需要保留設計脈絡可直接刪除；只有真的需要保存歷史時，才在當下建立 `_archive/`。
- `_archive/` 內容永遠不視為目前有效資料。

## 11. 不預先建立的機制

以下機制目前不加入核心系統：

- Knowledge ID 編號系統
- 正式 Evidence Source 分級
- 文件內 Version History 表格／Update Trigger checklist
- Specification Migration 流程
- Capability 分類／需求解析層
- 正式 Conflict Resolution Pipeline
- Knowledge Graph / Dependency Database / Registry
- 自動 Cascade Update
- 複雜相關性分級
- 多層 Context Loading 系統
- 預先建立 `_archive/`
- 預先建立獨立 Runtime
- Atomic Knowledge
- Knowledge Aggregation
- 複雜內容狀態機
- Capability Lifecycle / Capability-Driven Pruning
- 大型自動化 Knowledge Pipeline

這些不是待辦事項。若未來出現實際問題，依 `HANDOFF.md` 的 Gate 重新評估。

## 12. 新機制加入前的判斷

任何新機制先問：

> **它是否直接降低下一次重新研究問題的成本？**

如果沒有，不加入。

如果有，先尋找最小解法。優先使用 Markdown + Git + repository 原生檔案結構；只有實際證明不足，才增加新的機制。
