import requests
import json


class jztdata(object):

    def __init__(self):
        self.start_url = "http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow=0&pageSize=500&keyword=&interestrate=&limitday=&background=&profittype="
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
        #print(type(html))
        #'max_profit':i['max_profit'],
        #'plat_name':i['plat_name'],'id':i['id'],'profit_type':i['profit_type'],'start_money':i['start_money'],'limit_day':i['limit_day']

        json_content = json.loads(html)
        content_list = [{'product_name':i['product_name'],'id':i['id'],'plat_name':i['plat_name'],'profit_type':i['profit_type'],'max_profit':i['max_profit'],'start_money':i['start_money'],'limit_day':i['limit_day']}for i in json_content['data']['platform']]
        return content_list

    def save_content(self, content_list,next_url):
        with open('jztd.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(str(content))
                f.write('\n')

        with open('jztdid.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(str(content['id']))
                f.write('\n')

        # 爬取完数据后，将该详情页url，写入已爬取过的url txt文档中
        with open('loaded.txt', 'a') as f:
            f.write(str(next_url))
            f.write('\n')



    loaded_list = []
    def run(self):
        # 1.start_url
        next_url = self.start_url
        next_url_list = []
        for i in range(552):
            next_url = "http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow={}&pageSize=500&keyword=&interestrate=&limitday=&background=&profittype=".format(
                i)
            if next_url not in next_url_list:
                next_url_list.append(next_url)
        try:
            with open('loaded.txt') as f:
                while True:
                    url = f.readline()
                    if url:
                        self.loaded_list.append(url.replace('\n', ''))
                    else:
                        break
        except Exception as ret:
            print(ret)
        else:
            pass
        for next_url in next_url_list:
            if next_url not in self.loaded_list:
               # while next_url is not None:
                    # 2.发送请求，获取响应
                    html = self.parse_url(next_url)
                    print('____________')
                    print(html)
                    print('____________')
                    # 3.提取数据
                    content_list = self.get_content(html)
                    # 4.保存数据
                    self.save_content(content_list,next_url)
                    #for i in range(552):
                        #next_url ="http://www.jztdata.com/jzt-api/rest/v1/bankProduct/query?startRow={}&pageSize=500&keyword=&interestrate=&limitday=&background=&profittype=".format(i)




if __name__ == '__main__':
    zt = jztdata()
    zt.run()







