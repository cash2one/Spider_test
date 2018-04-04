# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from lxml import etree
import time
from copy import deepcopy
from selenium.webdriver import ActionChains
from scrapy import Selector

class JigouSpider(scrapy.Spider):
    name = 'jigou'
    allowed_domains = ['http://www.interotc.cn/mall/gtlmcp.co?typeId=3']
    start_urls = []
    driver = webdriver.Chrome()
    driver.get(str(start_urls))
    html_str = driver.page_source
    tree = etree.HTML(html_str)

    num = 0
    def parse(self,response):
        global num
        #driver = webdriver.Chrome()
        #driver.get(self.start_urls)
        #html_str = driver.page_source
        # 将html加载lxml.etree
        #tree = etree.HTML(html_str)
        # 定位表格区域
        xpath_str = '//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li'
        items = response.xpath(xpath_str)
        # 逐行读取文本
        items = []
        for item in items:
            item = {}
            item['chanpin'] = item.xpath('./div//text()').extract()[0]
            alist = []
            for temp in item['chanpin']:
                for i in temp.split():
                    alist.append(i)

            item['chanpin'] = alist
            items.append(item)
            print(item)
            yield(item)
            # with open('jigo.txt', 'a', encoding='utf-8') as f:
            #     print(item)
            #     f.write(str(item))
            #     f.write('\n')

        # 定位跳转页码按钮
        ac = self.driver.find_element_by_xpath(
            '//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[3]/div/div/div[3]/a[6]')
        ActionChains(self.driver).move_to_element(ac).click(ac).perform()
        time.sleep(1)
        num += 1
        # 点击跳转页码
        # page_jump.click()
        # time.sleep(10)
        if num > 2:
            return
        #get_content()
    #get_content()




