# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class Pistonlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://piston.mini.topka.com.cn")
        time.sleep(5)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("admin@topka.cn")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
#        url1 = driver.current_url
#        print url1
    
#ͨ���Ե�ǰҳ���URL�ж���֤�Ƿ�ɹ���¼     
    def test_currenttitle(self):
        driver = self.driver
        url2 = driver.current_url
        self.assertEquals("http://piston.mini.topka.com.cn/#/main", url2)


#ͨ���Ե�ǰҳ���������ʾ�ж���֤�Ƿ�ɹ���¼    
    def test_wordappear(self):
        driver = self.driver
        p = driver.find_element_by_css_selector("#page-title h1").text
        self.assertEquals(u"admin�����������ˣ�", p)
#        js = "var q=document.getElementById(\"page-title\").childNodes[0].textContent"
#        driver.execute_script(js)
         
       
              
    def tearDown(self):
        self.driver.quit()
       

if __name__ == "__main__":
    unittest.main()

