from selenium import webdriver
from selenium.webdriver.common.by import By
from Fixture.locators import admin_page
from Model.contact import Contact


class TestTestaddcontact():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test_add_contact(self):
    self.login("admin", "secret")
    self.add_new_contact(Contact("Name_1", "MiddleName_1", "LastName_1", "NickName_1", "Title_1", "MyCompany",
                                 "MyAddress", "555555", "9261664735", "4956753452", "1234", "email@mail.ru",
                                 "email_2@mail.com","email_3@mail.ru", "6", "April", "2005", "2010", "SecondAddress",
                                 "Home", "MyNotes"))
    self.logout()

  def add_new_contact(self, contact):
    self.driver.find_element(By.LINK_TEXT, "add new").click()
    self.driver.find_element(By.NAME, "firstname").click()
    self.driver.find_element(By.NAME, "firstname").send_keys(contact.name)
    self.driver.find_element(By.NAME, "middlename").click()
    self.driver.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
    self.driver.find_element(By.NAME, "lastname").click()
    self.driver.find_element(By.NAME, "lastname").send_keys(contact.last_name)
    self.driver.find_element(By.NAME, "nickname").click()
    self.driver.find_element(By.NAME, "nickname").send_keys(contact.nick_name)
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys(contact.title)
    self.driver.find_element(By.NAME, "company").click()
    self.driver.find_element(By.NAME, "company").send_keys(contact.my_company)
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys(contact.address)
    self.driver.find_element(By.NAME, "theform").click()
    self.driver.find_element(By.NAME, "home").click()
    self.driver.find_element(By.NAME, "home").send_keys(contact.home_phone)
    self.driver.find_element(By.NAME, "mobile").click()
    self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
    self.driver.find_element(By.NAME, "work").click()
    self.driver.find_element(By.NAME, "work").send_keys(contact.work_phone)
    self.driver.find_element(By.NAME, "fax").click()
    self.driver.find_element(By.NAME, "fax").send_keys(contact.fax)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(contact.email_1)
    self.driver.find_element(By.NAME, "email2").click()
    self.driver.find_element(By.NAME, "email2").send_keys(contact.email_2)
    self.driver.find_element(By.NAME, "email3").click()
    self.driver.find_element(By.NAME, "email3").send_keys(contact.email_3)
    self.driver.find_element(By.NAME, "bday").click()
    dropdown = self.driver.find_element(By.NAME, "bday")
    dropdown.find_element(By.XPATH, f"//option[. = {contact.bth_day}]").click()
    self.driver.find_element(By.NAME, "bday").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    dropdown = self.driver.find_element(By.NAME, "bmonth")
    dropdown.find_element(By.XPATH, f"//option[. = '{contact.bth_month}']").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    self.driver.find_element(By.NAME, "byear").click()
    self.driver.find_element(By.NAME, "byear").send_keys(contact.bthday_year)
    self.driver.find_element(By.NAME, "aday").click()
    dropdown = self.driver.find_element(By.NAME, "aday")
    dropdown.find_element(By.XPATH, "//option[. = '6']").click()
    self.driver.find_element(By.NAME, "aday").click()
    self.driver.find_element(By.NAME, "amonth").click()
    dropdown = self.driver.find_element(By.NAME, "amonth")
    dropdown.find_element(By.XPATH, "//option[. = 'April']").click()
    self.driver.find_element(By.NAME, "amonth").click()
    self.driver.find_element(By.NAME, "ayear").click()
    self.driver.find_element(By.NAME, "ayear").send_keys(contact.a_year)
    self.driver.find_element(By.NAME, "address2").click()
    self.driver.find_element(By.NAME, "address2").send_keys(contact.second_address)
    self.driver.find_element(By.NAME, "phone2").click()
    self.driver.find_element(By.NAME, "phone2").send_keys(contact.home_phone2)
    self.driver.find_element(By.NAME, "notes").click()
    self.driver.find_element(By.NAME, "notes").send_keys(contact.notes)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

  def login(self, login, password):
    self.go_to_website(admin_page)
    self.driver.find_element(By.NAME, "user").send_keys(login)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def go_to_website(self, url):
    self.driver.get(url)
