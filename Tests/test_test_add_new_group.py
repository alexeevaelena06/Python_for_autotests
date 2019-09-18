import pytest
from Fixture.application import Application
from Model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_1_add_new_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group("group_2", "ghghgh", "ghhghghgh"))
    app.group.check_record_of_group()
    app.session.logout()


def test_2_add_new_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.group.check_record_of_group()
    app.session.logout()
