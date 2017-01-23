# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class DoubanItem(Item):

    bookname = Field()
    author = Field()
    rating_nums = Field()
    quote = Field()
    comment_nums = Field()
    pubday = Field()
    price = Field()
    url = Field()

