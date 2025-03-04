# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.service import Service
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="C:\\Windows\\SysWOW64\\geckodriver.exe")
        self.webdriver = webdriver.Firefox()
        self.webdriver.implicitly_wait(30)
    
    def test_add_group(self):
        webdriver = self.webdriver
        webdriver.get("http://localhost/addressbook/")
        webdriver.find_element(By.NAME,"user").clear()
        webdriver.find_element(By.NAME,"user").send_keys("admin")
        webdriver.find_element(By.NAME,"pass").click()
        webdriver.find_element(By.NAME,"pass").clear()
        webdriver.find_element(By.NAME,"pass").send_keys("secret")
        webdriver.find_element(By.XPATH,"//input[@value='Login']").click()
        webdriver.find_element(By.LINK_TEXT,"groups").click()
        webdriver.find_element(By.NAME,"new").click()
        webdriver.find_element(By.NAME,"group_name").click()
        webdriver.find_element(By.NAME,"group_name").clear()
        webdriver.find_element(By.NAME,"group_name").send_keys("Jk")
        webdriver.find_element(By.NAME,"group_header").click()
        webdriver.find_element(By.NAME,"group_header").clear()
        webdriver.find_element(By.NAME,"group_header").send_keys("Jkjkjk")
        webdriver.find_element(By.NAME,"submit").click()
        webdriver.find_element(By.LINK_TEXT,"group page").click()
        webdriver.find_element(By.LINK_TEXT,"Logout").click()
    
    def is_element_present(self, how, what):
        try: self.webdriver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.webdriver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.webdriver.quit()

if __name__ == "__main__":
    unittest.main()
