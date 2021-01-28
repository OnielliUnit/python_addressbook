# -*- coding: utf-8 -*-
from model.contacts import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", address="",
                    homephone="", mobile="",
                    work="", fax="", mail="", bday="", bmounth="", byear="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 15), address=random_string("address", 10),
                       homephone=random_string("homephone", 11), mobile=random_string("mobile", 11),
                       work=random_string("work", 11), fax=random_string("fax", 11),
                       mail=random_string("mail", 15))
               for i in range(5)
           ]


@pytest.mark.parametrize("contacts", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contacts):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contacts)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
