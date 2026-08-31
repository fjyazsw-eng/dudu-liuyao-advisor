# 资料来源与取舍说明

本文件记录规则依据和工程借鉴，不把整本古籍复制进 Skill。

## 经典

- [《增删卜易》校对本 PDF](https://data.guoxueruanjian.com/books/%E5%A2%9E%E5%88%A0%E5%8D%9C%E6%98%93%EF%BC%88%E6%A0%A1%E5%AF%B9%EF%BC%9A%E4%B8%AD%E5%9B%BD%E7%94%B7%E5%84%BF%EF%BC%89.pdf)：取用神、原忌仇神、月建日辰、动变本位作用、旬空月破、飞伏、进退和应期总注。特别吸收“先看用神旺相与原忌是否有力”“静值冲、动值合、墓待冲、破待填合、空待填冲”等条件式规则。
- [维基文库《黄金策》](https://zh.wikisource.org/wiki/%E9%BB%84%E9%87%91%E7%AD%96)：吸收“世为己、应为人；动为始、变为终”“别衰旺、辨动静”“六神不胜生克制化”等总纲，并保留“用克世不可机械作凶”的题意裁决。
- [《卜筮正宗》PDF](https://www.xuanxuecenter.com/files/bu_shi_zheng_zong.pdf)：用于交叉核对世应、婚姻财官、六合六冲与案例；同时吸收其对机械爻位分断和大限套法的批评。
- [维基文库《火珠林》](https://zh.wikisource.org/zh-hant/%E7%81%AB%E7%8F%A0%E6%9E%97) 与 [中国哲学书电子化计划《火珠林》](https://ctext.org/wiki.pl?chapter=597193&if=en)：用于理解纳甲火珠林法的源流与六亲、旺衰、生克主线。
- [维基文库《周易》](https://zh.wikisource.org/zh-hans/%E6%98%93) 与 [中国哲学书电子化计划《周易》](https://ctext.org/book-of-changes/yi-jing/zhs)：用于核对卦辞爻辞；在本 Skill 中定位为辅助校义，不取代纳甲断法。

## GitHub 工程借鉴

- [Johnson-Jia/liuyao-divination](https://github.com/Johnson-Jia/liuyao-divination)：MIT。借鉴八步断卦路由、按专题拆 references、暗动/日破和虚合/实局辨析；未照搬其全部速断结论。
- [MIAOzhenhao2002/liuyao](https://github.com/MIAOzhenhao2002/liuyao)：MIT。借鉴“代码管确定事实、模型管综合合成”、作用链和交叉验证思想；本 Skill 不重复其排盘引擎。
- [shubhaviatiningsih-byte/fortune-liuyao-skill](https://github.com/shubhaviatiningsih-byte/fortune-liuyao-skill)：借鉴领域语义路由、事实审计、多现用神比较、“当前病处→解除条件→机会窗口→落实窗口”和防止无根据扩张的约束。
- [world-fortune/6yao-skills](https://github.com/world-fortune/6yao-skills)：借鉴输入明确、计算可回查、结果结构化、排盘与解读分离、支持后续复盘的模块化原则。
- [yaomancy/liuyao-engine](https://github.com/yaomancy/liuyao-engine)：Apache-2.0。作为确定性排盘/事实层的工程参考；用户现有工具已能提供完整盘面，因此不纳入本 Skill 主体。

## 现代案例材料

公开网络案例质量参差，主要用于发现易错点，不作为“准确率证明”。优先采用有完整盘面、原断、明确反馈和时间戳的案例。例如：

- [申请博士是否成功，反馈未成功](https://www.reddit.com/r/EasternOccult/comments/1cdf8ge)
- [感情关系后续反馈](https://www.reddit.com/r/EasternOccult/comments/1g9xwyh)
- [民间体系连载案例](https://www.reddit.com/r/EasternOccult/comments/1lgs9ac)

网络案例可能存在选择性发布、事后解释和无法验证身份的问题，因此只提取“如何保存与复盘”，不将个别命中升级为硬规则。

## 股票专题材料

- 《增删卜易·求财章》提供股票专题的经典骨架：求财以财为用，子孙为财源，兄弟通常劫财，但兄生子、子生财或官制兄时需要按有效作用链权变。古籍没有股票交易这一门，不能把求财断语直接等同K线涨跌。
- [王虎应《细说六爻预测学》公开PDF检索结果](https://vr-d.com/pdf-file/%E5%8D%A0%E5%8D%9C%2F%E7%BB%86%E8%AF%B4%E5%85%AD%E7%88%BB%E9%A2%84%E6%B5%8B%E5%AD%A6_%E7%8E%8B%E8%99%8E%E5%BA%94.pdf)含“一日之内价位变化”案例，采用财爻及原忌神按时辰观察；只借鉴“连续时序逐段触发”，不照搬卦数定点数。
- [王虎应《六爻分类占验技法》公开文本](https://www.scribd.com/document/935528320/%E5%85%AD%E7%88%BB%E5%88%86%E7%B1%BB%E5%8D%A0%E9%AA%8C%E6%8A%80%E6%B3%95%E7%8E%8B%E8%99%8E%E5%BA%94)提供了次日、分时、一周和买卖时点的连续股票案例。吸收“财为行情用神、先总趋势后逐日、原忌必须有效、旺衰决定冲的极性、世与六亲双重解读”等方法；将“官鬼固定为庄家、财受克日固定买入、作者自述命中”降为待验证经验。具体边界见 [王虎应股票断法取舍](wang-huying-stock.md)。
- [《六爻经济预测学》出版目录](https://xinyibooks.net/goods-8191.html)确认该书有独立股票预测章节；未获得可独立核验的完整原始案例数据库，因此不据书名宣称准确率。
- [六爻预测股市卦例探讨](https://www.cafengshuinet.com/m/show_detail.php?id=1904)保留了预测与实际点数的对照，显示财爻主线有一定共识，但化合、卦数和振幅算法分歧很大；作为比较案例，不作硬规则。
- [许西川股市预测法则案例](https://blog.sina.com.cn/s/blog_4ba4633f01000ed4.html)明确承认现代股票断法尚无统一模式，并提出世应看价位的另一派做法。本 Skill 不采用“世爻固定等于股价”，而将世定位为求测者，财为默认行情主用；应爻独发且直连财时才提高其行情权重。
- [现代股票专题文章](https://www.howzhan.com/gu-shi-chen-fu-shui-zuo-zhu-liu-yao-yu-ce-gu-piao-zhang-die-de-yong-shen-xuan-qu-yu-shi-zhan/)常见“财为价格、父母为消息、官鬼为风险”的映射，但案例可核验性有限，神煞结论不纳入核心。
- GitHub现有六爻 Skills 主要成熟在排盘、输入规范、事实审计与通用断卦，没有发现经过公开回测的股票专用 Skill。因此股票模块借鉴其工程结构，不宣称存在可直接移植的成熟股市模型。
- 本工作区既往股票卦采用冻结预测与历史OHLCV复核，已经确认最常见错误是“触发日找对、涨跌极性判反”。由此新增“整体结构→现实阶段→触发→极性→确认条件”的固定顺序。

## 取舍结论

采用：传统取用与生克主线、确定性事实和解释分层、病处—解除条件应期、现实背景校准、冻结预测复盘。

降级为辅助：卦名吉凶、六神、爻位人物画像、十二长生细枝、刑害、方位数字。

暂不纳入核心：无法稳定复核的神煞堆叠、仅凭爻位断具体人物物件、以单一卦名决定结果、用固定打分替代推理、事后为结果重选用神。
