#! /usr/bin/env python
# -*- coding:utf-8 -*-
import random

import requests
import lxml.html
from selenium import webdriver
import time


class Goubanjia():
    def __init__(self,page):
        # 构造url
        self.urls = ['http://www.goubanjia.com/free/gngn/index{}.shtml'.format(i) for i in range(1,page+1)]  # 高匿代理
        # self.urls = ['http://www.goubanjia.com/free/gngn/index{}.shtml'.format(i) for i in random.sample(range(1,101),page)]  # 全部免费代理
        # 构造请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
        # 每次爬取ip，清空原ip文件
        with open('gngnip.txt','w') as f:
            f.write('')
        # 创建一个文件用来存储ip
        self.file = open('gngnip.txt','a')
        self.driver = webdriver.Chrome()
        self.flag = False
    def parse_url(self,url):
        if not self.flag:
            time.sleep(3)
            self.flag = True
        self.driver.get(url)
        html_str = self.driver.page_source
        # with open('index.html', 'w', encoding='utf-8') as f:
        #     f.write(html_str)
        tree = lxml.html.fromstring(html_str)
        return tree

    def save_data(self,data):
        self.file.write(data+'\n')

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):

        for n,url in enumerate(self.urls):
            tree = self.parse_url(url)
            ip_str = '//*[@id="list"]/table/tbody/tr'
            tr_list = tree.xpath(ip_str)
            for tr in tr_list:
                # 全部ip
                all_str = './td[1]//*[@style]/text()'
                # 端口
                port_str = './td[1]/span[@class]/text()'
                # 响应速度
                response_str = './td[6]/text()'
                # 全部ip列表
                ip_list = tr.xpath(all_str)
                # 端口
                port = tr.xpath(port_str)[0]
                # 拼接成完整ip代理
                ip = ''.join(ip_list) + ':' + port

                # 响应速度超过5秒的不要
                # if float(response_list[0].split()[0]) >= 5:
                #     continue
                # proxies = {'http': 'http://' + ip }
                # try:
                #     res = requests.get('http://www.baidu.com/robots.txt', proxies=proxies,timeout=3)
                #     assert res.status_code == 200
                # except Exception as e:
                #     print(e)
                #     continue
                self.file.write(ip + '\n')
                print(str(n + 1) + '|' + ip)

if __name__ == '__main__':
    goubanjia = Goubanjia(100)
    goubanjia.run()





