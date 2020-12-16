from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
from email._header_value_parser import get_attribute
from Base import *
from lib2to3.tests.support import driver

# b=Baseclass()
#  
# driver=b.browser_launch()
#  
# b.get_url("https://facebook.com")######################To GET URL
#  
# user=driver.find_element_by_id("email")
#  
# b.send_keys(user,"Guna")         #####################TO SEND_KEYS
#  
# password=driver.find_element_by_id("pass")
#  
# b.password(password,"123456")            ######################TO SEND PASSWORD
#  
# b.get_attribute(password)                   #########################TO GET_ATTRIBUTE

############# DRAG AND DROP############
# b=Baseform()
# 
# driver=b.browser()
# 
# b.get_url("http://demo.guru99.com/test/drag_drop.html ")
# 
# drag=driver.find_element_by_xpath("(//A[@class='button button-orange'])[2]")
# 
# b.action()
# 
# drop=driver.find_element_by_id("amt7")
# 
# b.drag_drop(drag, drop)
# 
# b.quit()
##################################### JAVA SCRPIT EXECUTOR
# b=Baseform()
# driver=b.browser()
# b.get_url("http://facebook.com")
# user=driver.find_element_by_id("email")
# driver.execute_script("arguments[0].setAttribute('value','Bala')",user)
# time.sleep(3)
# b.txtAttribute(user)