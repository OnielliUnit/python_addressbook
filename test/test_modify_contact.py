from model.contacts import Contact


def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstName="New firstName"))
