from selenium import webdriver
from fixture.session import sessionHelper
from fixture.contact import contactHelper
from fixture.group import groupHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=r'C:\\Users\proun\Desktop\Python\geckodriver.exe')
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=r'C:\\Users\proun\Desktop\Python\chromedriver.exe')
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path=r'C:\\Users\proun\Desktop\Python\IEDriverServer.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.session = sessionHelper(self)
        self.contact = contactHelper(self)
        self.group = groupHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
