import scrapy
class GaoxiaoSpider(scrapy.Spider):
    name = "gaoxiao"
    allowed_domains = ["www.dxsbb.com"]
    start_urls = ["https://www.dxsbb.com/news/34310.html?tdsourcetag=s_pctim_aiomsg"]

    def parse(self, response):
        print("开始解析页面：",response.url)
        trs = response.css(".tablebox tr")

        print(trs)
        for tr in trs[3::]:
            #对每一行td做判断
            if len(tr.xpath("td"))<6:
                continue
            id = tr.xpath("./td[1]/span/text()").extract_first()
            names = tr.xpath("./td[2]/span//text()").extract()
            name = "".join(names)
            department = tr.xpath("./td[3]/span/text()").extract_first()
            area = tr.xpath("./td[4]/span/text()").extract_first()
            level = tr.xpath("./td[5]/span/text()").extract_first()
            notes = tr.xpath("./td[6]/span/text()").extract_first()

            item = {"id":id,"name":name,"department":department,"area":area,"level":level,"notes":notes}
            print(item)
            yield item

