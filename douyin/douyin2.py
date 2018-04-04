# -*- coding:utf-8 -*-
import json
import requests
with open('douyin.json',encoding='utf-8') as f:
    data = f.read()

data = json.loads(data)
aweme_list = data['aweme_list']
print(len(aweme_list))
for i,li in enumerate(aweme_list):
    url = li['video']['download_addr']['url_list'][0]
    content = requests.get(url).content
    with open(str(i)+'.mp4','wb') as f:
        f.write(content)
