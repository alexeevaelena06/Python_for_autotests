from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, homephone=None, workphone=None, mobilephone=None,
                 secondryphone=None, all_phones_from_home_page=None, all_phones_from_view_page=None,
                 all_phones_from_edit_page=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondryphone = secondryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_phones_from_view_page = all_phones_from_view_page
        self.all_phones_from_edit_page = all_phones_from_edit_page

    def __repr__(self):
        return f"{self.id}:{self.firstname} {self.lastname}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
