from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Harry", header="Potter", footer="wizard"))
    app.session.logout()