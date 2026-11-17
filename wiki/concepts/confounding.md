# 干擾因子（Confounding Factor）

> **一句話重點**：兩件事看起來有關，不一定是 A 造成 B，可能是背後另一個因素同時影響了 A 和 B，這個因素就叫「干擾因子」。

## 白話說明

研究常常會發現「做 A 的人，比較常出現 B」。直覺上我們會以為是 A 造成 B，但其實可能有第三個因素 C：C 讓人比較常做 A，**同時** C 也讓人比較常出現 B。這時候 A 和 B 看起來有關，但 A 不一定是原因。這個 C 就是**干擾因子**（confounding factor，也譯為混淆因子）。S6 在討論早餐與肥胖時提到，可能有「早餐習慣以外的因素」才是原因（S6）；這和干擾因子的概念有關，但 S6 沒有使用這個名詞。

## 教學用例子

夏天時，**冰淇淋賣得越多，溺水的人也越多**。所以吃冰淇淋會讓人溺水嗎？

當然不是。背後的干擾因子是「天氣熱」：天氣熱 → 吃冰淇淋的人變多；天氣熱 → 去游泳的人也變多 → 溺水的人變多。冰淇淋和溺水只是「一起變多」，彼此沒有因果關係。

## 在早餐研究中的例子

S6 的論證順序是：先有一項研究的觀察 → 這類研究受到批評 → 另一項研究支持這個疑慮（S6）。

1. **觀察**：S6 轉述一項被廣泛引用的 2007 年研究暗示，選擇不吃早餐的人比吃早餐的人傾向顯著較常過重或肥胖（S6）。
   > "a widely quoted 2007 study suggested: people who choose to skip breakfast tend to be overweight or obese significantly more often than those who eat breakfast" — S6, Breakfast and weight
2. **批評**：作者指出，這類研究受到批評，因為真的有可能是早餐習慣以外的因素，讓不吃早餐者的肥胖比例較高（S6）。
   > "such studies have been criticized because of the real possibility that a factor other than breakfast habit might be responsible for the higher rates of obesity among breakfast skippers" — S6, Breakfast and weight
3. **支持疑慮的研究**：支持這個疑慮的是，S6 轉述一項近期研究發現，吃早餐的人比較注重健康、也比較規律運動（S6）。
   > "Supporting this concern is a recent study finding that people who eat breakfast are more health conscious and exercise more regularly." — S6, Breakfast and weight

**對照干擾因子的觀念**（以下是本 wiki 的教學解讀，不是 S6 的原文主張）：如果「注重健康、常運動」同時和「吃早餐」以及「體重」有關，它就可能是干擾因子，讓「吃早餐」和「體重」看起來有關。原文只說這是一種可能性，並沒有證明它就是原因。

## 研究者怎麼處理干擾因子？

### 方法一：統計調整（S1 的做法）

觀察型研究沒辦法控制誰吃早餐，所以研究者會先測量可能的干擾因子，再用統計模型把它們的影響「扣掉」（S1）。

- **先找出兩群人的差異**：比起有吃早餐的人，沒吃早餐的參與者比較年輕，也比較可能抽菸、全職工作、未婚、運動較少、喝較多酒（S1）。
  > "Participants who did not report eating breakfast were younger than those who did, and were more likely to be smokers, employed full time, unmarried, less physically active, and drink more alcohol" — S1, Results
- **再調整**：多變項模型調整了已知與疑似的冠心病風險因子，例如熱量攝取（S1）。
  > "Multivariate models were adjusted for known and suspected risk factors of CHD such as energy intake" — S1, Methods

### 調整的限制

- 只能調整「有測量到」的因素；作者表示，他們無法排除有未測量到的干擾因子的可能性（S1）。
  > "we cannot exclude the possibility of unmeasured confounding" — S1, Discussion
- 作者指出，雖然已調整飲食品質、壓力、定期健檢等因素，飲食習慣仍有可能只是生活規律或整體重視健康的標記（S1）。這和 S6 提出的疑慮方向一致（S6）。
  > "Although we adjusted for factors such as diet quality, stress and having regular physical exams to control for a chaotic versus stable lifestyle, it is possible that eating habits could be a marker of lifestyle consistency or general health-seeking behavior." — S1, Discussion

### 方法二：隨機分組（S3、S4、S5 的做法）

把人隨機分組，讓兩組在其他方面一開始就差不多，干擾因子的影響自然變小（本 wiki 的教學說明，見[觀察型研究 vs 隨機對照試驗](observational-vs-rct.md)）。

- S5 作者認為，隨機對照試驗和觀察型研究結果不一致，很可能反映了社經因素和健康生活型態造成的殘餘干擾（S5）。
  > "the discordance between findings from the randomised controlled trials and observational studies are likely to reflect residual confounding by socioeconomic factors and healthy lifestyles" — S5, Discussion

也要注意：調整後關聯變弱，不一定都是干擾因子造成的，也可能是調整到了[中介因子](mediator.md)（S1 稱 BMI、高血壓等為可能的中介因子）。

## 相關頁面
- [不吃早餐會變胖嗎？](../topics/breakfast-and-weight.md)
- [Shmerling 2017（S6）](../studies/shmerling-2017.md)
- [Cahill 2013（S1）](../studies/cahill-2013.md)
- [中介因子](mediator.md)
- [名詞表：干擾因子](../glossary.md#confounding)

## 出處
- S1：Cahill et al. 2013, *Circulation*
- S5：Sievert et al. 2019, *BMJ*
- S6：Shmerling 2017, Harvard Health Blog
- （見 [sources.md](../../sources.md)）

*僅供教學，不構成醫療建議。*
