from selenium import webdriver
import lxml.html
import time
#启动chrome
driver = webdriver.Chrome()
seed_url = 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html'
#打开网址
driver.get(seed_url)
time.sleep(8)
# 设置初始第一页
num = 1
# 设置初始有弹窗
flag = True
while num <= 1086:
    #定位关闭按钮
    xpath_str ='/html/body/div[6]/div[3]/div/button'
    elem = driver.find_element_by_xpath(xpath_str)
    #点击按钮
    if flag:
        elem.click()
        # 无弹窗，不再点击关闭
        flag = False
    page_num = driver.find_element_by_id('goInput')
    # 清空页码输入框
    page_num.clear()
    # 向输入框写入下一页的页码
    page_num.send_keys(num)
    # 定位跳转页码按钮
    page_jump = driver.find_element_by_class_name('btn-go')
    # 点击跳转页码
    page_jump.click()
    time.sleep(0.5)
    #导出html源码
    html_str = driver.page_source
    #将html加载问lxml.etree
    tree=lxml.html.fromstring(html_str)
    #定位表格区域
    xpath_str ='//*[@id="managerList"]/tbody/tr/td[2]/a/@href'
    sub_tree_list = tree.xpath(xpath_str)
    # 测试获取到的数据
    # print(sub_tree_list)
    # 处理数据成可访问的url
    # 将url存入文档
    with open('smjj2.txt','a',encoding='utf-8') as f :
        for temp in sub_tree_list:
            detail_url = seed_url.replace('index.html',temp)
            # 测试拼接好的url
            print(detail_url)
            f.write(detail_url)
            f.write('\n')

    # 页码+1
    num += 1
    time.sleep(0.5)
    # time.sleep(10)



