# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class AvitoparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        # БД можно выбрать и так
        self.db = client['avito']
        # выбор коллекции документов

    def process_item(self, item, spider):
        coll = self.db[spider.name]
        coll.insert_one(item)
        return item


class AvitoPhotosPipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def file_path(self, request, response=None, info=None):
        #TODO: Сделать обработку - чтобы фотографии от разных объяевлений складывались в соотвествующие папки
        pass

    def item_completed(self, results, item, info):
        if results[0]:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
