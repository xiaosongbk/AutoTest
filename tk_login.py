# -*- coding: utf-8 -*-   
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("http://mini.topka.com.cn")
time.sleep(20)
driver.find_element_by_link_text(u"µ«¬º").click()

WebDriverWait(driver, 10).until(lambda the_driver:the_driver.find_element_by_class_name('J_popup_body').is_displayed())
email = driver.find_element_by_class_name('J_popup_body').find_element_by_id("login_email").send_keys("xiaosongbk@sina.com")
passwd = driver.find_element_by_class_name('J_popup_body').find_element_by_id("login_password").send_keys("123456")
driver.find_element_by_class_name('J_popup_body').find_element_by_id("login").click()
time.sleep(20)
t=driver.find_element_by_class_name('userbox_bg')
if(t):
    print(u"” œ‰’ ∫≈µ«¬º≥…π¶")
    
else:
    print(u"” œ‰’ ∫≈µ«¬º ß∞‹")