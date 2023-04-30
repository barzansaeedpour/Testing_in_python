# we are using unittest module to test the functions below



######################################################


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y==0:
        raise ZeroDivisionError('cant divide by zero...')
    return x / y

