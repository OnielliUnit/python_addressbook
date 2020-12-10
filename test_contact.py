# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contacts import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self, firefox=webdriver.Firefox()):
        self.wd = firefox
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.create_contact(wd, Contact(firstName="1", middleName="1", lastName="1",
                            nickName="1", titleName="1", companyName="1",
                            addressName="1", homeNumber="1", mobileNumber="1",
                            workNumber="1", faxNumber="1", email="1",
                            personalWebsite="1", birthDay="10", birthMonth="May", birthYear="1995", annivarsaryDay="1", annivarsaryMonth="May",
                            annivarsaryYear="1995"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_contact(self, wd, contacts):
        # add full name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contacts.firstName)
        wd.find_element_by_name("middlename").send_keys(contacts.middleName)
        wd.find_element_by_name("lastname").send_keys(contacts.lastName)
        wd.find_element_by_name("nickname").send_keys(contacts.nickName)
        # add work address
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(contacts.titleName)
        wd.find_element_by_name("company").send_keys(contacts.companyName)
        wd.find_element_by_name("address").send_keys(contacts.addressName)
        # add numbers by phone
        wd.find_element_by_name("home").send_keys(contacts.homeNumber)
        wd.find_element_by_name("mobile").send_keys(contacts.mobileNumber)
        wd.find_element_by_name("work").send_keys(contacts.workNumber)
        wd.find_element_by_name("fax").send_keys(contacts.faxNumber)
        # add mail
        wd.find_element_by_name("email").send_keys(contacts.email)
        # adding a personal website
        wd.find_element_by_name("homepage").send_keys(contacts.personalWebsite)
        # add the date of birth
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.birthDay)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.birthMonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contacts.birthYear)
        # add anniversary
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.annivarsaryDay)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.annivarsaryMonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contacts.annivarsaryYear)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_xpath("//html").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()