from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.groupname)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group
        wd.find_element(By.NAME, "submit").click()
        # return to group page
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        # choose group
        wd.find_element(By.NAME, "selected[]").click()
        # delete group
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()
