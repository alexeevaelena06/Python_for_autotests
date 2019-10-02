from selenium import webdriver
from Fixture.contact import ContactHelper
from Fixture.group import GroupHelper
from Fixture.locators import admin_page
from Fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()

    def go_to_website(self, url):
        wd = self.wd
        wd.get(url)

    def open_home_page(self):
        wd = self.wd
        wd.get(admin_page)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
