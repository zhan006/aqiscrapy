# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class BeijingaqiPipeline(object):
    def open_spider(self,spider):
        self.file=open('aqi.json','w')
    def process_item(self, item, spider):
        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()
    
