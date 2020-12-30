from model.contacts import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstName="2", middleName="3", lastName="4",
                                 nickName="2"))
    app.session.logout()
