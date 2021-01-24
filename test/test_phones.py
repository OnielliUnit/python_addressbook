import re

from model.contacts import Contact


def test_phones_on_phone_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstName="test",
            lastName="test",
            address="test",
            homePhone="+79999999999",
            mobilePhone="+73832229222",
            workPhone="+9588766578",
            secondaryPhone="+79877654332",
            email="test@test.test"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# def test_phone_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homePhone == contact_from_edit_page.homePhone
#     assert contact_from_view_page.workPhone == contact_from_edit_page.workPhone
#     assert contact_from_view_page.mobilePhone == contact_from_edit_page.mobilePhone
#     assert contact_from_view_page.secondaryPhone == contact_from_edit_page.secondaryPhone

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(lambda x: clear(x),
                   filter(lambda x: x is not None,
                          [contact.homePhone, contact.mobilePhone, contact.workPhone, contact.secondaryPhone]))))
