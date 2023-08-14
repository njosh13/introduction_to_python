# Read File

file = open('Files/file.txt')
file_content = file.read()
print(file_content)

hosts = open('/etc/hosts')
print('Current Position:', hosts.tell())
print(hosts.read())


print('Current Position:', hosts.tell())
print(hosts.read())


hosts.seek(0)
print('found 0')
print('Current Position:', hosts.tell())
print(hosts.read())

hosts.seek(0)
print('first three variables in the file:', hosts.read(10))
print('tell:', hosts.tell())
