# Create a list of airports that includes a series of tuples
#  containing an airport's name and its code.

airports = [
    ('Ohare', 'ORD'),
    ('Los Angeles International', 'LAX'),
    ('Dallas/Fort Worth International Airport', 'DFW'),
    ('Denver International Airport', 'DEN')
]

# Loop through the list and utilize tuple assignment


for (name, code) in airports:
    print("The code for {} is {}" .format(name, code))
