# we are using doctest module to test the functions below

# the tests can be declare globaly or inside the functions

# to run the tests, we use the commands below:
# > python -m doctest one.py
# or to see more detail:
# > python -m doctest -v one.py

######################################################

"""
>>> add(5, 6)
11

>>> subtract(7, 6)
1

>>> multiply(4, 5)
20
"""

def add(x, y):
    """
    >>> add(7, 6)
    13
    
    >>> add(4, -1)
    3

    >>> add(0, 5)
    5

    """
    return x + y

def subtract(x, y):
    """
    >>> subtract(5, 4)
    1
    
    >>> subtract(6, 9)
    -3
    """
    return x - y

def multiply(x, y):
    """
    >>> multiply(5, 6)
    30
    
    >>> multiply(5, 'b')
    'bbbbb'
    """
    return x * y

