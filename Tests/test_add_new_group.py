from Model.group import Group


def test_1_add_new_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group("group_2", "ghghgh", "ghhghghgh"))
    app.session.logout()


def test_2_add_new_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
