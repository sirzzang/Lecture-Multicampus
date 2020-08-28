import scrapy
from naver_crawler.items import NaverCrawlerItem


class NaverSpider(scrapy.Spider):
    name = "naver"

    def start_requests(self):
        urls = [
            "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0011729190"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = NaverCrawlerItem()
        item["url"] = response.url
        item["content"] = response.xpath(
            "//div[@id='articleBodyContents']//text()"
        ).getall()
        item["media"] = response.xpath("//div[@class='press_logo']/a/img/@alt").get()

        yield item