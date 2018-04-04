# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from chehang.items import ChehangItem
from selenium import webdriver
import time

url = 'http://www.chehang168.com/index.php?c=index&m=series&psid=124'
# url2 = 'http://www.chehang168.com/index.php?c=login&m=index'
#
# options = webdriver.ChromeOptions()
#
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#
# driver= webdriver.Chrome(chrome_options=options)
#
# dr = webdriver.Chrome()
#
# dr.get(url2)
#
# e1_1 = dr.find_elenium_by_xpath('div[@class="right"]')
# dr.switch_to.frame(e1_1)
#
# # rl = dr.find_elenium_by_id('')
# el_user = dr.find_elenium_by_id('uname')
# el_user.send_keys('15050262552')
# el_pwd = dr.find_elenium_by_id('pwd')
# el_pwd.send_keys('rise19970717')
# time.sleep(2)
#
# el_sub = dr.find_elenium_by_id('div[@class="right"]')
# # el_sub.click()

# cookie = 'U=765542_6d62d6942e00e771fd58f9379197e68e; SERVERID=5453c49dad5b9c491daed5aecccecb9e|1520925599|1520925404'
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
#            'Cookie':cookie
#            }


class BentianSpider(scrapy.Spider):
    name = 'bentian'
    allowed_domains = ['chehang168.com']
    start_urls = ['http://www.chehang168.com/index.php?c=index&m=series&psid=127']

    print(start_urls)

    # rules = (
    #     Rule(LinkExtractor(allow=r'\&pricetype=0&page=\d+'),callback='parse_item',follow=True)
    # )
    #
    # def start_requests(self):
    #     url = self.start_urls[0]
    #     post_data ={
    #         'email': '15050262552',
    #         'password': 'rise19970717',
    #     }
    #     # 发送post请求
    #     yield scrapy.FormRequest(
    #         url,
    #         formdata=post_data
    #     )


    def parse(self, response):
        # 获取所有车节点列表？
        node_list = response.xpath('ul[@class="ch_carlistv3"]')
        print('------------',len(node_list))

        for node in node_list:
            item = ChehangItem()

            item['model'] = node.xpath('//li/div/h3/a/text()').extract_first()
            item['price'] = node.xpath('./li/div/span/b/text()').extract_first()
            item['color'] = node.xpath('./li/p/text()').extract_first()
            item['address'] = node.xpath('./li/p[2]/a/text()').extract_first()
            item['volume'] = node.xpath('./li/p[2]/cite[2]/text()').extract_first()
            item['guide_price'] = node.xpath('./li/div/h3/b/text()').extract_first()
            print(item)

