from Model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digit(maxlen):
    symbols = string.digits*11
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
                    homephone=random_digit(11), workphone=random_digit(11),
                    mobilephone=random_digit(11), secondryphone=random_digit(11))]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contact):
    app.contact.create(contact)
