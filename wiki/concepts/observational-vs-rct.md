# 觀察型研究 vs 隨機對照試驗（Observational Study vs RCT）

> **一句話重點**：觀察型研究「看」人們自己的選擇，只能找出相關；隨機對照試驗用抽籤決定誰吃早餐，比較能推論因果。早餐研究中，兩種研究的結論並不一致。

## 白話說明

**觀察型研究**：研究者不介入，只記錄人們平常有沒有吃早餐，再看誰後來比較胖或生病（本 wiki 的教學說明）。問題是吃早餐的人和不吃的人，本來就可能在很多地方不同（見[干擾因子](confounding.md)）。

**隨機對照試驗（Randomized Controlled Trial, RCT）**：研究者用隨機的方式（像抽籤）決定誰吃早餐、誰不吃（本 wiki 的教學說明）。因為是隨機分的，兩組在其他方面一開始大致相同，所以最後的差異比較可能來自早餐本身（本 wiki 的教學說明）。

- 作者指出，觀察型證據無法排除一種可能：吃早餐的人傾向較輕，是因為其他與吃早餐相關的體重因素（S3）。
  > "observational evidence does not preclude the possibility that breakfast eaters tend to weigh less because of other weight-related factors associated with breakfast eating" — S3, Introduction
- 作者認為，隨機分組的設計與嚴謹的統計分析，讓因果推論更有力（S3）。
  > "our randomized design and rigorous statistical analysis strengthen inferences about causation" — S3, Discussion

## 教學用例子

想知道「吃早餐會不會讓人變瘦」：

- **觀察型**：去問全班誰有吃早餐，再量體重。結果吃早餐的人比較瘦。但他們可能也比較常運動、比較早睡。
- **實驗型（RCT）**：把全班抽籤分兩組，A 組每天吃早餐、B 組不吃，幾週後再量體重。因為是抽籤，兩組運動、睡眠習慣大致一樣，差異就比較能歸因於早餐。

## 統合分析（Meta-analysis）

單一 RCT 可能人數少、時間短。統合分析是把多個試驗的結果合起來算，看整體趨勢（本 wiki 的教學說明）。S5 就是 RCT 的統合分析，共納入 13 個試驗：7 個看體重變化，10 個看熱量攝取（S5）。

## 在早餐研究中：兩種研究結論不同

| | 觀察型研究 | 隨機對照試驗／統合分析 |
|---|---|---|
| 代表 | S1（以及 S3、S4 提到的流行病學研究） | S3、S4、S5 |
| 發現 | 不吃早餐與較高冠心病風險、較重體重**相關**（S1、S3） | 「建議吃或不吃早餐」對減重沒有顯著影響（S3）；吃早餐的人平均略重 0.44 公斤（S5） |

- 作者指出，在觀察型研究中，吃早餐與較低的體重相關（S3）。
  > "Breakfast is associated with lower body weight in observational studies." — S3, Abstract
- 作者指出，流行病學的發現不能推論因果，因為習慣吃早餐的人往往也不抽菸等等（S4）。
  > "these findings do not infer causality because habitual breakfast consumers also tend to be nonsmokers" — S4, Introduction
- 作者認為，隨機對照試驗和觀察型研究結果不一致，很可能反映了社經因素和健康生活型態造成的殘餘干擾（S5）。
  > "the discordance between findings from the randomised controlled trials and observational studies are likely to reflect residual confounding by socioeconomic factors and healthy lifestyles" — S5, Discussion

## RCT 也有限制

- 早餐 RCT 通常時間短：S5 指出所有納入的試驗至少有一個面向的偏誤風險高或不明，而且追蹤期都很短（體重平均 7 週，熱量平均 2 週）（S5）。
  > "All of the included trials were at high or unclear risk of bias in at least one domain and had only short term follow-ups (mean period seven weeks for weight, two weeks for energy intake)." — S5, Abstract
- RCT 研究的結果（例如體重）和觀察型研究 S1 研究的結果（冠心病）不同，所以兩者不是在回答同一個問題（本 wiki 的說明）。

## 相關頁面
- [干擾因子](confounding.md)、[前瞻性世代研究](prospective-cohort.md)
- [Dhurandhar 2014（S3）](../studies/dhurandhar-2014.md)、[Betts 2014（S4）](../studies/betts-2014.md)、[Sievert 2019（S5）](../studies/sievert-2019.md)
- [名詞表：RCT](../glossary.md#rct)、[名詞表：統合分析](../glossary.md#meta-analysis)

## 出處
- S1、S3、S4、S5（見 [sources.md](../../sources.md)）

*僅供教學，不構成醫療建議。*
