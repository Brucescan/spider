import scrapy


class GushiSpider(scrapy.Spider):
    name = "gushi"
    allowed_domains = ["gushiwen.cn"]
    start_urls = ["http://gushiwen.cn/"]

    def parse(self, response, **kwags):
        # print(response.text)
        # print(response.body)
        # print(response.json())
        # print(response.url)
        # print(response.requests.url)
        # print(response.requests.headers)
        print(response)


