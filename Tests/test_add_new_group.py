# from Data.data_groups import testdata
from Model.group import Group
# import pytest


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_new_group(app, db, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    # TODO подправить проверку
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
