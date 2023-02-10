from model.group import Group
from random import randrange
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    new_group = Group(name="Harry1", header="Potter1", footer="wizard1")
    # group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id, new_group)
    # assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for i in range(len(old_groups)):
        if old_groups[i].id == group.id:
            old_groups[i] = new_group
            old_groups[i].id = group.id
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    new_group = Group(name="Harry Potter")
    app.group.edit_group_by_id(group.id, new_group)
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == app.group.count()  # len(new_groups)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit(Group(header="wizard"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


# def test_edit_first_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#   old_groups = app.group.get_group_list()
#    app.group.edit(Group(footer="Potter"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
