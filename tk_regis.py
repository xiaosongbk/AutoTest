# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://mini.topka.com.cn")
time.sleep(10)

driver.find_element_by_link_text(u"ע��").click()

if(WebDriverWait(driver,10).until(lambda the_driver:the_driver.find_element_by_class_name("J_popup_body").is_displayed())):
    print(u"�û�ע�ᵯ����ʾ����")
else:
    print(u"�û�ע�ᵯ����ʾ������")


#�������������ʽ����֤ϵͳ�Ƿ��ܹ���ȷ�ж�
driver.find_element_by_id("email").send_keys("aa")
driver.find_element_by_id("nick").click()


element = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/div[2]/span/em")

assert element.text == "�����ʽ����ȷ"
print(u"������ʾ��ȷ")