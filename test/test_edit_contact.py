from model.contacts import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_add(Contact(firstName="2", middleName="3", lastName="4",
                               nickName="2", titleName="2", companyName="2",
                               addressName="2", homeNumber="2", mobileNumber="2",
                               workNumber="1", faxNumber="1", email="1",
                               personalWebsite="1", birthDay="10", birthMonth="May", birthYear="1995",
                               annivarsaryDay="1", annivarsaryMonth="May",
                               annivarsaryYear="1991"))
    app.session.logout()