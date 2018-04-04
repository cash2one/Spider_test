# -*- coding:utf-8 -*-
import requests
# post请求的url
url = 'http://www.pkulaw.cn/doSearch.ashx'
# 请求头
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
# form = [{
#     'menu_item':'law',
#     'clust_db':'chl',
#     'clusterwhere':'效力级别=XA01',
#     'aim_page':{i}
# } for i in range(61)]
#
# for n,f in enumerate(form):
#     res = requests.get(url,data = f,headers=headers)
#     print(res.content.decode('gbk'))
#     with open(str(n)+'.html','wb') as g:
#         g.write(res.content)
# post请求的from表单，据我测试，page_count是必须要有的，aim_page代表第几页
# menu_item可以在法律法规等右击检查看到有gotomenu，
form = {



    'Db':'chl,protocol,lawexplanation,whitebook,workreport,introduction',

    'menu_item':'law',
    'range':'name',
    'aim_page':0,
    'page_count':218,

}
res = requests.post(url,data = form,headers=headers)
print(res.content.decode('gbk'))
with open('0.html','w',encoding='utf-8') as f:
    f.write(res.content.decode('gbk'))