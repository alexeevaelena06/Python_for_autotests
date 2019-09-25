from Model.group import Group


def test_1_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name="group_2", group_header="ghghgh", group_footer="ghhghghgh"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_2_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("", "", ""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
