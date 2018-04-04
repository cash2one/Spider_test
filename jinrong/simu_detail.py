#! /usr/bin/env python
# -*- coding:utf-8 -*-
import time
import requests
from lxml import etree
# 设置空列表，用来存放详情页url
url_list = list()
# 设置空列表，用来存放已爬取过的url
loaded_list = list()
# 读取详情页url
with open('smjj2.txt') as f:
    while True:
        url = f.readline()
        if url:
            url_list.append(url.replace('\n',''))
        else:
            break
    # url_list = f.readlines()
# for url in url_list:
#     print(url)
# url_list = ['http://gs.amac.org.cn/amac-infodisc/res/pof/manager/101000000138.html']
# 读取已爬取过的url，如果不存在，则pass
try:
    with open('loaded.txt') as f:
        while True:
            url = f.readline()
            if url:
                loaded_list.append(url.replace('\n',''))
            else:
                break
except Exception as ret:
    print(ret)
else:
    pass
content_list = []
# 遍历请求详情页url
for url in url_list:
    # 如果url不在已爬取过的url中，则执行以下代码，否则跳过不执行
    if url not in loaded_list:
        # 设置请求头信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
        # 设置代理信息
        proxies = {'http':'http://106.14.51.145:8118'}
        # 获取详情页的源码并转换成xpath对象
        html = etree.HTML(requests.get(url,headers=headers,proxies=proxies).content)
        # 设置字典，用来存放爬取到的数据
        item = dict()
        content = {}
        # print("-" * 8)
        content['gongsi'] = ''.join(html.xpath('//*[@id="complaint1"]/text()')[0].split()).replace('&nbsp', '')
        content['company'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[4]/td[2]/text()')[0]
        content['Registration number'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[5]/td[2]/text()')[0].split())
        content['Organization code'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[6]/td[2]/text()')[0].split())
        content['Registration time'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[7]/td[2]/text()')[0].split())
        content['Registration time'] = ''.join(
            str(content['Registration time']).replace('\n', '').replace(' ', '')[0].split())
        content['Establishment time'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[7]/td[4]/text()')[0].split())
        content['Registered address'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[8]/td[2]/text()')[0].split())
        content['Office address'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[9]/td[2]/text()')[0].split())
        content['Registered capital (10000 yuan)'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[10]/td[2]/text()')[0].split())
        content['Paid in capital (10000 yuan)'] = ''.join(
            html.xpath('///html/body/div/div[2]/div/table/tbody/tr[10]/td[4]/text()')[0].split())
        content['Enterprise nature'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[11]/td[2]/text()')[0].split())
        content['Type of mechanism'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[12]/td[2]/text()')[0].split())
        content['Number of employees'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[2]/text()')[0].split())
        content['Institutional website'] = ''.join(
            html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()')[0].split()) if html.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()') else html.xpath(
            '/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()')
        # print(len(content[1]))
        content_list.append(content)
        # content1 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr/td[1]/text()')
        # print(len(content1))
        # content2 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr/td[2]/text()')
        # print(len(content2))
        # 爬取数据的xpath
        content3 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr//text()')
        # 将爬取到的数据进行一定的清洗，比如空格去掉
        with open('detail.txt','a',encoding='utf-8') as f:

            for temp in content3:
                content = temp.split()

                for i in content:
                    if len(i) == 0:
                        content.remove(i)
                if len(content) != 0:
                    print(content)
                    f.write(str(content))
                    f.write('\n')
            f.write('-'*100)
            f.write('\n')
        # 爬取完数据后，将该详情页url，写入已爬取过的urltxt文档中
        with open('loaded.txt','a') as f:
            f.write(url)
            f.write('\n')
        # 防止反爬，等待0.5秒
        time.sleep(0.5)




