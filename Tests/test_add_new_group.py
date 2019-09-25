from Model.group import Group


def test_1_add_new_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="group_2", group_header="ghghgh", group_footer="ghhghghgh")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_2_add_new_group(app):
    old_groups = app.group.get_group_list()
    group = Group()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
