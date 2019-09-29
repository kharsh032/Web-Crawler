from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy import Item
from scrapy import Field


class UrlItem(Item):
    url = Field()


class QuotesSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['www.fidelityinternational.com']
    start_urls = ['https://www.fidelityinternational.com']

    rules = (
        Rule(LinkExtractor(), callback='parse_url'),
    )
    def parse_url(self, response):
        item = UrlItem()
        item['url'] = response.url

        return item