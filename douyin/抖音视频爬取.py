import sys
import json
import time

import re

import os
import requests
from contextlib2 import closing


class DouYin(object):
    def __init__(self):
        print(sys.getdefaultencoding(), "抖音下载!")
        # urllib3连接错误时抛出exceptions.SSLError
        # http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    # 返回视频文件名字，视频链接和视频总数
    def get_video_url(self, nickname):
        self.nickname = nickname
        # 创建文件用来已爬取过的url，用来去重过滤不再重复爬取
        self.dumplicate = open(nickname + '.txt','a+')
        self.dumplicate.seek(0,0)
        self.urls = self.dumplicate.read().split()
        video_names = []
        video_urls = []
        user_agent = 'Aweme/1.5.8 (iPhone; iOS 11.0.3; Scale/2.00)'
        header = {'User-Agent': user_agent}
        # 搜索链接，通过抖音用户昵称搜索，获取用户id和视频总数
        search_url = "https://aweme.snssdk.com/aweme/v1/discover/search/?iid=15735436175&device_id=37063549497&os_api=18&app_name=aweme&channel=App%20Store&idfa=08621BB7-65C3-454D-908A-D02F565D85F1&device_platform=iphone&build_number=15805&vid=6BD753D7-C89A-4BEF-9C3D-7192E26CF330&openudid=ee5f41b63ff4704166b2f2d8920267fcd109136b&device_type=iPhone6,2&app_version=1.5.8&version_code=1.5.8&os_version=11.0.3&screen_width=640&aid=1128&ac=WIFI&count=10&cursor=0&keyword={0}&type=1&cp=9646915915dce7fbe1&as=a115d95e314449fffd&ts={1}".format(
            nickname, int(time.time()))

        req = requests.get(search_url)
        html = json.loads(req.content.decode('utf-8'))
        aweme_count = 0
        for each in html['user_list']:
            if each['user_info']['nickname'] == nickname:
                aweme_count = each['user_info']['aweme_count'] + 1
                print(aweme_count - 1)
                user_id = each['user_info']['uid']
                print(user_id)
                # 构造用户分享视频链接，用来获取视频连接
                user_url = 'https://www.douyin.com/aweme/v1/aweme/post/?user_id={}&max_cursor=0&count={}'.format(user_id,aweme_count)
                break
        # r = http.request('GET', user_url, headers=header)

        r = requests.get(user_url,headers = header)
        htm = json.loads(r.content.decode('utf-8'))
        # with open('test.json','w',encoding='utf-8') as f:
        #     f.write(r.content.decode())
        aweme_list = htm['aweme_list']
        aweme_list.reverse()
        for n,each in enumerate(aweme_list):
            share_desc = each['desc']
            if not share_desc:
                video_names.append('未命名'+str(n))
            else:
                video_names.append(share_desc)
            video_urls.append(each['video']['play_addr']['url_list'][0])
        return video_names, video_urls, aweme_count

    # 下载视频
    def video_download(self, video_name, video_url):
        # print(self.urls)
        # 判断视频是否已经下载过
        if video_url in self.urls:
            print("此视频已下载:" + video_name)
            return
        # 替换文件名特殊字符，避免创建文件时报错
        video_name = re.sub(r'[/\:*?<>|]','_',video_name)

        # size = 0
        # 下载视频绮里小爱
        with closing(requests.get(video_url,stream=True)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            # print(dir(response))
            if response.status_code == 200:
                print('[文件大小]：%0.2f MB' % (content_size / chunk_size / 1024) + '  ' + video_url)
                download_size = 0
                with open(video_name+'.mp4', 'wb') as file:
                    for data in response.iter_content(chunk_size):
                        file.write(data)
                        # size += len(data)
                        file.flush()
                        download_size += chunk_size
                        download_rate = download_size * 100 / content_size
                        # print("\r%.2f...(%s)" % (download_rate, video_name), end="")
                        print("[{}{}]{}...{}".format("#"*int(download_rate),' '* (100 - int(download_rate)),download_rate,video_name))
                    sys.stdout.flush()
                self.dumplicate.write(video_url+'\n')
                response.close()

    def run(self, nickname):
        video_names, video_urls, aweme_count = self.get_video_url(nickname)
        if nickname not in os.listdir():
            os.mkdir(nickname)
        os.chdir(nickname)
        print("视频下载中：\n")
        for n,video_url in enumerate(video_urls):
            video_url = video_url.replace('playwm', 'play')
            self.video_download(str(n) +'.' + video_names[n], video_url)
        else:
            print('视频已全部下载')


if __name__ == '__main__':
    douyin = DouYin()

    nickname = input("请输入要下载的抖音视频的作者昵称：")
    douyin.run(nickname)