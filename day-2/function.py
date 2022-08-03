def greetings_function(name, age):
    print('Welcome User '+name)
    print('Your age ', age)


greetings_function('Anupam', 23)


# pass unknown number of value using * it makes the parameter tuple -----------------------

def myFriends(*names):
    print('my friends name is', names[2])


myFriends('akash', 'raj', 'baj', 'tas')

# return in function -----------------------------------------------------------------


def add(a, b):
    return a+b


a = int(input('Enter your first number :'))
b = int(input('Enter your second number :'))
c = add(a, b)
print('your result is', c)
