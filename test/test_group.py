# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application_group import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session_group.login(username="admin", password="secret")
    app.group.create(Group(name="Lesson1", header="Lesson1", footer="Lesson1"))
    app.session_group.logout()


def test_add_empty_group(app):
    app.session_group.login(username="admin", password="secret")
    app.group.create(Group(name="Lesson1_1", header="Lesson1_1", footer="Lesson1_1"))
    app.session_group.logout()
