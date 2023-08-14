print('I {} Python.' .format('love'))
print('{} {} {}' .format('I', 'love', 'python'))
print('I {0} {1} and {1} {0}s me too.' .format('love', 'Python'))

# formatting variables
first = 'I'

second = 'Love'

third = 'Python'

print('{} {} {}' .format(first, second, third))

# with number
var = 3
print('{} {} {} {}' .format(first, second, third, var))

# create table in the print function
print('{0:8} | {1:8}' .format('Fruit', 'Quantity'))
print('{0:8} | {1:8}' .format('Apple', 3))
print('{0:8} | {1:8}' .format('Oranges', 10))

# Formatting String Alignments
print('{0:8} | {1:<8}' .format('Fruit', 'Quantity'))
print('{0:8} | {1:<8}' .format('Apple', 3))
print('{0:8} | {1:<8}' .format('Oranges', 10))

# Formatting Data Types
print('{0:8} | {1:<8}' .format('Fruit', 'Quantity'))
print('{0:8} | {1:<8.2f}' .format('Apple', 3))
print('{0:8} | {1:<8.2f}' .format('Oranges', 10))
