# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy
import time


class JztddaSpider(scrapy.Spider):
    name = 'jztdda'
    allowed_domains = ['jztdata.com']
    # 这里直接用列表推导式，生成所有待爬取的json数据对应的url
    start_urls = ['http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow={}&pageSize=500&keyword=&interestrate=&limitday=&background=&profittype='.format(i) for i in range(552)]

    def parse(self, response):
        #html = response.content.decode()
        #json_content = json.loads(html)
        jsonresponse = json.loads(response.body_as_unicode())
        content_list = jsonresponse['data']['platform']
        # 这里不需要列表
        # self.id_list = []
        for content in content_list:
            item = {}
            item['disbank'] = content['disbank']
            item['id'] = content['id']
            # self.id_list.append(item['id'])
            # print(item)
            # 这里不需要，json数据的url在起始url列表里可以直接放多个，scrapy框架会依次爬取start_urls列表里的所有url
            # for i in range(552):
            #     item['next_url'] = "http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow={}&pageSize=500&keyword=&interestrate=&limitday=&background=&profittype=".format(
            #         i)
            # 这里不需要遍历列表
            # for id in self.id_list:
            #
            # 每一个content对应的id键对应的值，直接用来拼接成url，交给下一个parse方法处理就可以了
            item['url'] = "http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/" + item['id'].replace('2525',
                                                                                                  '25') + "/0"
            yield scrapy.Request(
                item['url'],
                callback = self.parse_dtjztd,
                meta = {"item":deepcopy(item)}
            )
            # item['id'] = content['id']
            # id_list.append(item['id'])
            # for id in id_list:
            #     item['url'] = "http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/"+id.replace('2525','25')+"/0"
            #     if item['url'] is not None:
            #         yield scrapy.Request(
            #             item["url"],
            #             callback=self.parse_dtjztd,
            #             mata = {"item":deepcopy(item)}
            #         )

    def parse_dtjztd(self,response):
        item = deepcopy(response.meta["item"])
        jsonresponse = json.loads(response.body_as_unicode())
        i = jsonresponse['data']['product']
        # 这里不需要遍历i的items，直接赋值给item就可以了
        # for key,value in i.items():
        # 不要再重新创建一个字典，把这些关联的数据放在一个字典里
        # item = {}
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






        #while content_list is not None:
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




