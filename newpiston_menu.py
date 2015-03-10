# -*- coding:utf-8 -*- 
'''
Created on 2015-3-10

@author: test
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://piston.mini.topka.com.cn")
time.sleep(10)
 
driver.find_element_by_id("inputEmail").send_keys("admin@topka.cn")
driver.find_element_by_id("inputPassword").send_keys("123456")
time.sleep(3)
driver.find_element_by_css_selector("button").click()
time.sleep(3)

neirong = driver.find_element_by_id("content-data").find_element_by_css_selector("h1").text
print neirong
time.sleep(3)

chain = ActionChains(driver)
implement = driver.find_element_by_xpath("/html/body/header/div/section/nav/ul/li")
chain.move_to_element(implement).perform()


#driver.find_element_by_link_text(u"后台用户管理").click()


