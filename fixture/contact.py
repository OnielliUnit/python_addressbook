from model.contacts import Contact


class contactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("./") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstName)
        self.change_field_value("lastname", contact.lastName)


    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contacts_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.open_contacts_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # change contact data
        self.fill_contact_form(contact)
        # submit changing contact
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_contacts_page()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("id")
            lastName = element.find_element_by_xpath("./td[2]").text
            firstName = element.find_element_by_xpath("./td[3]").text
            contacts.append(Contact(id=id, firstName=firstName, lastName=lastName))
        return contacts