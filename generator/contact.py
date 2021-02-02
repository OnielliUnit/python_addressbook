from model.contacts import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", address="",
                    homephone="", mobile="",
                    work="", fax="", mail="", bday="", bmounth="", byear="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 15), address=random_string("address", 10),
                       homephone=random_string("homephone", 11), mobile=random_string("mobile", 11),
                       work=random_string("work", 11), fax=random_string("fax", 11),
                       mail=random_string("mail", 15))
               for i in range(5)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))