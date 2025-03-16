# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from group_hw1 import Group_hw1
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="C:\\Windows\\SysWOW64\\geckodriver.exe")
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def Open_home_page(self, wd):
        # Open home page
        wd.get("http://localhost/addressbook/")

    def Login(self, wd, username, password):
        # Login
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def Create_new_contact(self, wd, group_hw1):
        # Create new contact
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill group form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(group_hw1.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(group_hw1.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(group_hw1.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(group_hw1.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(group_hw1.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(group_hw1.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(group_hw1.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(group_hw1.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(group_hw1.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(group_hw1.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(group_hw1.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(group_hw1.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(group_hw1.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(group_hw1.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(group_hw1.homepage)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(group_hw1.bday)
        wd.find_element(By.XPATH, "//option[@value='10']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(group_hw1.bmonth)
        wd.find_element(By.XPATH, "//option[@value='June']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(group_hw1.byear)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(group_hw1.aday)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[12]").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(group_hw1.amonth)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[7]").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(group_hw1.ayear)
        # Submit contact creation
        wd.find_element(By.NAME, "theform").submit()

    def Logout(self, wd):
        # Logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def test_untitled_test_case(self):
        wd = self.wd
        self.Open_home_page(wd)
        self.Login(wd, "admin", "secret")
        self.Create_new_contact(wd, "Sabrina", "Mark", "Adamson", "worker", "S@_brin@", "Froffice",
                                "34e, Lenina Street, 5, Omsk, Russia", "-", "7(978) 199-08-09", "7(999) 100-99-99",
                                "(499) 772-5189", "-", "SabrinaAdamson@mail.ru", "-", "-", "10", "June", "1996", "10",
                                "June", "2026")
        self.Logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
