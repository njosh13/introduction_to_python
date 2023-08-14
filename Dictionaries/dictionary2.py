# For loops on Dictionaries.

contacts = {
    'Jason': '552-9202',
    'Carl': '89719-0929'
}

for contact in contacts:
    print('The number for {0} is {1}.' .format(contact, contacts[contact]))


for person, phone_number in contacts.items():
    print('The number for {0} is {1}.' .format(person, phone_number))


# Nested Dictionaries

contacts = {
    'Jason': {
        'phone': '827-789',
        'email': 'jason@exapmle.com'
    },
    'Naomi': {
        'phone': '78263-038',
        'email': 'naomi@example.com'
    }
}

for contact in contacts:
    print("{}'s contact info" . format(contact))
    print('phone:', contacts[contact]['phone'])
    print('email:', contacts[contact]['email'])
