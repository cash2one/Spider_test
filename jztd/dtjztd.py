import requests
import json


class dtjztdata(object):

    def __init__(self):
        self.start_url = "http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/XeAolVntMM660%252BHkp9ECPw%253D%253D/0"
        #self.headers = {"User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}

    def _parse_url(self,url):  # 解析url,return html_str
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

        #proxies = {'http': 'http://125.45.87.12:9999'}
        response = requests.get(url, headers=headers,)
        #assert response.status_code == 200
        return response.content.decode()

    def parse_url(self,url):
        #try:
            html_str = self._parse_url(url)
       # except Exception as e:
           # print(e)
           # html_str = None
            return html_str

    def get_content(self,html):

        json_content = json.loads(html)
        #content_list = [{'regis_code':i['regis_code'],'profit_type':i['profit_type'],'limit_day':i['limit_day'],'start_date':i['start_date'],'end_date':i['end_date'],'disbank':i['disbank'],'start_money':i['start_money'],'oprate_mode':i['oprate_mode'],'limit_type':i['limit_type'],'limit_type':i['limit_type'],'pro_start_date':i['pro_start_date'],'pro_end_date':i['pro_end_date'],'limit_day':i['limit_day'],'max_profit':i['max_profit'],'max_profit':i['max_profit'],'expect_profit_year':i['expect_profit_year'],'name':i['name']}for i in json_content['data']['product']]
        json_content = json.loads(html)
        i = json_content['data']['product']
        content_list = [{'regis_code': i['regis_code'],
                        'profit_type': i['profit_type'],
                        'limit_day': i['limit_day'],
                        'start_date': i['start_date'],
                        'end_date': i['end_date'],
                        'disbank': i['disbank'],
                        'start_money': i['start_money'],
                        'oprate_mode': i['oprate_mode'],
                        'limit_type': i['limit_type'],
                        'pro_start_date': i['pro_start_date'],
                        'pro_end_date': i['pro_end_date'],
                        'max_profit': i['max_profit'],
                        'expect_profit_year': i['expect_profit_year'],
                        'name': i['name']}]
        return content_list

    def save_content(self, content_list):
        with open('dtjztdda.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                print(content)
                f.write(str(content))
                f.write('\n')

        #爬取完数据后，将该详情页url，写入已爬取过的url txt文档中
        # with open('loaddded.txt', 'a') as f:
        #     f.write(str(next_url))
        #     print(str(next_url))
        #     f.write('\n')

    #loaddded_list = []
    def run(self):
        # 1.start_url
        id_list = []
        #next_url = self.start_url
        with open('jztdid.txt') as f:
            while True:
                id = f.readline()
                if id:
                    id_list.append(id.replace('\n', ''))
                else:
                    break
        next_url_list = []
        for id in id_list:
            next_url = "http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/"+id.replace('2525','25')+"/0"
            if next_url not in next_url_list:
                next_url_list.append(next_url)
        # try:
        #     with open('loaddded.txt') as f:
        #         while True:
        #             url = f.readline()
        #             if url:
        #                 self.loaddded_list.append(url.replace('\n', ''))
        #             else:
        #                 break
        # except Exception as ret:
        #     print(ret)
        # else:
        #     pass
            #while next_url is not None:
        for next_url in next_url_list:
            #if next_url not in self.loaddded_list:

            # 2.发送请求，获取响应
            html = self.parse_url(next_url)
            print('____________')
            print(html)
            print('____________')
            # 3.提取数据
            content_list = self.get_content(html)
            # 4.保存数据
            self.save_content(content_list,)
           # next_url ="http://www.jztdata.com/jzt-api/rest/v1/product/web/bank/"+id.replace('2525','25')+"/0"
            #print(next_url)



if __name__ == '__main__':
    zt = dtjztdata()
    zt.run()







