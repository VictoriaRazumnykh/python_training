from model.contact import Contact
import random


def test_edit_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="Harry", middlename="James", lastname="Potter", title="Title",
                          company="Hogwarts", address="Sennaya", home_phone="7777777",
                          mobile_phone="89609999999",
                          work_phone="567", fax="678", email1="mu@ya.ru", email2="victoria@ya.ru",
                          email3="victori@ya.ru",
                          byear="1993", bday="16", bmonth="January", secondary_phone="6666666")
    # contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_edit_first_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="Olivia")
    app.contact.edit_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
