# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from Lesson_5_Scrapy.src.jobparser.items import JobparserItem


class SjruSpider(scrapy.Spider):
    name = 'sj_ru'
    allowed_domains = ['russia.superjob.ru']

    def __init__(self, name):
        start_urls = [f'https://russia.superjob.ru/vacancy/search/?keywords={name}']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe']/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancy_links = response.xpath("//div[@class='_3mfro CuJz5 PlM3e _2JVkc _3LJqf']/a/@href").extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = ''
        salary = ''
        link = response.url
        company = ''
        location = ''
        yield JobparserItem(name=name, salary=salary, link=link, company=company, location=location)
