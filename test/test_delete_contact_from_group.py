from fixture.contact import Contact
from fixture.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group2"))
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Ronald"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    if contact not in (orm.get_contacts_in_group(group)):
        app.contact.add_contact_to_group(contact, group)
    app.contact.delete_contact_from_group(contact, group)
    assert contact not in orm.get_contacts_in_group(group)