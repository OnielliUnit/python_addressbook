from model.contacts import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
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
    if len(db.get_contacts_not_in_group()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_contacts = db.get_contacts_not_in_group()
    c = random.choice(old_contacts)
    gs = db.get_group_list()
    g = random.choice(gs)
    app.contact.add_contact_in_group(c.id, g.id)
    new_contacts = db.get_contacts_not_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)