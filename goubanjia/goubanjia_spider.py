#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import lxml.html
with open('gngnip.txt','w') as f:
    f.write('')
# 构造url
seed_urls = ['http://www.goubanjia.com/free/gngn/index{}.shtml'.format(i) for i in range(1,2)]
# 构造请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    # 'Referer':'http://www.goubanjia.com/free/gwgn/index.shtml',
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control':'max-age=0',
    # 'Host':'www.goubanjia.com',
    # 'Upgrade-Insecure-Requests':'1',
}
# 定义解析函数
def parse(seed_url):

    html_str = requests.get(seed_url,headers=headers).content.decode()
    #导出html源码

    # with open('index.html','w',encoding='utf-8') as f:
    #     f.write(html_str)
    #将html加载问lxml.etree
    tree=lxml.html.fromstring(html_str)
    #定位表格区域
    ip_str = '//*[@id="list"]/table/tbody/tr'
    tr_list = tree.xpath(ip_str)
    with open('gngnip.txt','a',encoding='utf-8') as f:

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

            f.write(ip + '\n')
            print(str(n + 1) + '|' + ip)

if __name__ == '__main__':

    for n,seed_url in enumerate(seed_urls):

        parse(seed_url)




