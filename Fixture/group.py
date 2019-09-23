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
        self.fill_group_form(group)
        # submit group
        wd.find_element(By.NAME, "submit").click()
        # return to group page
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        # choose group
        self.select_first_group()
        # delete group
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.group_header)
        self.change_field_value("group_footer", group.group_footer)

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        # choose first group
        self.select_first_group()
        # edit first group
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit group
        wd.find_element(By.NAME, "update").click()
        # return to group page
        self.return_to_group_page()

    def count(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        return len(wd.find_elements(By.NAME, "selected[]"))
