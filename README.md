# 豆瓣图书TOP250 - Scrapy项目练习

简书文章地址：http://www.jianshu.com/p/efa80ef9ebd0


----

本文没有什么新的内容，就是提供练习、分析思路和讲解，方法步骤都可以参考我之前写的文章。都说豆瓣（图书、电影、小组）、知乎的内容是爬虫学习最好的练习，整理一下作为刚开始学习童鞋的资料，也回答一下之前有同学留言的问题，看代码就行了。另外把之前没有整理的代码，抽这几天时间集中整理一下。

豆瓣图书TOP250 URL
```
https://book.douban.com/top250
```

![](http://upload-images.jianshu.io/upload_images/938707-2c57d973fd9d9f8d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


要抓取的字段
```
    bookname = Field()
    author = Field()
    rating_nums = Field() #豆瓣评分
    quote = Field()  # 一句话介绍、推荐
    comment_nums = Field() # 评价人数
    pubday = Field()
    price = Field()
    url = Field()
```

依然是关键三步：
1. 分析页面，确定循环抓取点，解析字段
  
		selector = Selector(response)

        infos = selector.xpath('//tr[@class="item"]')

        item = DoubanItem()

        for info in infos:
            bookname = info.xpath('td/div/a/@title').extract()[0]
            url = info.xpath('td/div/a/@href').extract()[0]
       
  　

2. 确定分页的方式
 
  ```
for i in range(25,250,25):
            url = 'https://book.douban.com/top250?start=%s'%i
            yield Request(url,callback=self.parse)
```
3. 保存数据
  数据比较少，保存为csv，分析起来方便。在配置文件settings.py中两行代码：
  ```
FEED_URI=u'/Users/apple/Desktop/douban-top250.csv'
FEED_FORMAT='CSV'
```

######[代码Github地址](https://github.com/ppy2790/douban)


----

####豆瓣图书TOP250数据

1. 把这些书都读完需要RMB **7688.55元**，要多长时间不知道
* 最贵的一本（套）书是《明朝那些事儿（1-9）》358.20元
  最便宜的一本书是《呐喊》0.36元（现在肯定不是这个价吧）
  最新的一本书是《无声告白》[美] 伍绮诗  2015-7
* 上榜推荐图书最多的作家是 **村上春树**
  推荐入选图书3本以上的作家还有以下：
  ![](http://upload-images.jianshu.io/upload_images/938707-c1b055b790bf9791.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
* 豆瓣评分最高的三本书 都是9.5分
红楼梦	[清] 曹雪芹 著
灌篮高手31	[日] 井上雄彦
海贼王	尾田荣一郎 
* 可以对比一下简书上的读书推荐。[2016你读了哪些书？-- 简书·读书](http://www.jianshu.com/p/62e494156ed3)

  ![豆瓣图书Top250](http://upload-images.jianshu.io/upload_images/938707-3e424a839573a64d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
