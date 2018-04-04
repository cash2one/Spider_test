#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from selenium import webdriver
import lxml.html
import time
#启动chrome
driver = webdriver.Chrome()
seed_urls = ['http://www.goubanjia.com/free/gngn/index{}.shtml'.format(i) for i in range(1,2)]
#打开网址
def parse(seed_url):
    driver.get(seed_url)
    time.sleep(3)

    #导出html源码
    html_str = driver.page_source
    with open('index.html','w',encoding='utf-8') as f:
        f.write(html_str)
    #将html加载问lxml.etree
    tree=lxml.html.fromstring(html_str)
    #定位表格区域
    ip_str = '//*[@id="list"]/table/tbody/tr'
    tr_list = tree.xpath(ip_str)
    with open('ip3.txt','a',encoding='utf-8') as f:

        for tr in tr_list:
            # 全部ip
            all_str = './td[1]//text()'
            # 重复ip
            span_str = './td[1]//*[not(@style)]/text()'
            # 类型
            type_str = './td[3]/a/text()'
            # 响应速度
            response_str = './td[6]/text()'
            # 全部ip列表
            ip_list = tr.xpath(all_str)
            # 端口
            port = ip_list[-1]
            # 重复ip列表
            span_list = tr.xpath(span_str)
            type_list = tr.xpath(type_str)
            # 响应速度列表
            response_list = tr.xpath(response_str)
            # print(ip_list)
            # print(span_list)
            # 遍历重复列表，把重复的数字从全部ip列表里去掉
            for temp in span_list:
                if temp in ip_list:
                    ip_list.remove(temp)
            ip_list.append(port)
            # 拼接成完整ip代理
            ip = ''.join(ip_list)
            type_ = type_list[0]
            # print(type_,ip)
            # if type_list[0] == 'socks5':
            #     continue
            # if len(type_) >7:
            #     type2 = type_.split(',')
            #     try:
            #         dic1 = dict()
            #         dic1[type2[0]] = type2[0] + '://' + ip
            #         html = requests.get('http://www.baidu.com',proxies=dic1,timeout=5)
            #     except Exception as ret:
            #         print(ret)
            #         continue
            #     else:
            #         f.write(str(dic1))
            #         f.write('\n')
            #         print(dic1)
            #     try:
            #         dic2 = dict()
            #         dic2[type2[1]] = type2[1] + '://' + ip
            #         html = requests.get('https://www.baidu.com',proxies=dic2,timeout=5)
            #     except Exception as ret:
            #         print(ret)
            #         continue
            #     else:
            #         f.write(str(dic2))
            #         f.write('\n')
            #         print(dic2)
            #     continue
            try:
                dic = dict()
                dic[type_] = type_ + '://' + ip
                # html = requests.get(type_ + '://www.baidu.com',proxies=dic,timeout=5)
                # if float(response_list[0].split()[0]) >= 5:
                #     continue
            except Exception as ret:
                print(ret)
                continue
            else:
                f.write(str(dic))
                f.write('\n')
                print(dic)


    # 测试获取到的数据
    # print(sub_tree_list)
    # 处理数据成可访问的url
    # 将url存入文档
    # with open('smjj2.txt','a',encoding='utf-8') as f :
    #     for temp in sub_tree_list:
    #         detail_url = seed_url.replace('index.html',temp)
    #         测试拼接好的url
    #         print(detail_url)
    #         f.write(detail_url)
    #         f.write('\n')
    # driver.close()
for seed_url in seed_urls:
    parse(seed_url)
driver.close()



