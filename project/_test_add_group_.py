# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from project.group import Group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="C:\\Windows\\SysWOW64\\geckodriver.exe")
        self.webdriver = webdriver.Firefox()
        self.webdriver.implicitly_wait(30)

    def open_home_page(self, webdriver):
        # open home page
        webdriver.get("http://localhost/addressbook/")

    def login(self, webdriver, username, password):
        # login
        webdriver.find_element(By.NAME, "user").clear()
        webdriver.find_element(By.NAME, "user").send_keys(username)
        webdriver.find_element(By.NAME, "pass").click()
        webdriver.find_element(By.NAME, "pass").clear()
        webdriver.find_element(By.NAME, "pass").send_keys(password)
        webdriver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self, webdriver):
        # open groups page
        webdriver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, webdriver, group):
        # init group creation
        webdriver.find_element(By.NAME, "new").click()
        # fill group form
        webdriver.find_element(By.NAME, "group_name").click()
        webdriver.find_element(By.NAME, "group_name").clear()
        webdriver.find_element(By.NAME, "group_name").send_keys(group.name)
        webdriver.find_element(By.NAME, "group_header").click()
        webdriver.find_element(By.NAME, "group_header").clear()
        webdriver.find_element(By.NAME, "group_header").send_keys(group.header)
        webdriver.find_element(By.NAME, "group_footer").click()
        webdriver.find_element(By.NAME, "group_footer").clear()
        webdriver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        webdriver.find_element(By.NAME, "submit").click()

    def return_to_group_page(self, webdriver):
        # return to groups page
        webdriver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self, webdriver):
        # logout
        webdriver.find_element(By.LINK_TEXT, "Logout").click()

    def test_add_group(self):
        webdriver = self.webdriver
        self.open_home_page(webdriver)
        self.login(webdriver, "admin", "secret")
        self.open_groups_page(webdriver)
        self.create_group(webdriver, Group("Jk", "Jkjkjk", "Jkjcdskjk"))
        self.return_to_group_page(webdriver)
        self.logout(webdriver)

    def test_add_empty_group(self):
        webdriver = self.webdriver
        self.open_home_page(webdriver)
        self.login(webdriver, "admin", "secret")
        self.open_groups_page(webdriver)
        self.create_group(webdriver, Group("", "", ""))
        self.return_to_group_page(webdriver)
        self.logout(webdriver)

    def tearDown(self):
        self.webdriver.quit()

if __name__ == "__main__":
    unittest.main()
