from selenium.webdriver.common.by import By
from Fixture.locators import admin_page


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_contact_page(self):
        wd = self.app.wd
        self.app.go_to_website(admin_page)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nick_name)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact.my_company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").send_keys(contact.home_phone)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(contact.work_phone)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(contact.email_1)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").send_keys(contact.email_2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").send_keys(contact.email_3)
        wd.find_element(By.NAME, "bday").click()
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, f"//option[. = {contact.bth_day}]").click()
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.NAME, "bmonth").click()
        dropdown = wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, f"//option[. = '{contact.bth_month}']").click()
        wd.find_element(By.NAME, "bmonth").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(contact.bthday_year)
        wd.find_element(By.NAME, "aday").click()
        dropdown = wd.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '6']").click()
        wd.find_element(By.NAME, "aday").click()
        wd.find_element(By.NAME, "amonth").click()
        dropdown = wd.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = 'April']").click()
        wd.find_element(By.NAME, "amonth").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").send_keys(contact.a_year)
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").send_keys(contact.second_address)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").send_keys(contact.home_phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.return_to_contact_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.CSS_SELECTOR, ".left:nth-child(8) > input").click()
        assert wd.switch_to.alert.text == "Delete 1 addresses?"
        wd.switch_to.alert.accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))
