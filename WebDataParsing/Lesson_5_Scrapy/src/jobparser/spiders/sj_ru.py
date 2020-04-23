# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

from Lesson_5_Scrapy.src.jobparser.items import JobparserItem


class SjruSpider(scrapy.Spider):
    name = 'sj_ru'
    allowed_domains = ['russia.superjob.ru']

    def __init__(self, name):
        self.start_urls = [f'https://russia.superjob.ru/vacancy/search/?keywords={name}']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe']/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)

        vacancy_links = response.xpath("//div[@class='_3mfro CuJz5 PlM3e _2JVkc _3LJqf']/a/@href").extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='_3mfro rFbjy s1nFK _2JVkc']/text()").extract()[0]
        salary = response.xpath("//span[@class='_3mfro _2Wp8I ZON4b PlM3e _2JVkc']/text()").extract()
        link = response.url
        company = response.xpath("//h2[@class='_3mfro PlM3e _2JVkc _2VHxz _3LJqf _15msI']/text()").extract_first()
        location = response.xpath("//span[@class='_6-z9f']").extract()
        yield JobparserItem(name=name, salary=salary, link=link, company=company, location=location)
