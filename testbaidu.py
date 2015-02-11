# -*- coding=uft-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(10)


