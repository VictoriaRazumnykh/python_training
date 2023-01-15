from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Harry", middlename="James", lastname="Potter", title="Title",
                                   company="Hogwarts", address="Sennaya", home_phone="7777777",
                                   mobile_phone="89609999999",
                                   work_phone="567", fax="678", email1="mu@ya.ru", email2="victoria@ya.ru",
                                   byear="1993", bday="16", bmonth="January")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Olivia")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
