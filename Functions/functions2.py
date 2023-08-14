# help function

def say_hi(first, last='Doe'):
    """Hello"""  # Doc string
    print('Hi {} {}' .format(first, last))


# help(say_hi) uncomment


def odd_or_even(number):
    """Determine if a number is odd or even"""
    if number * 2 == 0:
        return 'Even'
    else:
        return 'Odd'


value = odd_or_even(0)
print(value)


# Inheritance

def get_name():
    name = input('what is your name? ')
    return name


def say_name(name):
    print('Your name is {}' . format(name))


def get_and_say_name():
    """Get and display name"""
    name = get_name()
    say_name(name)


get_and_say_name()
