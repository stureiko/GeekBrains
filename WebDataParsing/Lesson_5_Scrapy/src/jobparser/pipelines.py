# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re
from lxml import html


class JobparserPipeline(object):

    def __init__(self):
        client = MongoClient('localhost', 27017)
        # БД можно выбрать и так
        self.db = client['vacancies']
        # выбор коллекции документов

    @staticmethod
    def get_hh_salary(item: []) -> []:
        s = item['salary']
        if len(s) > 1:
            r = ''
            for i in s:
                r = r + i
        else:
            r = s[0]

        sal = [None, None, None]

        regex__min_pos = re.compile('^от\s\d')
        min_pos = re.findall(regex__min_pos, r)

        regex_num = re.compile('\d{1,3}\xa0\d{3}')
        num = re.findall(regex_num, r)
        regex_sub = re.compile('\xa0')
        if len(num) == 1:
            if min_pos:
                sal[0] = int(re.sub(regex_sub, '', num[0]))
            else:
                sal[1] = int(re.sub(regex_sub, '', num[0]))
        elif len(num) == 2:
            sal[0] = int(re.sub(regex_sub, '', num[0]))
            sal[1] = int(re.sub(regex_sub, '', num[1]))
        else:
            pass

        regex_cur = re.compile('\d{1,3}\xa0\d{3}\s\w{3}')
        cur_pos = re.findall(regex_cur, r)
        regex_cur_sub = re.compile('\d{1,3}\xa0\d{3}\s')
        if len(cur_pos) > 0:
            sal[2] = re.sub(regex_cur_sub, '', cur_pos[0])

        return sal

    @staticmethod
    def get_hh_company(item: []) -> str:
        r = ''
        for i in item['company']:
            r += i
        return r

    @staticmethod
    def get_hh_name(item: []) -> str:
        r = ''
        for i in item['name']:
            r += i
        return r

    @staticmethod
    def get_hh_location(item: []) -> str:
        r = ''
        a = ''

        for i in item['location']:
            r += i

        root = html.fromstring(r)
        span = root.xpath("//span")
        if len(span) < 1:
            adrr_l = root.xpath("//p/text()")
        else:
            adrr_l = root.xpath("//span/text()")

        for s in adrr_l:
            a += s

        return a

    @staticmethod
    def get_hh_id(line: str) -> str:
        return line.split('?')[0].split('/')[-1]

    @staticmethod
    def get_sj_id(s: str) -> str:
        return s.split('.')[-2].split('-')[-1]

    @staticmethod
    def get_sj_name(item: [])->str:
        return item['name']

    @staticmethod
    def get_sj_location(item: [])->str:
        r = ''
        a = ''

        for i in item['location']:
            r += i
        root = html.fromstring(r)
        adrr_l = root.xpath("//span/text()")

        for s in adrr_l:
            a += s

        return a

    def process_item(self, item, spider):
        doc = {}
        if spider.name == 'hh_ru':
            doc['_id'] = self.get_hh_id(item['link'])
            doc['name'] = self.get_hh_name(item)
            doc['link'] = item['link']
            doc['salary_str'] = item['salary']
            doc['salary'] = self.get_hh_salary(item)
            doc['company'] = self.get_hh_company(item)
            doc['location'] = self.get_hh_location(item)

        if spider.name == 'sj_ru':
            doc['_id'] = self.get_sj_id(item['link'])
            doc['link'] = item['link']
            doc['name'] = self.get_sj_name(item)
            doc['salary_str'] = item['salary']
            doc['company'] = item['company']
            doc['location'] = self.get_sj_location(item)
            doc['salary'] = self.get_hh_salary(item)

        coll = self.db[spider.name]
        coll.update_one({'_id': doc['_id']}, {'$set': doc}, upsert=True)
        return item



