from model.contacts import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm, check_ui):
    if app.contact.count() == 0:
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
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    if orm.all_contacts_in_all_groups(groups):
        app.group.create(Group(name="test", header="test", footer="test"))
    edit_contact = random.choice(contacts)
    add_group_to_contact = random.choice(groups)
    app.contact.add_contact_in_group(edit_contact.id, add_group_to_contact.id)
    new_contacts = orm.get_contact_list()
    list_contacts_in_group = orm.get_contacts_in_group(add_group_to_contact)
    assert edit_contact in list_contacts_in_group
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)