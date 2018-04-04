import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#启动chrome
driver = webdriver.Chrome()
seed_url ='http://www.interotc.com/CASServer/login?service=http%3A%2F%2Fwww.interotc.cn%2Fsso%2FstLogin.co%3Fservice%3Dhttp%253A%252F%252Fwww.interotc.cn%252Fmall%252Fgtlmcp.co%253FtypeId%253D3'
#打开网址
driver.get(seed_url)
time.sleep(5)
#driver.find_element_by_id("__aoc_taglib_auto_gen_btn_id_583207591834384").click()
#ac = driver.find_element_by_xpath("//*[@id='__aoc_taglib_auto_gen_btn_id_583207591834384']")
#ActionChains(driver).move_to_element(ac).click(ac).perform()
#输入账号
driver.find_element_by_xpath('//*[@id="username"]').send_keys("18501573414")
# 输入密码
driver.find_element_by_xpath('//*[@id="password_text"]').send_keys("4580DAF97D62603B59CC7D8D553B135748483FEF99E0EBF5")
#输入验证码
driver.find_element_by_xpath('//*[@id="j_captcha_response"]').send_keys("")
time.sleep(10)
#点击登陆
driver.find_element_by_class_name("loginBtn").click()
#cookies={"BIGipServerbaojia=3041962176.20480.0000; jsessioncc=DLjC26SEaf3y1cRmontDwRn5D2wFoQCyjqlZxvBLsqZvHvSrlV2m!-81929920!-752267356; jsessionotc5=s2_DtxAv_O4QPd1zoQIF7cosGBflrrUUvkVlcpxUcYX9zCdNrcSm!1162031241!1255679804"}
