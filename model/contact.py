
from sys import maxsize
import re



class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, title=None, company=None, address=None,
                 home_phone=None, mobile_phone=None,
                 work_phone=None, fax=None, email1=None, email2=None, email3=None, byear=None, bday=None, bmonth=None, id=None,
                 secondary_phone=None, all_phones_from_home_page=None, all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.bday = bday
        self.bmonth = bmonth
        self.id = id
        self.secondary_phone = secondary_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails = all_emails


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self):
        return re.sub("[() -]", "", self)

    def merge_phones_like_on_home_page(self):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: Contact.clear(x),
                                    filter(lambda x: x is not None,
                                           [self.home_phone, self.mobile_phone, self.work_phone,
                                            self.secondary_phone]))))

    def merge_emails_like_on_home_page(self):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None, [self.email1, self.email2, self.email3])))




