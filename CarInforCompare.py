# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

model_num = 24286
driver = webdriver.Chrome()
driver.get("http://newcar.xcar.com.cn/m24286/config.htm")
time.sleep(8)

#carmodel = driver.find_element_by_class_name("gocar_gmibox_top2").text
print u'xcar-2015款福睿斯 1.5L 手动舒适型 基本参数配置:'

#厂商指导价
cs_price_id = "price_" + str(model_num)
#print cs_price_id
#获取经销商指导价的内容
cs_price = driver.find_element_by_id(cs_price_id).text
print u'厂商指导价:'+ cs_price

#品牌
b_name_id = "bname_" + str(model_num)
#print b_name_id
#获取品牌内容
b_name = driver.find_element_by_id(b_name_id).text
print u'品牌:' + b_name

#级别
type_name_id = "type_name_" + str(model_num)
#print type_name_id
#获取级别内容
type_name = driver.find_element_by_id(type_name_id).text
print u'级别:' + type_name

#发动机
m_disl_working_mpower_id = "m_disl_working_mpower_" + str(model_num)
#print m_disl_working_mpower_id
#获取发动机内容
m_disl_working_mpower = driver.find_element_by_id(m_disl_working_mpower_id).text
print u'发动机:' + m_disl_working_mpower

#变速箱
m_speed_transtype_id = "m_speed_transtype_" + str(model_num)
#print m_speed_transtype_id
#获取变速箱内容
m_speed_transtype = driver.find_element_by_id(m_speed_transtype_id).text
print u'变速箱:' + m_speed_transtype


#车身（长*宽*高）
m_length_width_height_id = "m_length_width_height_" + str(model_num)
#print m_length_width_height_id
#获取车身（长、宽、高）的内容
m_length_width_height = driver.find_element_by_id(m_length_width_height_id).text
print u'车身长宽高:' + m_length_width_height


#上市年份
syear_id = "syear_" + str(model_num)
#print syear_id
#获取上市年份的内容
syear = driver.find_element_by_id(syear_id).text
print u'上市年份:' + syear


#最高车速（km/h）
m_mspeed_id = "m_mspeed_" + str(model_num)
#print m_mspeed_id
#获取最高车速（km/h）的内容
m_mspeed = driver.find_element_by_id(m_mspeed_id).text
print u'最高车速:' + m_mspeed


#0-100加速时间(s)
m_hatime_id = "m_hatime_" + str(model_num)
#print m_hatime_id
#获取0-100加速时间（s）的内容
m_hatime = driver.find_element_by_id(m_hatime_id).text
print u'0-100加速时间:' + m_hatime


#工信部油耗(L/100km)
m_comfuel_id = "m_comfuel_" + str(model_num)
#print m_comfuel_id
#获取工信部油耗（L/100km）的内容
m_comfuel = driver.find_element_by_id(m_comfuel_id).text
print u'工信部油耗:' + m_comfuel


#官方综合油耗（L/100km）
m_officfuel_id = "m_officfuel_" + str(model_num)
#print m_officfuel_id
#获取官方综合油耗（L/100km）的内容
m_officfuel = driver.find_element_by_id(m_officfuel_id).text
print u'官方综合油耗:' + m_officfuel


#保修政策
m_ypolicy_id = "m_ypolicy_" + str(model_num)
#print m_ypolicy_id
#获取保修政策的内容
m_ypolicy = driver.find_element_by_id(m_ypolicy_id).text
print u'保修政策:' + m_ypolicy

print '-' * 50



print u'topka-2015款福睿斯 1.5L 手动舒适型 基本参数配置:'

driver2 = webdriver.Chrome()
driver2.get("http://topka.cn/cars/changan-ford/escort/2015/22472")
time.sleep(8)

#获取厂商指导价
topka_cs_price = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li/p[2]").text
print u'topka-厂商指导价:' + topka_cs_price

#获取品牌
topka_b_name = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[2]/p[2]").text
print u'topka-品牌:' + topka_b_name

#获取级别
topka_type_name = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[3]/p[2]").text
print u'topka-级别:' + topka_type_name

#获取发动机
topka_m_disl_working_mpower = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[4]/p[2]").text
print u'topka-发动机:' + topka_m_disl_working_mpower

#获取变速箱内容
topka_m_speed_transtype = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[5]/p[2]").text
print u'topka-变速箱:' + topka_m_speed_transtype

#获取车身长*宽*高
topka_m_length_width_height = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[6]/p[2]").text
print u'topka-车身长*宽*高:' + topka_m_length_width_height

#获取上市年份
topka_syear = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[7]/p[2]").text
print u'topka-上市年份:' + topka_syear

#获取工信部油耗
topka_m_comfuel = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[10]/p[2]").text
print u'topka-工信部油耗（L/100km）:' + topka_m_comfuel














print '-' * 50

print u'2015款福睿斯 1.5L 手动舒适型 基本参数配置比对结果:'

print '*' * 30

print u'厂商指导价比对:'
print u'xcar-厂商指导价:' + cs_price
print u'topka-厂商指导价:' + topka_cs_price
if (cs_price == topka_cs_price):
    print u'Congratulations! 厂商指导价内容一致'
else:
    print u'Sorry.厂商指导价内容不一致'


print '*' * 30

print u'品牌比对:'
print u'xcar-品牌:' + b_name
print u'topka-品牌:' + topka_b_name
if (b_name == topka_b_name):
    print u'Congratulations! 品牌内容一致'
else:
    print u'Sorry.品牌内容不一致'
    

print '*' * 30

print u'级别比对:'
print u'xcar-级别:' + type_name
print u'topka-级别:' + topka_type_name
if (type_name == topka_type_name):
    print u'Congratulations! 级别内容一致'
else:
    print u'Sorry.级别内容不一致'


print '*' * 30

print u'发动机比对:'
print u'xcar-发动机:' + m_disl_working_mpower
print u'topka-发动机:' + topka_m_disl_working_mpower
if (m_disl_working_mpower == topka_m_disl_working_mpower):
    print u'Congratulations! 发动机内容一致'
else:
    print u'Sorry.发动机内容不一致'


print '*' * 30

print u'变速箱比对:'
print u'xcar-变速箱:' + m_speed_transtype
print u'topka-变速箱:' + topka_m_speed_transtype
if (m_speed_transtype == topka_m_speed_transtype):
    print u'Congratulations! 变速箱内容一致'
else:
    print u'Sorry.变速箱内容不一致'


print '*' * 30

print u'长*宽*高比对:'
print u'xcar-长*宽*高:' + m_length_width_height
print u'topka-长*宽*高:' + topka_m_length_width_height
if (m_length_width_height == topka_m_length_width_height):
    print u'Congratulations! 长*宽*高内容一致'
else:
    print u'Sorry.长*宽*高内容不一致'


print '*' * 30

print u'上市年份比对:'
print u'xcar-上市年份:' + syear
print u'topka-上市年份:' + topka_syear
if (syear == topka_syear):
    print u'Congratulations! 上市年份内容一致'
else:
    print u'Sorry.上市年份内容不一致'


print '*' * 30

print u'工信部油耗（L/100km）比对:'
print u'xcar-工信部油耗:' + m_comfuel
print u'topka-工信部油耗:' + topka_m_comfuel
if (m_comfuel == topka_m_comfuel):
    print u'Congratulations! 工信部油耗内容一致'
else:
    print u'Sorry.工信部油耗内容不一致'


print '*' * 30


















