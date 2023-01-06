from model.contact import Contact


def test_edit_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit(Contact(firstname="Harry", middlename="James", lastname="Potter", title="Title",
                                   company="Hogwarts", address="Sennaya", home_phone="7777777",
                                   mobile_phone="89609999999",
                                   work_phone="567", fax="678", email1="mu@ya.ru", email2="victoria@ya.ru",
                                   byear="1993", bday="16", bmonth="January"))
    app.session.logout()


def test_edit_contact_firstname(app):
    app.session.login("admin", "secret")
    app.contact.edit(Contact(firstname="Olivia"))
    app.session.logout()