from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import admin_page


class TestTestaddnewgroup():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1_add_new_group(self):
    self.go_to_website(admin_page)
    self.login("admin", "secret")
    self.add_new_group("group_1", "ghghgh", "ghhghghgh")
    self.check_record_of_group()

  def test_2_add_new_group(self):
    self.go_to_website(admin_page)
    self.login("admin", "secret")
    self.add_new_group("", "", "")
    self.check_record_of_group()

  def check_record_of_group(self):
    # check record of group
    self.driver.find_element(By.LINK_TEXT, "group page").click()
    self.driver.find_element(By.CSS_SELECTOR, ".group").click()

  def add_new_group(self, group_name, group_header, group_footer):
    # add new group
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    self.driver.find_element(By.NAME, "new").click()
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys(group_name)
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys(group_header)
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys(group_footer)
    self.driver.find_element(By.NAME, "submit").click()

  def login(self, login, password):
    # login
    self.driver.find_element(By.NAME, "user").send_keys(login)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def go_to_website(self, url):
    # go to website
    self.driver.get(url)
