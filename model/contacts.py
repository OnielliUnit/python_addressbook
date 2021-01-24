from sys import maxsize


class Contact:
    def __init__(self,
                 firstName=None,
                 lastName=None,
                 middleName=None,
                 address=None,
                 email=None,
                 homePhone=None,
                 mobilePhone=None,
                 workPhone=None,
                 secondaryPhone=None,
                 all_phones_from_home_page=None,
                 id=None):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.address = address
        self.email = email
        self.homePhone = homePhone
        self.mobilePhone = mobilePhone
        self.workPhone = workPhone
        self.secondaryPhone = secondaryPhone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstName, self.lastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstName == other.firstName and self.lastName == other.lastName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize