# This file provides the main code to the automation for OrangeHRM for the testcase of forgot password

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data21 import data21
from Test_Locators21 import Locators21
from selenium.webdriver.common.by import By

class openlink:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
   
    def Forgotpass1(self):
        self.driver.find_element(by=By.XPATH, value=Locators21.Locators_loginnew().forgotpass_box).click()
        self.driver.find_element(by=By.NAME, value=Locators21.Locators_loginnew().username_box).send_keys(data21.Loginnew().username)
        self.driver.find_element(by=By.XPATH, value=Locators21.Locators_loginnew().resetpass_box).click()
        self.driver.implicitly_wait(25)


    def shutdown(self):
        self.driver.quit()


a = openlink(data21.Loginnew().url)
a.Forgotpass1()
a.shutdown()
print("Reset Password Link sent successfully")
