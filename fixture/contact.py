from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.change_field_value("email3", contact.email3)
        self.change_box_value("bday", contact.bday)
        self.change_box_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("phone2", contact.secondary_phone)

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

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()
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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
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
                address = text[3].text
                all_emails = text[4].text
                all_phones = text[5].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails=all_emails,
                                                  address=address))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_xpath(".//td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_xpath(".//td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        # открываем форму редактирования по заданному индексу
        self.open_contact_to_edit_by_index(index)
        # читаем информацию из формы
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, secondary_phone=secondaryphone, email1=email1, email2=email2,
                       email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        first_second_name = re.search("(.*)\n", text).group(1).split()
        firstname = first_second_name[0]
        lastname = first_second_name[2]
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        all_emails = []
        for element in wd.find_element_by_id("content").find_elements_by_css_selector("a"):
            if re.search("(.*)@(.*).*", element.text) is not None:
                all_emails.append(element.text)
        address = text.split()[5]
        return Contact(firstname=firstname, lastname=lastname, home_phone=homephone, mobile_phone=mobilephone,
                       work_phone=workphone, secondary_phone=secondaryphone, email1=all_emails[0], email2=all_emails[1],
                       email3=all_emails[2], address=address)
