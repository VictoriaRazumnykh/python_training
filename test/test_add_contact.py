from model.contact import Contact



def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="Victorya", middlename="Alexandr", lastname="Razumnykh", title="Title",
                                   company="bercut", address="Sennaya", home_phone="7777777",
                                   mobile_phone="89609999999",
                                   work_phone="567", fax="678", email1="mu@ya.ru", email2="victoria@ya.ru",
                                   byear="1993", bday="16", bmonth="January"))


