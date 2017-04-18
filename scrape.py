import scrapy

class ZeitSpider(scrapy.Spider):
    name = "Zeit"  # Name of the Spider
    start_urls = ["http://www.zeit.de/digital/2016-09/kuenstliche-intelligenz-kommentar-bot-zeit"]

    # Entry point for the spider
    def parse(self, response):
        for href in response.css('.pager__page a::attr(href)'):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_item)

    # Method for parsing a product page
    def parse_item(self, response):
        yield {
            'texts': response.css('.comment__body p::text').extract()
        }
