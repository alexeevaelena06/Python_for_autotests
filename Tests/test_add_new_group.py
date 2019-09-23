from Model.group import Group


def test_1_add_new_group(app):
    app.group.create(Group("group_2", "ghghgh", "ghhghghgh"))


def test_2_add_new_group(app):
    app.group.create(Group("", "", ""))
