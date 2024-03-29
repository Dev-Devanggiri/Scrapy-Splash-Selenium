# -*- coding: utf-8 -*-
import scrapy
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']
  
    def parse(self, response):
        countries = response.xpath("//td/a")

        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
        
            # absolute_url = f"https://www.worldometers.info{link}"
            absolute_url = response.urljoin(link)


        # title = response.xpath("//h1/text()"),get()
        # countries = response.xpath("//td/a/text()").getall()

            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link,callback=self.parse_country)


        # yield {
        #     'country_name' : name,
        #     'country_link' : link
        # }


    def parse_country(self,response):
        logging.info(response.url)