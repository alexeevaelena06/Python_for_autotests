from Model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Old_name", "LastName_1", "NickName_1", "555555", "9261664735", "4956753452", "1234"))
    app.contact.delete_first_contact()
