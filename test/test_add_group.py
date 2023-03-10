from model.group import Group
import pytest
import allure

#C:\Tools\allure-2.21.0\bin\allure.bat generate allure-results
#py.test --alluredir allure-results test\test_add_group.py

# или для использования фиксированных значений:
# from data.add_group import constant as testdata

# def test_add_group(app, data_groups):
#    group = data_groups
#    old_groups = app.group.get_group_list()
# group = Group(name="mmm", header="fggffhhg", footer="fhfghhgng")
#    app.group.create(group)
#   assert len(old_groups) + 1 == app.group.count()
#   new_groups = app.group.get_group_list()
#   old_groups.append(group)
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_json_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When i add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then a new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
