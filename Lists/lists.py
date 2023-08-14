# Lists examples
item_1 = 1
item_2 = 2

list_name = [item_1, item_2]
print('Your list is: {},{}' .format(list_name[0], list_name[1]))


# Set Values by Index
list_name[0] = 0  # Changes index 0 the variable to 0
print('Index 0 is now {}' .format(list_name[0]))
print('Your new list is {}' .format(list_name))


# Check Last Item in the List
print('Your List from backward is  {},{}' .format(
    list_name[-1], list_name[-2]))  # Since it replaced 1 to 0
print('Your new list is {}' .format(list_name))

# Add Item as the last value of the list
list_name.append(3)
print('The last Value is {}' .format(list_name[-1]))
print('Your new list is {}' .format(list_name))

# Add Items to the List directly as the last values
list_name.extend([4, 5])
print('Your have added {},{}' .format(list_name[-2], list_name[-1]))
print('Your new list is {}' .format(list_name))

# Add Items to the List with variable as the last values
add_values = [6, 7]
list_name.extend(add_values)
print('Your have added {},{}' .format(add_values[0], add_values[1]))
print('Your new list is {}' .format(list_name))


# Add Values via index using the insert method
list_name.insert(1, 1)  # insert value 1  to index 1
print('Your have added {}' .format(list_name[1]))
print('Your new list is {}' .format(list_name))
