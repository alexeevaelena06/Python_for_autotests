from Model.contact import Contact


def test_test_add_contact(app):
    app.contact.create(Contact("Name_1", "MiddleName_1", "LastName_1", "NickName_1", "Title_1", "MyCompany",
                               "MyAddress", "555555", "9261664735", "4956753452", "1234", "email@mail.ru",
                               "email_2@mail.com", "email_3@mail.ru", "6", "April", "2005", "2010", "SecondAddress",
                               "Home", "MyNotes"))
