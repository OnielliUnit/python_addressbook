# -*- coding: utf-8 -*-
import pytest
from contacts import Contact
from application_contact import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstName="1", middleName="1", lastName="1",
                               nickName="1", titleName="1", companyName="1",
                               addressName="1", homeNumber="1", mobileNumber="1",
                               workNumber="1", faxNumber="1", email="1",
                               personalWebsite="1", birthDay="10", birthMonth="May", birthYear="1995",
                               annivarsaryDay="1", annivarsaryMonth="May",
                               annivarsaryYear="1995"))
    app.logout()