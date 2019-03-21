# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
# import pymysql as pq


class ExPipeline(object):
    """ def __init__(self):
        self.conn = pq.connect(
            host='localhost',
            user='root',
            password='ctj20100030928',
            db='extags',
        )
        self.cur = self.conn.cursor()

    
    def process_item(self, item, spider):
        url = item.get("url", "N/A")
        parody = item.get("parody", "N/A")
        character = item.get("character", "N/A")
        group = item.get("group", "N/A")
        artist = item.get("artist", "N/A")

        sql = "insert into extags(url, parody, character, group, artist)"
        self.cur.execute(sql, (url, parody, character, group, artist))
        self.conn.commit()


    def close_spider(self, spider):
        self.cur.close()
        self.conn.close() """
    

    def __init__(self):
        self.file = codecs.open('tags.json', 'w', encoding='utf-8')
    

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


    def close_spider(self, spider):
        self.file.close()


    def spider_closed(self, spider):
        self.file.close()