# Dictionary is a hold key value pairs

# dictionary_name = {key_1: value_1, key_N: value_N}

contacts = {'Jason': '555-0213', 'Njosh': '0789768'}

jasons_phone = contacts['Jason']
njosh_phone = contacts['Njosh']

print('Dial {} to call Jason' .format(jasons_phone))
print('Dial {} to call Njosh' .format(njosh_phone))

# Set values by Key
contacts['Jason'] = '555-0000'
jasons_phone = contacts['Jason']

print('Jason"s New number is {} ' .format(jasons_phone))

# add new numbers through assignment
contacts['Tony'] = '09299398'
print('The contacts dictionary are {0}. Length =  {1}' .format(
    contacts, len(contacts)))

# remove items from the dictionary
del contacts['Jason']
print('new contacts: ', contacts)

# Add dictionaries with different data types
contacts['Kim'] = 256801037
contacts['Ronaldo'] = ['555907', '907280']

print('Kim is Number {0} , Ronaldo is a list {1}'.format(
    contacts['Kim'], contacts['Ronaldo']))

# Accessing the Ronaldo list from the dictionary
for number in contacts['Ronaldo']:
    print('Phone: ', contacts['Ronaldo'])

if 'Ronaldo' in contacts.keys():
    print("Ronaldo's phone number are: {0} , {1}" .format(
        contacts['Ronaldo'][0], contacts['Ronaldo'][1]))

print(256801037 in contacts.values())
