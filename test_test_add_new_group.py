import pytest
from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_1_add_new_group(app):
    app.login(login="admin", password="secret")
    app.add_new_group(Group("group_2", "ghghgh", "ghhghghgh"))
    app.check_record_of_group()


def test_2_add_new_group(app):
    app.login("admin", "secret")
    app.add_new_group(Group("", "", ""))
    app.check_record_of_group()
