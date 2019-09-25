from Model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="old_group", group_header="old_header", group_footer="old_footer"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(group_name="New_name_group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
