from model.group import Group
from random import randrange
import allure


def test_modify_group_name(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    with allure.step('When I edit the group %s from the list' % group):
        app.group.modify_group_by_index(index, group)
    with allure.step('Then the new list of groups is equal to the old list with the replacement of the edited group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups[index] = group
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
