import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        # print(response.body)
        resp = json.loads(response.body)
        quotes = resp.get('quotes')
        # print(quotes)

        for quote in quotes:
            yield{
                'author': quote.get('author').get('name'),
                'tags' : quote.get('tags'),
                'quote_text' : quote.get('text')
            }

        has_next = resp.get('has_next')

        if has_next:
            next_pagno = resp.get('page')+1

            yield scrapy.request(
                url = 'http://quotes.toscrape.com/api/quotes?page={next_pagno}',
                callback=self.parse
            )