# -*- coding: utf-8 -*-
import pytest
from group import Group
from application_group import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Lesson1", header="Lesson1", footer="Lesson1"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Lesson1_1", header="Lesson1_1", footer="Lesson1_1"))
    app.logout()
