# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']

    def __init__(self, text):
        self.start_urls = [f'https://www.avito.ru/moskva?q={text}']


    def parse(self, response: HtmlResponse):
        ads_links = response.xpath("//h3/a[@class='snippet-link']/@href").extract()
        pass
