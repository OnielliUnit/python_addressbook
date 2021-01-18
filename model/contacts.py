from sys import maxsize


class Contact:
    def __init__(self, firstName=None, middleName=None, lastName=None,
                 nickName=None, id=None):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.nickName = nickName
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