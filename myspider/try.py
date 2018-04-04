#! /usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("传智播客")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.save_screenshot("./qasedd.png")
time.sleep(5)
driver.quit()#退出driver