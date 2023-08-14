# Create a program that asks the user how far they want to travel. If they want to travel less than
# three miles tell them to walk. If they want to travel more than three miles, but less than three
# hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
# fly.

# input the number of miles
# less than 3 miles walk
# more than 3 but less than 300 miles drive
# >300 miles fly

miles = int(input('How far would you like to travel in miles?'))

if miles < 3:
    print('I suggest walking to your destination.')

elif miles > 3 and miles < 300:
    print('I suggest driving to your destination.')

elif miles >= 300:
    print('I suggest flying to your destination.')
