from model.contact import Contact
from random import randrange


def test_contacts_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones == Contact.merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_emails == Contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_contacts_on_view_page(app):
    index = randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone
    assert contact_from_view_page.address == contact_from_edit_page.address
    assert contact_from_view_page.email1 == contact_from_edit_page.email1
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3


def test_compare_contacts_with_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(len(contacts_from_home_page)):
        assert (contacts_from_home_page[index].firstname, contacts_from_home_page[index].lastname,
                contacts_from_home_page[index].address, contacts_from_home_page[index].all_emails,
                contacts_from_home_page[index].all_phones) == \
               (contacts_from_db[index].firstname.strip(), contacts_from_db[index].lastname.strip(),
                contacts_from_db[index].address.strip(),
                Contact.merge_emails_like_on_home_page(contacts_from_db[index]),
                Contact.merge_phones_like_on_home_page(contacts_from_db[index]))
