# from Model.contact import Contact
# import pytest
# import random
# import string


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, json_contacts):
    contact = json_contacts
    app.contact.create(contact)
