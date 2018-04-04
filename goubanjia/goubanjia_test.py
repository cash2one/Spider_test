#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import lxml.html
from selenium import webdriver
import time


class Goubanjia():
    def __init__(self):
        # 构造url
        # self.urls = ['http://www.goubanjia.com/free/gngn/index{}.shtml'.format(i) for i in range(1,100)]  # 高匿代理
        self.urls = ['http://www.goubanjia.com/free/gngn/index{}.shtml'.format(i) for i in range(1,2)]  # 全部免费代理
        # 构造请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
        with open('gngnip_test.txt','w') as f:
            f.write('')
        self.file = open('gngnip_test.txt','a',encoding='utf-8')
        self.file2 = open('index.html',encoding='utf-8')
        # self.driver = webdriver.Chrome()
    def parse_url(self,url):

        tree = lxml.html.fromstring(self.file2.read())
        return tree

    def save_data(self,data):
        self.file.write(data+'\n')

    def __del__(self):
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
                ip = ''.join(ip_list)+':'+ port

                # 响应速度超过5秒的不要
                # if float(response_list[0].split()[0]) >= 5:
                #     continue

                self.file.write(ip+'\n')
                print(str(n+1)+'|'+ip)

if __name__ == '__main__':
    goubanjia = Goubanjia()
    goubanjia.run()





