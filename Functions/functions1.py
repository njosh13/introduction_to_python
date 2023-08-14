# Defining a function
def say_hi():
    print('Hi')


# calling it
say_hi()

# Parameters


def say_hi(name):
    print('Hi {}' .format(name))


# calling it with parameters
say_hi('Jason')


# default value
def say_hi(name='You'):
    print('Hi {}' .format(name))


# calling it with or without parameters due to the default value
say_hi()


# multiple values


def say_hi(first, last):
    print('Hi {} {}' .format(first, last))


# calling it with or without parameters due to the default value
say_hi('John', 'Baker')
say_hi(last='John', first='Baker')
