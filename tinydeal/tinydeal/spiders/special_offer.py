import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
    # start_urls = ["https://www.web.archive.org"]
    start_urls = [
        'https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html'
    ]

    def parse(self, response):
        pass
