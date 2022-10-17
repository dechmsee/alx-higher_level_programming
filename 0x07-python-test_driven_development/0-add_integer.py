#!/usr/bin/python3
"""
Module has one function that adds up 2 integers
"""


def add_integer(a, b=98):
    """Return the sum of 2 integers or floats as integers

    Args:
        a: first argument
        b: second argument

        Returns:
            sum of the 2 arguments

        Raises:
            TypeError: If either of the 2 arguments is not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
