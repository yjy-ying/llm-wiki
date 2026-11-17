# 中介因子（Mediator）

> **一句話重點**：中介因子是「A 影響 B 的中間路徑」；它跟干擾因子不同：干擾因子是在 A 和 B 之外、同時影響兩者的第三個因素。

## 白話說明

假設 A 真的會影響 B，但不是直接影響，而是透過 M：A → M → B。這個 M 就是**中介因子**（mediator），也就是 A 影響 B 的「中間站」（本 wiki 的教學說明）。

如果研究者在統計上把 M 也「調整掉」，A 和 B 之間的關聯通常會變弱，因為中間那條路被擋住了（本 wiki 的教學說明）。S1 就看到這種情形：調整 BMI、高血壓等可能的中介因子後，風險數字變小、也不再顯著（S1）。

**和干擾因子的差別**（本 wiki 的教學說明，S1 未直接比較兩者）：
| | 干擾因子 | 中介因子 |
|---|---|---|
| 位置 | 在 A、B 之外，同時影響兩者 | 在 A 和 B 中間 |
| 圖示 | A ← C → B | A → M → B |
| 早餐例子 | 抽菸、運動少（見[干擾因子](confounding.md)） | BMI、高血壓（S1 的說法） |

## 教學用例子

「熬夜 → 早上起不來 → 遲到」：「早上起不來」就是熬夜造成遲到的中間站。如果只比較「早上都準時起床」的人，熬夜和遲到的關聯就會變弱，但這不代表熬夜沒影響，而是你把它發揮作用的那條路擋掉了。

## 在早餐研究中的例子（S1）

- 只調整年齡時，比起吃早餐的男性，不吃早餐的男性冠心病風險高 33%（S1）。
  > "In age-adjusted models, men who did not eat breakfast had a 33% higher risk of CHD as compared with men who did (RR=1.33, 95% CI: 1.13-1.57)" — S1, Results
- 再調整飲食、人口、活動等因素後，比起吃早餐的男性，不吃早餐的男性冠心病風險高 27%（S1）。
  > "Men who skipped breakfast had a 27% higher risk of CHD as compared with men who did not (RR=1.27, 95% CI:1.06-1.53)." — S1, Abstract
- 再進一步調整 BMI、高膽固醇、高血壓和糖尿病這些可能的中介因子後，風險減弱為 RR=1.18（S1）。
  > "but was attenuated (RR=1.18, 95% CI: 0.98-1.43) when further adjusted for the potential mediators of BMI, hypercholesterolemia, hypertension and diabetes" — S1, Results
- 作者認為，這暗示飲食習慣可能透過與這些傳統風險因子相關的路徑影響冠心病風險（S1）。
  > "suggesting that eating habits may impact risk of CHD through pathways associated with these traditional risk factors" — S1, Discussion

## 要注意的地方

- **S1 內部的語氣不一致**（本 wiki 並列呈現，不替原文選邊）：
  - 肯定語氣：摘要寫道，這些關聯是透過 BMI、高血壓、高膽固醇和糖尿病中介的（S1）。
    > "These associations were mediated by BMI, hypertension, hypercholesterolemia and diabetes." — S1, Abstract
  - 肯定語氣：討論段開頭也用肯定語氣寫道：這些關聯已大幅調整人口、飲食與生活型態因素，並且是透過 BMI 與高血壓、高膽固醇、糖尿病中介的（S1）。
    > "These associations included extensive adjustment for demographic, diet and lifestyle factors, and were mediated by BMI and the health conditions of hypertension, hypercholesterolemia and diabetes." — S1, Discussion
  - 保守語氣：結果段稱它們為「可能的」中介因子；討論段後面也說，這暗示飲食習慣可能透過與這些傳統風險因子相關的路徑影響冠心病風險（S1）。
    > "suggesting that eating habits may impact risk of CHD through pathways associated with these traditional risk factors" — S1, Discussion
  - 保守語氣：臨床觀點段則用保守語氣說，這個關聯可能來自肥胖、高血壓、高膽固醇和糖尿病等機制路徑的組合（S1）。
    > "an association that was potentially due to a combination of the mechanistic pathways of obesity, hypertension, hypercholesterolemia and diabetes" — S1, Clinical Perspective
- 作者也承認，病例數不足以做詳細的中介分析（S1）。
  > "However, we were under powered with cases for a detailed mediation analysis, especially for late night eating." — S1, Discussion
- 關聯變弱，也可能是因為這些因素同時扮演干擾因子；觀察型研究很難完全分清楚（本 wiki 的教學解讀）。

## 相關頁面
- [干擾因子](confounding.md)
- [相對風險與信賴區間](relative-risk.md)
- [Cahill 2013（S1）](../studies/cahill-2013.md)
- [名詞表：中介因子](../glossary.md#mediator)

## 出處
- S1：Cahill et al. 2013, *Circulation*（見 [sources.md](../../sources.md)）

*僅供教學，不構成醫療建議。*
