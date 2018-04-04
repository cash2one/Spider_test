import time
import requests
from lxml import etree
# 设置空列表，用来存放详情页url
url_list = list()
# 设置空列表，用来存放已爬取过的url
loaded_list = list()
# 读取详情页url
with open('smjjgl.txt') as f:
    while True:
        url = f.readline()
        if url:
            url_list.append(url.replace('\n',''))
        else:
            break
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

# content_list = []
for url in url_list:
    # 如果url不在已爬取过的url中，则执行以下代码，否则跳过不执行
    if url not in loaded_list:
         #print(url)
         html_content = requests.get(url).content
         html_source = html_content.decode('utf-8')
         with open('detail.html','w',encoding='utf-8') as f:
             f.write(html_source)
         html = etree.HTML(requests.get(url).content)
         content = {}
         #print("-" * 8)
         content['gongsi'] = ''.join(html.xpath('//*[@id="complaint1"]/text()')[0].replace('&nbsp',''))
         content['company'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[4]/td[2]/text()')
         content['Registration number'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[5]/td[2]/text()')
         content['Organization code'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[6]/td[2]/text()')
         content['Registration time'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[7]/td[2]/text()')[0].split())
         content['Establishment time'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[7]/td[4]/text()')[0].split())
         content['Registered address'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[8]/td[2]/text()')
         content['Office address'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[9]/td[2]/text()')
         content['Registered capital (10000 yuan)'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[10]/td[2]/text()')
         content['Paid in capital (10000 yuan)'] = html.xpath('///html/body/div/div[2]/div/table/tbody/tr[10]/td[4]/text()')
         content['Enterprise nature'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[11]/td[2]/text()')
         content['Type of mechanism'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[12]/td[2]/text()')
         content['Number of employees'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[2]/text()')
         content['Institutional website'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()')
         #print(len(content[1]))
         # content_list.append(content)
         #content2 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr/td[2]/text()')
         #print(len(content2))
         #content3 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr//text()')
         with open('detail.txt', 'a', encoding='utf-8') as f:

            # for temp in content_list:
            print(content)
            f.write(str(content))
            f.write('\n')
                # content = temp.split()
                #
                # for i in content:
                #     if len(i) == 0:
                #         content.remove(i)
                # if len(content) != 0:
                #     print(content)
                #     f.write(str(content))
                #     f.write('\n')

            # 爬取完数据后，将该详情页url，写入已爬取过的urltxt文档中
            with open('loaded.txt', 'a') as f:
                f.write(url)
                f.write('\n')
            # 防止反爬，等待3秒
            time.sleep(3)
