# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from Lesson_5_Scrapy.src.jobparser.items import JobparserItem


class HhRuSpider(scrapy.Spider):
    name = 'hh_ru'
    allowed_domains = ['hh.ru']

    def __init__(self, text):
        self.start_urls = [f'https://hh.ru/search/vacancy?L_save_area=true&clusters=true&enable_snippets=true&text={text}&showClusters=true']

    def parse(self, response: HtmlResponse):
        next_page = response.css("a.HH-Pager-Controls-Next::attr(href)").extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancy_links = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.css("div.vacancy-title h1::text").extract()
        salary = response.xpath("//span[@class='bloko-header-2 bloko-header-2_lite']/text()").extract()
        link = response.url
        company = response.xpath("//span[@class='bloko-section-header-2 bloko-section-header-2_lite']/text()").extract()
        location = response.xpath("//p[@data-qa='vacancy-view-location']").extract()
        yield JobparserItem(name=name, salary=salary, link=link, company=company, location=location)
