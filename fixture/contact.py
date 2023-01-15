from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    contact_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.add_new_contact()
        # add firstname
        self.fill_contact_form(contact)
        self.return_to_address_book_entry()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        # add title
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_box_value("bday", contact.bday)
        self.change_box_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def return_to_address_book_entry(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit(self, contact):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_box_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def delete(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_elements_by_xpath(".//td")
                id = text[0].find_element_by_name("selected[]").get_attribute("value")
                last_name = text[1].text
                first_name = text[2].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id))
        return list(self.contact_cache)
