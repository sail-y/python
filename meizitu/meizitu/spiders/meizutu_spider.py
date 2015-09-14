# -*- coding:utf-8 -*-
__author__ = 'xiaomai'

from scrapy.spiders import BaseSpider
from scrapy import Selector
from meizitu.items import MeizituItem


class MeizituSpider(BaseSpider):
    name = "meizitu"
    allowed_domains = ["meizitu.com"]
    start_urls = [

    ]

    for i in range(1, 10):
        url = "http://www.meizitu.com/a/" + str(i) + ".html"
        start_urls.append(url)

    def parse(self, response):
        hxs = Selector(response)
        title = hxs.xpath('/html/head/title/text()').extract()
        sites = hxs.xpath('//div[@class="postContent"]/p')
        items = []
        for site in sites:
            item = MeizituItem()
            item['link'] = site.xpath('img/@src').extract()
            item['title'] = title
            items.append(item)
        return items
