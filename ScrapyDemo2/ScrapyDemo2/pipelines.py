# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import jionlp
import pymysql
from ScrapyDemo2.spiders.gaokao import GaokaoSpider
from ScrapyDemo2.spiders.gaoxiao import GaoxiaoSpider

class SchoolBaseMysqlPipeline:
    def process_item(self,item,spider):
        if isinstance(spider, GaoxiaoSpider):
            print("数据从gaoxiao爬虫传来的")
            item['province'] = jionlp.parse_location(item['area'])['province']
            sql = "insert into school_base(id,name,department,province,area,level,notes) values (%s,%s,%s,%s,%s,%s,%s)"

            with pymysql.connect(host="localhost", user="root", password="", database="spider", charset='utf8') as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (item['id'], item['name'], item['department'], item['area'], item['level'],item['notes']))
                conn.commit()
            print("已存入数据", item)
        else:
            print("数据是从schooldetail传来")

        return item


class SchoolDetialMysqlPipeline:
    def process_item(self,item,spider):
        if isinstance(spider,GaokaoSpider):
            print("数据是从gaokao爬虫传来的")
            sql = "insert into school_detail(name,num_library,create_date,area,is_fenxiao,type_name,school_nature_name,address,content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            with pymysql.connect(host="localhost",user="root",password="",database="spider",charset='utf8') as conn:
                with conn.cursor() as cur:
                    cur.execute(sql,(item['name'],item['num_library'],item['create_date'],item['area'],item['is_fenxiao'],item['type_name'],item['school_nature_name'],item['address'],item['content']))
                conn.commit()
            print("已存入数据",item)
        else:
            print("数据是从schoolbase传来")

        return item