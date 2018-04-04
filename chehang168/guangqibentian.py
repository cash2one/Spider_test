# -*- coding:utf-8 -*-
import requests
import re
url = 'http://www.chehang168.com/index.php?c=index&m=series&psid=127'
cookie = 'U=765542_6d62d6942e00e771fd58f9379197e68e; SERVERID=5453c49dad5b9c491daed5aecccecb9e|1520925599|1520925404'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
           'Cookie':cookie
           }
res1 = requests.get(url,headers=headers)
res2 = res1.content.decode()
print(re.findall(r'26.68万',res2))
