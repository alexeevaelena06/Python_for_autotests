from Model.group import Group


def test_modify_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group(Group(group_name="New_name_group"))
    app.session.logout()
