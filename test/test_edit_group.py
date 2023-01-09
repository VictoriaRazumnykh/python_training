from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Harry", header="Potter", footer="wizard"))
    app.session.logout()


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Harry Potter"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(header="wizard"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(footer="Potter"))
    app.session.logout()