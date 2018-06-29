# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi

class RegionPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('pymysql',
            host = 'localhost',
            db = 'python',
            user = 'root',
            passwd = 'root',
            cursorclass = pymysql.cursors.DictCursor,
            charset = 'utf8',)


    # def open_spider(self, spider):
    #     self.db = pymysql.connect('localhost', 'root', 'root', 'python')
    #     self.db.set_charset('utf8')
    #
    # def close_spider(self, spider):
    #     self.db.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self._conditonal_insert, item)
        return item

    def _conditonal_insert(self, tx, item):
        tx.execute("insert into china_regions(p_code, code, `name`, `url`, `level`) values('%s','%s','%s', '%s', '%s')" % (item['p_code'], item['code'], item['name'], item['url'], item['level']))


        # cursor = self.db.cursor()
        # # cursor.execute("select count(id) from china_regions where code=%s" % item['code'])
        # # if cursor.fetchone()[0] == 0:
        # sql = "insert into china_regions(p_code, code, `name`, `url`, `level`) values('%s','%s','%s', '%s', '%s')" % (item['p_code'], item['code'], item['name'], item['url'], item['level'])
        # cursor.execute(sql)
        # self.db.commit()
