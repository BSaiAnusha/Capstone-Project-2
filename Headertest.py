# This file provides the main code to the automation for OrangeHRM for Headertestcase
 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data21 import datahead
from Test_Locators21 import Locatorshead
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class HeaderTest:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
   
    def login(self):
        self.driver.find_element(by=By.NAME, value=Locatorshead.Locators_login1().username_input_box).send_keys(datahead.Data_login1().username)
        self.driver.find_element(by=By.NAME, value=Locatorshead.Locators_login1().password_input_box).send_keys(datahead.Data_login1().password)
        self.driver.find_element(by=By.XPATH, value=Locatorshead.Locators_login1().submit_button).click()
   

        adminbutton= self.driver.find_element(by=By.XPATH, value=Locatorshead.adminpage().adminbtn).click()
        print("Title of the page is ", self.driver.title)
        expected_options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Banking", "Configuration"]

        options_elements = [self.driver.find_element(By.XPATH, value=Locatorshead.adminpage().header_box)]
        options_text = options_elements[0].text

        action = ActionChains(self.driver)
        action.click(on_element=adminbutton).perform()

        self.driver.implicitly_wait(10)

        if options_text == expected_options:
            print("All the Admin page headers are visible\n", options_text)
        else:            
            print("All the Admin page headers are visible\n", options_text)
    
    def shutdown(self):
        self.driver.quit()


a = HeaderTest(datahead.Data_login1().url)
a.login()
a.shutdown()
