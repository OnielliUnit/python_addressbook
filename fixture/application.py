from selenium import webdriver
from fixture.session import sessionHelper
from fixture.contact import contactHelper
from fixture.group import groupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\\Users\proun\Desktop\Python\geckodriver.exe')
        self.wd.implicitly_wait(30)
        self.session = sessionHelper(self)
        self.contact = contactHelper(self)
        self.group = groupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
