学习笔记

### 任务分解

1.爬虫抓取电影《肖申克的救赎》40个评论并转化为pandas的DateFrame格式

2.使用snownlp对短评进行情感分析

3.把以上步骤取得的数据保存到数据库

4.使用课程豆瓣Django模板，连接数据库进行数据的展示

5.添加搜索模块，页面对应显示搜索后的结果

### 学习心得

1.使用requests.get需要加header，不要会报错

2.豆瓣电影短评span标签的title属性根据评分不同而不同，因此使用正则表达式查找该标签的title属性并读取对应评分，例如title=‘allstar50 rating',读取其中的5为评分

3.发现使用snownlp对短评进行情感分析，对英文的分析结果不太准确，对中文的分析结果比较准确。

4.保存数据到数据库，列名保持和课程豆瓣django模板一样，尽量减少使用成本。

5.搜索模板参考https://cloud.tencent.com/developer/article/1099922，按照本项目的特点进行了修改，增加了一个简单的搜索框，页面所有相关数据会根据搜索结果变化。

