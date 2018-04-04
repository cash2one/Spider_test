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
num = 1
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

        # 定位跳转页码
        #driver.find_element_by_class_name("list-item fixedRate").click()
        #//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li[6]/div/div
        #//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li[7]/div/div
        #//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li[1]/div/div
        #//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li[6]/div/div
        #ac = driver.find_element_by_xpath('//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li[2]/div/div')
        #ActionChains(driver).move_to_element(ac).click(ac).perform()
        ac = driver.find_element_by_xpath('//*[@id="gtlmcp_img_list_container_id"]/div[1]/div[1]/ul/li')
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        # detail_content = {}
        # detail_content['name'] = li.xpath('//*[@id="cpdetail_head_containerid"]/tbody/tr[1]/td[2]/div/span/text()')
        # with open('dtjigo.txt', 'a', encoding='utf-8') as f:
        #     f.write(str(detail_content))
        #     f.write('\n')
        #定位区域
        dtxpath_str = '//*[@id="cpdetail_head_containerid"]/tbody/tr'
        tr_list = tree.xpath(dtxpath_str)
        detail_content = {}
        for tr in tr_list:
            detail_content['name'] = tr.xpath('./tr[1]/td[2]/div/span/text()')
            with open('dtjigo.txt', 'a', encoding='utf-8') as f:
                f.write(str(detail_content))
                f.write('\n')





        content = {}
        content['chanpin'] = li.xpath('./div//text()')
        alist = []
        for temp in content['chanpin']:
            for i in temp.split():
                alist.append(i)

        content['chanpin'] = alist
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
    time.sleep(2)
    num +=1
    # 点击跳转页码
    #page_jump.click()
    # time.sleep(10)
    if num > 2:
        return
    get_content()
get_content()






