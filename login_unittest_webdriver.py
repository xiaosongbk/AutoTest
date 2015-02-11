# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Logintest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.base_url = "http://mini.topka.com.cn"

    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"µÇÂ¼").click()
        driver.find_element_by_id("login_email").clear()
        driver.find_element_by_id("login_email").send_keys("xiaosongbk@sina.com")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("123456")
        driver.find_element_by_id("login").click()
        time.sleep(15)
    

    def tearDown(self):
       self.driver.quit()
       

if __name__ == "__main__":
    unittest.main()
