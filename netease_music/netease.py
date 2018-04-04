# -*- coding:utf-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
url = 'http://music.163.com/discover/playlist/'
driver.get(url)
driver.switch_to.frame('g_iframe')
el = driver.find_element_by_xpath('//*[@id="m-pl-container"]/li[1]/div/a')

print(el)


