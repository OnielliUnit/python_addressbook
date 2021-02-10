Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>, <homephone>, <mobile>, <work> and <mail>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  |firstname  |lastname   |address  |homephone  |mobile  |work  |mail  |
  |firstname1 |lastname1  |address1 |homephone1 |mobile1 |work1 |mail1 |
  |firstname2 |lastname2  |address2 |homephone2 |mobile2 |work2 |mail2 |



Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact

Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list