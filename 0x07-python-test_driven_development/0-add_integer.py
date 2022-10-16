#!/usr/bin/python3
def add_integer(a, b=98):
    """
    returns the sum of a and b
    """
    a1, b1 = 0, 0
    try:
        a1 = a + 1
        b1 = b + 1
    except TypeError:
        if not a1:
            return "a must be an integer"
        if not b1:
            return "b must be an integer"
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
