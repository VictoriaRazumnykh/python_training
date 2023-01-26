from model.group import Group



# или для использования фиксированных значений:
# from data.add_group import constant as testdata

def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    # group = Group(name="mmm", header="fggffhhg", footer="fhfghhgng")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_json_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    # group = Group(name="mmm", header="fggffhhg", footer="fhfghhgng")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
