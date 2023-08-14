animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

# Values from index 1 to index 3 Doesnt include 4
some_animals = animals[1:4]
print('Some animals:{}'. format(some_animals))

# First Two Values
first_two = animals[0:2]
print('First two animals:{}' .format(first_two))

# First Two Values Again without writing index 0
first_two_again = animals[:2]
print('First two animals:{}' .format(first_two_again))

# Last Two Values
last_two = animals[4:6]
print('Last two animals:{}' .format(last_two))

# Last Two Values Again without writing index 0
last_two_again = animals[-2:]
print('Last two animals:{}' .format(last_two_again))

# String Slices
part_of_a_horse = 'horse'[1:3]
print('Slice of the string horse is: {}'.format(part_of_a_horse))
