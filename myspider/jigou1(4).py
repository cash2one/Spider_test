import time
from selenium import webdriver
from lxml import etree
from selenium.webdriver import ActionChains
#启动chrome
driver = webdriver.Chrome()
seed_url ='http://www.interotc.cn/mall/gtlmcp.co?typeId=3'
#打开网址
driver.get(seed_url)
time.sleep(5)
#导出html源码
num = 0
def get_content():
    global num
    html_str = driver.page_source
    # 将html加载问lxml.etree
    tree=etree.HTML(html_str)
    #定位表格区域
    xpath_str ='//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li'
    li_list = tree.xpath(xpath_str)
    # 逐行读取文本
    content_list = []
    for li in li_list:
        content = {}
        content['chanpin'] = li.xpath('./div/div/span/b/p/a/text()')
        #'/ li[2] / div / div'
        #content['stage'] = sub_tree.xpath('./li[1]/div/div/span/text()')
        #content['Expected annualized'] = sub_tree.xpath('./li[1]/div/div/div[1].text()')
        #content['stage'] = sub_tree.xpath('./li[1]/div/div/span/text()')
        #content['stage'] = sub_tree.xpath('./li[1]/div/div/span/text()')
        content_list.append(content)
        with open('jigo.txt', 'a', encoding='utf-8') as f:
            print(content)
            f.write(str(content))
            f.write('\n')

    # 定位跳转页码按钮
    ac = driver.find_element_by_xpath('//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[3]/div/div/div[3]/a[6]')
    ActionChains(driver).move_to_element(ac).click(ac).perform()
    time.sleep(1)
    num +=1
    # 点击跳转页码
    #page_jump.click()
    # time.sleep(10)
    if num > 2:
        return
    get_content()
get_content()






