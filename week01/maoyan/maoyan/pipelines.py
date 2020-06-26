# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanPipeline:
    def process_item(self, item, spider):
        title = item['title']
        mtype = item['mtype']
        mtime = item['mtime']
        movie_info = [[title, mtype, mtime]]
        df = pd.DataFrame(movie_info, columns=['title', 'mtype', 'mtime'])
        df.to_csv('./movies.csv',mode='a',encoding='utf8',index=False,header=False)
        return item
