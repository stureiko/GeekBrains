from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Lesson_6_images.src.leroymerlin import settings
from Lesson_6_images.src.leroymerlin.spiders.leroy_m import LeroyMSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroyMSpider, text='ламинат')
    process.start()
