from selenium import webdriver
from lxml import etree
import time
import requests

#启动chrome
driver = webdriver.Chrome()
seed_url = 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html'
#打开网址
driver.get(seed_url)
time.sleep(8)
# 设置初始第一页
num = 0
# 设置初始有弹窗
flag = True
def get_content():
    global num
    global flag
    #定位关闭按钮
    xpath_str ='/html/body/div[6]/div[3]/div/button'
    elem = driver.find_element_by_xpath(xpath_str)
    #点击按钮
    if flag:
        elem.click()
        # 无弹窗，不再点击关闭
        flag = False
    #导出html源码
    html_str = driver.page_source
    #将html加载问lxml.etree
    tree=etree.HTML(html_str)
    #定位表格区域
    xpath_str ='//*[@id="managerList"]/tbody/tr'
    sub_tree_list = tree.xpath(xpath_str)
    #逐行读取文本
    for sub_tree in sub_tree_list:
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
        # proxies = {'http': '88.198.219.62:80'}
        content ="http://gs.amac.org.cn/amac-infodisc/res/pof/manager/"+sub_tree.xpath('./td[2]/a/@href')[0]
        with open('smjjgl.txt','a',encoding='utf-8') as f:
            f.write(content)
            f.write('\n')

    page_num = driver.find_element_by_id('goInput')
    # 页码+1
    num += 1
    # 清空页码输入框
    page_num.clear()
    # 向输入框写入下一页的页码
    page_num.send_keys(num)
    # 定位跳转页码按钮
    page_jump = driver.find_element_by_class_name('btn-go')
    time.sleep(1)
    # 点击跳转页码
    page_jump.click()
    # time.sleep(10)
    if num >= 1:
        return
    get_content()
get_content()





