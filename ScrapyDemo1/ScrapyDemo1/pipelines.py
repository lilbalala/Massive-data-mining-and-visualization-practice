# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapydemo1Pipeline:
    def process_item(self, item, spider):
        # print("管道接收到的数据：",item)

        with open('./data.csv','a',encoding='utf-8') as f:
            f.write(f"{item['name']},{item['type']},{item['date']}\n")
        return item


