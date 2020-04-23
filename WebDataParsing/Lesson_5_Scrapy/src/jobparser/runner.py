from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Lesson_5_Scrapy.src.jobparser import settings
from Lesson_5_Scrapy.src.jobparser.spiders.hh_ru import HhRuSpider
from Lesson_5_Scrapy.src.jobparser.spiders.sjru import SjruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhRuSpider, text='java')
    # process.crawl(SjruSpider, text='java')
    process.start()

