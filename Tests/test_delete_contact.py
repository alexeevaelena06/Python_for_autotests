from Model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Old_name", "Old_MiddleName_1", "LastName_1", "NickName_1", "Title_1", "MyCompany",
                                   "MyAddress", "555555", "9261664735", "4956753452", "1234", "email@mail.ru",
                                   "email_2@mail.com", "email_3@mail.ru", "6", "April", "2005", "2010", "SecondAddress",
                                   "Home", "MyNotes"))
    app.contact.delete_first_contact()
