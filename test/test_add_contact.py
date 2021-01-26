# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstname="test", middlename="test", lastname="test", nickname="test", address="1",
                       homephone="222", mobile="222",
                       work="333", secondary="444", mail="test@mail.ru", bday="11", bmounth="11", byear="11")
    app.contact.create(contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)