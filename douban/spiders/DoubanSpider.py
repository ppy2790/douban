#coding=utf-8
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

from douban.items import DoubanItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class DoubanSpider(CrawlSpider):

    name = "douban"

    start_urls=['https://book.douban.com/top250']


    def parse(self, response):

        selector = Selector(response)


        infos = selector.xpath('//tr[@class="item"]')

        item = DoubanItem()

        for info in infos:

            bookname = info.xpath('td/div/a/@title').extract()[0]

            url = info.xpath('td/div/a/@href').extract()[0]

            author_info = info.xpath('td/p/text()').extract()[0]

            author_info = str(author_info)

            author_infos = author_info.split('/')

            price = str(author_infos[len(author_infos)-1])



            rating = info.xpath('td/div/span[2]/text()').extract()[0]
            comment_nums = info.xpath('td/div/span[3]/text()').extract()[0]

            quote = info.xpath('td/p/span/text()').extract()

            if len(quote)>0 :
                quote = quote[0]
            else:
                quote = ''


            item['bookname']= bookname
            item['author']=author_infos[0]
            item['rating_nums']=rating
            item['quote']=quote
            item['comment_nums'] = filter(str.isdigit, (str(comment_nums)))
            item['pubday']=author_infos[len(author_infos)-2]
            item['price'] = price
            item['url']=url
            yield item



        for i in range(25,250,25):

            url = 'https://book.douban.com/top250?start=%s'%i

            yield Request(url,callback=self.parse)











