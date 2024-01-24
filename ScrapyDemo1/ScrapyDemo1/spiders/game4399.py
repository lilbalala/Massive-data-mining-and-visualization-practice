import scrapy


class Game4399Spider(scrapy.Spider):
    name = "game4399"
    allowed_domains = ["4399.com"]
    start_urls = ["https://4399.com/flash/new.htm"]

    def parse(self, response):
        print("开始解析页面：",response.url)
        lis = response.css("ul.n-game>li")

        for li in lis:
            name = li.xpath("./a/b/text()").extract_first()
            type = li.xpath("./em/a/text()").extract_first()
            date = li.xpath("./em[2]/text()").extract_first()

            item = {"name":name,"type":type,"date":date}


            yield item

        next_url = response.xpath("//div[@id='pagg']/a[contains(text(),'下一页')]/@href").extract_first()
        if next_url:
            next_url = response.urljoin(next_url)

            yield scrapy.Request(url=next_url,callback=self.parse)