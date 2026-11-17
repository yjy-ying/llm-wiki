# 相對風險與信賴區間（Relative Risk & Confidence Interval）

> **一句話重點**：相對風險（RR）是「一組人的風險是另一組的幾倍」；信賴區間（CI）是這個數字可能的範圍，如果範圍包含 1，就代表兩組可能沒有差別。

## 白話說明

**相對風險（Relative Risk, RR）**：拿一組人當比較基準（RR = 1），看另一組的風險是它的幾倍（本 wiki 的教學說明）。S1 用吃早餐的人當基準，不吃早餐的人 RR = 1.27，意思是風險大約是 1.27 倍，也就是高出 27%（S1）。

**95% 信賴區間（Confidence Interval, CI）**：研究只調查了一部分人，所以算出來的數字有誤差；CI 是這個數字「合理可能」的範圍（本 wiki 的教學說明）。S1 的主要結果 CI 是 1.06–1.53，整個範圍都大於 1（S1）。

**怎麼看顯不顯著**：如果 CI 的範圍包含 1（例如 0.98–1.43），就代表「兩組沒差別」也在合理範圍內，這時通常說結果「不顯著」（本 wiki 的教學說明）。S1 在年紀較大的參與者中得到 RR 1.06（CI 0.84–1.33），作者就說這個關聯不顯著（S1）。

## 教學用例子

假設吃早餐的班級每 100 人有 4 人感冒，不吃早餐的班級每 100 人有 5 人感冒。那麼 RR = 5 ÷ 4 = 1.25，風險高 25%。

但要注意：「高 25%」聽起來很多，實際上只是每 100 人多 1 個。RR 是**相對**的比較，不是「有 25% 的人會生病」。（S1 沒有報告這種絕對數字，以上為教學說明。）

## 在早餐研究中的例子（S1）

- **顯著**：比起吃早餐的男性，不吃早餐的男性冠心病風險高 27%（S1）。CI 1.06–1.53 不包含 1。
  > "Men who skipped breakfast had a 27% higher risk of CHD as compared with men who did not (RR=1.27, 95% CI:1.06-1.53)." — S1, Abstract
- **不顯著**：再進一步調整 BMI、高膽固醇、高血壓和糖尿病這些可能的中介因子後，風險減弱為 RR=1.18，CI 0.98–1.43 包含 1（S1）。
  > "but was attenuated (RR=1.18, 95% CI: 0.98-1.43) when further adjusted for the potential mediators of BMI, hypercholesterolemia, hypertension and diabetes" — S1, Results
- **不顯著**：在年紀較大的那一半參與者中，這個關聯並不顯著（S1）。
  > "while this association was not significant in the older half of participants (RR = 1.06, 95%CI: 0.84-1.33" — S1, Results
- **百分比和 RR 對不上的例子**：在 60 歲以下的男性中，比起吃早餐的人，不吃早餐的人冠心病風險較高；原文文字寫高 50%，但同一句的 RR 為 1.55（S1）。依 RR 換算應是高 55%，論文內部不一致，本 wiki 兩者並列。
  > "among men ≤ 60 years old, those who skipped breakfast had a 50% higher risk of CHD as compared with men who ate breakfast (multivariate RR = 1.55, 95% CI: 1.09-2.22)" — S1, Results

## 相關頁面
- [前瞻性世代研究](prospective-cohort.md)
- [Cahill 2013（S1）](../studies/cahill-2013.md)
- [早餐和心臟病有關嗎？](../topics/breakfast-and-heart.md)
- [名詞表：RR](../glossary.md#rr)、[名詞表：CI](../glossary.md#ci)

## 出處
- S1：Cahill et al. 2013, *Circulation*（見 [sources.md](../../sources.md)）

*僅供教學，不構成醫療建議。*
