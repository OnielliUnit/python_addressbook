from selenium import webdriver
from fixture.session_contact import sessionContactHelper
from fixture.contact import contactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session_contact = sessionContactHelper(self)
        self.contact = contactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()