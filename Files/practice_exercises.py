with open('Files/ptext.txt') as file:
    line_number = 1
    for line in file:
        print('{}: {}' . format(line_number, line.rstrip()))
        line_number += 1


unsorted_file_name = 'Files/animals.txt'
sorted_file_name = 'Files/animals-sorted.txt'
animals = []
try:
    with open(unsorted_file_name) as animals_file:
        for line in animals_file:
            animals.append(line)
            animals.sort()
except:
    print('Could not open {}.'.format(unsorted_file_name))
try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}.'.format(sorted_file_name))
