from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit(Contact(firstname="Harry", middlename="James", lastname="Potter", title="Title",
                                   company="Hogwarts", address="Sennaya", home_phone="7777777",
                                   mobile_phone="89609999999",
                                   work_phone="567", fax="678", email1="mu@ya.ru", email2="victoria@ya.ru",
                                   byear="1993", bday="16", bmonth="January"))


def test_edit_first_contact_firstname(app):
    app.contact.edit(Contact(firstname="Olivia"))
