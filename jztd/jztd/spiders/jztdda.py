# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy


class JztddaSpider(scrapy.Spider):
    name = 'jztdda'
    allowed_domains = ['jztdata.com']
    start_urls = [
        'http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow={}&pageSize=50&keyword=&interestrate=&limitday=&background=&profittype='.format(
            i) for i in range(0, 553)]

    def parse(self, response):
        # html = response.content.decode()
        # json_content = json.loads(html)
        # content_list = [{'product_name':i['product_name'],'id':i['id'],'plat_name':i['plat_name'],'profit_type':i['profit_type'],'max_profit':i['max_profit'],'start_money':i['start_money'],'limit_day':i['limit_day']}for i in json_content['data']['platform']]
        jsonresponse = json.loads(response.body_as_unicode())
        content_list = jsonresponse['data']['platform']
        # self.id_list = []
        for content in content_list:
            item = {}
            item['disbank'] = content['disbank']
            item['id'] = content['id']
            # item['createTime'] = content['createTime']
            # item['updateTime'] = content['updateTime']
            # item['profit_type'] = content['profit_type']
            # self.id_list.append(item['id'])
            print(item)
            # yield(item)
            # for i in range(552):
            #     item['next_url'] = "http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow={}&pageSize=500&keyword=&interestrate=&limitday=&background=&profittype=".format(
            #         i)

            # for id in self.id_list:
            item['url'] = "http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/" + item['id'].replace('2525',
                                                                                                          '25') + "/0"
            yield scrapy.Request(
                item['url'],
                callback=self.parse_dtjztd,
                meta={"item": deepcopy(item)}
            )

    def parse_dtjztd(self, response):
        item = deepcopy(response.meta["item"])
        jsonresponse = json.loads(response.body_as_unicode())
        i = jsonresponse['data']['product']

        # for key,value in i.items():
        #     item = {}
        # item['pro_start_date'] = i['pro_start_date']
        # item['create_time'] = i['create_time']
        item['limit_day'] = i['limit_day']
        # print(item)
        # for id in self.id_list:
        #     item['next_url'] = "http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/" + id.replace('2525',
        #                                                                                           '25') + "/0"
        # if item['next_url'] is not None:
        #     yield scrapy.Request(
        #         item['next_url'],
        #         callback=self.parse_book_list,
        #         meta={"item": deepcopy(response.meta["item"])}
        #     )

        # while content_list is not None:
        # content_list = [{'regis_code': i['regis_code'],
        #                  'profit_type': i['profit_type'],
        #                  'limit_day': i['limit_day'],
        #                  'start_date': i['start_date'],
        #                  'end_date': i['end_date'],
        #                  'disbank': i['disbank'],
        #                  'start_money': i['start_money'],
        #                  'oprate_mode': i['oprate_mode'],
        #                  'limit_type': i['limit_type'],
        #                  'pro_start_date': i['pro_start_date'],
        #                  'pro_end_date': i['pro_end_date'],
        #                  'max_profit': i['max_profit'],
        #                  'expect_profit_year': i['expect_profit_year'],
        #                  'name': i['name']}]
        yield item
