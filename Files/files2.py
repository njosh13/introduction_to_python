# Closing Files is best practice

file = open('Files/file.txt')
file_content = file.read()
print(file_content)
file.close()

# Check if file is closed using closed attribute

file = open('Files/file.txt')
file_content = file.read()
print('Is file closed?', file.closed)
if not file.closed:
    file.close()
print('Is file closed?', file.closed)

print()

# Automatically Close A file
print('Start Reading the file')

with open('/etc/hosts') as hosts:
    print('Is file closed?', hosts.closed)
    print(hosts.read(11))
print('Finished Reading the file')
print('Is file closed?', hosts.closed)
print()

# for loops inside the file with rstrip method to remove white spaces
with open('Files/file.txt') as file:
    for line in file:
        print(line.rstrip())
print()

# Write data into a file
with open('Files/file2.txt', 'w') as file:
    file.write('This is what I want to write in that file.')
    file.write('More text in the same line.\n')  # If you want an end line
    file.write('More text in a new line.')

with open('Files/file2.txt') as file:
    print(file.read())
print()

# Binary File like an image
with open('Files/image.jpg', 'rb') as image:
    image.seek(2)
    image.read(4)
    print(image.tell())
    print(image.mode)

# Exception errors
try:
    contacts = open('contacts.txt').read()
except:
    contacts = ''

print(len(contacts))
