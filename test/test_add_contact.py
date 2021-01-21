# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contacts = Contact(firstName="Dima", lastName="Tikhonov")
    app.contact.create(contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)