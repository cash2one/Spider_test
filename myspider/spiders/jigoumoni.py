#! /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
# 创建session对象，用来存储登录信息
session = requests.session()
yanzheng = session.get('http://www.interotc.com/CASServer/captcha.do')

# 模拟登录的用户名和密码
login_data = {'username':'18501573414','password':'4580DAF97D62603B59CC7D8D553B135748483FEF99E0EBF5'}
# 下面的url是从登录页面找到的处理登录的url，模拟登录记录登录信息
session.post('http://www.interotc.com/CASServer/login?service=http%3A%2F%2Fwww.interotc.cn%2Fsso%2FstLogin.co%3Fservice%3Dhttp%253A%252F%252Fwww.interotc.cn%252Fmall%252Fgtlmcp.co%253FtypeId%253D3',data = login_data)
# 现在已经可以登录并保存登录状态了
html = session.get('http://www.interotc.cn/mall/gtlmcp.co',verify = False)
a = html.content.decode('utf=8')
print(a)
print(re.findall(r"18501573414",html.content.decode('utf-8')))
# cookies = {'Cookie':'jsessionotc5=jlvD6YEa7ISMGtzzfLcv6A3kO0wVUiJVEs6kidkqgCGyDMQ1Cp2G!1162031241!1255679804; BIGipServerbaojia=3058739392.20480.0000'}
# html = requests.get('http://www.interotc.cn/mall/gtlmcp.co?typeId=3',cookies=cookies)
# a = html.content.decode('utf-8')
# print(a)
