# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import requests 
import json

class CrawlerPipeline:

    def process_item(self, item, spider):
        author = item['author']
        comment = item['comment']
        phone_info = [[author,comment]]
        df = pd.DataFrame(phone_info, columns=['author', 'comment'])
        df.to_csv('./phones.csv',mode='a',encoding='utf8',index=False,header=False)
        return item
