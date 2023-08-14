# Create a Python program that captures and displays a person's to­do list. Continually prompt
# the user for another item until they enter a blank item. After all the items are entered, display the
# to­do list back to the user.

to_do_ist = []
finished = False

while not finished:
    task = input('Enter a task to your to do list. Press <enter> when done: ')
    if len(task) == 0:
        finished = True
    else:
        to_do_ist.append(task)
        print('Task Added')

# Display To do list
print('Your To Do List')
for task in to_do_ist:
    print(task)
