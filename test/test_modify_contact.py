from model.contacts import Contact
from random import randrange
import allure


def test_modify_contact_name(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="1"))
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        index = randrange(len(old_contacts))
    contact = Contact(firstname="New firstName")
    contact.id = old_contacts[index].id
    with allure.step('When I edit the contact %s from the list' % contact):
        app.contact.modify_contact_by_index(index, contact)
    with allure.step('Then the new list of contacts is equal to the old list with the replacement of the edited contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == app.contact.count()
        old_contacts[index] = contact
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)