# -*- coding:utf-8 -*-
import requests
url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?user_id=58971010464&max_cursor=0&count=20&retry_type=no_retry&iid=29462375699&device_id=42368141810&ac=wifi&channel=meizu&aid=1128&app_name=aweme&version_code=179&version_name=1.7.9&device_platform=android&ssmix=a&device_type=M6+Note&device_brand=Meizu&language=zh&os_api=25&os_version=7.1.2&uuid=867291035210274&openudid=311447d77b3ba2c1&manifest_version_code=179&resolution=1080*1920&dpi=480&update_version_code=1792&_rticket=1522551461662&ts=1522551461&as=a155042c652abadab08055&cp=45a8af5f560fc3ade1dqqo&mas=0078027838a508308a666e6663e092a4aaacac0c1c0c4686268646'

res = requests.post(url,verify=False)

print(res.content.decode())
with open('zhanzhan.json','w',encoding='utf-8') as f:
    f.write(res.content.decode())