from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Lesson_6_images.src.avitoparser import settings
from Lesson_6_images.src.avitoparser.spiders.avito import AvitoSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(AvitoSpider, text='телевизор')
    process.start()
