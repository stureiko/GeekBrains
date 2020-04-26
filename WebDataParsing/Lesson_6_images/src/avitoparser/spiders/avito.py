# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from Lesson_6_images.src.avitoparser.items import AvitoparserItem
from scrapy.loader import ItemLoader

class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']

    def __init__(self, text):
        self.start_urls = [f'https://www.avito.ru/moskva?q={text}']

    def parse(self, response: HtmlResponse):
        ads_links = response.xpath("//h3/a[@class='snippet-link']/@href").extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('name', "//h1/span/text()")
        loader.add_xpath('photos', "//div[contains(@class, 'gallery-img-frame')]/@data-url")
        yield loader.load_item()
