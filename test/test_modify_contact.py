from model.contacts import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="1"))
    app.contact.modify_first_contact(Contact(firstName="New firstName"))
