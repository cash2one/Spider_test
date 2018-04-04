# -*- coding:utf-8 -*-
from parse2 import *
import json


class KrSpider:
    def __init__(self):
        self.start_url = "http://36kr.com/api/info-flow/main_site/posts?per_page=20"
        '''http://36kr.com/api/info-flow/main_site/posts?b_id=5088197&per_page=20'''
        self.b_id = 0
        '''<script>var props=({"activeInvestors|investor".*),locationnal='''

    def get_content_list(self, html):
        json_content = json.loads(html)
        content_list = [{'b_id':i['id'],'title':i['title'],'img':i['cover']} for i in json_content['data']['items']]
        return content_list

    def save_content(self, content_list):
        with open('3kr.txt', 'a',encoding='utf-8') as f:
            for content in content_list:
                f.write(content['title'])
                f.write('\n')
                f.write(content['img'])
                f.write('\n')
                f.write("http://36kr.com/p/{}.html".format(content['b_id']))
                f.write('\n')
                self.b_id = str(content['b_id']) if content['b_id'] else None
                print(content)

    def run(self):
        # 1.start_url
        next_url = self.start_url
        while next_url is not None:
            # 2.发送请求，获取响应
            html = parse_url(next_url)
            # 3.提取数据，id
            content_list = self.get_content_list(html) if html is not None else []
            # 4.保存数据
            self.save_content(content_list)
            next_url = "http://36kr.com/api/info-flow/main_site/posts?b_id=" + self.b_id + "&per_page=20" if self.b_id else None


if __name__ == '__main__':
    kr = KrSpider()
    kr.run()

