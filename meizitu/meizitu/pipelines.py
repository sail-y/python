# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
import time


class MeizituPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        image_urls = item['link']
        dir = item['title'][0]
        print dir

        if not os.path.exists('pic/' + dir):
            os.mkdir('pic/' + dir)
        for image_url in image_urls:
            fname = str(time.time()) + '.' + image_url.split('.')[-1]
            urllib.urlretrieve(image_url, 'pic/' + dir + '/%s' % fname)
        return item

