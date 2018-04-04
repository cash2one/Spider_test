# -*- coding:utf-8 -*-
import requests
from lxml import etree
import re
cookie = 'SINAGLOBAL=4380370452482.112.1516539969108; un=453052784@qq.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh4wIswkT768X6Xgx-FD_ah5JpX5KMhUgL.Foz7ehnfS0q71KM2dJLoI0qLxKML1hnLBo2LxK.L1-BL1--LxK.L1KBL1K.LxKqLBoeLB-2LxK.L1-BL1--LxKnLB.qL1hMt; UOR=,,login.sina.com.cn; SWB=usrmdinst_9; ALF=1552377903; SSOLoginState=1520841918; SCF=AnI_jKMnwXTxalLODMld1PTMzf-ijPj3IuNoGtVTcsmsn5PytA9cyLlGH3_5tCM_TXS7Bu62hWL63-5kJoDPZDM.; SUB=_2A253okTvDeRhGeRO61oU9yjMwjuIHXVU1jEnrDV8PUNbmtBeLWbnkW9NUJk8ioJtdZXgylZy3BgV27TAIrdJw3l6; SUHB=0oUp2OwTMcFhKO; _s_tentry=-; Apache=8858577403383.348.1520841926165; ULV=1520841926195:9:3:1:8858577403383.348.1520841926165:1520487940808'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','Cookie':cookie}
url = 'http://s.weibo.com/user/%E4%BA%92%E8%81%94%E7%BD%91&Refer=SUer_box'
res = requests.get(url,headers=headers)

a = res.content

html = etree.HTML(a)
el = html.xpath('//a/text()')
print(el)
