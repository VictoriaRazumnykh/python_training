from model.group import Group


def test_edit_first_group(app):
    app.group.edit(Group(name="Harry", header="Potter", footer="wizard"))


def test_edit_first_group_name(app):
    app.group.edit(Group(name="Harry Potter"))


def test_edit_first_group_header(app):
    app.group.edit(Group(header="wizard"))


def test_edit_first_group_footer(app):
    app.group.edit(Group(footer="Potter"))
