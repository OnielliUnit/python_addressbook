from selenium.webdriver.support.ui import Select


class contactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contacts):
        wd = self.app.wd
        self.open_contact_page()
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
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
