"""
Tuple is an immutable list and are ordered.
Once defined it cannot be changed.
Use when data should not change.
Example: tuple_name = (item_1, item_2, item_N)
"""

days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday')
monday = days_of_week[1]
print(monday)


print()

for day in days_of_week:
    print(day)

# Delete a tuple

day = ('Sunday')
del day


# Methods to convert from tuple to lists and vice versa

# Tuple to list
weekend_tuple = ('Sunday', 'Saturday')
weekend_list = list(weekend_tuple)
print('Weekend Tuple is:', type(weekend_tuple))
print('Weekend List is:', type(weekend_list))

# list to tuple
animal_list = ['man', 'bear']
animal_tuple = tuple(animal_list)
print('Animal Tuple is:', type(animal_tuple))
print('Animal List is:', type(animal_list))


# use tuples to  assign values to multiple variables at once
weekend_days = ('Saturday', 'Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)


contact_info = ['7181603', 'exa@exa.com']
(phone, email) = contact_info

print(phone)
print(email)


# Used in functions
def high_and_low(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)


lottery_numbers = [-1, 1, 2, 3, 4, 5, 90]
(highest, lowest) = high_and_low(lottery_numbers)
print('highest:', highest)
print('lowest:', lowest)


# for loops of a list of tuples

contacts = [('Jason', 718202), ('Carl', 90181)]

for (name, phone) in contacts:
    print("{}'s phone number is {}".format(name, phone))
