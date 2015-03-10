# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

model_num = 24286
driver = webdriver.Chrome()
driver.get("http://newcar.xcar.com.cn/m24286/config.htm")
time.sleep(8)

#carmodel = driver.find_element_by_class_name("gocar_gmibox_top2").text
print u'xcar-2015��˹ 1.5L �ֶ������� ������������:'

#����ָ����
cs_price_id = "price_" + str(model_num)
#print cs_price_id
#��ȡ������ָ���۵�����
cs_price = driver.find_element_by_id(cs_price_id).text
print u'����ָ����:'+ cs_price

#Ʒ��
b_name_id = "bname_" + str(model_num)
#print b_name_id
#��ȡƷ������
b_name = driver.find_element_by_id(b_name_id).text
print u'Ʒ��:' + b_name

#����
type_name_id = "type_name_" + str(model_num)
#print type_name_id
#��ȡ��������
type_name = driver.find_element_by_id(type_name_id).text
print u'����:' + type_name

#������
m_disl_working_mpower_id = "m_disl_working_mpower_" + str(model_num)
#print m_disl_working_mpower_id
#��ȡ����������
m_disl_working_mpower = driver.find_element_by_id(m_disl_working_mpower_id).text
print u'������:' + m_disl_working_mpower

#������
m_speed_transtype_id = "m_speed_transtype_" + str(model_num)
#print m_speed_transtype_id
#��ȡ����������
m_speed_transtype = driver.find_element_by_id(m_speed_transtype_id).text
print u'������:' + m_speed_transtype


#������*��*�ߣ�
m_length_width_height_id = "m_length_width_height_" + str(model_num)
#print m_length_width_height_id
#��ȡ�����������ߣ�������
m_length_width_height = driver.find_element_by_id(m_length_width_height_id).text
print u'�������:' + m_length_width_height


#�������
syear_id = "syear_" + str(model_num)
#print syear_id
#��ȡ������ݵ�����
syear = driver.find_element_by_id(syear_id).text
print u'�������:' + syear


#��߳��٣�km/h��
m_mspeed_id = "m_mspeed_" + str(model_num)
#print m_mspeed_id
#��ȡ��߳��٣�km/h��������
m_mspeed = driver.find_element_by_id(m_mspeed_id).text
print u'��߳���:' + m_mspeed


#0-100����ʱ��(s)
m_hatime_id = "m_hatime_" + str(model_num)
#print m_hatime_id
#��ȡ0-100����ʱ�䣨s��������
m_hatime = driver.find_element_by_id(m_hatime_id).text
print u'0-100����ʱ��:' + m_hatime


#���Ų��ͺ�(L/100km)
m_comfuel_id = "m_comfuel_" + str(model_num)
#print m_comfuel_id
#��ȡ���Ų��ͺģ�L/100km��������
m_comfuel = driver.find_element_by_id(m_comfuel_id).text
print u'���Ų��ͺ�:' + m_comfuel


#�ٷ��ۺ��ͺģ�L/100km��
m_officfuel_id = "m_officfuel_" + str(model_num)
#print m_officfuel_id
#��ȡ�ٷ��ۺ��ͺģ�L/100km��������
m_officfuel = driver.find_element_by_id(m_officfuel_id).text
print u'�ٷ��ۺ��ͺ�:' + m_officfuel


#��������
m_ypolicy_id = "m_ypolicy_" + str(model_num)
#print m_ypolicy_id
#��ȡ�������ߵ�����
m_ypolicy = driver.find_element_by_id(m_ypolicy_id).text
print u'��������:' + m_ypolicy

print '-' * 50



print u'topka-2015��˹ 1.5L �ֶ������� ������������:'

driver2 = webdriver.Chrome()
driver2.get("http://topka.cn/cars/changan-ford/escort/2015/22472")
time.sleep(8)

#��ȡ����ָ����
topka_cs_price = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li/p[2]").text
print u'topka-����ָ����:' + topka_cs_price

#��ȡƷ��
topka_b_name = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[2]/p[2]").text
print u'topka-Ʒ��:' + topka_b_name

#��ȡ����
topka_type_name = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[3]/p[2]").text
print u'topka-����:' + topka_type_name

#��ȡ������
topka_m_disl_working_mpower = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[4]/p[2]").text
print u'topka-������:' + topka_m_disl_working_mpower

#��ȡ����������
topka_m_speed_transtype = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[5]/p[2]").text
print u'topka-������:' + topka_m_speed_transtype

#��ȡ����*��*��
topka_m_length_width_height = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[6]/p[2]").text
print u'topka-����*��*��:' + topka_m_length_width_height

#��ȡ�������
topka_syear = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[7]/p[2]").text
print u'topka-�������:' + topka_syear

#��ȡ���Ų��ͺ�
topka_m_comfuel = driver2.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/ul/li[10]/p[2]").text
print u'topka-���Ų��ͺģ�L/100km��:' + topka_m_comfuel














print '-' * 50

print u'2015��˹ 1.5L �ֶ������� �����������ñȶԽ��:'

print '*' * 30

print u'����ָ���۱ȶ�:'
print u'xcar-����ָ����:' + cs_price
print u'topka-����ָ����:' + topka_cs_price
if (cs_price == topka_cs_price):
    print u'Congratulations! ����ָ��������һ��'
else:
    print u'Sorry.����ָ�������ݲ�һ��'


print '*' * 30

print u'Ʒ�Ʊȶ�:'
print u'xcar-Ʒ��:' + b_name
print u'topka-Ʒ��:' + topka_b_name
if (b_name == topka_b_name):
    print u'Congratulations! Ʒ������һ��'
else:
    print u'Sorry.Ʒ�����ݲ�һ��'
    

print '*' * 30

print u'����ȶ�:'
print u'xcar-����:' + type_name
print u'topka-����:' + topka_type_name
if (type_name == topka_type_name):
    print u'Congratulations! ��������һ��'
else:
    print u'Sorry.�������ݲ�һ��'


print '*' * 30

print u'�������ȶ�:'
print u'xcar-������:' + m_disl_working_mpower
print u'topka-������:' + topka_m_disl_working_mpower
if (m_disl_working_mpower == topka_m_disl_working_mpower):
    print u'Congratulations! ����������һ��'
else:
    print u'Sorry.���������ݲ�һ��'


print '*' * 30

print u'������ȶ�:'
print u'xcar-������:' + m_speed_transtype
print u'topka-������:' + topka_m_speed_transtype
if (m_speed_transtype == topka_m_speed_transtype):
    print u'Congratulations! ����������һ��'
else:
    print u'Sorry.���������ݲ�һ��'


print '*' * 30

print u'��*��*�߱ȶ�:'
print u'xcar-��*��*��:' + m_length_width_height
print u'topka-��*��*��:' + topka_m_length_width_height
if (m_length_width_height == topka_m_length_width_height):
    print u'Congratulations! ��*��*������һ��'
else:
    print u'Sorry.��*��*�����ݲ�һ��'


print '*' * 30

print u'������ݱȶ�:'
print u'xcar-�������:' + syear
print u'topka-�������:' + topka_syear
if (syear == topka_syear):
    print u'Congratulations! �����������һ��'
else:
    print u'Sorry.����������ݲ�һ��'


print '*' * 30

print u'���Ų��ͺģ�L/100km���ȶ�:'
print u'xcar-���Ų��ͺ�:' + m_comfuel
print u'topka-���Ų��ͺ�:' + topka_m_comfuel
if (m_comfuel == topka_m_comfuel):
    print u'Congratulations! ���Ų��ͺ�����һ��'
else:
    print u'Sorry.���Ų��ͺ����ݲ�һ��'


print '*' * 30


















