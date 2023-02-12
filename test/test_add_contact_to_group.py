import random

from fixture.contact import Contact
from fixture.group import Group


def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group_new"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Victoria"))
    group = random.choice(db.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="Victoria2"))
        contact = orm.get_contacts_not_in_group(group)[0]
    else:
        contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group(contact, group)
    assert contact in orm.get_contacts_in_group(group)
