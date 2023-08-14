animals = ['man', 'bear', 'pig']
sorted_animals = sorted(animals)
# Sorted Method
print('Animals list:              {}'.format(animals))
print('Sorted Animals list:       {}'.format(sorted_animals))

# Sort Method
animals.sort()
print('Animals after sort method: {}' . format(animals))

# Concatenate
more_animals = ['cows', 'duck', 'horse']
all_animals = animals + more_animals
print('all animals:', all_animals)

# Length of Lists
print('Length of the List before append:', len(animals))

animals.append('dog')
print('Length of the List after append:', len(animals))


# Ranges
for number in range(1, 3):
    print(number)

# Print Ranges with step parameters (1-> start , 10->end , 2->step)
for number in range(1, 10, 2):
    print(number)

for number in range(0, len(all_animals), 2):
    print(all_animals[number])
