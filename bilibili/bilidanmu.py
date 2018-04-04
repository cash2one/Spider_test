#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json
import random
with open('bilidm.txt','w') as f:
    f.write('')
cid_list = []
try:
    with open('yipa.txt',encoding='utf-8') as f:
        aid_list1 = f.read().split(',')
        # print(aid_list1)
except:
    pass
aid_list = [i for i in range(2000000)]
random.shuffle(aid_list)
aid_list = aid_list[:100]
for temp in aid_list:
    try:
        json_data = json.loads(requests.get('https://api.bilibili.com/x/player/pagelist?aid={}&jsonp=jsonp'.format(temp)).content.decode('utf-8'))
        # print(json_data)
        cid = json_data['data'][0]['cid']
        if str(temp) in aid_list1:
            continue
        url = 'https://comment.bilibili.com/{}.xml'.format(cid)

        with open('bilidm.txt','a',encoding='utf-8') as f:
            html = etree.HTML(requests.get(url).content)
            d_content_list = html.xpath('//d/text()')
            d_p_content_list = html.xpath('//d/@p')
            if d_content_list and str(cid) not in aid_list:
                with open('yipa.txt','a',encoding='utf-8') as g:
                    g.write(str(temp)+',')
                f.write('aid:'+str(temp)+',cid:'+str(cid)+',弹幕个数:'+str(len(d_content_list))+',弹幕内容='+str(d_content_list)+',time:'+str(d_p_content_list))
                f.write('\n')
                print(d_content_list)
                print('aid='+str(temp))
                print('p='+str(d_p_content_list))
    except:
        continue



