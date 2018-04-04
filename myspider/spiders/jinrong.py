# -*- coding: utf-8 -*-
import scrapy
import json

class JinrongSpider(scrapy.Spider):
    name = 'jinrong'
    allowed_domains = ['gs.amac.org.cn']
    '''http://gs.amac.org.cn/amac-infodisc/api/pof/manager?rand=0.2541594341484972&page=1086&size=20'''

    # start_urls = ['http://gs.amac.org.cn/amac-infodisc/api/pof/manager?rand=0.2541594341484972&page={}&size=20'.format(i) for i in range(10)]
    start_urls = ['http://gs.amac.org.cn/amac-infodisc/api/pof/manager/register-address-agg/province']
    def parse(self, response):
         # json_data = json.loads(response.body_as_unicode())
         print(response.body_as_unicode())

