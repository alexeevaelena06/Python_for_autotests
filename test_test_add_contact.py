from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import admin_page


class TestTestaddcontact():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test_add_contact(self):
    self.go_to_website(admin_page)
    self.login("admin", "secret")
    self.add_new_contact("Name_1", "MiddleName_1", "LastName_1", "NickName_1", "Title_1", "MyCompany", "MyAddress",
                         "555555", "9261664735", "4956753452", "1234", "email@mail.ru", "email_2@mail.com",
                         "email_3@mail.ru", "6", "April", "2005", "2010", "SecondAddress", "Home", "MyNotes")

  def add_new_contact(self, name, middle_name, last_name, nick_name, title, my_company, address, home_phone,
                      mobile_phone, work_phone, fax, email_1, email_2, email_3, bth_day, bth_month, bthday_year, a_year,
                      second_address, home_phone2, notes):
    # add new contact
    self.driver.find_element(By.LINK_TEXT, "add new").click()
    self.driver.find_element(By.NAME, "firstname").click()
    self.driver.find_element(By.NAME, "firstname").send_keys(name)
    self.driver.find_element(By.NAME, "middlename").click()
    self.driver.find_element(By.NAME, "middlename").send_keys(middle_name)
    self.driver.find_element(By.NAME, "lastname").click()
    self.driver.find_element(By.NAME, "lastname").send_keys(last_name)
    self.driver.find_element(By.NAME, "nickname").click()
    self.driver.find_element(By.NAME, "nickname").send_keys(nick_name)
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys(title)
    self.driver.find_element(By.NAME, "company").click()
    self.driver.find_element(By.NAME, "company").send_keys(my_company)
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys(address)
    self.driver.find_element(By.NAME, "theform").click()
    self.driver.find_element(By.NAME, "home").click()
    self.driver.find_element(By.NAME, "home").send_keys(home_phone)
    self.driver.find_element(By.NAME, "mobile").click()
    self.driver.find_element(By.NAME, "mobile").send_keys(mobile_phone)
    self.driver.find_element(By.NAME, "work").click()
    self.driver.find_element(By.NAME, "work").send_keys(work_phone)
    self.driver.find_element(By.NAME, "fax").click()
    self.driver.find_element(By.NAME, "fax").send_keys(fax)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email_1)
    self.driver.find_element(By.NAME, "email2").click()
    self.driver.find_element(By.NAME, "email2").send_keys(email_2)
    self.driver.find_element(By.NAME, "email3").click()
    self.driver.find_element(By.NAME, "email3").send_keys(email_3)
    self.driver.find_element(By.NAME, "bday").click()
    dropdown = self.driver.find_element(By.NAME, "bday")
    dropdown.find_element(By.XPATH, f"//option[. = {bth_day}]").click()
    self.driver.find_element(By.NAME, "bday").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    dropdown = self.driver.find_element(By.NAME, "bmonth")
    dropdown.find_element(By.XPATH, f"//option[. = '{bth_month}']").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    self.driver.find_element(By.NAME, "byear").click()
    self.driver.find_element(By.NAME, "byear").send_keys(bthday_year)
    self.driver.find_element(By.NAME, "aday").click()
    dropdown = self.driver.find_element(By.NAME, "aday")
    dropdown.find_element(By.XPATH, "//option[. = '6']").click()
    self.driver.find_element(By.NAME, "aday").click()
    self.driver.find_element(By.NAME, "amonth").click()
    dropdown = self.driver.find_element(By.NAME, "amonth")
    dropdown.find_element(By.XPATH, "//option[. = 'April']").click()
    self.driver.find_element(By.NAME, "amonth").click()
    self.driver.find_element(By.NAME, "ayear").click()
    self.driver.find_element(By.NAME, "ayear").send_keys(a_year)
    self.driver.find_element(By.NAME, "address2").click()
    self.driver.find_element(By.NAME, "address2").send_keys(second_address)
    self.driver.find_element(By.NAME, "phone2").click()
    self.driver.find_element(By.NAME, "phone2").send_keys(home_phone2)
    self.driver.find_element(By.NAME, "notes").click()
    self.driver.find_element(By.NAME, "notes").send_keys(notes)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

  def login(self, login, password):
    # login
    self.driver.find_element(By.NAME, "user").send_keys(login)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def logout(self):
    # logout
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def go_to_website(self, url):
    # go to website
    self.driver.get(url)
