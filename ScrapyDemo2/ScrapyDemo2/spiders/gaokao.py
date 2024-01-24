import json
import pymysql
import scrapy


class GaokaoSpider(scrapy.Spider):
    name = "gaokao"
    allowed_domains = ["gaokao.cn"]
    def start_requests(self) :
        print("start_requests方法被调用了")
        with pymysql.connect(host="localhost",database='spider',user='root',password='',charset='utf8') as conn:
            with conn.cursor() as cur:
                cur.execute("select id from school_base")
                while line := cur.fetchone():
                    school_id = line[0]
                    if school_id:
                        url = f"https://static-data.gaokao.cn/www/2.0/school/{school_id}/info.json"
                        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        json_str = response.text
        json_obj = json.loads(json_str)

        name = json_obj['data']['name']
        num_library = json_obj['data']['num_library']
        create_date = json_obj['data']['create_date']
        area = json_obj['data']['area']
        is_fenxiao = json_obj['data']['is_fenxiao']
        type_name = json_obj['data']['type_name']
        school_nature_name = json_obj['data']['school_nature_name']
        address = json_obj['data']['address']
        content = json_obj['data']['content']

        yield {'name':name,
               'num_library':num_library,
               'create_date':create_date,
               'area':area,
               'is_fenxiao':is_fenxiao,
               'type_name':type_name,
               'school_nature_name':school_nature_name,
               'address':address,
               'content':content,
        }
