from model.contacts import Contact
from model.group import Group
import random
import allure


def test_del_contact_in_group(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="test",
                                       middlename="test",
                                       lastname="test",
                                       nickname="test",
                                       address="test",
                                       homephone="777333",
                                       mobile="777333",
                                       work="777333",
                                       fax="777333",
                                       mail="test@test.ru",
                                       mail2="test@test.ru",
                                       mail3="test@test.ru",
                                       bday="11",
                                       byear="1999",
                                       bmounth="January"))
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name='Test'))
    with allure.step('When I delete contact %s in group %s from the list' % (edit_contact, del_group_from_contact)):
        if len(db.get_groups_with_contacts()) == 0:
            gs = db.get_group_list()
            g = random.choice(gs)
            cs = db.get_contacts_not_in_group()
            c = random.choice(cs)
            app.contact.add_contact_in_group(c.id, g.id)
        gs = db.get_groups_with_contacts()
        g = random.choice(gs)
        old_contacts = db.get_contacts_in_group()
        c = random.choice(old_contacts)
        app.contact.del_contact_in_group(c.id, g.id)
    with allure.step('Then the edited contact will not be in the contact list of the selected group'):
        new_contacts = db.get_contacts_in_group()
        assert len(old_contacts) - 1 == len(new_contacts)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)