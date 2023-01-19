from model.contact import Contact
import pytest
import random
import string

#import calendar
#import locale
#import pymorphy2


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits * 15 + string.punctuation + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.digits + string.ascii_letters + string.punctuation
    symbols_letters = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(symbols_letters) for i in range(random.randrange(maxlen))]) + "." + \
           "".join([random.choice(symbols_letters) for i in range(random.randrange(maxlen))])


#def random_month():
#    morph = pymorphy2.MorphAnalyzer()
#    locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
#    symbols = []
#    for name in calendar.month_name:
#        symbols.append(morph.parse(name)[0].normal_form.capitalize())
#    return random.choice(symbols)


def random_month():
    symbols = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
    return random.choice(symbols)


# testdata = [Contact(firstname="Victorya", middlename="Alexandr", lastname="Razumnykh", title="Title",
#                    company="bercut", address="Sennaya", home_phone="7777777",
#                    mobile_phone="89609999999",
#                    work_phone="567", fax="678", email1="mu@ya.ru", email2="victoria@ya.ru", email3="victori@ya.ru",
#                    byear="1993", bday="16", bmonth="January", secondary_phone="6666666")
#            for firstname in [random_string("firstname", 10)]
#            for middlename in [random_string("middlename", 10)]
#            for lastname in [random_string("lastname", 10)]
#            for title in [random_string("title", 10)]
#            for company in [random_string("company", 10)]
#            for address in [random_string("address", 10)]
#            for home_phone in [random_phone(10)]
#            for mobile_phone in [random_phone(10)]
#            for work_phone in [random_phone(10)]
#            for fax in [random_phone(10)]
#            for email1 in [random_email(10)]
#            for email2 in [random_email(10)]
#            for email3 in [random_email(10)]
#            for byear in [str(random.randrange(1990, 2023))]
#            for bday in [str(random.randrange(31))]
#            for bmonth in [random_month()]
#            for secondary_phone in [random_phone(10)]
#            ]

testdata = [Contact(firstname="", middlename="", lastname="", title="",
                    company="", address="", home_phone="",
                    mobile_phone="",
                    work_phone="", fax="", email1="", email2="", email3="",
                    byear="", bday="", bmonth="", secondary_phone="")] + [
               Contact(firstname=random_string("firstname", 5),
                       middlename=random_string("middlename", 5),
                       lastname=random_string("lastname", 5),
                       title=random_string("title", 5),
                       company=random_string("company", 5),
                       address=random_string("address", 5),
                       home_phone=random_phone(5),
                       mobile_phone=random_phone(5),
                       work_phone=random_phone(5),
                       fax=random_phone(5),
                       email1=random_email(5),
                       email2=random_email(5),
                       email3=random_email(5),
                       byear=str(random.randrange(1990, 2023)),
                       bday=str(random.randrange(30)),
                       bmonth=random_month(),
                       secondary_phone=random_phone(5))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
