# Context Grounding and Hallucination Detection｜上下文失真與幻覺檢測原理

版本：v1.0
狀態：【候選知識；由 C05 建立；待最小實測】

## 一、定位
C05 的目標不是把所有錯誤都稱為 Hallucination。

它要區分：
~~~text
Context 不足 → 推測／補全 → Unsupported Claim
Context 過量 → 注意力／判斷品質下降 → Context-induced Error
證據存在但模型仍錯誤引用／扭曲 → Grounding Failure
~~~

## 二、核心判定
對輸出拆成可驗證的最小主張（Atomic Claims），逐項判定：

| 狀態 | 定義 |
|---|---|
| Supported | 可由提供 Context 或可靠外部證據支持 |
| Contradicted | 與證據直接矛盾 |
| Unsupported | 找不到足夠證據支持 |
| Uncertain | 證據不足以判定 |
| Context-induced | 主要錯誤與 Context 大小／組成變化相關 |

Unsupported 不必然等於惡意或模型內部幻覺；它首先是「目前輸出缺乏可追溯支持」。

## 三、測試方法
同一問題至少建立：
1. 無／極少 Context。
2. 最小充分 Context。
3. 完整相關 Context。
4. 大量低相關 Context。

比較：
- 主張數量。
- Supported Claim Ratio。
- Unsupported Claim Ratio。
- Contradiction Rate。
- 規則違反。
- 與基準答案的差異。

## 四、證據鏈
每一個重要主張應能回到：
~~~text
Claim → Evidence → Context Source → 判定
~~~
如果無法追溯，不應直接標記為「已證實」。

## 五、外部方法比較
FActScore 將長文拆成 atomic facts，再判斷各事實是否有可靠來源支持，說明二元「整篇正確／錯誤」不足以描述混合了支持與不支持內容的輸出。

SelfCheckGPT 則以黑箱模型多次採樣的一致性作為無外部資料時的幻覺偵測方向。

本方案採用兩者可互補的概念，但不直接複製其實作：
- 有可靠 Context 時優先做 claim-to-evidence grounding。
- 缺乏外部真值時，可把多次輸出一致性作為輔助訊號。
- 不把一致性本身當成真實性的證明。

## 六、重要限制
「Context 越長，幻覺越多」不是固定定律。

必須用控制實驗證明：
- Context 不足是否提高 Unsupported Claims。
- Context 過量是否降低 grounding / reliability。
- 哪一類資料最容易造成失真。
- 哪些錯誤其實與 Context 無關，而是模型能力或任務本身造成。

## 七、停止條件
若主張已能可靠追溯到證據，且增加 Context 不再降低 Unsupported／Contradicted Claims，即可停止擴張 Context。

若仍有重大未知，必須標記未知，不得以高置信度語氣掩蓋。
