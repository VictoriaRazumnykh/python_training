from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name="Harry", header="Potter", footer="wizard"))


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(name="Harry Potter"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(header="wizard"))


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit(Group(footer="Potter"))
