# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Lesson1", header="Lesson1", footer="Lesson1"))


def test_add_empty_group(app):
    app.group.create(Group(name="Lesson1_1", header="Lesson1_1", footer="Lesson1_1"))
