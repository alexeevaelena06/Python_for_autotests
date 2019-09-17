from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import admin_page


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        # self.wd.implicity_wait(20)

    def destroy(self):
        self.wd.quit()

    def check_record_of_group(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
        wd.find_element(By.CSS_SELECTOR, ".group").click()

    def add_new_group(self, group):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.groupname)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "submit").click()

    def login(self, login, password):
        wd = self.wd
        self.go_to_website(admin_page)
        wd.find_element(By.NAME, "user").send_keys(login)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def go_to_website(self, url):
        wd = self.wd
        wd.get(url)
