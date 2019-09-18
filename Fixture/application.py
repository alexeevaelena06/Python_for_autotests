from selenium import webdriver
from selenium.webdriver.common.by import By
from Fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)

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

    def go_to_website(self, url):
        wd = self.wd
        wd.get(url)
