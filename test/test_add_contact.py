# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app):
    app.contact.open_contacts_page()
    app.contact.create(Contact(firstName="1", middleName="1", lastName="1",
                               nickName="1"))