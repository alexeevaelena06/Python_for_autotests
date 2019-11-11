import random
from Model.group import Group


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test_group"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    # assert len(old_groups) - 1 == len(new_groups)
    # old_groups[index:index+1] = []
    new_groups = db.get_group_list()
    # old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
