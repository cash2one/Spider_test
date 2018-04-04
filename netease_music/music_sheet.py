#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
url_list = ['http://music.163.com/discover/playlist/?offset={}'.format(i*35) for i in range(38) ]
with open('music_sheet1.txt','a',encoding='utf-8') as f:
    for url in url_list:
        html = etree.HTML(requests.get(url).content)
        sheet_names = html.xpath('//p[@class="dec"]/a/text()')
        sheet_urls = []
        for url in html.xpath('//p[@class="dec"]/a/@href'):
            sheet_urls.append('http://music.163.com'+url)
        i = 0
        while i < len(sheet_names):
            f.write('歌单名：'+sheet_names[i]+'\n歌单链接地址：' + sheet_urls[i])
            f.write('\n')
            print(sheet_names[i])
            print(sheet_urls[i])
            # print(type(sheet_names[i]))
            # print(type(sheet_urls[i]))
            i+= 1

