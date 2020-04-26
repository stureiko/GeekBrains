# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from Lesson_6_images.src.leroymerlin.items import LeroymerlinItem
from scrapy.loader import ItemLoader


class LeroyMSpider(scrapy.Spider):
    name = 'leroy_m'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, text):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={text}']

    def parse(self, response):
        next_page = response.xpath("//a[@class='paginator-button next-paginator-button']/@href").extract_first()
        ads_links = response.xpath("//a[@class='black-link product-name-inner']/@href").extract()
        for link in ads_links:
            yield response.follow(link, callback=self.good_parse)
        yield response.follow(next_page, callback=self.parse)

    def good_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroymerlinItem(), response=response)
        loader.add_xpath('name', "//h1[@slot='title']/text()")
        loader.add_xpath('photos', "//img/@data-origin")
        loader.add_xpath('price', "//span[@slot='price']/text()")
        # loader.add_xpath('param_keys', "//dt[@class='def-list__term']/text()")
        # loader.add_xpath('param_values', "//dd[@class='def-list__definition']/text()")
        yield loader.load_item()

