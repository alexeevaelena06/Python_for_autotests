from Model.contact import Contact


def test_test_add_contact(app):
    app.contact.create(Contact("Name_1", "LastName_1", "NickName_1", "555555", "9261664735", "4956753452",
                               "8888888888"))
