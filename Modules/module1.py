""" 
Module: A file containing a set of functions you want to include in your application.
import time 
time.method_name()
time.attribute_name
"""

import module2
from time import asctime, sleep
import time
import sys

print(time.asctime())
print(time.timezone)


print(asctime())
# sleep(3) This will stop the process for about 3 seconds
print(asctime())


try:
    for path in sys.path:
        print(path)

except Exception as e:
    print('error:', e)


file_name = 'Modules/file.txt'

try:
    with open(file_name) as test_file:
        for line in test_file:
            print(line.rstrip())
except:
    print('Could not open', file_name)
    sys.exit(1)

print()

module2.main()
