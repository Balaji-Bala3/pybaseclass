from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# class Baseclass():
#     def browser_launch(self):
#         self.driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
#         return self.driver
#     def get_url(self,url):
#         self.driver.get(url)
#     def send_keys(self,element,keys):
#         element.send_keys(keys)
#     def password(self,element,keys):
#         element.send_keys(keys)
#     def get_attribute(self,element):
#         txt=element.get_attribute("value")
#         print(txt)
# 
# class Baseform():
#     def browser(self):
#         self.driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
#         return self.driver
#     def get_url(self,url):
#         self.driver.get(url)
#     def action(self):
#         self.ac=ActionChains(self.driver)
#         return self.ac
#     def drag_drop(self,element1,element2):
#         self.ac.drag_and_drop(element1,element2).perform()     
#     def quit(self):
#         self.driver.quit()

# class Baseform():
#     def browser(self):
#         self.driver=webdriver.Chrome(executable_path=r"C:\Users\User\eclipse-workspace\chromedriver.exe")
#         return self.driver
#     def get_url(self,url):
#         self.driver.get(url)
#     def txtAttribute(self,element):
#         txt=self.driver.execute_script("return arguments[0].getAttribute('value')",element)
#         print(txt)        