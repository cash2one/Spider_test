import time
import requests
from lxml import etree
url_list = []
with open('smjjgl.txt') as f:
    while True:
        url = f.readline()
        if url:
            url_list.append(url.replace('\n',''))
        else:
            break
content_list = []
for url in url_list:
     #print(url)
     html = etree.HTML(requests.get(url).content)
     content = {}
     #print("-" * 8)
     content['gongsi'] = ''.join(html.xpath('//*[@id="complaint1"]/text()')[0].split()).replace('&nbsp','')
     content['company'] = html.xpath('/html/body/div/div[2]/div/table/tbody/tr[4]/td[2]/text()')[0]
     content['Registration number'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[5]/td[2]/text()')[0].split())
     content['Organization code'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[6]/td[2]/text()')[0].split())
     content['Registration time'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[7]/td[2]/text()')[0].split())
     content['Registration time'] = ''.join(str(content['Registration time']).replace('\n','').replace(' ','')[0].split())
     content['Establishment time'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[7]/td[4]/text()')[0].split())
     content['Registered address'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[8]/td[2]/text()')[0].split())
     content['Office address'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[9]/td[2]/text()')[0].split())
     content['Registered capital (10000 yuan)'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[10]/td[2]/text()')[0].split())
     content['Paid in capital (10000 yuan)'] = ''.join(html.xpath('///html/body/div/div[2]/div/table/tbody/tr[10]/td[4]/text()')[0].split())
     content['Enterprise nature'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[11]/td[2]/text()')[0].split())
     content['Type of mechanism'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[12]/td[2]/text()')[0].split())
     content['Number of employees'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[2]/text()')[0].split())
     content['Institutional website'] = ''.join(html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()')[0].split()) if html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()') else html.xpath('/html/body/div/div[2]/div/table/tbody/tr[13]/td[4]/a/text()')
     #print(len(content[1]))
     content_list.append(content)
     #content2 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr/td[2]/text()')
     #print(len(content2))
     #content3 = html.xpath('/html/body/div/div[2]/div/table/tbody/tr//text()')
     with open('detail.txt', 'a', encoding='utf-8') as f:
        for content in content_list:
            if len(content) == 0:
                content_list.remove(content)
            if len(content) != 0:
                print(content)
                f.write(str(content))
                f.write('\n')
     time.sleep(0.5)
