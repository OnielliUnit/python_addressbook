from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="Lesson8", header="Lesson8", footer="Lesson8"))
    app.session.logout()
