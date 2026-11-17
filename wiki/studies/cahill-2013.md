# Cahill 2013：吃早餐與冠心病的前瞻性研究（Breakfast Eating and Incident Coronary Heart Disease）

> **一句話重點**：追蹤近 2.7 萬名美國男性 16 年後發現，不吃早餐的人冠心病風險較高，但這是觀察型研究，只能看出「相關」，作者也說結果幅度不大、需要重現。

| 項目 | 內容 |
|---|---|
| 編號 | S1 |
| 研究類型 | [前瞻性世代研究](../concepts/prospective-cohort.md)（觀察型研究） |
| 證據等級 | 中：只能看出相關（等級定義見 [AGENTS.md](../../AGENTS.md) 第 1 節） |
| 樣本 | 26,902 名美國男性醫療專業人員，45–82 歲 |
| 期間 | 1992 年起追蹤 16 年 |
| 期刊 | *Circulation*，2013 |
| 引句卡 | [cards/S1.md](../../cards/S1.md) |

## 白話說明

研究者沒有叫任何人改變飲食，而是在 1992 年先問一大群男性「你平常什麼時段會吃東西」，然後追蹤 16 年，看誰後來得了冠心病（S1）。最後比較「有吃早餐的人」和「沒吃早餐的人」誰比較常生病（S1）。

這種研究的好處是人數多、時間長；限制是「吃不吃早餐」是參與者自己選的，所以兩群人可能本來就有很多不同（見[干擾因子](../concepts/confounding.md)）。作者自己也說，無法排除有未測量到的干擾因子（S1）。

## 研究設計

- 研究在 1992 年調查了 26,902 名 45–82 歲、沒有心血管疾病和癌症的美國男性的飲食習慣，包括是否吃早餐（S1）。
  > "Eating habits including breakfast eating were assessed in 1992 in 26,902 American men aged 45-82 years from the Health Professionals Follow-up Study who were free of cardiovascular disease and cancer." — S1, Abstract
- 追蹤 16 年期間，共有 1,527 人新診斷出冠心病（S1）。
  > "During 16 years of follow-up, 1,527 incident CHD cases were diagnosed." — S1, Abstract
- **怎麼算有吃早餐**：只要在前三個進食時段（早餐前、早餐、早餐與午餐之間）中任一個回答有吃，就算有吃早餐（S1）。
  > "we defined breakfast as a positive response to any of the first three eating times" — S1, Methods
- 研究用統計模型調整了已知與疑似的冠心病風險因子，例如熱量攝取，以及飲食品質、抽菸、運動、看電視、睡眠等（S1），見[統計調整](../glossary.md#adjustment)。
  > "Multivariate models were adjusted for known and suspected risk factors of CHD such as energy intake" — S1, Methods

## 主要發現

- **主要結果**：比起吃早餐的男性，不吃早餐的男性冠心病風險高 27%（S1），見[相對風險](../concepts/relative-risk.md)。
  > "Men who skipped breakfast had a 27% higher risk of CHD as compared with men who did not (RR=1.27, 95% CI:1.06-1.53)." — S1, Abstract
- **作者結論**：在這群男性醫療專業人員中，吃早餐與顯著較低的冠心病風險相關（S1）。注意摘要結論用的是 *associated with*（相關）。
  > "Eating breakfast was associated with significantly lower CHD risk in this cohort of male health professionals." — S1, Abstract, Conclusions
- **S1 內部語氣不一致**（並列呈現）：臨床觀點段寫道，作者認為這項研究為「吃早餐有助預防冠心病事件」提供了新證據（S1）。這比摘要結論的「相關」語氣更接近因果；但研究設計是觀察型研究（本 wiki 的說明）。
  > "Our study provides novel evidence of the benefit of breakfast consumption for the prevention of coronary events" — S1, Clinical Perspective
- **調整越多，風險數字越小**（S1）：
  - 只調整年齡時，比起吃早餐的男性，不吃早餐的男性冠心病風險高 33%（S1）。
    > "In age-adjusted models, men who did not eat breakfast had a 33% higher risk of CHD as compared with men who did (RR=1.33, 95% CI: 1.13-1.57)" — S1, Results
  - 再進一步調整 BMI、高膽固醇、高血壓和糖尿病這些可能的中介因子後，風險減弱為 RR=1.18，信賴區間包含 1（S1），見[中介因子](../concepts/mediator.md)。
    > "but was attenuated (RR=1.18, 95% CI: 0.98-1.43) when further adjusted for the potential mediators of BMI, hypercholesterolemia, hypertension and diabetes" — S1, Results
- **年齡差異**：在 60 歲以下的男性中，比起吃早餐的人，不吃早餐的人冠心病風險較高（S1）。⚠️ 原文文字寫「高 50%」，但同一句的 RR 為 1.55，兩者不一致；本 wiki 兩個數字都列出，不自行判斷。
  > "among men ≤ 60 years old, those who skipped breakfast had a 50% higher risk of CHD as compared with men who ate breakfast (multivariate RR = 1.55, 95% CI: 1.09-2.22)" — S1, Results
- 在年紀較大的那一半參與者中，這個關聯並不顯著（S1）。
  > "while this association was not significant in the older half of participants (RR = 1.06, 95%CI: 0.84-1.33" — S1, Results
- **不吃早餐的人會補吃嗎？** 吃早餐的男性平均每天比不吃早餐的男性多吃一次；作者據此推論，不吃早餐的人並沒有在當天稍晚額外補吃（S1）。這和 S6 的說法不同，見[爭議頁](../debates/do-skippers-eat-more-later.md)。
  > "Men who ate breakfast ate on average one more time per day than those who skipped breakfast, implying that those who abstained from breakfast were not eating additional make-up meals later in the day." — S1, Results
- **其他進食習慣**：比起不吃宵夜的男性，睡覺後還吃東西的男性冠心病風險高 55%；一天吃幾次與冠心病風險之間則沒有觀察到關聯（S1）。
  > "No association was observed between eating frequency (times/day) and risk of CHD." — S1, Abstract

## 兩群人本來就不一樣

- 比起有吃早餐的人，沒吃早餐的參與者比較年輕，也比較可能抽菸、全職工作、未婚、運動較少、喝較多酒（S1）。這些差異就是可能的[干擾因子](../concepts/confounding.md)，研究用統計調整處理了其中一部分（S1）。
  > "Participants who did not report eating breakfast were younger than those who did, and were more likely to be smokers, employed full time, unmarried, less physically active, and drink more alcohol" — S1, Results

## 研究限制（作者自己提到的）

- 作者表示，他們無法排除有未測量到的干擾因子的可能性（S1）。
  > "we cannot exclude the possibility of unmeasured confounding" — S1, Discussion
- 作者指出，雖然已調整飲食品質、壓力、定期健檢等因素，飲食習慣仍有可能只是生活規律或整體重視健康的標記（S1）。
  > "Although we adjusted for factors such as diet quality, stress and having regular physical exams to control for a chaotic versus stable lifestyle, it is possible that eating habits could be a marker of lifestyle consistency or general health-seeking behavior." — S1, Discussion
- 只有男性，而且約 97% 的參與者是歐洲白人後裔（S1）。
  > "Approximately 97% of participants were of white European descent." — S1, Methods
- 研究對象整體平均飲食品質良好，所以還不知道結果能否推論到飲食品質較差的族群（S1）。
  > "The overall average diet quality of our study population was good, so it is not known if our results are generalizable to other populations with lower diet quality." — S1, Discussion
- 飲食習慣的問題只問過一次（S1）。
  > "The eating habits question was only asked once" — S1, Discussion
- 研究只有固定飲食習慣的資料，所以無法估計與偶爾不吃早餐相關的冠心病風險可能有多大（S1）。
  > "The present study only had data on regular eating habits, and so we could not estimate the risk of CHD associated with occasional eating habits such as skipping breakfast a couple of days a week." — S1, Discussion
- 作者表示，他們發現的關聯雖然顯著，但幅度不大，需要其他研究重現（S1）。
  > "the associations we report are significant but modest, requiring replication" — S1, Discussion

## 作者的條件式看法

- 作者認為，**如果**在女性和其他族群中得到重現，這項研究的結果可以作為醫師和衛生單位提出每天吃早餐建議的證據（S1）。這是作者有前提的看法，本 wiki 不把它當成建議。
  > "If replicated in women and other ethno-cultural groups, the findings from the present study provide evidence to support a recommendation of daily breakfast eating by clinicians and health authorities" — S1, Discussion

## 和其他研究的關係

- 早餐與心臟病的整理：[早餐和心臟病有關嗎？](../topics/breakfast-and-heart.md)
- 「不吃早餐的人會補吃嗎？」S6 與 S1 說法不同：[爭議頁](../debates/do-skippers-eat-more-later.md)
- 研究方法：[前瞻性世代研究](../concepts/prospective-cohort.md)、[相對風險](../concepts/relative-risk.md)、[干擾因子](../concepts/confounding.md)、[中介因子](../concepts/mediator.md)

## 出處
- S1：Cahill et al. 2013, *Circulation*（見 [sources.md](../../sources.md)）

*僅供教學，不構成醫療建議。*
